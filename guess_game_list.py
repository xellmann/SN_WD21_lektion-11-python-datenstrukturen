import random
import json

secret = random.randint(1, 30)
count = 0
low_score = 0

with open("score.json", "r") as score:
    score_list = json.loads(score.read())
    score_list.sort()
    out_list = ""
    for x in range(len(score_list)):
        out_list = out_list + str(score_list[x])
        if x != len(score_list) - 1:
            out_list += ", "

print("Guesses so far: {0}".format(out_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    count += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret) + "!")
        print("You have guessed {0} times.".format(count))
        score_list.append(count)
        with open("score.json", "w") as score:
            score.write(json.dumps(score_list))
        break
    elif guess < secret:
        print("Sorry, your guess is too small... The secret number is not " + str(guess))
    else:
        print("Sorry, your guess is too big... The secret number is not " + str(guess))
