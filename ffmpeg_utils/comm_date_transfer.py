from .data.utils import date_transfer
from argparse import ArgumentParser, Namespace
from datetime import datetime
import os


def get_arguments() -> Namespace:
  parser: ArgumentParser = ArgumentParser(
    description=(
      "Transfers (copies) modification date from a file "
      "(file_take_date) to another (file_modify_date)"
    ) 
  )
  parser.add_argument(
    "file_take_date", 
    help="name of the file we want to take modification date"
  )
  parser.add_argument(
    "file_modify_date", 
    help="name of the file we want to change modification date"
  )

  args: Namespace = parser.parse_args()
  return args


def main():
  args: Namespace = get_arguments()

  # get old and new file date for print
  old_timestamp: float = os.path.getmtime(args.file_modify_date)
  new_timestamp: float = os.path.getmtime(args.file_take_date)

  old_date: datetime = datetime.fromtimestamp(old_timestamp)
  new_date: datetime = datetime.fromtimestamp(new_timestamp)

  # transfer date from `fname_take_date` to `fname_modify_date`
  date_transfer(args.file_take_date, args.file_modify_date)

  # show changes
  print(
    f'  Changed "{args.file_modify_date}" date:',
    f'\n\t· from {old_date}',
    f'\n\t· to   {new_date}'
  )