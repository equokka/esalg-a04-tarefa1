#!/usr/bin/env python

import yaml # pip install pyyaml
from random import randint

def yes_no(q) -> bool:
  while True:
    ans = input("{:.<44}(y/n) ".format(q)).lower()
    if len(ans) != 1: continue
    if   ans == "y": return True
    elif ans == "n": return False
  # else ask again

with open("levels.yml", "r", encoding="utf-8") as f:
  questions = yaml.load(f, Loader=yaml.FullLoader)

def get_severity(manual = False) -> int:
  if manual:
    for level in range(len(questions.keys())):
      for question in list(questions.values())[level]:
        if yes_no(question):
          return abs(4 - level)
        # else continue
      # then asks questions on the next level
    # else is zero (blue)
    return 0
  else:
    return randint(0, 4)

def is_int(str: str) -> bool:
  try: int(str)
  except ValueError: return False
  return True

def get_option(q: str, num: int, tab: int = 2) -> int:
  error_str = "%sNúmeros 1-%d, por favor." % (tab * " ", num)
  while True:
    i = input(q).strip()

    if is_int(i):
      i = int(i)
      if i in range(1, num + 1):
        return i

    print(error_str)
