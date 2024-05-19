# Auto Image Classifier

The Auto Image Classifier is an application for image classification using a pre-trained YOLO (You Only Look Once) model. It allows users to train the model on their own dataset, specifying parameters such as epochs, learning rate, and batch size. After training, the application generates an output JSON file containing detailed results.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction
The Auto Image Classifier provides a convenient way to perform image classification tasks using a pre-trained YOLO model. Users can train the model on their custom datasets, fine-tuning the parameters to achieve optimal performance.

## Features
- Utilizes a pre-trained YOLO model for image classification.
- Enables training on custom datasets with customizable parameters.
- Provides detailed training results in an output JSON file.

## Installation
To use the Auto Image Classifier, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/vamshigaddi/auto-image-classifier.git

   ```
   ```bash
   pip install -r requirements.txt
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
## License
This project is licensed under the MIT License. See the LICENSE file for details.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


