"Test content to work on"
"Second set of changes"

def func_args2(arg1,*args,arg2):
    print('arg1', arg1)
    print('args', *args)
    print('arg2', arg2)

func_args("Hello World",1,2,3,4,5,arg2 = 12)
    return(func_args2(arg1,*args,arg2))