"""""
*author - Ritesh KT
*date - 31-07-2021
*time - 08:00 AM
*title - Read and Write data from JSON File
"""""

import json

Students = [{"Name": "Ritesh"}, {"RollNo": "10"}, {"Address": "Pune"}]

def write_data(data):  #method to write data in json(user.json) file
    with open("user.json", "w") as fp:
        json.dump(data, fp)   #dump is used to write data into a file, fp is file pointer
        print("Data is inserted into the Json File")
    return data

def read_data(): #method to read data from json file
    with open("user.json", "r") as fp:
        studentData = json.load(fp)
    return studentData

write_data(Students) #method is called for write data into the json file
studentData = read_data() #method is called to read data fom json file
print("Student data in JSON File is: ", studentData)