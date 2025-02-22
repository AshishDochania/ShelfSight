import React, { useState, useEffect } from 'react';
import StoreLayout from '../components/StoreLayout';
import KeyMetrics from '../components/KeyMetrics';

const Dashboard = () => {
  const [shelves, setShelves] = useState([]);
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    // Fetch shelf data and metrics from API
    // This is where you'd make API calls to your backend
  }, []);

  return (
    <div className="dashboard">
      <h2>Store Overview</h2>
      <StoreLayout shelves={shelves} />
      <KeyMetrics {...metrics} />
    </div>
  );
};

export default Dashboard;