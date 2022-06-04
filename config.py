from pathlib import Path


DATA_FOLDER_PATH = Path("/data")
DATA_RAW_FOLDER_PATH = DATA_FOLDER_PATH.joinpath("raw")
DATA_EXTERNAL_FOLDER_PATH = DATA_FOLDER_PATH.joinpath("external")
DATA_INTERIM_FOLDER_PATH = DATA_FOLDER_PATH.joinpath("interim")
DATA_PROCESS_FOLDER_PATH = DATA_FOLDER_PATH.joinpath("process")