import random,string,sys
import argparse

usage_msg = """
Write a random permutation of the input lines to standard output.
With no FILE, or when FILE is -, read standard input.
Mandatory arguments to long options are mandatory for short options too.
  -e, --echo     treat each command-line operand as an input line.
  -i, --input-range=LO-HI   treat each number LO through HI as an input line
  -n, --head-count=COUNT    output at most COUNT lines
  -r, --repeat              output lines can be repeated
      --help     display this help and exit
      --version  output version information and exit """

version_msg = """
shuf (Simplified version based on GNU coreutils 8.30)
"""
class Shuf:
    def __init__(self, lines, repeat, count):
        random.shuffle(lines)
        self.lines = lines
        self.repeat = repeat
        self.count = count
        self.index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0 or self.index == len(self.lines):
            raise StopIteration
        if self.repeat:
            result = random.choice(self.lines)
        else:
            result = self.lines[self.index]
            self.index += 1
        if self.count > 0:
            self.count -= 1
        return result


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-range", 
                      action="store", dest="input_range", default=None,
                      help="treat each number LO through HI as an input line")
    parser.add_argument("-n", "--head-count", type=int,
                      action="store", dest="head_count", default=-1,
                      help="output at most COUNT lines")
    parser.add_argument("-r", "--repeat",
                      action="store_true", dest="repeat", default=False,
                      help="output lines can be repeated")
    parser.add_argument("-e", "--echo",
                        action="store_true", dest="echo",
                        help="treat each ARG as an input line")
    options, args = parser.parse_known_args(sys.argv[1:])

    if options.input_range is not None:
        if len(args) != 0:
            parser.error("extra operand '%s'" % args[0])
            return
        try:
            start_str, end_str = (options.input_range).split("-")
        except ValueError:
            parser.error("invalid input range: %s" % options.input_range)
            return
        start, end = int(start_str), int(end_str)
        if end < start:
            parser.error("invalid input range: %s" % options.input_range)
            return
        lines = [str(x) for x in range(start, end + 1)]
    elif options.echo:
        lines = args
    elif len(args) == 0 or args[0] == '-':
        lines = sys.stdin.read().splitlines()
    else:
        if len(args) != 1:
            parser.error("extra operand '%s' " % args[1])
            return
        filename = args[0]
        file_s = open(filename)
        lines = file_s.read().splitlines()
        file_s.close()
    shuf = Shuf(lines, options.repeat, options.head_count)
    for line in shuf:
        sys.stdout.write(line+'\n')


if __name__ == "__main__":
    main()
