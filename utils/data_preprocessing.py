# Script for data cleaning and preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle


# Load the dataset
tweets_df = pd.read_csv('../data/Tweets.csv')

# Fill missing 'negativereason_confidence' values with 0
tweets_df['negativereason_confidence'] = tweets_df['negativereason_confidence'].fillna(0)

# Drop columns that are not essential for our analysis
tweets_df.drop(columns=['tweet_coord', 'tweet_location', 'user_timezone', 'airline_sentiment_gold', 'negativereason_gold'], inplace=True)

# Normalize 'tweet_created' to datetime format
tweets_df['tweet_created'] = pd.to_datetime(tweets_df['tweet_created'])

# Selecting features and target
X = tweets_df['text']
y = tweets_df['airline_sentiment']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preparing the preprocessed data for pickling
preprocessed_data = {
    "X_train": X_train,
    "X_test": X_test,
    "y_train": y_train,
    "y_test": y_test
}

# Specifying the path for the pickle file
pickle_file_path = '../data/preprocessed_tweets.pkl'

# Pickling the preprocessed data
with open(pickle_file_path, 'wb') as file:
    pickle.dump(preprocessed_data, file)

# Save as csv file
tweets_df.to_csv('../data/preprocessed_tweets.csv', index=False)