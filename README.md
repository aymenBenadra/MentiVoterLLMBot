# Mentimeter Voting Bot

[Mentimeter polls](https://www.menti.com/) is a website that allows polling and receiving votes from an audience. Its a great evening timepass to play with my friends. There are groups of friends who intentionally put questions to demean others. A very light example: not knowing what does POTUS or LOTUS stand for. This repository provides a way (although a bit evil) to sabotage such malicious attempts at singling out people for heir lack of general knowledge.

This bot needs id of the menti poll and it automatically goes and scrambles the votes by adding numerous fake votes.

## How to run

1. Install [chromedriver dependency](http://chromedriver.storage.googleapis.com/index.html) - download chromedriver, unzip, move to /usr/local/bin (Mac OS / Linux)

2. Install selenium: `pip install selenium`

3. Use `venv`:

```
vishwarajan-mbp:chrome_automation vishwarajanand$ virtualenv venv

# to open editor
(venv) vishwarajan-mbp:chrome_automation vishwarajanand$ code .

# to run
vishwarajan-mbp:chrome_automation vishwarajanand$ source venv/bin/activate
(venv) vishwarajan-mbp:chrome_automation vishwarajanand$ python web_bot.py
```

### Note

If mac stops `chromedriver` claiming "the developer cannot be verified", do the following steps:

1. `cd /usr/local/bin`
2. `xattr -d com.apple.quarantine chromedriver`

## Demo Video

[![Watch on YouTube](https://img.youtube.com/vi/Z_TMaeemu6Y/sddefault.jpg)](https://youtu.be/Z_TMaeemu6Y)
