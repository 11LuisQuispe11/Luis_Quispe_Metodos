# DVC support

The pipeline is described in `dvc.yaml` and its current public-synthetic artifact state is recorded in `dvc.lock`.

A future confidential dataset must be referenced through an approved private DVC remote or immutable data hash. It must never be pushed to the public repository.
