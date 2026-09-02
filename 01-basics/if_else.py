age = 20

if age >= 18:
    print("You are an adult.")
    
age = int(input("How old are  you? "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
    
score = int(input("Berapa score mu? "))

if score >= 90 and score <= 100:
    print("Excellent")
elif score < 90 and score >= 80:
    print("Very Good")
elif score < 80 and score >= 70:
    print("Good")
else:
    print("Need Improvement")