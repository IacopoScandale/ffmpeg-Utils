from .data.utils import set_date
from argparse import ArgumentParser, Namespace
from datetime import datetime
import os


def get_arguments() -> Namespace:
  parser: ArgumentParser = ArgumentParser(
    description="Change manually filename modification date"
  )
  parser.add_argument("filename")
  parser.add_argument("year", type=int)
  parser.add_argument("month", type=int)
  parser.add_argument("day", type=int)
  parser.add_argument("hour", type=int, nargs='?', default=0, help="(optional)")
  parser.add_argument("minute", type=int, nargs='?', default=0, help="(optional)")
  parser.add_argument("second", type=int, nargs='?', default=0, help="(optional)")

  args: Namespace = parser.parse_args()
  return args


def main():
  args: Namespace = get_arguments()

  # get old file date for print
  old_date: datetime = datetime.fromtimestamp(os.path.getmtime(args.filename))

  # set new date to filename
  set_date(
    args.filename, 
    args.year, 
    args.month, 
    args.day, 
    args.hour, 
    args.minute, 
    args.second
  )
  # get new date
  new_date: datetime = datetime(
    args.year, 
    args.month, 
    args.day, 
    args.hour, 
    args.minute, 
    args.second
  )

  # print changes
  print(
    f'  Changed "{args.filename}" date:',
    f'\n\t· from {old_date}',
    f'\n\t· to   {new_date}'
  )