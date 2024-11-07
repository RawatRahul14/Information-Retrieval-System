import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = "[%(asctime)s]: %(message)s:")

list_of_files = [
    f"src/__init__.py",
    f"src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for files in list_of_files:
    file_path = Path(files)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok = True)
        logging.info(f"Created directory: {file_dir}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")