import random
# name of the person who will be asking the question
name = "BB"

# question you’d like to ask 
question = ["Am I cool or what?"]

# store the answer of the Magic 8-Ball in this variable
answer = ""
 
# variable to store the randomly generated value
random_number = random.randint(1, 9)

# print(random_number) test randint works

#implement core logic here
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer =  "Error"

print(name +  " asks: " + question)
print("Magic 8-Ball's answer: " +  answer)
