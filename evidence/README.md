# Coursera evidence checklist (capture real output from your environment)

Required evidence files from the assignment:

- `oc-pipelines-console-pvc-details.png` — actual PVC details for `oc-lab-pvc`, storage class `skills-network-learner`, request `1Gi`.
- `cicd-github-validate` — actual logs from the successful GitHub Actions run, including the workflow's real steps.
- `oc-pipelines-oc-final.png` — actual OpenShift Pipeline detail/graph showing cleanup, git-clone, flake8, nose, buildah, deploy.
- `oc-pipelines-oc-green.png` — actual successful PipelineRun screenshot showing the six task stages and evidence that `deployment/cicd-app` exists.
- `oc-pipeline-application-logs` — actual application pod logs showing `SERVICERUNNING on port 8000` among surrounding log lines.

Capture screenshots from the real GitHub/OpenShift interfaces. Do not submit generated mockups or invented terminal output as live evidence.

Useful commands:

```bash
# GitHub Actions (GitHub CLI installed and authenticated)
gh run list --repo K-p-01/ci-cd-final-project
gh run view RUN_ID --repo K-p-01/ci-cd-final-project --log > cicd-github-validate

# OpenShift
oc get pvc oc-lab-pvc
oc get pipelinerun
oc get deployment cicd-app
oc rollout status deployment/cicd-app
oc logs deployment/cicd-app --tail=100 > oc-pipeline-application-logs
```
