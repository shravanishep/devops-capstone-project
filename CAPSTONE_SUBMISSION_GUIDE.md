# IBM DevOps Capstone audit and submission guide

Repository: https://github.com/shravanishep/oaqjp-final-project-emb-ai  
Branch: `main`

## Important limits

The supplied assignment description states **33 tasks worth 50 points**, but it
does not include the official task numbering, individual task names, or
per-task point allocation. The task labels below are therefore an explicit
mapping to the requirements in the supplied description, not a claim that they
are the hidden IBM rubric's exact numbering. Per-task points are **not stated
in the supplied material**; do not invent them when submitting.

Public file URL pattern:
`https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/<path>`

## Tasks 1-33

| Task | Points | Exact answer / submission text | Public URL or evidence | Status |
| ---: | :--- | --- | --- | --- |
| 1 | Not stated | Workspace inspected; existing Git repository and remote preserved. | [README.md](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/README.md) | Verified |
| 2 | Not stated | Python Flask project initialized with dependency and ignore files. | [requirements.txt](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/requirements.txt), [.gitignore](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/.gitignore) | Verified |
| 3 | Not stated | User stories documented for setup, CRUD, CI, security, Docker, Kubernetes, and CD. | [user-story.md](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/user-story.md) | Verified locally; GitHub board pending |
| 4 | Not stated | Create GitHub Project columns New Issues, Ice Box, Product Backlog, Sprint Backlog, and Done. | No URL captured; create manually in GitHub Project. | Pending |
| 5 | Not stated | Add Technical Debt and Enhancement labels, estimates, and sprint assignments. | No URL captured; create manually in GitHub Issues/Project. | Pending |
| 6 | Not stated | Create the required user-story issues and move them through the board. | No issue URLs captured. | Pending |
| 7 | Not stated | Development environment setup is documented and reproducible. | [README.md](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/README.md) | Verified |
| 8 | Not stated | `POST /accounts` creates an account and returns HTTP 201. | [app.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/app.py), `evidence/rest-create-done.txt` | Verified locally |
| 9 | Not stated | `GET /accounts/<id>` reads an account and returns HTTP 200 or HTTP 404. | [app.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/app.py), `evidence/rest-read-done.txt` | Verified locally |
| 10 | Not stated | `GET /accounts` lists accounts. | [app.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/app.py), `evidence/rest-list-done.txt` | Verified locally |
| 11 | Not stated | `PUT` and `PATCH /accounts/<id>` update an account. | [app.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/app.py), `evidence/rest-update-done.txt` | Verified locally |
| 12 | Not stated | `DELETE /accounts/<id>` deletes an account and returns HTTP 204. | [app.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/app.py), `evidence/rest-delete-done.txt` | Verified locally |
| 13 | Not stated | Invalid input and missing accounts return JSON errors with HTTP 400/404. | [tests/test_accounts.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/tests/test_accounts.py) | Verified locally |
| 14 | Not stated | SQLite persistence is used for accounts. | [app.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/app.py) | Verified locally |
| 15 | Not stated | CRUD tests cover create, list, read, update, delete, validation, and missing records. | [tests/test_accounts.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/tests/test_accounts.py) | Verified locally |
| 16 | Not stated | REST command evidence is internally consistent. | `evidence/rest-*-done.txt` | Verified locally |
| 17 | Not stated | `python -m pytest -q` completed successfully. | `evidence/pytest-output.txt` | Verified |
| 18 | Not stated | `python -m flake8 .` completed successfully. | `evidence/flake8-output.txt` | Verified |
| 19 | Not stated | Coverage completed at 93%. | `evidence/coverage-report.txt` | Verified |
| 20 | Not stated | Pylint completed with rating 10.00/10. | `evidence/pylint-output.txt` | Verified |
| 21 | Not stated | `setup.cfg` contains pytest, coverage, nosetests, Flake8, and Pylint sections. | [setup.cfg](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/setup.cfg) | Verified |
| 22 | Not stated | CI workflow installs dependencies, runs Flake8, and runs pytest on push/PR. | [ci-build.yaml](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/.github/workflows/ci-build.yaml) | Configured; remote run pending |
| 23 | Not stated | GitHub Actions must be run after push and its real run URL submitted. | No run URL observed. | Pending |
| 24 | Not stated | Talisman security headers are enabled. | [app.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/app.py), `evidence/pytest-output.txt` | Verified locally |
| 25 | Not stated | CORS is configured and preflight behavior is tested. | [app.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/app.py), [tests/test_accounts.py](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/tests/test_accounts.py) | Verified locally |
| 26 | Not stated | Dockerfile builds a non-root image exposing port 8080. | [Dockerfile](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/Dockerfile), `evidence/docker-build.txt` | Verified locally |
| 27 | Not stated | Docker container responded to `GET /health` with `{"status":"ok"}`. | `evidence/docker-app-output.txt`, `evidence/kube-images.txt` | Verified locally |
| 28 | Not stated | Kubernetes Deployment and Service manifests are prepared. | [k8s/accounts.yaml](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/k8s/accounts.yaml) | Prepared; cluster deployment pending |
| 29 | Not stated | Kubernetes deployment output must be captured with `kubectl get deployments,pods,replicasets,services`. | `evidence/kubernetes-get-nodes.txt` records current cluster failure; no deployment output exists. | Blocked: cluster API unavailable |
| 30 | Not stated | Kubernetes application response must be captured after port-forwarding. | No `kube-app-output` exists because no cluster deployment was verified. | Blocked |
| 31 | Not stated | Tekton Task, Pipeline, and PipelineRun manifests are prepared. | [tekton/task.yaml](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/tekton/task.yaml), [tekton/pipeline.yaml](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/tekton/pipeline.yaml), [tekton/pipelinerun.yaml](https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/tekton/pipelinerun.yaml) | Prepared; run pending |
| 32 | Not stated | Tekton PipelineRun logs and successful deployment must be captured. | No `pipelinerun.txt`; no successful PipelineRun observed. | Blocked: Tekton/cluster unavailable |
| 33 | Not stated | Genuine GitHub Project, CI, Docker, Kubernetes, and Tekton screenshots must be captured. | No screenshots are claimed; see manual instructions below. | Pending |

