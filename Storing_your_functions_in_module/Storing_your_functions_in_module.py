"""
8-15. Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.
"""
import pizza_function as p
p.make_pizza(12,'pepperoni')

"""
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
import pizza_function
from pizza_function import make_pizza
from pizza_function import make_pizza as mp
import pizza_function as pf
from pizza_function import *

"""
8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.
"""

import pizza_function as p
p.make_pizza(12,'peeperoni','cheese','macoroni'
				 'butter','beef','sausage')







