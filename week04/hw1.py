from datetime import datetime

def restrict_hour(start, end):
    def decorator(func):
        def wrapper():

            hour = datetime.now().hour
            if start <= hour < end:
                func()

        return wrapper
    return decorator


@restrict_hour(start=22, end=24)
def do_work():
    print("Working... ")

do_work()
