'''
It is a simply file that contains python code with the .py extentsion or it is a source file which contains commonly used variables, functions, classes etc.

Note : Below module-name is a module and in that module x is a function and y is a variabl inside that module based on that i have added the examples

* we can use module using import keyword with the module name.
    import module-name
    => we can access the resource like below
       module-name.x()
       module-name.y
   
* we can use alias name also 
    import module-name as md
    => we can access the resource like below
       md.x()
       md.y
       
* if we want not to use the module name while accessing the resources then also we can directly access the resource
    from module-name import x
    => Now we can directly access
       x
       y
    
    => Here also we can use the alias
       from module-name import x as p
       print(p) // it return the value of x
       
* if we want to access all the resources without using module name
    from module-name import *
    => Now we can directly access all the resources which is inside  the module-name
    x()
    y
'''
