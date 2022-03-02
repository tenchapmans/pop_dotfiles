'''A config module for the Kitty Theme Changer Tool.'''
from pathlib import Path
from os import getpid
from psutil import process_iter
import psutil

theme_dir = Path('~/.config/kitty/themes').expanduser()
conf_dir = Path('~/.config/kitty').expanduser()
theme_link = conf_dir.joinpath('theme.conf')
light_theme_link = conf_dir.joinpath('light-theme.conf')
dark_theme_link = conf_dir.joinpath('dark-theme.conf')

def kitty_pid():
  ps = {x.pid: x for x in psutil.process_iter(['name', 'pid', 'ppid'])}
  cp = ps[getpid()]
  while cp.name() != 'kitty':
     cp = cp.parent()
  return cp.pid

socket = 'unix:/tmp/kitty-socket-{}'.format(kitty_pid())