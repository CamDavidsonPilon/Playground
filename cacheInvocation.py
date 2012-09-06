
import inspect

class cacheInvocation(object):
    
    def __init__(self, f):
        self.func = f
        self.count = 0 

    def __call__(self, *args):
        print args
        invocation = zip( inspect.getargspec( self.func)[0], args )
        print args, invocation
        self.invocation = invocation
        return self.func( *args)


@cacheInvocation
def f(x,y):
    return x,y


g = f(1,2)
print f.invocation
