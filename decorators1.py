def decorators(function):
    def wrapper(x):
        print("Before Decorating function.....")
        function(x)
        print('After decoration...')
    return wrapper

@decorators
def foo(n):
    print("This is the function we are decorating")
    print('Value is: ', n)
##d=decorators(foo)
##d(8)
foo(8)
