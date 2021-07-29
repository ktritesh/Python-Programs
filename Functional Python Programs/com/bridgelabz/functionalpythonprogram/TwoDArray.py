"""""
*author - Ritesh KT
*date - 29-07-2021
*time - 08:00 AM
*title - Two Dimensional Array
"""""

class TwoDArray:
    def __init__(self, noOfRows, noOfColumns):
        self.noOfRows = noOfRows               #initialize constructor using parameters
        self.noOfColumns = noOfColumns          #initialize constructor using parameters

    def calMatrix(self):   #define calculate Matrix method to calculate the two dimensional matrix
        matrix = []
        for rows in range(self.noOfRows):
            data = []
            for columns in range(self.noOfColumns):
                data.append(int(input()))
            matrix.append(data)

            for rows in range(self.noOfRows):
                for columns in range(self.noOfColumns):
                    print(matrix[rows][columns], end=" ")
                print()

            return matrix

#main method
if __name__ == '__main__':
    # Exceptional Handeling
    try:
        noOfRows = int(input("Enter the number of rows: "))
        noOfColumns = int(input("Enter the number of Columns: "))
        twoDArrayObject = TwoDArray(noOfRows, noOfColumns) #Creating Object
        z = twoDArrayObject.calMatrix() #Calling method using reference variable
        print(z)
    except ValueError:
        print("Enter integer value")
    except:
        print("Exception Occured")