import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

class TaxModel:
    def __init__(self):
        self.model = LinearRegression()
        self.trained = False

    def train(self):
        # Correct path to the dataset
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'financial_data.csv')
        
        # Load and prepare data
        data = pd.read_csv(data_path)
        X = data[['income', 'expenses', 'investments']]
        y = data['tax_liability']

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        self.model.fit(X_train, y_train)
        self.trained = True

    def predict_tax_liability(self, income, expenses, investments):
        if not self.trained:
            raise Exception("Model not trained. Call train() first.")
        
        input_data = np.array([[income, expenses, investments]])
        predicted_tax = self.model.predict(input_data)[0]
        return round(predicted_tax, 2)

    def suggest_tax_savings(self, income, expenses, investments):
        current_tax = self.predict_tax_liability(income, expenses, investments)
        max_deduction = 150000  # Example: Section 80C limit in India

        if investments < max_deduction:
            additional_investment = max_deduction - investments
            new_tax = self.predict_tax_liability(income, expenses, max_deduction)
            tax_savings = current_tax - new_tax

            return f"Consider investing an additional ₹{additional_investment} in tax-saving instruments. This could potentially save you ₹{tax_savings:.2f} in taxes."
        else:
            return "You've already maximized your tax-saving investments under the current model."

# Usage example
if __name__ == "__main__":
    model = TaxModel()
    model.train()
    suggestion = model.suggest_tax_savings(800000, 300000, 100000)
    print(suggestion)
