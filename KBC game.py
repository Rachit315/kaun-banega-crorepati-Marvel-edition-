name = input("Enter Your Name:")
print(f"{name.upper()} WELCOME TO kaun-banega-crorepati(Marvel-edition)") 
age = input("Enter Your Age:")

ques = ["How many Infinity Stones are there?",
        "Where is Captain America from?",
        "Who is Tony Stark’s father?",
        "Captain America’s shield is made of what?",
        "Who was able to pick up Thor’s hammer in Endgame?"]
ans = ["Six", "Brooklyn", "Howard Stark", "Vibranium", "Captain America"]

print("""Rules are:
1. For every right answer you will get 10,000Rs.
2. But if the your answer is wrong you will lose it all.
3. There are total of 5 Questions.
4. Only play if you are a marvel fan. """)

ready = input("Are you ready yes/no:")
if ready == "yes":
    score = 0
    for i in range(len(ques)):
        print(f"Question {i+1}: {ques[i]}")
        user_ans = input("Your answer: ")
        if user_ans.lower() == ans[i].lower():
            print("Correct Answer!")
            score += 10000
        else:
            print("Wrong answer!")
            break
    print(f"Your final score is: {score} Rs.")
elif ready == "no":
    print("Thank you for playing!")

else:
    print("Please answer in yes or no")
