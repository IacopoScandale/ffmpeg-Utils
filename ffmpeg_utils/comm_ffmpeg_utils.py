from .data.utils import add_one_to_counter
from .data.strings import COMMANDS, PACKAGE_NAME, COUNTER_JSON
from argparse import ArgumentParser, Namespace
import os
import json


def get_arguments() -> Namespace:
  parser: ArgumentParser = ArgumentParser(
    description=f"Shows all '{PACKAGE_NAME}' package commands"
  )
  args: Namespace = parser.parse_args()
  return args


def main():
  _ = get_arguments()
  add_one_to_counter(PACKAGE_NAME)

  # open counter json as dictionary
  here: str = os.path.dirname(os.path.abspath(__file__)) 
  full_path_counter_json: str = os.path.join(here, COUNTER_JSON)
  with open(full_path_counter_json, "r") as jsonfile:
    usage_counter: dict[str,int] = json.load(jsonfile)

  # print title and all commands
  print(f"ffmpeg_utils package\n\ncommands:{' '*15}times used:")

  for i, command in enumerate(COMMANDS.keys(), 1):
    times_used: int = usage_counter.setdefault(command, 0)
    print(f"{i:>4}. {command:<20} {times_used:>7}")