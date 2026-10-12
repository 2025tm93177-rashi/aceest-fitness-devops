# ACEest Fitness & Gym — Automated CI/CD Deployment Workflow

## Project Overview
This repository contains the backend service and automated DevOps pipeline for **ACEest Fitness & Gym**. The solution incorporates a Flask REST API, Pytest automated testing, Docker containerization, and dual CI/CD pipeline automation via GitHub Actions and Jenkins.

---

## Architecture & DevOps Workflow
1. **Source Control:** Git branching model with automated triggers on `push` and `pull_request`.
2. **Local Validation:** Pytest validation for calorie calculations and endpoint behavior.
3. **Containerization:** Docker container packaging running as a non-root user.
4. **Automated CI (GitHub Actions):** Lints code, builds the container image, and runs unit tests inside the container.
5. **Quality Gate (Jenkins):** Pulls code, executes isolated builds, and builds production-ready Docker artifacts.

---

## Local Setup and Execution Instructions

### 1. Run Flask Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
