# ==========================================
# 1. CORE FUNCTION (The Original Action)
# ==========================================
def drive_car():
  print("🚗 Engine started! Driving the car now, bro!")


# ==========================================
# 2. THE DECORATOR (The Seatbelt Safety Check)
# ==========================================
def seat_belt_decorator(original_function):
  # Building the wrapper function to add pre and post actions
  def wrapper():
    print("🔒 [SAFETY CHECK] Seatbelt automatically fastened.") # Pre-action)
    original_function()
    print("🔓 [SAFETY CHECK] Arrived safely. Seatbelt unfastened.") # Post-action
  return wrapper

# ==========================================
# 3. BEHIND THE SCENES EXECUTION (Manual Wrapping)
# ==========================================

decorated_drive = seat_belt_decorator(drive_car)

decorated_drive()