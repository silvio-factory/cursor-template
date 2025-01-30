# Backend

This directory contains the FastAPI-based backend server implementation of our SaaS application.

## Directory Structure

- `src/` - Main source code directory
  - `api/` - API routes and endpoint handlers
  - `models/` - Database models and schemas
  - `services/` - Business logic and service layer
  - `utils/` - Helper functions and utilities
  - `ai/` - AI/ML integration code
- `tests/` - Test files and test utilities
- `.env` - Environment variables configuration
- `requirements.txt` - Python package dependencies

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

- Windows: `.venv\Scripts\activate`
- Unix/MacOS: `source .venv/bin/activate`

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Development

To run the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation will be available at `http://localhost:8000/docs`
