from .data.utils import print_clear_terminal, change_date_from_filename_pattern, date_transfer
import os
import subprocess
from argparse import ArgumentParser, Namespace


def get_arguments() -> Namespace:
  parser: ArgumentParser = ArgumentParser(
    description=(
      "This commands applies inner_ffmpeg_command to every file mp4 "
      "in the current folder. Then it asks some choiches to take: "
      "e.g. if you want to keep date in new files."
    )
  )
  parser.add_argument(
    "ffmpeg_options",
    type=str,
    help=(
      'ffmpeg options STRING (use "") '
      'e.g.: "-c:v copy -b:v 3000k -vf scale=1280:720"'
    )
  )

  args: Namespace = parser.parse_args()
  return args


def main():
  args: Namespace = get_arguments()

  # command to execute for every mp4 file
  command_to_execute = 'ffmpeg -i "{in_mp4}" {inner_command} -hide_banner "{out_mp4}"'

  # ask date handling
  print("\n· Select an option for file dates:")
  date_choices = [
    "Ignore dates\n\t(new files will have today date)",
    "Insert filenames date pattern\n\t(must be the same for all files to process) e.g.:\n\tfilename = 'VID_20240612_211403_video.mp4'\n\tpattern  = '____YYYYMMDD_hhmmss'",
    "Take modification date from every file\n\t(NB it could not be your file creation date, be careful if you are concerned about dates)",
  ] # show choices
  for i, date in enumerate(date_choices):
    print(f"  {i+1}. {date}")
  date_choice_index = int(input("\nChoose an option number: ")) - 1


  # insert pattern if asked
  if date_choice_index == 1:
    pattern = input("\nInsert filneames pattern: ")


  message = "" # main terminal screen
  i = 0 # processed files counter
  # for every file in current directory
  for fname in os.listdir():
    if fname.endswith(".mp4") and not fname.endswith("_ff.mp4"):
      i += 1
      
      # append ff for new filename
      new_name = fname[:-4] + "_ff.mp4"
      # curent command to execute
      cur_command = command_to_execute.format(
        in_mp4 = fname, 
        inner_command = args.ffmpeg_options, 
        out_mp4 = new_name
      )
      # print(cur_command)

      # show info in current screen
      print(f"  {i}. Processing file: '{fname}'")
      print(f"        query: '{cur_command}'")

      # run ffmpeg command (one at time) into another terminal
      if os.name == "nt": # windows
        ffmpeg_process = subprocess.Popen(cur_command, creationflags=subprocess.CREATE_NEW_CONSOLE)
        ffmpeg_process.wait() # for running only one command at time
      elif os.name == "posix": # linux
        # TODO
        raise NotImplementedError
      else:
        raise OSError(f"Your os {os.name} is not supported")


      # date choices
      if date_choice_index == 0:
        pass
      elif date_choice_index == 1:
        change_date_from_filename_pattern(new_name, pattern)
      elif date_choice_index == 2:
        date_transfer(fname, new_name)


      # main terminal clear message
      message += f"\n  {i}. '{fname}'"
      print_clear_terminal(message)