import random, sys, string
import argparse

class randline:
  def __init__(self, filename):
    f = open(filename, 'r')
    self.lines = f.readlines()
    f.close()

def main():
  version_msg = "%prog 3.0"
  usage_msg = """%prog [OPTION]... FILE
Shuffles FILE  by outputting a random permutation of its lines."""

  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input-range",
                    action="store", dest="input_range",
                    help="treat each number LO through HI as an input line")
  parser.add_argument("-n", "--head-count", 
                    action="store", dest="head_count",
                    help="output at most COUNT lines")
  parser.add_argument("-r", "--repeat", default=False,
                    action="store_true", dest="repeat",
                    help="output lines can be repeated")
  parser.add_argument("-e", "--echo", 
                    action="store_true", dest="echo",
                    help="treat each ARG as an input line")
  options, args = parser.parse_known_args(sys.argv[1:])
  
  num = None 
  lines = []
  try:
    if options.head_count is not None:
      num = int(options.head_count)
  except:
    parser.error("invalid HEAD COUNT: {0}".
                 format(options.head_count))
  if num != None and num < 0:
    parser.error("negative count: {0}".
                     format(none))
  if options.echo is not None:
    lines = args
  if options.input_range is not None:
    try:
      ir_str = str(options.input_range)
      split_str = ir_str.split("-")
      ir_lo = int(split_str[0])
      ir_hi = int(split_str[1])
      lines = list(range(ir_lo, ir_hi + 1))
    except:
      parser.error("invalid INPUT RANGE: {0}".
                   format(options.input_range))
    if ir_lo < 0 or ir_hi < 0:
      parser.error("negative range: {0}".
                   format(ir_str))
  if options.input_range == None and len(args) > 1:
    parser.error("wrong number of operands")
  elif options.input_range != None and len(args) != 0:
    parser.error("wrong number of operands")

  try:
    if options.input_range is None:
      if len(args) == 0 or args[0] == "-":
        lines = sys.stdin.readlines() 
      else:
        input_file = args[0]
        generator = randline(input_file)
        lines = generator.lines
    random.shuffle(lines)
    if options.repeat is False:
      if num is None:
        num = len(lines)
      for index in range(0, num):
        sys.stdout.write(lines[index])
    else:
      if options.head_count is None:
        num = True 
      while num != 0:
        sys.stdout.write(lines[0])
        random.shuffle(lines)
        if isinstance(num, bool) is False:
           num -= 1
  except IOError as err:
    parser.error("I/O error({0}): {1}".
                 format(errno, strerror)) 
if __name__ == "__main__":
  main()
