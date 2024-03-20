global_var = 10

def modify_global():
    global global_var
    global_var += 5
    print("Inside the function:", global_var)

print("Before the function call:", global_var)
modify_global()
print("After the function call:", global_var)
print("==============================")

def example_function():
    local_var = 20
    print("Inside the function:", local_var)

example_function()
# Trying to access local_var outside the function will result in an error
print("==============================")

def outer_function():
    outer_var = 30

    def inner_function():
        nonlocal outer_var
        outer_var += 10
        print("Inside the inner function:", outer_var)

    inner_function()
    print("Inside the outer function:", outer_var)

outer_function()
print("==============================")
