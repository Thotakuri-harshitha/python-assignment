# Create a class Student with:
# Class variable: school_name = "XYZ School"
# A method set_details()
#  → inside method, assign:
# name = "harshie"
# marks = 85
# A method display()
#  → print:
# Name
# Marks
# School name
# 👉 Outside the class:
# Create object
# Call set_details()
# Call display()


# class student:
#     school_name = "XYZ School"
#     def set_details(self):
#         self.name = "harshie"
#         self.marks = 85

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)
#         print("school:", student.school_name)

# s1 = student()
# s1.set_details()
# s1.display()

# Create a class Employee with:
# Class variable: company = "Infosys"
# A method set_data()
#  → assign:
# name = "harshie"
# salary = 20000
# A method increase_salary()
#  → add 5000 to salary
# A method display()
#  → print all details
# 👉 Outside the class:
# Create object
# Call all methods

# class employee:
#     company = "Infosis"
    
#     def set_data(self):
#         self.name = "harshie"
#         self.salary = 20000
#     def increase_salary(self):
#         self.salary = self.salary + 5000

#     def display(self):
#         print("Name:", self.name)
#         print("salary:", self.salary)
#         print("company:", employee.company)

# e1 = employee()
# e1.set_data()
# e1.increase_salary()
# e1.display()


# Create a class Mobile with:
# Class variable: brand = "Apple"
# A method set_details()
#  → assign:
# model = "iPhone 14"
# price = 80000
# A method discount()
#  → reduce price by 10%
# A method show_details()
#  → print all details
# 👉 Outside the class:
# Create object
# Call methods

class mobile:
    brand = "Apple"

    def set_details(self):
          self.model = "iphone 14"
          self.price = 80000
  
    
    def discount(self):
        self.price = self.price - (self.price * 10 / 100)

    def show_details(self):
        print("Brand:", mobile.brand)
        print("model:", self.model)
        print("Price:", self.price)

m1 = mobile()
m1.set_details()
m1.discount()
m1.show_details()
