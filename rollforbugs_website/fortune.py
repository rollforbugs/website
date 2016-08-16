import random

fortunes = [
    "OH GOD THEY'RE EVERYWHERE",
    "Have you tried jQuery?",
    "chmod a-x \"$(which chmod)\""
]

def get_fortune():
    return random.choice(fortunes);