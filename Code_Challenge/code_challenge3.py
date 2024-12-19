Name = input("What is your Name? ")
Gender = input("What is your Gender? ")
Age = int(input("How old are you? "))
City_Address = input("What is your City Address? ")
Contact_Number = int(input("What is your Contact Number? "))
Email_Address = input("What is your E-mail Address? ")
DOB = input("When is your Birthday? (MM/DD/YYYY) ")
POB = input("Place of Birth? ")
Civil_Status = input("Are you Single, Married, Divorced? ")
Citizenship = input("What is your Citizenship? ")
Height = float(input("What is your Height? "))
Weight = float(input("What is your Weight? "))
Employed = input("Are you currently employed? (yes/no) ")

Elementary = input("What is the name of your Elementary school? ")
EYG = int(input("What year did you graduate Elementary? "))
Highschool = input("What is the name of your Highschool? ")
HYG = int(input("What year did you graduate Highschool? "))
College = input("What is the name of your College? ")
CYG = int(input("What year did you graduate College? "))
Degree_Received = input("What degree did you receive in College? ")
Special_Skills = input("Do you have any special skills? ")

print("Personal Data:\n\tName: " + Name +
    "\n\tGender: " + Gender +
    "\n\tAge: " + str(Age) +
    "\n\tCity Address: " + City_Address +
    "\n\tContact No: " + str(Contact_Number) +
    "\n\tEmail Address: " + Email_Address +
    "\n\tDate of Birth: " + DOB +
    "\n\tPlace of Birth: " + POB +
    "\n\tCivil Status: " + Civil_Status +
    "\n\tCitizenship: " + Citizenship +
    "\n\tHeight: " + str(Height) +
    "\n\tWeight: " + str(Weight) +
    "\n\tCurrently Employed: " + str(Employed) +
    "\n\nEducational Background:\n\tElementary: " + Elementary +
    "\n\tYear of Graduate (Elementary): " + str(EYG) +
    "\n\tHighschool: " + Highschool +
    "\n\tYear of Graduate (Highschool): " + str(HYG) +
    "\n\tCollege: " + College +
    "\n\tYear of Graduate (College): " + str(CYG) +
    "\n\tDegree Received: " + Degree_Received +
    "\n\tSpecial Skills: " + Special_Skills)