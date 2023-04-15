def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide
  }


def calculator():
  num1 = int(input("What`s the first number: "))
  for key in operations:
    print(key)
  should_continue = True
  
  while should_continue:
    operational_symbol = input("Pick an operation: ")
    num2 = int(input("What`s the next number?: "))
    calc = operations[operational_symbol]
    answer = calc(num1, num2)
    
    print(f"{num1} {operational_symbol} {num2} = {answer} ")
    
    if input(f"Type 'y' to continue calculating with {answer}: or 'n' to begin calculation") == 'y':
      num1 = answer
    else: 
      should_continue = False
      calculator()


calculator()