# Without Using inner wrapper function
# def add_spinkles(func):
#     print("**You add spinkles**")
#     func()
  

# @add_spinkles
# def ice_cream():
#   print("Here is your ice cream")

# Using Wrapper Function

# def add_spinkles(func):
#   def wrapper():
#     print("**You add spinkles**")
#     func()
#   return wrapper

# def add_fudge(func):
#   def wrapper():
#     print("**You add fudge**")
#     func()
#   return wrapper
  
# @add_spinkles
# @add_fudge
# def get_ice_cream():
#   print("Here is your ice cream.")

# get_ice_cream()

# Apply Argument

def add_spinkles(func):
  def wrapper(*arg, **kwarg):
    print("**You add spinkles**")
    func(*arg, **kwarg)
  return wrapper

def add_fudge(func):
  def wrapper(*arg, **kwarg):
    print("**You add fudge**")
    func(*arg, **kwarg)
  return wrapper

@add_spinkles
@add_fudge
def get_ice_cream(flavor):
  print(f"Here is your {flavor} flavor ice cream.")

get_ice_cream("chocolate")
