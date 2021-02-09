# Diceware Password Generator - Generate High Entropy Passwords

**Please Note - This Program Do Not Store Passwords In Any Form And All The Passwords Are Generated Locally Inside You Device.**

[Diceware](https://theworld.com/~reinhold/diceware.html) is a method used to generate cryptographically strong memorable passphrases. This is a python implementation of the diceware password generating algorithm.

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

## Support & Contributions
- Please ⭐️ this repository if this project helped you!
- Contributions of any kind welcome!

<a href="https://www.buymeacoffee.com/sameeramadushan" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## License
Diceware Password Generator is made with ♥ by [@_\_sa_miya__](https://twitter.com/__sa_miya__) and it is released under the MIT license.

**Diceware** is a **trademark** of [Arnold Reinhold](https://theworld.com/~reinhold/).
