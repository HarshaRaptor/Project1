from time import sleep
import sys
from data import Countries

CountryL = Countries.countries_list

def prompt():
    #Globalizing input variables to be used in the main function, to write the data onto the document
    global first_name
    global last_name
    global age
    global gender
    global email
    global state
    global city
    global living_country
    global country_of_birth
    global occupation
    global error
    global pronoun
    global ggender
    #survey rules
    print("You are required to answer the following quetions honestly.")
    #time given for user to read
    sleep(2)
    #ask if user is ready and had agreed to rules
    print("Are you ready? (y/n)")
    #get user's input
    take = input('>')
    #check if the user agreed to the rules
    try:
        if take == 'y':           
            #prompt the user the questions
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            age = int(input("Enter your age: "))
            gender = input("Enter your gender (M)ale | (F)emale | (O)ther: ")
            living_country = input("What country do you live in?(first letter MUST be upper case): ")
            country_of_birth = input("What is your country of birth?(first letter MUST be upper case): ")
            state = input("What state do you live in? ")
            city = input("What city do you live in? ")
            occupation = input("What is your occupation? ")
            email = input("Enter your Email:")
            print("Thanks for answering the questions!")
        #if not agreed, quit from program
        else:
            exit()
    except:
        print("Wrong input")
        quit()
        
    #check if the user's input's country even exists from the list of countries
    if living_country in CountryL:
        error = "no"
    else:
        error = "yes"
    #check if the user's input's country even exists from the list of countries
    if country_of_birth in CountryL:
        error = "no"
    else:
        error = "yes"
    #Only awailable options for gender, any other reply will be error is true
    if gender == "M" or gender == "m" or gender == "F" or gender == "f" or gender == "O" or gender == "o":
        error = "no"
    else:
        error = "yes"
    #check if the entered age is valid or just a random number
    if age < 110 and age > 3:
        error = "no"
    else:
        error = "yes"
    
    if ".com" in email and "@" in email:
        error = "no"
    else:
        error = "yes"
    
    if gender == "M" or gender == "m":
        pronoun = "he"
        ggender = "male"
    elif gender == "F" or gender == "h":
        pronoun = "she"
    elif gender == "O" or gender == "o":
        pronoun = "they"
    else:
        error = "yes"
    
    
#main function to execute the whole program
def main():
    global view
    #function to get user's input
    prompt()
    #open document with writing permission
    try:
        outfile = open("info.txt", "a")
        #write info onto document
        if error == "no":
            print("Survey had been successfully finished!")
            outfile.write("__NEW USER__")
            outfile.write("\n")
            outfile.write("First name: " + first_name)
            outfile.write("\n")
            outfile.write("Last name: " + last_name)
            outfile.write("\n")
            outfile.write("Age: " + str(age))
            outfile.write("\n")
            outfile.write("Gender: " + gender)
            outfile.write("\n")
            outfile.write("Country of living: " + living_country)
            outfile.write("\n")
            outfile.write("Country of birth: " + country_of_birth)
            outfile.write("\n")
            outfile.write("State of living: " + state)
            outfile.write("\n")
            outfile.write("City of living: " + city)
            outfile.write("\n")
            outfile.write("Occupation : " + occupation)
            outfile.write("\n")
            outfile.write("Email: " + email)
            outfile.write("\n")
            outfile.write("\n")

            print("To see summary type '1' to end session type '0'")
            view = int(input('>'))
            if view == 1:
                print("Generating...")
                sleep(2)
                print(f'{first_name} {last_name} is a {ggender}, \n{pronoun} is from {city}, {state}, {living_country},\n{pronoun} was born in {country_of_birth}.\n{first_name} is currently {age} years old, and {pronoun} works as a {occupation}. \nYou can contact {first_name} via email: {email} ')
            else:
                pass
            
        #if error is positive, display a message and exit the program without considering any info
        elif error == "yes":
            print("Not considered!")
            quit()
        else:
            pass
    except:
        print("Error occured")
    finally:
        #Closing file
        outfile.close()

#execute the function
main()

