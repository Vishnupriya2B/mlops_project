#template.py is all the files and folders that I want to create
import os #interact with the os
from pathlib import Path #For system compatable part

package_name="mongodb_connect"

list_of_files=[
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/int.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt", 
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
    #".github/workflows/.gitkeep",
    #src folder for managing the source code
    #if we push empty folder into the github it won't be visible that's why we kept .gitkeep
    #"src/components/__init__.py",#each stage of Machine learning pipeline is called a component
    #"src/components/data_ingestion.py",
    #"src/components/data_transformations.py",
    #"src/components/model_trainer.py",
    #"src/components/model_evaluation.py",
    #"src/pipeline/__init__.py",
    #"src/pipeline/training_pipeline.py",
    #"src/pipeline/prediction_pipeline.py",
    #"src/utils/__init__.py",
    #"src/utils/utils.py", 
    #"src/logger/logging.py",
    #"src/exception/exception.py",
    
]

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        #logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass #create an empty path