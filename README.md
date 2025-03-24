# TaxSmart AI

## Overview
TaxSmart AI is an innovative tax planning application that combines artificial intelligence and blockchain technology to provide secure, transparent, and efficient tax advice. It helps users optimize their tax planning while ensuring the integrity and immutability of financial records.

## Solution Approach
TaxSmart AI employs a combination of AI, blockchain, and modern web technologies to streamline tax management. The key components include:

- **AI-driven tax planning suggestions**: Utilizing Scikit-learn models to analyze financial data and provide intelligent tax-saving recommendations.
- **Blockchain-based immutable audit trail**: Ethereum smart contracts (using Truffle and Ganache) ensure transparency and security in financial record-keeping.
- **User-friendly interface**: A React-based frontend that allows users to input financial details and receive insights seamlessly.
- **Verification system for tax records**: Ensures authenticity and compliance using blockchain validation mechanisms.

## Technologies Used
- **Frontend**: React
- **Backend**: Flask
- **AI Model**: Scikit-learn
- **Blockchain**: Ethereum (Truffle, Ganache)
- **Database**: PostgreSQL

## Architectue Diagram
<img width="362" alt="image" src="https://github.com/user-attachments/assets/9d780369-b6ba-4b64-a728-adcf87fa85d4" />


## Results
- **AI Tax Optimization**: Analyzes tax-saving opportunities and provides users with personalized recommendations.
- **Blockchain Verification**: Ensures tax documents are tamper-proof and accessible for audits.
- **User Insights Dashboard**: Displays financial metrics and tax efficiency scores in an interactive format.
  ![WhatsApp Image 2025-02-25 at 23 48 27_f63c5fc9](https://github.com/user-attachments/assets/89a7bc08-d4fb-4cdf-90e1-19e2c1e44c9d)


## Getting Started
To set up and run TaxSmart AI on your local machine, follow these steps:

### Clone the Repository
```bash
git clone https://github.com/yourusername/taxsmart-ai.git
cd taxsmart-ai
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd ../frontend
npm install
```

### Blockchain Setup
```bash
cd ../blockchain
npm install -g truffle
truffle migrate
```

## Usage
### Start the Backend Server
```bash
cd backend
python app.py
```

### Start the Frontend Development Server
```bash
cd frontend
npm start
```

Navigate to [TaxSmart AI](https://taxsmart.netlify.app/) to access the application.

## License
This project is licensed under the MIT License.
