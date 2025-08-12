import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data():
    # Load dataset
    data = pd.read_csv('data/house_prices.csv')
    # Select features and target variable
    X = data[['OverallQual', 'GrLivArea', 'GarageCars', 'FullBath', 'YearBuilt']]
    y = data['SalePrice']
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Save preprocessed data
    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)

if __name__ == "__main__":
    preprocess_data()
