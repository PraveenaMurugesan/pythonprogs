temp=float(input("Enter the temperature:"))
unit=input("Enter the unit of Measurement C/c,F/f,K/k:")
#celsius to fahrenheit and kelvin
a=((9/5)*temp)+32            #celsius to fahernheit
b=(temp+273.15)              #celsius to kelvin
#fahernheit to celcius and kelvin
c=((5/9)*(temp-32))          #fahernheit to celsius
d=(((5/9)*(temp-32))+273.15) #fahernheit to kelvin
#Kelvi to celsius and fahernheit
e=temp-273.15                #kelvin to celsius
f=(((9/5)*(temp-273.15))+32) #kelvin to fahrenheit

if(unit =="C"or unit=="c"):
    print("You have entered the temperature in celsius,converting to fahernheit and kelvin.....")
    print("The temperature in fahernheit:",a,"F")
    print("The temperature in kelvin:",b,"K")
elif(unit=="F"or unit=="f"):
    print("You have entered the temperature in Fahrenheit,converting to celsius and kelvin.....")
    print("the temperature in celsius:",c,"C")
    print("the temperature in kelvin:",d,"K")
elif(unit=="K"or unit=="k"):
    print("You have entered the temperature in kelvin,converting to celsius and fahrenheit.....")
    print("the temperature in celsius:",e,"C")
    print("the temperature in fahrenheit:",f,"F")
else:
    print("Invalid Unit of Measurement.")
