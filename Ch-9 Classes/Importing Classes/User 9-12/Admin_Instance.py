"""
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly
"""
from Admin import Admin,Privileges

Admin = Privileges(["Store data",'Edit data'])
print(f"{Admin.show_privileges()}")