import React, { useState, useEffect } from "react";
import axios from "axios";
import { FaCalculator, FaCheckCircle, FaExclamationCircle } from "react-icons/fa";
import "./components/TaxPlanner.css";


function TaxPlanner() {
  const [formData, setFormData] = useState({
    income: "",
    expenses: "",
    investments: "",
  });
  const [suggestion, setSuggestion] = useState("");
  const [blockchainRecord, setBlockchainRecord] = useState(null);
  const [verificationResult, setVerificationResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [fetchedData, setFetchedData] = useState(null);

  useEffect(() => {
    fetch("https://taxsmart-backend.onrender.com/")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setFetchedData(data);
      })
      .catch((err) => console.error("Error fetching data:", err));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSuggestion("");
    setBlockchainRecord(null);
    setVerificationResult(null);

    try {
      const response = await axios.post("https://taxsmart-backend.onrender.com/tax-planner", {
        income: parseInt(formData.income),
        expenses: parseInt(formData.expenses),
        investments: parseInt(formData.investments),
      });
      setSuggestion(response.data.suggestion);
      setBlockchainRecord(response.data.blockchain_record);
    } catch (err) {
      setError("An error occurred while fetching the suggestion. Please try again.");
      console.error("Error:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleVerify = async () => {
    setLoading(true);
    setError("");
    setVerificationResult(null);

    try {
      const response = await axios.post("https://taxsmart-backend.onrender.com/verify-tax-record", {
        block_index: blockchainRecord.block_index,
      });
      setVerificationResult(response.data.valid);
    } catch (err) {
      setError("An error occurred during verification. Please try again.");
      console.error("Error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="tax-planner-container">
      <h1 className="project-title">TaxSmart AI</h1>
      <div className="tax-planner-card">
        <h2 className="title">
          <FaCalculator className="icon" /> AI Tax Planner
        </h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="income">Annual Income (₹)</label>
            <input
              type="number"
              id="income"
              name="income"
              value={formData.income}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="expenses">Annual Expenses (₹)</label>
            <input
              type="number"
              id="expenses"
              name="expenses"
              value={formData.expenses}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="investments">Current Investments (₹)</label>
            <input
              type="number"
              id="investments"
              name="investments"
              value={formData.investments}
              onChange={handleChange}
              required
            />
          </div>
          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? "Processing..." : "Get Tax Suggestions"}
          </button>
        </form>

        {error && <p className="error"><FaExclamationCircle /> {error}</p>}

        {suggestion && (
          <div className="suggestion">
            <h3>Tax Saving Suggestion:</h3>
            <p>{suggestion}</p>
            {blockchainRecord && (
              <div className="blockchain-info">
                <p><strong>Block Index:</strong> {blockchainRecord.block_index}</p>
                <p><strong>Block Hash:</strong> {blockchainRecord.block_hash}</p>
                <p><strong>Timestamp:</strong> {blockchainRecord.timestamp}</p>
                <button onClick={handleVerify} className="verify-btn" disabled={loading}>
                  Verify Record
                </button>
              </div>
            )}
          </div>
        )}

        {verificationResult !== null && (
          <div className={`verification-result ${verificationResult ? "valid" : "invalid"}`}>
            <h3>
              {verificationResult ? <FaCheckCircle /> : <FaExclamationCircle />} Verification Result:
            </h3>
            <p>{verificationResult ? "Record is valid ✅" : "Record is invalid ❌"}</p>
          </div>
        )}
      </div>

      {/* Display fetched data */}
      {fetchedData && (
        <div className="fetched-data">
          <h3>Fetched Data:</h3>
          <pre>{JSON.stringify(fetchedData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default TaxPlanner;
