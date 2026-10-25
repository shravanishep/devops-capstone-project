# IBM DevOps Capstone submission guide

Repository: https://github.com/shravanishep/oaqjp-final-project-emb-ai  
All public file URLs below use the `main` branch.

The following answers use only evidence actually observed. Items requiring
GitHub Project screenshots, a Kubernetes cluster, or Tekton remain pending or
blocked; no screenshots or successful external logs are fabricated.

| Task | Points | Exact answer / URL / filename | Status |
| ---: | ---: | --- | --- |
| 1 | 1 | https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/README.md | Verified after push; badge points to the CI workflow |
| 2 | 1 | https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/user-story.md | Verified |
| 3 | 1 | Upload `planning-userstories-done.png` after capturing New Issues column. | Pending manual screenshot |
| 4 | 1 | Upload `planning-productbacklog-done.png` after capturing Ice Box column. | Pending manual screenshot |
| 5 | 1 | Upload `planning-labels-done.png` after capturing Product Backlog labels. | Pending manual screenshot |
| 6 | 1 | Upload `planning-kanban-done.png` after capturing Sprint Backlog estimates and Sprint 1. | Pending manual screenshot |
| 7 | 1 | https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/setup.cfg | Verified |
| 8 | 1 | Upload `rest-techdebt-done.png` showing setup story in Done. | Pending manual screenshot |
| 9 | 1 | Upload `read-accounts.png` showing read story in Done. | Pending manual screenshot |
| 10 | 1 | Upload `list-accounts.png` showing list story in Done. | Pending manual screenshot |
| 11 | 1 | Upload `update-accounts.png` showing update story in Done. | Pending manual screenshot |
| 12 | 1 | Upload `delete-accounts.png` showing delete story in Done. | Pending manual screenshot |
| 13 | 2 | Copy the complete contents of `evidence/rest-create-done`. | Verified locally |
| 14 | 2 | Copy the complete contents of `evidence/rest-list-done`. | Verified locally |
| 15 | 2 | Copy the complete contents of `evidence/rest-read-done`. | Verified locally |
| 16 | 2 | Copy the complete contents of `evidence/rest-update-done`. | Verified locally |
| 17 | 2 | Copy the complete contents of `evidence/rest-delete-done`. | Verified locally |
| 18 | 1 | Upload `sprint2-plan.png` showing the two Sprint 2 stories. | Pending manual screenshot |
| 19 | 2 | Copy the complete successful GitHub Actions output into `ci-workflow-done`. | Pending: latest run must finish successfully |
| 20 | 1 | Upload `ci-kanban-done.png` showing CI story in Done. | Pending manual screenshot |
| 21 | 4 | https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/.github/workflows/ci-build.yaml | Configured; remote run pending |
| 22 | 1 | https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/accounts/__init__.py | Verified; Talisman configuration is in this file |
| 23 | 1 | Copy `evidence/security-headers-done`. | Verified locally: 4 tests passed |
| 24 | 1 | Upload `security-kanban-done.png` showing security story in Done. | Pending manual screenshot |
| 25 | 1 | Upload `sprint3-plan.png` showing the three Sprint 3 stories. | Pending manual screenshot |
| 26 | 1 | Copy `evidence/kube-app-output` only after a Kubernetes port-8080 response exists. | Blocked: Kubernetes API unavailable |
| 27 | 1 | Upload `kube-docker-done.png` showing Docker story in Done. | Pending manual screenshot |
| 28 | 1 | Upload `kube-kubernetes-done.png` only after a real deployment. | Blocked: Kubernetes API unavailable |
| 29 | 2 | https://github.com/shravanishep/oaqjp-final-project-emb-ai/blob/main/Dockerfile | Verified |
| 30 | 2 | Copy `evidence/kube-images`. | Verified: local Docker image metadata |
| 31 | 2 | Copy `evidence/kube-deploy-accounts` after a real cluster deployment. | Blocked: Kubernetes API unavailable |
| 32 | 5 | Copy `evidence/pipelinerun.txt` after a real successful Tekton run. | Blocked: Tekton/cluster unavailable |
| 33 | 1 | Upload `cd-pipeline-done.png` after the CD pipeline deploys successfully. | Blocked pending Tekton deployment |

## Exact local text answers

### Tasks 13-17

The complete command and output for each REST operation is saved in the
extensionless files under `evidence/`:

```text
evidence/rest-create-done
evidence/rest-list-done
evidence/rest-read-done
evidence/rest-update-done
evidence/rest-delete-done
```

The verified sequence creates account ID 2, reads it, updates its last name
to Murray, lists it, and deletes it with HTTP 204.

### Task 23

```text
COMMAND: python -m pytest -q
OUTPUT:
....                                                                     [100%]
4 passed in 0.56s
```

This verifies the Accounts service tests, security headers, and CORS
preflight test. The exact saved file is `evidence/security-headers-done`.

### Task 30

The saved `evidence/kube-images` contains the locally observed Docker image
name, tag, image ID, creation time, and size. This is Docker verification, not
Kubernetes verification.

## Remaining actions before submission

1. Open the GitHub Actions workflow and wait for the current run to finish:
   https://github.com/shravanishep/oaqjp-final-project-emb-ai/actions
   Copy the full successful run output into `ci-workflow-done`.
2. Create the GitHub Project with columns New Issues, Ice Box, Product
   Backlog, Sprint Backlog, and Done. Create the required issues, labels,
   estimates, and sprint assignments. Capture each requested screenshot using
   the exact filename in Tasks 3-6, 8-12, 18, 20, 24-25, and 27-28.
3. Start an authorized Kubernetes cluster, then run:

   ```powershell
   kubectl apply -f k8s\accounts.yaml
   kubectl get deployments,pods,replicasets,services
   kubectl port-forward service/accounts 8080:8080
   ```

   Save the actual outputs to `kube-deploy-accounts` and `kube-app-output`.
4. Install Tekton in that cluster, apply `tekton\task.yaml`,
   `tekton\pipeline.yaml`, and `tekton\pipelinerun.yaml`, run the PipelineRun,
   and save the complete real logs to `pipelinerun.txt`.
5. Capture the CD screenshot only after the real deployment succeeds.
