

class logged(object):
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print "You called %s, with arguments %s, %s"%(self.func.__name__, str(self.args), str(self.kwargs) )
        return self.func( *args, **kwargs)

@logged
def f(x, y=0):
    pass

f(4)
f("this", y="that")
