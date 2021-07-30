import json
import random

# Reading my Json file which contains the Questions, Answers and Options
with open("data.json", "r") as f:
    file = f.read()
    data = json.loads(file)

# Extracting the data from the Json file in as a list
question = data.get("ques")
option = data.get("opt")
answer = data.get("ans")
# Counter for Counting the Correct Answers
count = 0

# Creating a Random List of Questions, so that every time questions gets radomized of their own
ques_pattern = []
while len(ques_pattern)<3:
    pattern = random.randint(0, len(question)-1)
    if pattern not in ques_pattern:
        ques_pattern.append(pattern)
    else:
        continue

# Main program part to perform Quiz
print("*****Welcome to the Quiz Show*****")
print("Created and Designed By: Vinay Pratap Singh")
for i in ques_pattern:
    print(question[i])
    print(option[i])
    try:
        user_answer = int(input("Select your Answer: "))
        if user_answer>4:
            print("Ivalid Option Selected")
            continue
        if user_answer == answer[i]:
            count+=1
        else:
            print("Wrong Answer")
            print("Correct Answer is: Option",answer[i])
    except:
        print("Invalid Option Selected")
        continue
        
print(f"\nTotal Marks: {count}/{len(question)}")
# Finding percentage of Marks upto 2 Decimal Digit only
percentage = (count/len(question))*100
percentage = "{0:.2f}".format(percentage)
print(f"Marks Percentage: ",percentage)