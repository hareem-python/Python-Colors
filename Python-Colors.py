color1 = input("Select a primary color from blue, red and yellow. ")
color2 = input("Select another primary color from blue, red and yellow. ")

if (color1.lower() == "blue") and (color2.lower() == "yellow"):
    print ("The secondary color formed is Green.")

elif (color1.lower() == "blue") and (color2.lower() == "red"):
    print ("The secondary color formed is Purple.")
    
elif (color1.lower() == "red") and (color2.lower() == "blue"):
    print ("The secondary color formed is Purple.")

elif (color1.lower() == "red") and (color2.lower() == "yellow"):
    print ("The secondary color formed is Orange.")

elif (color1.lower() == "yellow") and (color2.lower() == "red"):
    print ("The secondary color formed is Orange.")

elif (color1.lower() == "yellow") and (color2.lower() == "blue"):
    print ("The secondary color formed is Green.")

elif (color1.lower() == "blue") and (color2.lower() == "blue"):
    print ("The color formed is still Blue.")

elif (color1.lower() == "red") and (color2.lower() == "red"):
    print ("The color formed is still Red.")

elif (color1.lower() == "yellow") and (color2.lower() == "yellow"):
    print ("The color is still Yellow.")

else:
    print("Error.")