## Complete verified command output

### Tests

```text
....                                                                     [100%]
4 passed in 0.56s
```

### Coverage

```text
Name     Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------
app.py      89      4     20      4    93%   69, 72, 129, 136
----------------------------------------------------
TOTAL       89      4     20      4    93%
```

### Pylint

```text
Your code has been rated at 10.00/10
```

### REST CRUD

The complete commands and actual outputs are in:

- `evidence/rest-create-done.txt`
- `evidence/rest-list-done.txt`
- `evidence/rest-read-done.txt`
- `evidence/rest-update-done.txt`
- `evidence/rest-delete-done.txt`

The verified sequence created account ID 2, read it, updated the last name to
Murray, listed it, and deleted it with HTTP 204.

### Docker

```text
Name=customer-accounts:latest
ImageID=sha256:e2a31bd18e8d9b93ab7cc80457304dc2c97cf92d7cb8109717667a6d42bfa4b9
```

The actual image metadata and container response are in
`evidence/kube-images.txt` and `evidence/docker-app-output.txt`.

## Manual actions required before submission

1. Push is performed by this audit commit. Open the repository URL above and
   confirm the files are publicly visible.
2. Create the GitHub Project board and five columns. Create the required
   issues, labels, estimates, sprint assignments, and capture the requested
   board screenshots.
3. Open the pushed GitHub Actions workflow. Wait for a real successful run and
   paste that run URL into Task 23.
4. Start a supported Kubernetes cluster. Run:

   ```powershell
   docker build -t customer-accounts:latest .
   kubectl apply -f k8s\accounts.yaml
   kubectl get deployments,pods,replicasets,services
   kubectl port-forward service/accounts 8080:8080
   ```

   Save the real command output as `kube-deploy-accounts` and the real HTTP
   response as `kube-app-output`.
5. Install/configure Tekton in that cluster, apply the three files under
   `tekton\`, run a real PipelineRun, save its logs as `pipelinerun.txt`, and
   capture the deployment result.
6. Capture genuine screenshots only from the actual GitHub Project, successful
   Actions run, terminal, running container, Kubernetes state, and Tekton
   dashboard. Do not create placeholder images.
