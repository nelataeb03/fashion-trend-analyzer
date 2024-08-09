# Fashion Trend Analyzer

## Project Motive

As someone passionate about both fashion and technology, I created the Fashion Trend Analyzer to explore the intersection of these two fields. The goal is to analyze and track fashion trends using data from Pinterest, providing insights into the latest styles and preferences. This project combines my love for data science, software engineering, and fashion, demonstrating how technology can be leveraged to gain a deeper understanding of fashion trends.

## Overview
The Fashion Trend Analyzer project leverages machine learning and image processing techniques to analyze fashion trends from social media images. The project segments images, extracts latent spaces, performs clustering, and organizes images into clusters for trend analysis.

## Project Structure
### 1. Data
 - latent_spaces_clustered.json: JSON file containing the clustered latent space data.
 - latent_spaces.json: JSON file containing the latent space data before clustering.
 - posts_1.json & posts_2.json: JSON files containing Instagram post data.
 - posts_comments.csv: CSV file containing the comments extracted from Instagram posts.
 - posts.csv: CSV file containing the posts metadata extracted from Instagram.

### 2. Images
- clustered_images/: Directory where images organized by cluster are saved.
- original_images/: Directory containing the original images downloaded from Instagram.
- segmented_images/: Directory containing segmented images after the image segmentation process.

### 3. models
- autoencoder.h5: Pre-trained autoencoder model used for feature extraction.
- sam_weights.pth: Weights file for the SAM model used in segmentation. (not included)
- sentiment_analysis_model.joblib: Pre-trained model for sentiment analysis on comments.
- yolo_weights.pt: Weights file for the YOLO model used in object detection.

### 4. notebooks
- autoencoder_training.ipynb: Jupyter notebook for training the autoencoder model.
- clustering.ipynb: Jupyter notebook for performing clustering on the latent space.

### 5. scripts
- data_preprocessing.py: Script for preprocessing data before feeding it into models.
- download_images.py: Script for downloading images from Instagram.
- image_segmentation.py: Script for segmenting images using the SAM model.
- latent_space_clustering.py: Script for performing KMeans clustering on the latent spaces.
- latent_space_creation.py: Script for extracting and saving latent spaces from images.
- load_clusters.py: Script to visualize and save clustered images
- sentiment_analysis_model.py: Script for running sentiment analysis on captions

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fashion-trend-analyzer.git
    cd fashion-trend-analyzer
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### 1. Scraping Instagram Data
Use the `download_images.py` script to scrape images and captions from top fashion influencers on Instagram.

### 2. Image Segmentation
Use the `image_segmentation.py` script to segment the scraped images using the SAM model.

### 3. Latent Space Creation
Use the `latent_space_creation.py` script to create latent spaces from the segmented images.

### 4. Clustering Latent Spaces
Use the `latent_space_clustering.py` script to cluster the latent spaces and organize images into clusters.

### 5. Visualizing Clusters
Use the `load_clusters.py` script to visualize the clusters and save the images in directories labeled by cluster.

## Scripts Overview

- **data_preprocessing.py**: Preprocesses Instagram data for further analysis.
- **download_images.py**: Downloads images and captions from selected Instagram profiles.
- **image_segmentation.py**: Segments images using the Segment Anything Model (SAM).
- **latent_space_clustering.py**: Performs KMeans clustering on the latent spaces.
- **latent_space_creation.py**: Extracts latent spaces from images using a pretrained autoencoder.
- **load_clusters.py**: Visualizes clusters and saves clustered images to respective directories.
- **sentiment_analysis_model.py**: Analyzes sentiment of scraped captions.

## Notebooks Overview

- **autoencoder_training.ipynb**: Notebook for training the autoencoder model.
- **clustering.ipynb**: Notebook for performing clustering and analyzing the results.

## Data

The `data` directory contains JSON and CSV files with scraped posts and processed latent space data.

## Models

The `models` directory contains pretrained models used in the project, including the autoencoder, SAM, YOLO, and sentiment analysis models.

## Credits

Some of the code in this repository was adapted from [Future Fashion Trends Forecasting](https://github.com/macedoti13/Future-Fashion-Trends-Forecasting). Special thanks to the original authors for their work and contributions.