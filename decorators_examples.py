from functools import wraps


# A decorator adds behavior before and after a function runs.
def announce(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("The function is starting.")
        result = function(*args, **kwargs)
        print("The function has finished.")
        return result

    return wrapper


@announce
def greet():
    print("Hello!")


# *args and **kwargs let a decorator work with different function arguments.
def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@log_call
def add(first_number, second_number):
    return first_number + second_number


# A decorator can check conditions before allowing a function to run.
def requires_login(function):
    @wraps(function)
    def wrapper(user_is_logged_in):
        if not user_is_logged_in:
            print("Please log in first.")
            return None

        return function(user_is_logged_in)

    return wrapper


@requires_login
def view_profile(user_is_logged_in):
    print("Here is your profile.")


if __name__ == "__main__":
    print("--- Basic decorator ---")
    greet()

    print("\n--- Decorator with arguments ---")
    add(3, 5)

    print("\n--- Login-check decorator ---")
    view_profile(False)
    view_profile(True)
