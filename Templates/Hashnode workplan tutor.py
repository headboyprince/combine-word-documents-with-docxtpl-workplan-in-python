from docxtpl import DocxTemplate
import locale
import math
import re #this module will substitute substrings which match a certain pattern with another string.
locale.setlocale(locale.LC_ALL, 'en_US')


pattern = r'\d+(\. \d{1,2})?' #a regex pattern used to match any number

with open("employee_data.csv", "r") as csvfile: #name the csvfile whatever you want.
    file = csvfile.readlines()

for column in file [1:]:
    workplan_number = column.split(",")[0]#first column
    first_name = column.split(",")[1] #second column
    last_name = column.split(",")[2] #thrid column
    gender = column.split(",")[3] #fourth column
    age = column.split(",")[4] #fifth column
    email = column.split(",")[5] #sixth column
    phone = column.split(",")[6] #seventh column
    education = column.split(",")[7] #eight column
    experience = column.split(",")[8] #ninth column
    salary = column.split(",")[9] #tenth column

    salary_locale = re.sub(pattern, lambda x:locale.currency(float(x.group()), grouping =True), salary)





    context={'First_Name': first_name,
            'Last_Name': last_name,
            'Gender': gender,
            'Age': age,
            'Email_Address': email,
            'Phone_Number': phone,
            'Education_Qualification': education,
            'Years_of_Experience': experience,
            'Salary': salary_locale}

    doc = DocxTemplate("employee_workplan.docx")

    doc.render(context)
    doc.save(f'{workplan_number} {first_name} {last_name} workplan.docx')
    print(f'{workplan_number} {first_name} {last_name} workplan.docx')