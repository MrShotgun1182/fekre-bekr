from random import randint
import re


def maker():
    list_of_color = ['R', 'G', 'Y', 'P', 'G','B']
    _text = ""
    for i in range(4):
        index = randint(0, 5)
        _text += list_of_color[index]

    return _text


def trueStructureTest(PA):
    PA = PA.upper()
    test = re.search(r'^[RGOYPB]{4}$', PA)

    if test == None:
        print("Unknown color")
        PA = input("Enter again: ")
        trueStructureTest(PA)
    
    return PA


def colorTest(PA, CA):
    colorCounter = 0
    for colorPlayer in PA:
        colorPlace = 0

        for colorAnswer in CA:
            if colorPlayer == colorAnswer:
                CA = newCA(CA, colorPlace)
                colorCounter += 1
                break

            colorPlace += 1
    return colorCounter


def placeTest(PA, CA):
    colorPlayerIndex = 0
    placeCounter = 0

    for colorPlayer in PA:
        colorAnswerIndex = 0

        for colorAnswer in CA:

            if colorPlayer == colorAnswer and colorAnswerIndex == colorPlayerIndex:
                placeCounter += 1

            colorAnswerIndex += 1

        colorPlayerIndex += 1
    return placeCounter


def newCA(CA, trueColorIndex):
    cheng = ""
    iCounter = 0
    for i in CA:
        if trueColorIndex != iCounter:
            cheng += i
        iCounter += 1
    return cheng


def intro():
    print("Hello, welcome to the fekre bekr game")
    print("You have to try to find the four colored beads that the machine has already defined in this game")
    print("Your number of attempts is equal to: 22")
    print("To make it easier to work, briefly call the colors as follows")
    print("Orange = O || Red = R  || Yellow = Y")
    print("Purple = P || Blue = B || Green = G")


def endGame():
    global _try

    if _try == 22:
        print("Sorry, you could not win the game.\n You lose")
        return

    print("Well done, you were able to win the game!!!")
    print("Your number of attempts in this round is equal to: %s" % _try)
    print("score: %s/20" % (22 - _try))
    print("Try to score better in the next round")
    if _try == 1 or _try == 2:
        print("Don't think I didn't understand\nYou chatted, but I didn't bring it to myself -_-")


if __name__ == '__main__':

    intro()

    computerAnswer = maker()

    _try = 0

    while (True):

        playerAnswer = input()
        playerAnswer = trueStructureTest(playerAnswer)

        colorCheck = colorTest(playerAnswer, computerAnswer)
        placeCheck = placeTest(playerAnswer, computerAnswer)
        _try += 1

        if colorCheck == 4 and placeCheck == 4:
            endGame()
            break

        if _try == 22:
            endGame()
            break

        print("***" * 20)
        print("Attempt number: %s" % _try)
        print("Number of correct colors: %s" % colorCheck)
        print("Number of correct places: %s" % placeCheck)
        print("***" * 20)
        print("Orange = O || Red = R  || Yellow = Y")
        print("Purple = P || Blue = B || Green = G")
        # print(computerAnswer)
