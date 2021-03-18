# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/height ** 2)
if(bmi < 18.5):
  print("Dear user, your bmi is "+ str(bmi)+" which suggests you are underweight")
elif(bmi >= 18.5 < 25):
  print("Dear user, your bmi is "+str(bmi)+" which suggests you have normal weight")
elif(bmi >= 25 < 30):
  print("Dear user, your bmi is "+str(bmi)+" which suggests you are slightly overweight")
elif(bmi>=30<35):
  print(f"Dear user, your bmi is {bmi} which suggests that you are obese")
else:
  print("Dear user, your bmi is "+str(bmi)+" which suggests you are clinically obese")
