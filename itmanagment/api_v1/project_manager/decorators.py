
def pm(func,request):
    def function():
        if request.user.is_authenticated:
            func()
    return function()