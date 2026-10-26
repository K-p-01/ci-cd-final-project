# Tekton resources

- `pvc.yml`: 1 GiB workspace claim using the required `skills-network-learner` storage class.
- `tasks.yml`: reusable Task resources for cleanup, clone, lint, nose tests, Buildah build/push, and deployment.
- `pipeline.yml`: Pipeline named `oc-pipelines-oc-final`.

Apply the PVC, tasks, and pipeline in the OpenShift project used for the course lab. See the root README for example commands. Cluster security and registry permissions are environment-specific; a YAML file alone cannot prove a successful run.
