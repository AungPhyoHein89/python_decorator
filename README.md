# python_decorator
concept and behind the scene of decorator

# Python Decorator Learning Journey 🚀

This repository contains a practical implementation of Python Decorators, demonstrating how to modify or upgrade the behavior of functions without modifying their actual source code.

## 💡 Key Concepts Learned Today

1. **Separation of Concerns (DRY Principle):**
   Instead of writing PIN validation logic inside every single core banking function (like `check_balance` and `top_up_phone`), we extracted the security logic into a central decorator.

2. **The `@` Magic (Syntactic Sugar):**
   Using the `@check_pin_decorator` syntax allows us to dynamically wrap functions. It makes the code clean, readable, and incredibly easy to maintain.

3. **Function vs. Function Execution:**
   - `return wrapper` (Without parentheses): Passes the actual code block (function object) to be called later when the user triggers it.
   - `return wrapper()` (With parentheses): Executes the function immediately, which causes logical bugs (NoneType errors).

## 🖥️ How It Works (Behind the Scenes)

When `@check_pin_decorator` is placed above `check_balance()`, Python automatically wraps it like this:
```python
check_balance = check_pin_decorator(check_balance)