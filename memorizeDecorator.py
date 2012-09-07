#memorizing decorator


class memorize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        
        if args in self.cache:
            return self.cache[args]
        else:
            self.cache[args] = self.func(*args)
            return self.cache[args]
       
   
    def __repr__(self):
        return self.func.__doc__
        
        
#TESTING

@memorize
def fib(n):
    if n==1 or n==2:
        return 1
    else:
       return fib(n-1) + fib(n-2)