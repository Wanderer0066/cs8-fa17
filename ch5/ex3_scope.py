#!/usr/bin/python3

# Module variables are accessible from any code inside of a file, and by any
# modules that include this module.
module_variable = 'foo'

def main():
    name = 'Jason'
    # This statement creates a new local variable named module_variable that
    # 'masks' or hides the value of the module-scope variable with the same name
    # It has no impact on the module-scope variable.
    module_variable = 'bar'
    print(module_variable)
    
    other_func()
    print('In main, you entered', name)
        
def other_func():
    # This will print foo since there is no module_variable in other_func()'s
    # local scope.
    print(module_variable)
    name = 'Bob'
    print('Now, inside of other_func, name is', name)

main()
# Note, you cannot access name outside of a function
# This is known as a the 'module' scope
# print(name)