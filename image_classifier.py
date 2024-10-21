import os
import shutil
import random
import json
from ultralytics import YOLO
from dataset_info_script import calculate_dataset_info
from create_split_folder import create_split_folders

def train_and_validate_yolo(data_path, epochs=5, imgsz=224, lr0=0.01, batch_size=16):
    # Load a model
    model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

    # Train the model
    results_train = model.train(data=data_path, epochs=epochs, imgsz=imgsz, batch=batch_size, lr0=lr0)

    # Validate the model
    results_test = model.val(data=data_path, split='test', epochs=epochs, imgsz=imgsz, batch=batch_size)

    num_classes, class_names, train_images, test_images, val_images = calculate_dataset_info(updated_folder_path)

    output_dict = {
        "epochs": epochs,
        "learning_rate": lr0,
        "batch_size": batch_size,
        "train_accuracy": results_train.top1,
        "test_accuracy": results_test.top1,
        "num_classes": len(set(class_names)),
        "class_names": list(set(class_names)),
        'total_images':(train_images+test_images+val_images),
        "train_dataset_images": train_images,
        "test_dataset_images": test_images,
        "valid_dataset_images": val_images
    }
    # Convert dict to JSON and print
    output_json = json.dumps(output_dict, indent=4)
    print(output_json)
    current_directory = os.getcwd()

    # Define the file name
    output_file_name = "output.json"

    # Join the current directory with the file name to create the file path
    output_file_path = os.path.join(current_directory, output_file_name)
    with open(output_file_path, "w") as output_file:
      output_file.write(output_json)
    print("JSON file saved successfully at:", output_file_path)
    return results_train, results_test

# Ask user for input
#data_folder_path = input("Enter the path to your data folder: ")
#epochs_input = int(input("Enter the number of epochs: "))
#learning_rate_input = float(input("Enter the learning rate: "))
#batch_size_input = int(input("Enter the batch size: "))

# Ask user for input
try:
    data_folder_path = input("Enter the path to your data folder: ")
    use_default = input("Do you want to use default values? (yes/no): ").strip().lower()
    if use_default == "yes":
        epochs_input = 1
        learning_rate_input = 0.01
        batch_size_input = 16
    elif use_default == "no":
        #data_folder_path = input("Enter the path to your data folder: ").strip()
        epochs_input = int(input("Enter the number of epochs: ").strip())
        learning_rate_input = float(input("Enter the learning rate: ").strip())
        batch_size_input = int(input("Enter the batch size: ").strip())
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        exit()
    
    if epochs_input <= 0:
        print("Number of epochs must be a positive integer. Using default value instead.")
        epochs_input = 1
    
    if learning_rate_input <= 0:
        print("Learning rate must be a positive float. Using default value instead.")
        learning_rate_input = 0.01
    
    if batch_size_input <= 0:
        print("Batch size must be a positive integer. Using default value instead.")
        batch_size_input = 16
    
except ValueError as ve:
    print(f"Error: {ve}")
    print("Using default values instead.")
    epochs_input = 1
    learning_rate_input = 0.01
    batch_size_input = 16


# Rest of the code remains the same

# Create split folders
# Get the current working directory
current_directory = os.getcwd()

# Define the folder name
updated_folder_path = "updated_folder"
#updated_folder_path = "/content/updated_folder"  # Destination folder path
create_split_folders(data_folder_path, updated_folder_path)

# Train and validate YOLO model
start_training = input("Do you want to start training? (yes/no): ")
if start_training.lower() == "yes":
    train_results, val_results = train_and_validate_yolo(updated_folder_path, epochs=epochs_input, lr0=learning_rate_input, batch_size=batch_size_input)
    print("Training and validation completed successfully!")
else:
    print("Training aborted.")
