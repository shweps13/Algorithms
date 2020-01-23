#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  add = ['rock', 'paper', 'scissors']
  result = []
  if n == 0:
    result = [[]]
  if n == 1:
    for i in range(0, 3):
      result.append([add[i]])
  if n > 1:
    for i in range(0, 3**n):
      result.append(add[2])

  print("Result is:", result)
  pass 


rock_paper_scissors(1)

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')