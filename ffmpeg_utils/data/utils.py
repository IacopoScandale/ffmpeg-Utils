import os, sys
from datetime import datetime


def date_transfer(fname_take_date:str, fname_modify_date:str) -> None:
  """
  Copies modification date from `fname_take_date` to `fname_modify_date`
  """
  # take the date from the first file
  date = os.path.getmtime(fname_take_date)

  # set new modification time to second file
  os.utime(fname_modify_date, (date, date))


def print_clear_terminal(message:str) -> None:
  """
  Clears terminal and prints the `message`
  """
  if os.name == "nt": # windows
    os.system("cls")
    print(message)

  elif os.system == "posix": # Linux
    os.system("clear")
    print(message)
    
  else:
    raise OSError(f"Your os {os.name} is not supported")
  

def set_date(filename:str, year:int, month:int, day:int, hour:int=0, minute:int=0, second:int=0) -> None:
  """
  Changes `filename` modification date according to input parameters
  """
  # create a datetime object
  modification_date = datetime(year, month, day, hour, minute, second)

  # convert the datetime object to a timestamp
  modification_time = modification_date.timestamp()

  # update the file's access and modification times
  os.utime(filename, (modification_time, modification_time))   


def change_date_from_filename_pattern(filename:str, pattern:str) -> None:
  """
  Changes `filename` modification date according to what is written on its
  title (i.e. `filename` string)
  For achieving this is necessary to have a `pattern` string that contains:
  * `_` for every character that is not including date
  * `Y,M,D` for year, month and day (they must appear)
  * `h,m,s` for hour, minute and second

  ## Input:
  * `filename`: name of the file we want to change modification date
  * `pattern` : pattern of the starting date format written in filename

  ## Example:
  filename = "VID_20240723_214238_video_name.mp4"

  pattern = "____YYYYMMDD_hhmmss"
  """
  year, month, day, hour, minute, second = "","","","","",""
  for pattern_char, fname_char in zip(pattern, filename):
    if pattern_char == "Y":
      year += fname_char
    elif pattern_char == "M":
      month += fname_char
    elif pattern_char == "D":
      day += fname_char
    elif pattern_char == "h":
      hour += fname_char
    elif pattern_char == "m":
      minute += fname_char
    elif pattern_char == "s":
      second += fname_char

  try:
    year = int(year)
    month = int(month)
    day = int(day)
    hour = 0 if hour == "" else int(hour)
    minute = 0 if minute == "" else int(minute)
    second = 0 if second == "" else int(second)
    set_date(filename, year, month, day, hour, minute, second)

  except:
    print(f"Error, wrong pattern:\n filename = {filename}\n pattern = {pattern}")
    sys.exit()