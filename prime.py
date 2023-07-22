#Python funcction to check if a number is prime or not

def prime(x):
    for i in range(x):
        if x % i == 0:
            return False
    else:
        return True
