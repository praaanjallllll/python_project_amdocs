# Application name - Employee Management System
# Author Name -Pranjal Desale
# Date - 24/10/2023

# Description -
# This python program is part of employee management system
# It allows user to perform various operations related to employee management ,
# including adding , modifying , viewing employee details.

from validate import *

class employee:
    def __init__(self, empid, empname, salary, age, gender, Address, City, DOB, DOJ, Deptname, Designation, pan,
                 aadhar):
        self.empid = empid
        self.empname = empname
        self.salary = salary
        self.age = age
        self.gender = gender
        self.Address = Address
        self.City = City
        self.DOB = DOB
        self.DOJ = DOJ
        self.Deptname = Deptname
        self.Designation = Designation
        self.pan = pan
        self.aadhar = aadhar

    def display(self):
        print(self.empid, " ", self.empname, " ", self.salary, " ", self.age, " ", self.gender, " ", self.Address, " ",
              self.City, " ", self.DOB, " ", self.DOJ, " ", self.Deptname, " ", self.Designation, " ", self.pan, " ",
              self.aadhar)


emp = []

while True:
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> EMPLOYEE MANAGEMENT SYSTEM <<--"))
    print("{:>60}".format("************************************"))
    print("1: Add a Record")
    print("2: Display a Record")
    print("3: Search the Record")
    print("4: Update the Record")
    print("5: Delete the Record")
    print("6: Display Details of Employee with Highest Salary")
    print("7: Display Details of Employee with Lowest Salary")
    print("8: Exit\n")
    print("{:>60}".format("--->> Choice Options:[1/2/3/4/5/6/7/8] <<---"))
    print(" ")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        while True:
            empid = input("Enter your Employee ID: ")
            if validid(empid):
                break
            else:
                print("Please Enter the Valid Employee ID")

        while True:
            empname = input("Enter the Name: ")
            if validname(empname):
                break
            else:
                print("Please Enter the valid name")

        while True:
            salary = int(input("Enter your Salary : "))
            if validsalary(salary):
                break
            else:
                print("Please Enter the valid Salary")

        while True:
            age = int(input("Enter Your Age: "))
            if validage(age):
                break
            else:
                print("Please Enter the Valid Age")
        while True:
            gender = input("Enter your Gender : ")
            if validGender(gender):
                break
            else:
                print("Please Enter the valid Gender")

        while True:
            Address = input("Enter your Address : ")
            if ValidAddress(Address):
                break
            else:
                print("Please Enter the valid Address")

        while True:
            City = input("Enter your city : ")
            state = input("Enter your state : ")
            if validcity(state.title(), City.title()):
                break
            else:
                print("Please Enter the valid City")

        while True:
            DOB = input("Enter your Date of Birth in dd/mm/yyyy format : ")
            if CheckDOB(DOB):
                break
            else:
                print("Please Enter the valid DOB")

        while True:
            DOJ = input("Enter your Date of Joining in dd/mm/yyyy format : ")
            if CheckDOJ(DOJ):
                break
            else:
                print("Please Enter the valid DOJ")

        while True:
            Deptname = input("Enter your Department Name : ")
            if validDept(Deptname):
                break
            else:
                print("Please Enter the valid Department name")


        while True:
            Designation = input("Enter your Designation : ")
            if validDesign(Designation):
                break
            else:
                print("Please Enter the valid Designation")

        while True:
            pan = input("Enter your Pan Number : ")
            if validPan(pan):
                break
            else:
                print("Please Enter the valid Pan Number")

        while True:
            aadhar = input("Enter your Aadhar Number : ")
            if validAadhar(aadhar):
                break
            else:
                print("Please Enter the valid Aadhar Number")


        e = employee(empid, empname, salary, age, gender, Address, City, DOB, DOJ, Deptname, Designation, pan, aadhar)

        emp.append(e)


    elif choice == 2:
        print("Details of Employee: ")
        for i in emp:
            i.display()

    elif choice == 3:
        print("Press A to be searched by Employee Name ")
        print("Press B to be searched by Employee ID ")
        print("Press C to be searched by Department Name ")
        print("Press D to be searched by Designation")
        ch = input("Enter your choice: ")

        if ch == "A":
            nm = input("Enter the name to be searched:  ")
            flag = True
            for i in emp:
                if i.empname == nm:
                    flag = False
                    i.display()
                    print("Record Searched")
            if flag == True:
               print("Please Enter the valid Name")
        elif ch == "B":
            id = input("Enter the Employee ID to be searched:  ")
            flag = True
            for i in emp:
                if i.empid == id:
                    flag = False
                    i.display()
                    print("Record Searched")
            if flag == True:
                    print("Please Enter the valid EmpID")
        elif ch == "C":
            dept = input("Enter the Department name to be searched:  ")
            flag = True
            for i in emp:
                if i.Deptname == dept:
                    flag = False
                    i.display()
                    print("Record Searched")
            if flag == True:
                    print("Please Enter the valid Department")
        elif ch == "D":
            des = input("Enter the Designation of employee to be searched:  ")
            flag = True
            for i in emp:
                if i.Designation == des:
                    flag = False
                    i.display()
                    print("Record Searched")
            if flag == True:
                    print("Please Enter the valid Designation")
        else:
            print("Please Enter the valid choice")


 
    elif choice ==4:
         print("Press I to update Name")
         print("Press II to update Address")
         print("Press III to update DOB")
         print("Press IV to update Salary")
         ch = input("Enter Your Choice : ")

         if ch == "I":
             id = input("Enter Employee id whose name have to updated: ")
             nm = input("Enter updated Name: ")

             flag = True
             for i in emp:
                 if i.empid == id:
                     flag = False
                     i.empname = nm
                     print("Name Updated Successfully")
             if flag == True:
                 print("Please Enter the valid EmpID")


         elif ch == "II":
             id = input("Enter Employee id whose address have to updated: ")
             a = input("Enter updated Address: ")
             flag = True
             for i in emp:
                 if i.empid == id:
                     flag = False
                     i.Address = a
                     print("Address Updated Successfully")
             if flag == True:
                 print("Please Enter the valid EmpID")

         elif ch == "III":
             id = input("Enter Employee id whose DOB have to updated: ")
             d = input("Enter updated DOB : ")
             flag = True
             for i in emp:
                 if i.empid == id:
                     flag = False
                     i.DOB = d
                     print("DOB Updated Successfully")
             if flag == True:
                 print("Please Enter the valid EmpID")


         elif ch == "IV":
                    # s = int(input("Enter updated salary: "))
             print("Press a to update salary of specific Employee by EID ")
             print("Press b to update salary of all Employee in specific department ")
             print("Press c to update salary of all employee")
             ch = input("Enter Your Choice: ")
             if ch == "a":
                s1 = input("Enter Employee ID to update their salary :")
                b1 = int(input("Enter increment amount in salary : "))
                flag = True
                for i in emp:
                # incr = 0
                    if i.empid == s1:
                              flag = False
                             # incr = (i.salary*(b1//100))
                             # i.salary = i.salary + incr
                              i.salary = i.salary + b1
                              print("Salary Updated Successfully")
                if flag == True:
                     print("Please Enter the valid Emp id")

             elif ch == "b":
                s1 = input("Enter Department to update their salary :")
                b1 = int(input("Enter increment in Salary : "))
                flag = True
                for i in emp:
                    if i.Deptname == s1:
                       flag = False
                       i.salary = i.salary + b1
                       print("Salary Updated Successfully")
                if flag == True:
                        print("Please Enter the valid Data")

             elif ch == "c":
                b1 = int(input("Enter increment in Salary of all employees: "))
                for i in emp:
                    i.salary = i.salary + b1
                    print("Salary Updated Successfully")

             else:
                print("Invalid Choice")

    elif choice == 5:
        print("Press A to be Delete by Employee ID ")
        print("Press B to be Delete by Employee Name ")
        print("Press C to be Delete by Department Name ")
        ch = input("Enter your choice: ")
        if ch == "A":
            id = input("Enter Employee ID to delete the record: ")
            flag = True
            for i in emp:
                if i.empid == id:
                    flag = False
                    emp.remove(i)
                    print("Record Deleted Successfully")
            if flag == True:
               print("Please Enter the valid EmpID")
        elif ch == "B":
            nm = input("Enter Employee Name to delete the record: ")
            flag = True
            for i in emp:
                if i.empname == nm:
                    flag = False
                    emp.remove(i)
                    print("Record Deleted Successfully")
            if flag == True:
               print("Please Enter the valid EmpName")

        elif ch == "C":
            d = input("Enter Department Name to delete the record: ")
            flag = True
            for i in emp:
                if i.Deptname == d:
                    flag = False
                    emp.remove(i)
                    print("Record Deleted Successfully")
            if flag == True:
               print("Please Enter the valid Department Name")

        else:
            print("Please Enter the Valid Choice")

    elif choice == 6:
        max_sal = -1
        empl = None
        for i in emp:
            salary = i.salary
            if salary > max_sal:
                max_sal = salary
                empl = i
        if max_sal != -1:
            i.display()
            # print("Max sal is :", max_sal)
        else:
            print("Invalid!!")

    elif choice == 7:
        min_sal = float('inf')
        empl = None
        for i in emp:
            salary = i.salary
            if salary < min_sal:
                min_sal = salary
                empl = i

        # if min_sal != float('inf'):
        if empl is not None:
            empl.display()
            # print("Min sal is :", min_sal)
        else:
            print("Invalid!!")

    elif choice == 8:
        break

    else:
      print("Invalid Choice")



