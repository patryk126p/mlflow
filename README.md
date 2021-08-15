# MLflow

In this repo only two components of MLflow are used:
- tracking - for tracking parameters, metrics and artefacts
- projects - for separating environments for executing steps in pipeline

## Setup

### Local tracking server

MLflow can be used locally without sharing experiments with the team.<br>
To run locally:
1. install necessary packages `pip install -r requirements.txt`
2. in one terminal run `mlflow server --default-artifact-root <PATH_WHERE_TO_STORE_ARTIFACTS>`


### Remote tracking server

To set up simple remote tracking server on EC2 follow instructions in `tracking_server` directory<br>
To use such server:
1. (install and) [configure aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
2. change `tracking_uri` in `config.yaml` to point to tracking server

## How to use this repo

After preparing tracking server:
- execute to run full pipeline:
```
cd <REPO_ROOT>
mlflow run .
```
- open `tracking_uri` in browser to see MLflow UI

All necessary pipeline configuration options can be found in `config.yaml`.<br>
Options specific to model are stored in `src/train_model/model_config.json`
<br><br><br>


#### Helper script
`download_artifact.py` is a helper script showing how artifacts can be downloaded
