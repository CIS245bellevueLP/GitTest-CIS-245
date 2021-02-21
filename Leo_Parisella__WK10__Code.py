def main():

    directory = input("Enter the directory that you want to save the file : ")

    filename = input("Enter the filename: ")

    name = input("Enter your name: ")

    address = input("Enter your address: ")

    phone_number = input("Enter your phone number: ")


    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(name+','+address+','+phone_number+'\n')
        writeFile.close()
        print("the file you just wrote to the file system and display the file contents to the user for validation purposes:")
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
      print("The dictory that you entered is not valid")
      
main()