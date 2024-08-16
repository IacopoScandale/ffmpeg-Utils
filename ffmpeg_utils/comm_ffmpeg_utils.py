from .data.strings import COMMAND_LIST, PACKAGE_NAME
from argparse import ArgumentParser


def main():
  parser: ArgumentParser = ArgumentParser(
    description=f"Shows all '{PACKAGE_NAME}' package commands"
  )
  _ = parser.parse_args()
  
  # print title and all commands
  print("ffmpeg_utils package\n\ncommands:")

  for i, command in enumerate(COMMAND_LIST, 1):
    print(f"{i:> 4}. {command}")