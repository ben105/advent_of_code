import functools
import parser
import sys

OPCODE_1_RANGE = 3
OPCODE_2_RANGE = 3
OPCODE_99_RANGE = 0


class IntcodeData:

  noun_address = 1
  verb_address = 2

  def __init__(self, memory):
    self.memory = memory

  def __len__(self):
    return len(self.memory)

  def set_noun(self, noun):
    self.write(self.noun_address, noun)

  def set_verb(self, verb):
    self.write(self.verb_address, verb)

  def get_positions(self, index, range):
    start = index + 1
    end = index + range + 1
    assert len(self.memory) > end, 'extends beyond memory bounds'
    return self.memory[start:end]

  def get_values(self, positions):
    return [self.read(position) for position in positions]

  def write(self, position, value):
    self.memory[position] = value

  def read(self, position):
    return self.memory[position]


class Intcode:

  def __init__(self, data):
    self.data = data
    self.pointer = 0

  def compute_opcode(self, range, operation):
    positions = self.data.get_positions(self.pointer, OPCODE_1_RANGE)
    output_pos = positions.pop()
    values = self.data.get_values(positions)
    result = functools.reduce(operation, values)
    self.data.write(output_pos, result)

  def opcode1(self):
    self.compute_opcode(OPCODE_1_RANGE, lambda a,b: a+b)
    self.pointer = self.pointer + OPCODE_1_RANGE + 1

  def opcode2(self):
    self.compute_opcode(OPCODE_2_RANGE, lambda a,b: a*b)
    self.pointer = self.pointer + OPCODE_2_RANGE + 1

  def opcode99(self):
    print(self.data.read(0))
    sys.exit(0)

  def run(self):
    self.pointer = 0
    while(self.pointer <= len(self.data)):
      opcode = self.data.read(self.pointer)
      if opcode == 1:
        self.opcode1()
      elif opcode == 2:
        self.opcode2()
      elif opcode == 99:
        self.opcode99()
      else:
        print('Invalid opcode found {}'.format(opcode))
        sys.exit(2)

  def run_with_params(self, noun, verb):
    self.data.set_noun(noun)
    self.data.set_verb(verb)
    self.run()

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('provide input file as command line parameter')
    sys.exit(1)
  numbers = parser.parse_intcode(sys.argv[1])
  data = IntcodeData(numbers)
  intcode = Intcode(data)
  intcode.run_with_params(12, 2)
