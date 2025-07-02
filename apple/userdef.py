class smallerror(Exception):
    pass
def check(num):
    if num < 10:
        raise smallerror("number is too small")
    print(f"number is fine{num}")
    
try:
    check(5)
except smallerror as e:
    print("caught an error")