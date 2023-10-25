import re
import datetime


def validname(name):
    l = name.split()
    if len(l) == 3:
        if l[0].isalpha() and l[1].isalpha() and l[2].isalpha():
            return True
        else:
            return False


valid_id = []
def validid(empid):
    exp = '^\d{3}$'
    if re.match(exp, empid):
        if empid not in valid_id:
            valid_id.append(empid)
            return True
        else:
            return False

def validage(age):
    if 20 <= age <= 80:
        return True
    else:
        return False

def validMobNo(mobileno):
    if len(mobileno) == 10 and mobileno.isdigit():
        return True
    else:
        return False

def validPan(pan):
    exp = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(exp, pan):
        return True
    else:
        return False


def validAadhar(aadharno):
    if len(aadharno) == 12 and aadharno.isdigit() and aadharno[0] not in ['0','1']:
        # re.match('^[^0].*',aadharno):
        return True
    else:
        return False


def validcity(state, city):
    sc = {"Maha": ["Mumbai", "Pune", "Nashik"],
          "MP": ["Indore", "Ujjain"],
          "Delhi": ["Gurgaon", "Noida"]}
    if state in sc.keys():
        v = sc[state]
        if city in v:
            return True
        else:
            return False
    return False


def validGender(gender):
    g = {"male", "female", "other", "Prefer not to say"}
    n = gender.strip().lower()
    if n in g:
        return True
    else:
        return False


def validsalary(salary):
    # if not salary.isdigit():
    #     return False
    sal = float(salary)
    if 20000 <= sal <= 100000:
        return True
    else:
        return False

#
#
def CheckDOB(dob):
    today = datetime.date.today()
    year = today.year

    exp = '^[0-9]{2}[/]{1}[0-9]{2}[/]{1}[0-9]{4}$'
    if re.match(exp, dob):
        if (int(dob[0:2]) <= 31 and int(dob[3:5]) <= 12 and int(dob[6:10]) <= year):
            if (int(dob[0:2]) > 28 and dob[3:5] == '02' and int(dob[6:10]) % 4 != 0):
                return False
            elif ((dob[3:5] == '04' or dob[3:5] == '06' or dob[3:5] == '09' or dob[3:5] == '11') and (
                    int(dob[0:2]) > 30)):
                return False
            return True
        return False

def validDept(deptname):
    validdept = ["HR", "IT", "Finance", "Marketing", "Operations", "Sales", "Account"]

    if deptname in validdept:
        return True
    else:
        return False


def validDesign(Designation):
    validdesign = ["Manager", "Associate", "Supervisor", "Developer", "Tester", "HR", "Support", "Analyst"]
    if Designation in validdesign:
        return True
    else:
        return False



def ValidAddress(address):
    exp = '^[A-Za-z0-9]+,[A-Za-z\s]+,[A-Za-z]+$'
    if re.match(exp, address):
        return True
    else:
        return False


def CheckDOJ(doj):
    today = datetime.date.today()
    year = today.year

    exp = '^[0-9]{2}[/]{1}[0-9]{2}[/]{1}[0-9]{4}$'
    if re.match(exp, doj):
        if (int(doj[0:2]) <= 31 and int(doj[3:5]) <= 12 and int(doj[6:10]) <= year):
            return True
        else:
            return False

