import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [jobs, setJobs] = useState([]);
  const [company, setCompany] = useState('');
  const [role, setRole] = useState('');

  const fetchJobs = async () => {
    try {
      const res = await axios.get('http://localhost:5000/jobs');
      setJobs(res.data);
    } catch (error) {
      console.error("Error fetching jobs", error);
    }
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  const addJob = async () => {
    if (!company.trim() || !role.trim()) {
      alert("Please enter company and role");
      return;
    }

    await axios.post('http://localhost:5000/jobs', {
      company: company.trim(),
      role: role.trim(),
      status: "Applied"
    });

    setCompany('');
    setRole('');
    fetchJobs();
  };

  const updateStatus = async (id) => {
    await axios.put(`http://localhost:5000/jobs/${id}`, {
      status: "Interview"
    });
    fetchJobs();
  };

  const runAI = async () => {
    const res = await axios.post('http://localhost:5000/ai/match');
    alert(JSON.stringify(res.data, null, 2));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Job Tracker</h1>

      {/* AI Button */}
      <button onClick={runAI}>Run AI Match</button>

      {/* Input Section */}
      <div style={{ marginTop: 10, marginBottom: 15 }}>
        <input
          placeholder="Company"
          value={company}
          onChange={e => setCompany(e.target.value)}
          style={{ marginRight: 10 }}
        />

        <input
          placeholder="Role"
          value={role}
          onChange={e => setRole(e.target.value)}
          style={{ marginRight: 10 }}
        />

        <button onClick={addJob} disabled={!company || !role}>
          Add Job
        </button>
      </div>

      <h3>Job List</h3>

      <ul>
        {jobs.map(job => (
          <li key={job[0]}>
            {job[1]} - {job[2]} - {job[3]}{" "}
            <button onClick={() => updateStatus(job[0])}>
              Move to Interview
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;