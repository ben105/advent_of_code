
import sys

def parse_intcode(filepath):
  f = open(filepath)
  string_of_numbers = f.read()
  numbers = string_of_numbers.split(',')
  return [int(number) for number in numbers]

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('provide input file as command line parameter')
    sys.exit(1)
  filepath = sys.argv[1]
  intcode = parse_intcode(filepath)
  print(intcode)
