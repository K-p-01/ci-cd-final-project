# CI/CD Final Project

A small Flask web application used to demonstrate an end-to-end CI/CD workflow with GitHub Actions and OpenShift Pipelines (Tekton).

## Project details

- **Project name:** CI/CD Final Project
- **Application:** Flask web service
- **Runtime port:** `8000`
- **Continuous integration:** GitHub Actions (`flake8` linting + `nose` unit tests)
- **Continuous delivery:** OpenShift Pipelines / Tekton (`cleanup` → `git-clone` → `flake8` → `nose` → `buildah` → `deploy`)
- **Container build:** Buildah

## Application endpoints

- `/` — returns a short welcome message.
- `/health` — returns JSON health status.

The application prints `SERVICERUNNING on port 8000` when started with its default configuration, which makes it easy to verify in actual OpenShift pod logs.

## Run locally

Python 3.10 is recommended for compatibility with the `nose` runner used in this assignment.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/health`.

## Run lint and unit tests locally

```bash
python -m pip install "setuptools<70" -r requirements-dev.txt -r requirements.txt
flake8 app.py tests
python scripts/run_nose.py
```

Both linting and unit tests are also run by `.github/workflows/workflow.yml` on every push and pull request.

## Build the container locally

```bash
docker build -t cicd-final-project:latest .
docker run --rm -p 8000:8000 cicd-final-project:latest
```

## GitHub repository setup

1. Create a **public** repository named `cicd-final-project` (or use your preferred repo name).
2. Upload the contents of this ZIP to the **repository root**. The `.github` and `.tekton` folders must be included.
3. Commit to the `main` branch.
4. Open **Actions** in GitHub and confirm the `CI / Lint and unit tests` workflow completes successfully.

Do not submit the ZIP's local path as a Coursera URL. After uploading, use the public GitHub URLs for the files listed in `SUBMISSION_URLS.txt`.

## OpenShift Pipelines (Tekton)

The `.tekton` folder contains:

- `pvc.yml` — a 1 GiB PVC using the course-required storage class `skills-network-learner`.
- `tasks.yml` — cleanup, clone, lint, unit-test, Buildah build/push, and OpenShift deployment tasks.
- `pipeline.yml` — pipeline named `oc-pipelines-oc-final` with the required sequence.

The exact permissions, Buildah security policy, internal image registry permissions, and storage class availability depend on the course's OpenShift cluster. Follow the course lab's cluster setup instructions if the cluster denies any command. Do not replace actual screenshots or logs with sample text.

### Configure and start the pipeline

Run these commands from a terminal that is logged in to the course OpenShift cluster with `oc` and has this repository cloned locally. Check the current project first:

```bash
oc whoami
oc project
```

Apply the PVC, tasks, and pipeline:

```bash
oc apply -f .tekton/pvc.yml
oc apply -f .tekton/tasks.yml
oc apply -f .tekton/pipeline.yml
```

Grant the default `pipeline` service account permission to push to the internal image registry and manage the deployment, if your course account allows it:

```bash
oc policy add-role-to-user system:image-builder -z pipeline
oc policy add-role-to-user edit -z pipeline
```

If Buildah is blocked by the cluster's security policy, use the Buildah task and service-account setup specified by the course lab rather than weakening cluster security yourself.

Start a run, substituting your public repository URL if its name differs:

```bash
PROJECT="$(oc project -q)"
IMAGE="image-registry.openshift-image-registry.svc:5000/${PROJECT}/cicd-final-project:latest"
tkn pipeline start oc-pipelines-oc-final \
  -p git-url=https://github.com/K-p-01/cicd-final-project.git \
  -p revision=main \
  -p image-url="$IMAGE" \
  -p deployment-name=cicd-final-project \
  -w name=shared-workspace,claimName=oc-pipelines-pvc \
  --showlog
```

Watch the run:

```bash
oc get pipelinerun
oc describe pipelinerun
```

The pipeline may need small environment-specific adjustments if the provided course cluster has pre-installed Tekton catalog tasks with different parameter names. The task definitions in this repository are a self-contained baseline, not proof that a run completed in your cluster.

## Evidence required for the Coursera submission

See [`evidence/README.md`](evidence/README.md) for the genuine screenshots and output still to capture from your own GitHub and OpenShift runs. Keep those files separate from source code until they have actually been captured.
