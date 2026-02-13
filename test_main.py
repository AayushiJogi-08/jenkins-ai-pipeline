
# test_main.py
import unittest
import joblib
from main import train_model

class TestModel(unittest.TestCase):
    def test_training(self):
        train_model()
        model = joblib.load("model.pkl")
        self.assertIsNotNone(model)

if __name__ == "__main__":
    unittest.main()
