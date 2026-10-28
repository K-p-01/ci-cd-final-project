# cicd-final-project

**Project name:** `cicd-final-project`  
**Repository name recommended for this submission:** `ci-cd-final-project`

A small Flask web application for the Coursera CI/CD Tools and Practices final project. It demonstrates GitHub Actions for continuous integration and Tekton/OpenShift Pipelines for container build and deployment.

![CI](https://github.com/K-p-01/ci-cd-final-project/actions/workflows/workflow.yml/badge.svg)

## Application

- Flask service listens on port `8000` by default.
- `GET /` returns a welcome message.
- `GET /health` returns a JSON health response.
- Startup logs include `SERVICERUNNING on port 8000`.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install "setuptools<70" -r requirements.txt -r requirements-dev.txt
python app.py
```

On macOS/Linux, activate the virtual environment with `source .venv/bin/activate` instead.

Browse to `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/health`.

## Test locally

```bash
flake8 app.py tests scripts
python scripts/run_nose.py
```

## GitHub Actions

`.github/workflows/workflow.yml` checks out the repository, installs Python dependencies, runs Flake8 linting, and runs nose unit tests on pushes and pull requests to `main`.

## OpenShift / Tekton

The `.tekton` directory contains:

- `tasks.yml`: cleanup (with a `remove` step that deletes files in `WORKSPACE_SOURCE_PATH`), clone, Flake8, nose unit tests, Buildah build/push, and OpenShift deployment.
- `pipeline.yml`: `oc-pipelines-oc-final`, with the six expected stages in order.
- `pvc.yml`: 1 GiB PVC named `oc-lab-pvc`, storage class `skills-network-learner`.

The cluster's image registry, security constraints, permissions, and installed Tekton version can differ. Apply resources only in your assigned course namespace and follow the course lab's service-account/security instructions.

Example preparation commands from a terminal already logged in to the course cluster:

```bash
oc project
oc apply -f .tekton/pvc.yml
oc apply -f .tekton/tasks.yml
oc apply -f .tekton/pipeline.yml
```

Check PVC readiness:

```bash
oc get pvc oc-lab-pvc
```

Then start the pipeline with your actual public repository URL and cluster image path. The usage notes in `.tekton/README.md` give an example. A successful run must be verified in your own cluster; source files alone are not evidence that it deployed.

## Coursera file URLs

After the repository is public and these files are pushed to `main`, use the following paths:

- README: `https://github.com/K-p-01/cicd-final-project/blob/main/README.md` (GitHub may redirect this legacy repository URL after the repository is renamed).
- GitHub Actions workflow: `https://github.com/K-p-01/ci-cd-final-project/blob/main/.github/workflows/workflow.yml`
- Tekton tasks: `https://github.com/K-p-01/ci-cd-final-project/blob/main/.tekton/tasks.yml`

The rubric previously gave contradictory repository-slug feedback across questions. Keep the project name text `cicd-final-project` in this README while using the repository slug `ci-cd-final-project` for the Q2/Q3 links, which the evaluator explicitly requested.

## Required evidence files

See `evidence/README.md`. Capture screenshots and log text from your actual GitHub/OpenShift environment. Do not substitute examples or mockups for genuine run evidence.
