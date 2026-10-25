# Customer Accounts Microservice

Flask REST API for the IBM DevOps Capstone assignment.

[![CI](https://github.com/shravanishep/oaqjp-final-project-emb-ai/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/shravanishep/oaqjp-final-project-emb-ai/actions/workflows/ci-build.yaml)

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:DATABASE_URL = "sqlite:///accounts.db"
python app.py
```

The service listens on `http://localhost:8080`.

## API

| Method | URL | Purpose |
| --- | --- | --- |
| POST | `/accounts` | Create an account |
| GET | `/accounts` | List accounts |
| GET | `/accounts/<id>` | Read one account |
| PUT/PATCH | `/accounts/<id>` | Update an account |
| DELETE | `/accounts/<id>` | Delete an account |
| GET | `/health` | Health check |

Example:

```powershell
Invoke-RestMethod http://localhost:8080/accounts -Method Post `
  -ContentType "application/json" `
  -Body '{"first_name":"Ada","last_name":"Lovelace","email":"ada@example.com"}'
```

## Verification

```powershell
python -m pytest -q
python -m flake8 .
```

## Docker

```powershell
docker build -t customer-accounts:latest .
docker run --rm -p 8080:8080 customer-accounts:latest
```

## Kubernetes

```powershell
kubectl apply -f k8s\accounts.yaml
kubectl get deployments,pods,services
kubectl port-forward service/accounts 8080:8080
```

## Project links

- [Application](app.py)
- [Security configuration](accounts/__init__.py)
- [Tests](tests/test_accounts.py)
- [Dependencies](requirements.txt)
- [CI workflow](.github/workflows/ci-build.yaml)
- [Dockerfile](Dockerfile)
- [Kubernetes manifest](k8s/accounts.yaml)
- [User stories](user-story.md)
- [Submission guide](CAPSTONE_SUBMISSION_GUIDE.md)
- [Evidence directory](evidence/)

Remote repository: <https://github.com/shravanishep/oaqjp-final-project-emb-ai>

External GitHub Project, screenshots, Kubernetes cluster output, and Tekton runs must be added only after they are genuinely performed.
