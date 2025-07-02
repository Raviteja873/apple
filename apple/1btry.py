try:
    x= 10
    y= 0
    z= x/y
except ZeroDivisionError :
    print("error")
else:
    print("result is ",z)
finally:
    print("code is excuted....!")
    
