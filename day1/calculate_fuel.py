import parser
import sys

def calculate_fuel(mass, include_fuel_as_mass=False):
  fuel = (mass / 3) - 2
  if include_fuel_as_mass and fuel > 0:
    fuel = fuel + calculate_fuel(fuel, True)
  return max(fuel, 0)

def calculate_fuel_from_list(modules, include_fuel_as_mass=False):
	all_fuel = [calculate_fuel(module_mass, include_fuel_as_mass) for module_mass in modules]
	return sum(all_fuel)

def calculate_fuel_from_filepath(filepath, include_fuel_as_mass=False):
  modules = parser.parse_modules(filepath)
  return calculate_fuel_from_list(modules, include_fuel_as_mass)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('provide input file as command line parameter')
    sys.exit(1)
  fuel = calculate_fuel_from_filepath(sys.argv[1])
  print(fuel)