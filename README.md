# AI Job Tracker

## Overview
A full-stack job tracking application with AI-powered resume matching.

## Tech Stack
- Backend: Flask (Python)
- Frontend: React
- Database: SQLite

## Features
- Add and manage job applications
- Update application status
- AI-based resume matching suggestions

## Architecture
- REST API using Flask
- React frontend communicates via Axios
- SQLite for persistent storage

## API Endpoints
- GET /jobs
- POST /jobs
- PUT /jobs/<id>
- POST /ai/match

## How to Run

### Backend
cd backend
venv\Scripts\activate
python app.py

### Frontend
cd frontend
npm start

## AI Usage
- Used structured prompt design
- Mock AI response for controlled output

## Tradeoffs
- Used SQLite for simplicity
- AI is mocked instead of real API

## Future Improvements
- Add authentication
- Deploy to cloud
- Real AI integration
