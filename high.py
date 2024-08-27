import random

def game():
    score = random.randint(1,100)
    with open("highscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score: {score}")
    if(score>hiscore):
        with open("highscore.txt"  , "w") as f:
            f.write(str(score))

    return score

game()