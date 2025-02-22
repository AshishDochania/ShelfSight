// src/frontend/src/pages/TaskManagement.js
import React, { useState, useEffect } from 'react';

const TaskManagement = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    // Fetch tasks from API
  }, []);

  return (
    <div className="task-management">
      <h2>Task Management</h2>
      <ul className="task-list">
        {tasks.map(task => (
          <li key={task.id} className={`task ${task.priority}`}>
            {task.description}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskManagement;