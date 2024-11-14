"""
STEP 1: Fix the declaration of the functions below to get the 
tests in test_functions.py to run.
"""

def get_date_of_birth(id_number): 
    """
    STEP 2: Extract the date of birth from the ID number and return it as a string
    """
    #todo
    DOB = id_number[0:6]
    Day = DOB[4:6]
    month = DOB[2:4]
    year = DOB[0:2] 
    return (f"{Day}/{month}/{year}")
    
print(get_date_of_birth("0004185035083"))
def get_gender(id_number):
    """
    STEP 3: Extract the gender from the ID number using the formula below and return
    it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is
    female and if it is greater than 4999, the person is male.
    """
    #todo
    gender = id_number[6]
    if int(gender) < int(5) :
        return "Female"
    elif int(gender) > int(4):
        return "Male"
    else:
        print("Invalid id")
print(get_gender('9106236034082'))
def get_citizenship(id_number):
    """
    STEP 4: Extract the citizenship from the ID number using the formula below and 
    return it as a string

    Formula: 1 if the ID number's 11th to 12th digit is less than 01, the person is
    a South African citizen and if it is greater than 01, the person is a non-South 
    African citizen.
    """
    #todo
    citizenship = id_number[10]
    if int(citizenship) > 0 == 0 :
        return "Non-South African"
    else:
        return "South African"
    
    
print(get_citizenship('9210304503082'))