# main.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

def train_model():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    
    # Save model
    joblib.dump(clf, "model.pkl")
    print("Model trained and saved as model.pkl")

if __name__ == "__main__":
    train_model()