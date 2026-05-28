# Without Using inner wrapper function
# def add_spinkles(func):
#     print("**You add spinkles**")
#     func()
  

# @add_spinkles
# def ice_cream():
#   print("Here is your ice cream")

# Using Wrapper Function

def add_spinkles(func):
  def wrapper():
    print("**You add spinkles**")
    func()
  return wrapper

def add_fudge(func):
  def wrapper():
    print("**You add fudge**")
    func()
  return wrapper
  
@add_spinkles
@add_fudge
def get_ice_cream():
  print("Here is your ice cream.")

get_ice_cream()
