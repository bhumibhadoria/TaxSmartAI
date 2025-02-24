import React, { useState } from 'react';
import axios from 'axios';
import './TaxPlanner.css';

function TaxPlanner() {
  const [formData, setFormData] = useState({
    income: '',
    expenses: '',
    investments: ''
  });
  const [suggestion, setSuggestion] = useState('');
  const [recordId, setRecordId] = useState('');
  const [verificationResult, setVerificationResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuggestion('');
    setRecordId('');
    setVerificationResult(null);

    try {
      const response = await axios.post('http://localhost:5000/tax-planner', {
        income: parseInt(formData.income),
        expenses: parseInt(formData.expenses),
        investments: parseInt(formData.investments)
      });
      setSuggestion(response.data.suggestion);
      setRecordId(response.data.record_id);
    } catch (err) {
      setError('An error occurred while fetching the suggestion. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleVerify = async () => {
    setLoading(true);
    setError('');
    setVerificationResult(null);

    try {
      const response = await axios.post('http://localhost:5000/verify-tax-record', {
        record_id: recordId,
        income: parseInt(formData.income),
        expenses: parseInt(formData.expenses),
        investments: parseInt(formData.investments)
      });
      setVerificationResult(response.data.is_valid);
    } catch (err) {
      setError('An error occurred during verification. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="tax-planner">
      <h2>AI Tax Planner</h2>
      <form onSubmit={handleSubmit}>
        {/* ... (existing form inputs) ... */}
        <button type="submit" disabled={loading}>
          {loading ? 'Processing...' : 'Get Tax Suggestions'}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
      {suggestion && (
        <div className="suggestion">
          <h3>Tax Saving Suggestion:</h3>
          <p>{suggestion}</p>
          <p>Record ID: {recordId}</p>
          <button onClick={handleVerify} disabled={loading}>
            Verify Record
          </button>
        </div>
      )}
      {verificationResult !== null && (
        <div className="verification-result">
          <h3>Verification Result:</h3>
          <p>{verificationResult ? 'Record is valid' : 'Record is invalid'}</p>
        </div>
      )}
    </div>
  );
}

export default TaxPlanner;
