from wordlist import wordlist
import secrets

DICE_COUNT = 5
dice_rolls = []
word_list = []

print('''

                8888888b.  8888888b.   .d8888b.
                888  "Y88b 888   Y88b d88P  Y88b
                888    888 888    888 888    888
                888    888 888   d88P 888
                888    888 8888888P"  888  88888
                888    888 888        888    888
                888  .d88P 888        Y88b  d88P
                8888888P"  888         "Y8888P88

        (Diceware Password Generator by Sameera Madushan)
''')

while True:
    try:
        ask_user = int(input('How many words do you want in your passphrase (Recommend a minimum of six words): '))
        val = int(ask_user)
        if val > 0:
            break
        else:
            print("\nSorry, Number can't be negative(-ve) or zero(0), try again\n")
            continue
    except ValueError:
        print("\nSorry, Input must be a number, try again\n")
        continue

# From reddit user u/turkoid
for _ in range(ask_user):
    dice = ''.join(str(secrets.randbelow(6) + 1) for _ in range(DICE_COUNT))
    dice_rolls.append(dice)

for i in dice_rolls:
    for k, v in wordlist.items():
        if i == k:
            word_list.append(v)

print('\n- YOUR WORDS ARE -\n')
for i in word_list:
    print(i, end=' ')

final_passphrase = " ".join(word_list).replace(" ", "")

print('\n\n- YOUR PASSPHRASE IS -\n')
print(final_passphrase)
