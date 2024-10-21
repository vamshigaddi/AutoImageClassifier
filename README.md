# Auto Image Classifier
The Auto Image Classifier is an application designed for image classification using a pre-trained YOLO (You Only Look Once) model. Users can upload their dataset files, which are then uploaded to the cloud. The application stores the dataset path in a PostgreSQL database. In the backend, the classification model trains on the uploaded data, allowing users to specify training parameters such as epochs, learning rate, and batch size. After the training process is complete, the application generates an output JSON file containing detailed results, including the status of the training and the trained parameters.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Dataset structure](#dataset-structure)
- [Usage](#usage)
- [License](#license)

## Introduction
The Auto Image Classifier provides a convenient way to perform image classification tasks using a pre-trained YOLO model. Users can train the model on their custom datasets, fine-tuning the parameters to achieve optimal performance.

## Features
- Utilizes a pre-trained YOLO model for image classification.
- Enables training on custom datasets with customizable parameters.
- Provides detailed training results in an output JSON file.
## Demo
[Watch the video](https://www.veed.io/view/cc7bcfbc-5948-47da-88b6-20ac580ce218?panel=share)


## Installation
To use the Auto Image Classifier, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/vamshigaddi/auto-image-classifier.git

   ```
   ```bash
   pip install -r requirements.txt
   ```
## Dataset structure
- Your Input dataset structure should look like this before you give to image_classifier.py script
- This is an Example you can have different folders and different images but structure of dataset should look like this.
```bash
Dataset/
├── Rose/
│ ├── image1.jpg
│ ├── image2.jpg
│ ├── ...
├── Lilly/
│ ├── image1.jpg
│ ├── image2.jpg
│ ├── ...
├── Daffodiles/
│ ├── image1.jpg
│ ├── image2.jpg
│ ├── ...
```
##  Usage
To train the model and generate classification results, follow these steps:

- Run the image_classifier.py script:
   ```bash
   python image_classifier.py
   ```
- Enter the path to your dataset and specify the desired parameters (epochs, learning rate, batch size) as prompted.

- The application will start training the model on the specified dataset with the provided parameters.

- Once training is complete, the application will generate an output JSON file (output.json) containing detailed results.
- A 'runs' folder is also generated, which contains the trained model weights.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


