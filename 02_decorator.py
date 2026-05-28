# Decorator (Security Guard)

def check_pin_decorator(original_function):
  def wrapper():
    print("\n"+"="*40)
    entered_pin = input(f"🔑 [KBZPay Security] Enter 4-digit PIN: ")
    if entered_pin == "1234":
      print("✅ PIN verified. Access granted!")
      original_function()
    else:
      print("❌ Invalid PIN. Connection terminated.")
    print("-"*40)
  return wrapper

@check_pin_decorator
def check_balance():
  print("💰 [BALANCE] Your current balance is 100,000 MMK.")

@check_pin_decorator
def top_up_phone():
  print("💸 [TOP-UP] Mobile top-up of 10,000 MMK to MPT was successful.")

check_balance()

top_up_phone()