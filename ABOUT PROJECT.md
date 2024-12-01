# BrainDiverseX: Brain Tumor Type Classification System Utilizes Deep Learning with Convolutional Neural Network (CNN) Algorithm

## Domain Project

The brain tumor classification system using CNN algorithm is designed to classify brain tumors into three types: Meningioma, Glioma, and Pituitary. With this capability, the system can accurately classify MRI scan images.

## Business Understanding
### Problem Statements
- How can the system effectively classify brain tumor types based on MRI scan images?
- What is the classification accuracy using the CNN algorithm?

## Goals
The project aims to determine the effectiveness and accuracy of classification from MRI scan images for brain tumor detection purposes.

## Solution Statements
To achieve these goals, we searched for a dataset containing MRI scan images. The dataset is limited to three tumor types: Meningioma, Glioma, and Pituitary.

The algorithm used for this task is Convolutional Neural Network. The model is trained with an image dataset divided into 3 folders: meningioma (708 images), glioma (1426 images), and pituitary (930 images).

## Data Uderstanding
The project uses a dataset consisting of 3 image folders. Each folder represents a brain tumor type to be classified: meningioma (708 images), glioma (1426 images), and pituitary (930 images). The dataset can be viewed at the following link [[HERE]](https://www.kaggle.com/datasets/denizkavi1/brain-tumor)

These three folders contain MRI scan images. Therefore, the model produced in this project is only capable of accurately detecting MRI scans.

## Data Preparation
Data preprocessing involves several steps:

- Each image will be scaled to a range of [0, 1]. This is important because many ML and DL algorithms are more effective when input is normalized
- Randomly rotate images within a 20-degree range
- Allow horizontal image flipping

## Modeling
The modeling involves several configurations to achieve maximum accuracy:

- The model consists of 4 convolutional layers divided into 2 parts. Each part is separated by 1 ```MaxPool2D()``` layer
- Each layer has a ReLU activation function
- Convolutional layers consist of 32 neurons
2 hidden layers process the ```Flatten()``` results
- The first hidden layer contains 256 neurons and the second hidden layer contains 128 neurons
- Uses ```categorical_crossentropy``` loss function
```Adam``` optimizer is used
- ```Callback``` is used to prevent overfitting
- 30 epochs are used.

## Evaluation
The project evaluation process measures accuracy. The obtained accuracy value is 95.59%.

## Recommendation
Recommendations for similar projects using the same dataset include:

- Use CNN-based algorithms or models like ResNet, AlexNet, and others
- Calculate additional evaluation metrics such as F1-Score, precision, recall, and others
