import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os
import hashlib
from blockchain_service import BlockchainService

class TaxModel:
    def __init__(self):
        self.model = LinearRegression()
        self.trained = False
        self.blockchain_service = BlockchainService()
        self.ai_model_version = "1.0.0"

    def train(self):
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'financial_data.csv')
        
        data = pd.read_csv(data_path)
        X = data[['income', 'expenses', 'investments']]
        y = data['tax_liability']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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

            suggestion = f"Consider investing an additional ₹{additional_investment} in tax-saving instruments. This could potentially save you ₹{tax_savings:.2f} in taxes."
        else:
            suggestion = "You've already maximized your tax-saving investments under the current model."

        # Generate hashes for blockchain
        financial_data_hash = hashlib.sha256(f"{income},{expenses},{investments}".encode()).hexdigest()
        computation_hash = hashlib.sha256(f"{current_tax},{max_deduction},{tax_savings}".encode()).hexdigest()

        # Add record to blockchain
        record_id = hashlib.sha256(f"{financial_data_hash}{computation_hash}".encode()).hexdigest()
        self.blockchain_service.add_tax_record(
            record_id,
            financial_data_hash,
            computation_hash,
            True,  # Compliance status
            self.ai_model_version
        )

        return suggestion, record_id

    def verify_tax_record(self, record_id, income, expenses, investments):
        financial_data_hash = hashlib.sha256(f"{income},{expenses},{investments}".encode()).hexdigest()
        return self.blockchain_service.verify_tax_record(record_id, financial_data_hash)

# Usage example
if __name__ == "__main__":
    model = TaxModel()
    model.train()
    suggestion, record_id = model.suggest_tax_savings(800000, 300000, 100000)
    print(suggestion)
    print(f"Record ID: {record_id}")
    
    # Verify the record
    is_valid = model.verify_tax_record(record_id, 800000, 300000, 100000)
    print(f"Record is valid: {is_valid}")
