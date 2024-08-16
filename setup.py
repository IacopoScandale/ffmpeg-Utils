from setuptools import setup, find_packages
from ffmpeg_utils.data.strings import *

setup(
  name=PACKAGE_NAME,
  version='0.1',
  packages=find_packages(),
  install_requires=[],
  entry_points={
    'console_scripts': [
      f"{PACKAGE_NAME}={PACKAGE_NAME}.comm_ffmpeg_utils:main",
      f"{FFMP4_COMM}={PACKAGE_NAME}.comm_ffmpeg_to_every_mp4_and_date:main",
      f"{DATE_SET_COMM}={PACKAGE_NAME}.comm_date_set:main",
      f"{DATE_TRANSFER_COMM}={PACKAGE_NAME}.comm_date_transfer:main",
    ],
  },
)
