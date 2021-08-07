"""""
*author - Ritesh KT
*date - 31-07-2021
*time - 11:00 AM
*title - Read and Write data in CSV File
"""""
import csv

class CsvFileIo:

    def read_write_data(self): #method to read data from CSV file
        with open('names.csv', 'r') as csv_file: #given address of CSV file and "r" is for read/open csv file
            csv_reader = csv.reader(csv_file)

            with open('new_names.csv', 'w') as new_csv_file:
                csv_writer = csv.writer(new_csv_file, delimiter='\t') #write data to csv file

                for data in csv_reader:
                    print(data) #printing data as a list
                    csv_writer.writerow(data) #write data to csv file
                    #print(data[2]) if you want to print through index 0 = fname, 1=lname, 2=email

csvFileIo = CsvFileIo() #creating object of CsvFileIo class and give a reference variable
csvFileIo.read_write_data()  #calling method read_write_data to read and write data from csv file using reference variable


