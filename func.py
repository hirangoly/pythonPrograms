def func1(*args):
    arg1, arg2, arg3 = args
    print 'arg1 = %s, arg2 = %s, arg3 = %s' % (arg1, arg2, arg3)
    
    
def func2(arg1, arg2, arg3):
    print 'arg1 = %s, arg2 = %s, arg3 = %s' % (arg1, arg2, arg3)
    func1(arg1, arg2, arg3)
    
    
func1('hello', 'hi', 'wats up')
func2('hi', 'hello', 'wats up')
