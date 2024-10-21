import os
import shutil
import requests
import zipfile
import json
import django
import time
from django.conf import settings
from django.db.models import Q
from ultralytics import YOLO
from dataset_info_script import calculate_dataset_info
from create_split_folder import create_split_folders

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_classifier.settings')

# Setup Django
django.setup()

from images.models import ImageDirectory  # Import your Django model

def download_and_unzip(url, extract_to):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        zip_path = os.path.join(extract_to, 'temp.zip')
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        os.remove(zip_path)
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

def train_and_validate_yolo(data_path, epochs=1, imgsz=224, lr0=0.01, batch_size=16):
    try:
        # Load a model
        model = YOLO('yolov8n-cls.pt')  # Load a pretrained model (recommended for training)

        print(f"Starting training with data at: {data_path}")
        # Train the model
        results_train = model.train(data=data_path, epochs=epochs, imgsz=imgsz, batch=batch_size, lr0=lr0)
        print("Training completed.")

        # Validate the model
        print("Starting validation...")
        results_test = model.val(data=data_path, split='test', epochs=epochs, imgsz=imgsz, batch=batch_size)
        print("Validation completed.")

        num_classes, class_names, train_images, test_images, val_images = calculate_dataset_info(data_path)

        output_dict = {
            "epochs": epochs,
            "learning_rate": lr0,
            "batch_size": batch_size,
            "train_accuracy": results_train.top1,
            "test_accuracy": results_test.top1,
            "num_classes": len(set(class_names)),
            "class_names": list(set(class_names)),
            'total_images': (train_images + test_images + val_images),
            "train_dataset_images": train_images,
            "test_dataset_images": test_images,
            "valid_dataset_images": val_images
        }
        # Convert dict to JSON
        # Parse JSON string to a Python dictionary
        data = json.loads(output_dict)

        # Convert Python dictionary back to a JSON string without newlines
        output_json = json.dumps(data, separators=(',', ':'))
        

        # Remove 'runs' directory if it exists
        runs_directory = os.path.join(os.getcwd(), 'runs')
        if os.path.exists(runs_directory):
            try:
                print(f"Deleting 'runs' directory at {runs_directory}")
                shutil.rmtree(runs_directory)
                print(f"Deleted 'runs' directory at {runs_directory}")
            except Exception as e:
                print(f"Error deleting 'runs' directory: {e}")

        return "Successfully trained", output_json
    except Exception as e:
        print(f"Error during training: {e}")
        return "Failed to train", json.dumps({"error": str(e)}, indent=4)

def process_datasets():
    while True:
        # Get IDs of rows where 'status' is empty, None, or whitespace
        empty_status_records = ImageDirectory.objects.filter(
            Q(status__isnull=True) | 
            Q(status='') | 
            Q(status__regex=r'^\s*$')
        )

        if not empty_status_records:
            print("No empty status records found. All records are trained.")
            time.sleep(10)  # Wait before checking again
            continue

        for record in empty_status_records:
            url = record.url
            print(f"Processing URL: {url}")  # Print the URL being processed
            
            # Define directories
            temp_folder_path = os.path.join(os.getcwd(), 'temp')
            updated_folder_path = os.path.join(os.getcwd(), 'updated_folder')

            # Ensure the temp folder exists
            if not os.path.exists(temp_folder_path):
                os.makedirs(temp_folder_path)
            
            # Clean the temp folder before extraction
            for filename in os.listdir(temp_folder_path):
                file_path = os.path.join(temp_folder_path, filename)
                try:
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    else:
                        os.remove(file_path)
                except Exception as e:
                    print(f"Error cleaning temp folder: {e}")

            # Download and unzip the file
            download_and_unzip(url, temp_folder_path)

            # Find and move the inner folder
            extracted_folder = next((f for f in os.listdir(temp_folder_path) if os.path.isdir(os.path.join(temp_folder_path, f))), None)

            if extracted_folder:
                flower_dic_path = os.path.join(temp_folder_path, extracted_folder)
                # Create updated folder if it doesn't exist
                if not os.path.exists(updated_folder_path):
                    os.makedirs(updated_folder_path)
                # Copy the inner folder to updated folder
                shutil.copytree(flower_dic_path, updated_folder_path, dirs_exist_ok=True)
            else:
                print(f"No valid inner folder found in the zip file for URL: {url}")
                record.status = 'Failed to process'
                record.save()
                continue

            # Create split folders
            create_split_folders(flower_dic_path, updated_folder_path)

            # Train and validate YOLO model
            status, results_json = train_and_validate_yolo(updated_folder_path, epochs=1, lr0=0.01, batch_size=16)
            
            # Update status and results in the database
            record.status = status
            record.results = results_json
            record.save()

        # Wait for 10 seconds before the next check
        time.sleep(10)

if __name__ == "__main__":
    process_datasets()
