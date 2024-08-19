import os

PACKAGE_NAME: str = "ffmpeg_utils"
COMMANDS_COPY_FOLDER: str = "Commands"
DATA_FOLDER: str = "data"
INFO_FOLDER: str = f"{PACKAGE_NAME}.egg-info"
VENV_FOLDER: str = "venv"

VENV_SCRIPTS_FOLDER_WIN: str = os.path.join(VENV_FOLDER, "Scripts")
VENV_SCRIPTS_FOLDER_LINUX: str = os.path.join(VENV_FOLDER, "bin")

COUNTER_JSON_NAME: str = "usage_counter.json"
COUNTER_JSON: str = os.path.join(DATA_FOLDER, COUNTER_JSON_NAME)

# command names
DATE_TRANSFER_COMM: str = "date_transfer"
DATE_SET_COMM: str = "date_set"
FFMP4_COMM: str = "ffmp4"


COMMANDS: dict[str,str] = {
  PACKAGE_NAME: "comm_ffmpeg_utils",
  DATE_TRANSFER_COMM: "comm_date_transfer",
  DATE_SET_COMM: "comm_date_set",
  FFMP4_COMM: "comm_ffmpeg_to_every_mp4_and_date",
}