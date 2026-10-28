# OpenShift/Tekton instructions

These manifests are a starting point for the course OpenShift environment. Cluster security, image registry permissions, the supported Tekton API version, and available storage class vary by cluster. Follow the course lab's service-account and Buildah instructions.

Verify your namespace and apply resources:

```bash
oc whoami
oc project
oc apply -f .tekton/pvc.yml
oc apply -f .tekton/tasks.yml
oc apply -f .tekton/pipeline.yml
oc get pvc oc-lab-pvc
```

The PVC must be Bound before starting a PipelineRun. Obtain the namespace from `oc project -q`, then set an image URL like this:

```bash
PROJECT="$(oc project -q)"
IMAGE="image-registry.openshift-image-registry.svc:5000/${PROJECT}/cicd-app:latest"
```

Start the pipeline using the repository you actually published:

```bash
tkn pipeline start oc-pipelines-oc-final \
  -p git-url=https://github.com/K-p-01/ci-cd-final-project.git \
  -p revision=main \
  -p image-url="${IMAGE}" \
  -p deployment-name=cicd-app \
  -w name=shared-workspace,claimName=oc-lab-pvc \
  --showlog
```

If the pipeline fails, inspect the real run logs. Do not claim it succeeded until the PipelineRun shows Succeeded and `oc get deployment cicd-app` shows the deployment.
