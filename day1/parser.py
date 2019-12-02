import sys

def parse_modules(filepath):
  f = open(filepath)
  modules = []
  for line in f.readlines():
    m = line.strip()
    m = int(m)
    modules.append(m)
  return modules


if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('provide input file as command line parameter')
    sys.exit(1)
  filepath = sys.argv[1]
  modules = parse_modules(filepath)
  print(modules)