import os
import shutil
import random


def create_split_folders(input_folder, destination_folder, split_folders=["train", "test", "val"], train_ratio=0.8, test_ratio=0.1):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    else:
        # Clear the destination folder to overwrite it
        shutil.rmtree(destination_folder)
        os.makedirs(destination_folder)

    # Check if split folders already exist, if not, create them
    for folder in split_folders:
        folder_path = os.path.join(destination_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        else:
            print(f"{folder_path} already exists.")

    # Function to copy files to train, test, and validation folders
    def copy_files(source_folder, destination_folder, split_ratio):
        for class_folder in os.listdir(source_folder):
            class_folder_path = os.path.join(source_folder, class_folder)
            if os.path.isdir(class_folder_path):
                files = os.listdir(class_folder_path)
                random.shuffle(files)
                split_index_train = int(len(files) * train_ratio)
                split_index_test = int(len(files) * (train_ratio + test_ratio))
                train_files = files[:split_index_train]
                test_files = files[split_index_train:split_index_test]
                val_files = files[split_index_test:]

                # Copy files to train folder
                train_folder_path = os.path.join(destination_folder, "train", class_folder)
                os.makedirs(train_folder_path)  # Create folder even if it exists to overwrite it
                for file in train_files:
                    shutil.copy(os.path.join(class_folder_path, file), train_folder_path)

                # Copy files to test folder
                test_folder_path = os.path.join(destination_folder, "test", class_folder)
                os.makedirs(test_folder_path)  # Create folder even if it exists to overwrite it
                for file in test_files:
                    shutil.copy(os.path.join(class_folder_path, file), test_folder_path)

                # Copy files to validation folder
                val_folder_path = os.path.join(destination_folder, "val", class_folder)
                os.makedirs(val_folder_path)  # Create folder even if it exists to overwrite it
                for file in val_files:
                    shutil.copy(os.path.join(class_folder_path, file), val_folder_path)

    # Copy files to train, test, and validation folders
    copy_files(input_folder, destination_folder, train_ratio)

    print("Files copied successfully!")


# Example usage
#create_split_folders("/content/flower_pics", "output_data")
