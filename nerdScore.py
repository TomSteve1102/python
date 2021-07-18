# Author:Tom_Steve
# Date:2021-07-17


# Functionality: calculate the skill score by the equation
# x, y, z are inputs

def calculateSkillEquation(FandomScore, HobbiesScore, SportsNum):
    skillScore = 0  # initialize the output list

    # Please write your own program here
    skillScore: float = FandomScore*((42 * HobbiesScore ** 2 / (SportsNum + 1)) ** 0.5)
    return skillScore


if __name__ == '__main__':
    FandomScore, HobbiesScore, SportsNum = 1, 4, 1  # the output should be 18.33030277982336

    print(calculateSkillEquation(FandomScore, HobbiesScore, SportsNum))
