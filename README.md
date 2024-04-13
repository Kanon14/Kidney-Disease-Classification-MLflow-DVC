# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Kanon14/Kidney-Disease-Classification-MLflow-DVC
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.8 -y
```

```bash
conda activate kidney
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)


### dagshub
[dagshub](https://dagshub.com/)

Run this to export as env variables:

```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/Kanon14/Kidney-Disease-Classification-MLflow-DVC.mlflow 

set MLFLOW_TRACKING_USERNAME=Kanon14 

set MLFLOW_TRACKING_PASSWORD=2a57f710b92c4261b14ebc77457c63fc1b2320f4

```