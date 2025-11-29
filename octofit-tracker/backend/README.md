# OctoFit Tracker Backend — quick start

This backend contains a small Django project configured to use djongo (MongoDB) and DRF for API endpoints.

Prerequisites
- Python 3.10+ (the project was created using Python 3.10)
- MongoDB running locally on port 27017 (or edit DATABASES in settings to point to your MongoDB)

Activate the venv (absolute path shown — do not cd):
```bash
source /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/activate
```

Install deps (if needed):
```bash
pip install -r /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/requirements.txt
```

Create DB/migrations and run server (when MongoDB is available):
```bash
# create migrations and apply them
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py makemigrations
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py migrate

# create a superuser
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py createsuperuser

# run development server
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

API endpoints (example):
- /api/activities/ — activities endpoint (list/create)
- /api/profiles/ — profiles endpoint (list/create)
- /api/auth/login/ and other auth endpoints provided by `dj-rest-auth`

Notes
- This is a minimal skeleton. Next steps usually include adding permissions, pagination, tests and CI.
