
import os
from pathlib import Path

list_of_file = [
    "src/__init__.py",
    "src/data_ingestion.py",
    "src/embeding.py",
    "src/model_api.py",
    "Expetiments/experiment.ipynb",
    "logger/__init__.py",
    "StreamlitApp.py",
    "exception/__init__.py",
    "setup.py"
]


for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            print(f"creating empty file: {filepath}")
    else:
        print(f"file {filename} already exists")







