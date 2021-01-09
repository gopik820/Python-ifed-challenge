import math

def nearest_square(n):
    if(n<=0):
        return 0
    else:
        return(math.floor(n**0.5)**2)