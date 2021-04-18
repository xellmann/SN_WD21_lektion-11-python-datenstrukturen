import random
import json
import datetime

secret = random.randint(1, 30)
count = 0

with open("score_dict.json", "r") as file_handle:
    score_list_dict = json.loads(file_handle.read())
    print(score_list_dict)

user_name = input("Enter your username: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    count += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret) + "!")
        print("You have guessed {0} times.".format(count))

        dict_entry = {
            "username": user_name,
            "attempts": count,
            "date": str(datetime.datetime.now()),
            "secret_number": secret
        }
        score_list_dict.append(dict_entry)
        with open("score_dict.json", "w") as file_handle:
            file_handle.write(json.dumps(score_list_dict))
        break
    elif guess < secret:
        print("Sorry, your guess is too small... The secret number is not " + str(guess))
    else:
        print("Sorry, your guess is too big... The secret number is not " + str(guess))
