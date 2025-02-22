// src/frontend/src/App.js
import "app.css";
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import ShelfDetail from './pages/ShelfDetail';
import ProductPerformance from './pages/ProductPerformance';
import TaskManagement from './pages/TaskManagement';
import Analytics from './pages/Analytics';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <div className="main-content">
          <Sidebar />
          <Switch>
            <Route exact path="/" component={Dashboard} />
            <Route path="/shelf/:id" component={ShelfDetail} />
            <Route path="/product/:id" component={ProductPerformance} />
            <Route path="/tasks" component={TaskManagement} />
            <Route path="/analytics" component={Analytics} />
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
