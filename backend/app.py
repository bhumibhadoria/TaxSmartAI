from flask import Flask, request, jsonify
from flask_cors import CORS
from tax_model import TaxModel

app = Flask(__name__)
CORS(app)

# Initialize and train the model
tax_model = TaxModel()
tax_model.train()

@app.route('/tax-planner', methods=['POST'])
def tax_planner():
    user_data = request.json
    income = user_data['income']
    expenses = user_data['expenses']
    investments = user_data['investments']

    suggestion, record_id = tax_model.suggest_tax_savings(income, expenses, investments)
    return jsonify({
        'suggestion': suggestion,
        'record_id': record_id
    })

@app.route('/verify-tax-record', methods=['POST'])
def verify_tax_record():
    data = request.json
    record_id = data['record_id']
    income = data['income']
    expenses = data['expenses']
    investments = data['investments']

    is_valid = tax_model.verify_tax_record(record_id, income, expenses, investments)
    return jsonify({'is_valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)
