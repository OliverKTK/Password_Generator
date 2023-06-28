import random as rdm
import string as stg

GENERATE = True
GENERATION_NUM = 1000
NUM_PASS = 1
PASS_SIZE = 8
LOWERCASE_NUM = 3   
UPPERCASE_NUM = 1   

list_lowercase = list(stg.ascii_lowercase)
list_uppercase = list(stg.ascii_uppercase)
password = []
generated_pass = []
finall_pass = []

num_lowercase = 0
num_uppercase = 0


while GENERATE:
    for i in range(PASS_SIZE):
        seed = rdm.randrange(0, 10)
        letter_seed = rdm.randrange(0, 26)
        if seed <= 2:
            password.append(list_lowercase[letter_seed])
            num_lowercase += 1
        elif seed <=4 and seed > 2:
            password.append(list_uppercase[letter_seed])
            num_uppercase += 1
        else:
            password.append(seed)
    password = ''.join(map(str, password))

    if num_lowercase == LOWERCASE_NUM and num_uppercase == UPPERCASE_NUM:
        generated_pass.append(password)
        if len(generated_pass) == GENERATION_NUM:
            for i in range(NUM_PASS):
                finall_choice = rdm.choice(generated_pass)
                finall_pass.append(finall_choice)
            GENERATE = False
    password = []
    num_lowercase, num_uppercase = 0, 0

print(finall_pass)
