import requests
import random
import re

min = 1
max = 6
n = 5

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

try:
    ask_user = int(input('How many word do you want in your passphrase (Recommend a minimum of six words): ')) * 5

    def main():

        result_list = []

        for i in range(0, ask_user):
            x = random.randint(min, max)

            result_list.append(x)

        final_list = [result_list[i * n:(i + 1) * n] for i in range((len(result_list) + n - 1) // n )]

        wordlist = []

        for i in final_list:
            word = ""
            for j in i:
                word = word+str(j)
            wordlist.append(word)

        diceware_list_url = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'

        req = requests.get(diceware_list_url).content.decode('utf-8')

        words = []

        for o in wordlist:
            t = re.search(o + r'.*', req)
            c = t.group()
            v = re.sub(r'\s+', '', c)[5:]
            words.append(v)

        print('\n- YOUR WORDS ARE -\n')
        for i in words:
            print(i, end=' ')

        final = " ".join(words).replace(" ", "")

        print('\n\n- YOUR PASSPHRASE IS -\n')
        print(final)

    main()

except(KeyboardInterrupt):
    print("\nProgramme Interrupted")
