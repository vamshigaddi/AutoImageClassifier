import os

def calculate_dataset_info(updated_folder_path):
    class_names = set()  # Using a set to store unique class names

    train_images = 0
    test_images = 0
    val_images = 0

    for split_folder in ["train", "test", "val"]:
        split_folder_path = os.path.join(updated_folder_path, split_folder)
        if not os.path.exists(split_folder_path):
            continue  # Skip if the split folder doesn't exist

        for class_folder in os.listdir(split_folder_path):
            class_names.add(class_folder)  # Add unique class names to the set

            class_folder_path = os.path.join(split_folder_path, class_folder)
            if os.path.isdir(class_folder_path):
                # Count images in current class folder
                if split_folder == "train":
                    train_images += len(os.listdir(class_folder_path))
                elif split_folder == "test":
                    test_images += len(os.listdir(class_folder_path))
                elif split_folder == "val":
                    val_images += len(os.listdir(class_folder_path))

    num_classes = len(class_names)  # Get the count of unique class names

    return num_classes, list(class_names), train_images, test_images, val_images
