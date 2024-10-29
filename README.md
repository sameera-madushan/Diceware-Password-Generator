# Diceware Password Generator - Generate High Entropy Passwords

**Please Note - This Program Do Not Store Passwords In Any Form And All The Passwords Are Generated Locally Inside You Device.**

[Diceware](https://theworld.com/~reinhold/diceware.html) is a method used to generate cryptographically strong memorable passphrases. This is a python implementation of the diceware password generating algorithm. Inspired after watching [this](https://youtu.be/Pe_3cFuSw1E) video.

![DPG](https://user-images.githubusercontent.com/55880211/107419797-34a05800-6b3e-11eb-9e47-455309604168.gif)

## How DPG Generate Passwords?

Traditional Diceware uses rolls of physical dice, this application uses a strong random number generator in place of the dice. A virtual dice is roled 5 times, and the 5 digit number used against a lookup [table of words](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt). 6 dice rolls gives you 6 random words which are easy for a human being to remember, yet have a high amount of entropy which makes them hard to crack.

__WARNING__ : [Using a computer to generate your passphrases is not as secure as rolling physical die with a paper reference of the diceware list.](https://theworld.com/~reinhold/dicewarefaq.html#:~:text=Generating%20truly%20random%20numbers%20using%20a,better%20way%20to%20select%20passphrase%20words.)

For more details check out the diceware passphrase [home page](https://theworld.com/~reinhold/diceware.html).

## Git Installation
```
# clone the repo
$ git clone https://github.com/sameera-madushan/Diceware-Password-Generator.git

# change the working directory to Diceware-Password-Generator
$ cd Diceware-Password-Generator
```

## Usage

```
usage: python dpg.py
```

**Diceware** is a **trademark** of [Arnold Reinhold](https://theworld.com/~reinhold/).
