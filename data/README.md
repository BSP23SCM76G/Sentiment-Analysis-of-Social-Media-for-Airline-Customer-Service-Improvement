# Data Directory

This directory contains the dataset used for the sentiment analysis project, focusing on analyzing Twitter posts related to airline services to predict consumer sentiment trends.

## Dataset Source

The primary dataset for this project is the "Twitter US Airline Sentiment" dataset, available on Kaggle. This dataset comprises tweets directed at various US airlines, including sentiment labels (positive, neutral, negative).

## How to Download the Dataset

1. Visit the [Kaggle dataset page](https://www.kaggle.com/crowdflower/twitter-airline-sentiment).
2. If not already done, sign up for a Kaggle account or log in.
3. Click the "Download" button on the dataset page to download the dataset as a `.zip` file.
4. Extract the `.zip` file and place the contents in this directory.

## Data Preprocessing

Before using the dataset for training machine learning models, it's essential to perform several preprocessing steps to clean and prepare the data effectively. These steps include:

- Removing Twitter usernames and URLs.
- Converting all text to lowercase.
- Removing punctuation and special characters.
- Tokenizing the tweets.
- Optionally, balancing the dataset to ensure equal representation of all sentiment classes.

The preprocessing scripts can be found in the `../utils/data_preprocessing.py` file.

## Final Note

Ensure that any personal use of the dataset complies with Kaggle's terms of service and use the data ethically and responsibly.
