## # End to End Data Science Project - Winequality Prediction

### Workflows--ML Pipeline

1. Data ingestion
2. Data validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation - MLFlow, Dagshub
6. Model Deployment



## Workflows 

1. Update config.yaml
2. Ypdate schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in `src/config/configuration.py`
6. Update the components in `src/components`
7. Update the pipeline stages in `src/pipeline`
8. Update `main.py` and `app.py`

## How to run?

### STEPS:

Clone the repository
```bash
git clone https://github.com/your-username/winequal-mlops-pipeline
```

### STEP 01- Create a conda environment after opening the repository
```bash
conda create -n wineq python=3.8 -y
conda activate wineq
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- Run the application
```bash
python app.py
```

Now, open your local host with the port 8080.
