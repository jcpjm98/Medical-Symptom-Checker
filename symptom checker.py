
print("Welcome! This app is designed to for anyone who is believed to have contracted Covid-19. A list of symptoms will appear to help with the diagnosis")

symptom_list = ["Fever,Cough,Shortness of breath,Tiredness,Aches,Runny Nose,Sore Throat,Headache,Diarrhea, Vomiting"]

print("These are the symptoms most commonly associated with the virus:", symptom_list)

# Number of symptoms displayed in numerical format
symptoms=[]
#Symptoms displayed will be appeneded into list
patient_symp =[]

symptom1= input("Are you experencing a high fever(A body tempature of 100.0 degrees or more)? (1 for yes) or (0 for No): ")
while True:
    #If it is a 1 it will add 1 to the list [symptoms] and append the symptom to the list [patient_symp]
    if symptom1 == "1":
        symptoms += ("1")
        patient_symp.append("Fever")
        break
    #If answer is 0, program will do nothing and move to the next option
    elif symptom1 == "0":
        break
    #Prevents the program from crashing. Will only take the following numbers.
    else:
        if symptom1 !="1" or "0":
            symptom1 = input("Please type either 1 for yes, or , 0 for no: ")
        
symptom2 = input("Have you experienced a dry cough within the past couple of days? (1 for yes) or (0 for no): ")
while True:
    if symptom2 == "1":
        symptoms += "1"
        patient_symp.append("Cough")
        break
    elif symptom2 == "0":
        break
    else:
        if symptom2 !="1" or "0":
            symptom2 = input("Please type either 1 for yes, or , 0 for no: ")

symptom3 = input("Have you experienced a shortness of breath within the past couple of days? (1 for yes) or (0 for no): ")
while True:
    if symptom3 == "1":
        symptoms +="1"
        patient_symp.append("Shortness of breath")
        break
    elif symptom3 =="0":
        break
    else:
        if symptom3 !="1" or "0":
            symptom3 = input("Please type either 1 for yes, or, 0 for no: ")

symptom4 = input("Have you felt abnormaly tired in the past couple of days? (1 for yes) or (0 for no): ")
while True:
    if symptom4 == "1":
        symptoms +="1"
        patient_symp.append("Tiredness")
        break
    elif symptom4 =="0":
        break
    else:
        if symptom4 !="1" or "0":
            symptom4 = input("Please type either 1 for yes, or, 0 for no: ")

symptom5 = input("Have you had any aches recently? (1 for yes) or (0 for no): ")
while True:
    if symptom5 == "1":
        symptoms +="1"
        patient_symp.append("Aches")
        break
    elif symptom5 =="0":
        break
    else:
        if symptom5 !="1" or "0":
            symptom5 = input("Please type either 1 for yes, or, 0 for no: ")
            
symptom6 = input("Do you have a runny nose ? (1 for yes) or (0 for no): ")
while True:
    if symptom6 == "1":
        symptoms +="1"
        patient_symp.append("Runny Nose")
        break
    elif symptom6 =="0":
        break
    else:
        if symptom6 !="1" or "0":
            symptom6 = input("Please type either 1 for yes, or, 0 for no: ")
            
symptom7 = input("Do you have a sore throat? (1 for yes) or (0 for no): ")
while True:
    if symptom7 == "1":
        symptoms +="1"
        patient_symp.append("Sore Throat")
        break
    elif symptom7 =="0":
        break
    else:
        if symptom7 !="1" or "0":
            symptom7 = input("Please type either 1 for yes, or, 0 for no: ") 

symptom8 = input("Are you experencing any headaches? (1 for yes) or (0 for no): ")
while True:
    if symptom8 == "1":
        symptoms +="1"
        patient_symp.append("Headache")
        break
    elif symptom8 =="0":
        break
    else:
        if symptom8 !="1" or "0":
            symptom8 = input("Please type either 1 for yes, or, 0 for no: ")    

symptom9 = input("Have you experienced diarrhea in the past couple of days? (1 for yes) or (0 for no): ")
while True:
    if symptom9 == "1":
        symptoms +="1"
        patient_symp.append("Diarrhea")
        break
    elif symptom9 =="0":
        break
    else:
        if symptom9 !="1" or "0":
            symptom9 = input("Please type either 1 for yes, or, 0 for no: ")   

symptom10 = input("Have you experienced vomitting? (1 for yes) or (0 for no): ")
while True:
    if symptom10 == "1":
        symptoms +="1"
        patient_symp.append("Vomitting")
        break
    elif symptom10 =="0":
        break
    else:
        if symptom10 !="1" or "0":
            symptom10 = input("Please type either 1 for yes, or, 0 for no: ")  
#Turns the string in the list [symptoms] and converts it to an interger so it can be added.
for i in range(0, len(symptoms)): 
    symptoms[i] = int(symptoms[i]) 

print("You stated you are experiencing",sum(symptoms),"symptom(s): \n", patient_symp,)

print("\n\n")
 
#Depending on answers above one of the following will show for the user

if sum(symptoms) >= 3 and "Fever" in patient_symp:
    print("You have 3 or more symptoms that could indicate you have contracted Covid-19.")
    print("You also indicated you had a fever. Please contact your primary care phsycian for better examination if it gets worse.")
elif sum(symptoms) >=3:
    print("You have 3 or more symptoms that could indicate you have contracted Covid-19.Please contact your primary care physician if your condition gets worse")
elif "Fever" in patient_symp:
    print("You indicated you had a fever. Please contact your primary care physican for better examination if it gets worse")
elif "Fever" and "Sore Throat" in patient_symp:
    print("A fever and sore throat could indicate you have contracted Covid-19. Contact your primary care physican if your condition gets worse.")
elif sum(symptoms)<=2 and "Fever" not in patient_symp:
    print("You most likely have not contracted Covid 19. If you do feel sick in the future, please contact your primary care physican")
else:
    if sum(symptoms) == 0:
        print("You seem fine. Let us know if you experience any complications")

#Ask user to input contact information
print("\nPlease Input your contact information or click enter to skip")
print("\n")
FirstName = input("Please Type in your First Name: ")
print("\n")
LastName = input("Please Type in Your Last Name:")
print("\n")
PhoneNum = input("Please Type in Your Phone Number in the Following format. (999-999-9999): ")
print("\n")

print("This is the contact information you submitted:", LastName, FirstName, PhoneNum, "\nThank you for running through the symptom checker.")




    
   
        
        




