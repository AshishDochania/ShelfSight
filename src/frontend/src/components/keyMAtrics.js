import React from 'react';

const KeyMetrics = ({ outOfStock, planogramCompliance, salesImpact }) => (
  <div className="key-metrics">
    <div className="metric">
      <h3>Out of Stock Items</h3>
      <p>{outOfStock}</p>
    </div>
    <div className="metric">
      <h3>Planogram Compliance</h3>
      <p>{planogramCompliance}%</p>
    </div>
    <div className="metric">
      <h3>Estimated Sales Impact</h3>
      <p>${salesImpact}</p>
    </div>
  </div>
);

export default KeyMetrics;