from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset (mock financial data)
data = pd.read_csv('../data/financial_data.csv')

# Simple rule-based tax-saving function
def suggest_tax_savings(income, expenses, investments):
    max_investment_limit = 150000  # Section 80C limit in India
    suggested_investment = max(0, max_investment_limit - investments)
    tax_saving_tip = f"Invest an additional ₹{suggested_investment} in tax-saving instruments."
    return tax_saving_tip

@app.route('/tax-planner', methods=['POST'])
def tax_planner():
    user_data = request.json  # Get JSON data from the frontend
    income = user_data['income']
    expenses = user_data['expenses']
    investments = user_data['investments']

    suggestion = suggest_tax_savings(income, expenses, investments)
    return jsonify({'suggestion': suggestion})

if __name__ == '__main__':
    app.run(debug=True)
