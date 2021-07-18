# Author:Tom_Steve
# Date:2021-07-17


# Please write your own program here
import nerdScore as ns

check1 = False
check2 = False
check3 = False  # 用于每一个选项的输入检查
while True:
    print(
        '1.Enter Fandom Score\n2.Enter Hobbies Score\n3.Enter Number of Sports played\n4.Calculate Nerd '
        'Score\n5.Print Nerd Rating of Students')
    menu = input("please input your choice or 'exit' to exit the program:")
    if menu == '1':
        print('1.Enter Fandom Score')
        while True:
            try:
                FandomScore = int(input('Please input the number of things you like:'))
            except ValueError:
                print('please enter the number not characters.')
            except ():
                print("unknown error, please contact the author.")
            else:
                if FandomScore > 0:
                    check1 = True
                    break
                else:
                    print('please enter the number which is greater zero.')

    elif menu == '2':
        print('2.Enter Hobbies Score')
        while True:
            try:
                hobbies = int(input('please input the number of things you like to do every week:'))
            except ValueError:
                print('please enter the number not characters.')
            except ():
                print('unknown error, please contact the author.')
            else:
                if hobbies >= 0:
                    HobbiesScore = hobbies * 4
                    check2 = True
                    break
                else:
                    print('please enter the number which is greater zero.')

    elif menu == '3':
        print('3.Enter Number of Sports played')
        while True:
            try:
                SportsNum = int(input('please input your sports play every week:'))
            except ValueError:
                print('please enter the number not characters.')
            except ():
                print('unknown error, please contact the author.')
            else:
                if SportsNum > 0:
                    check3 = True
                    break
                else:
                    print('please enter the number which is greater zero.')

    elif menu == '4':
        print('4.Calculate Nerd Score')
        if not check1:
            print('error,please finish the first part.')
        elif not check2:
            print('error,please finish the second part.')
        elif not check3:
            print('error,please finish the third part.')
        else:
            score=ns.calculateSkillEquation(FandomScore, HobbiesScore, SportsNum)
            print('your nerd score is', score)

    elif menu == '5':
        print('5.Print Nerd Rating of Students')
        if not check1:
            print('error,please finish the first part.')
        elif not check2:
            print('error,please finish the second part.')
        elif not check3:
            print('error,please finish the third part.')
        else:
            levels = 0
            studentScores=score
            if 0 <= studentScores <= 1:
                levels = 'Nerdlite'
            elif 1 < studentScores <= 10:
                levels = 'Nerdling'
            elif 10 < studentScores <= 100:
                levels = 'Nerdlinger'
            elif 100 < studentScores <= 500:
                levels = 'Nerd'
            elif 500 < studentScores <= 1000:
                levels = 'Nerdington'
            elif 1000 < studentScores <= 2000:
                levels = 'Nerdrometa'
            elif studentScores > 2000:
                levels = 'Nerd Superme'
            if levels == 0:
                print('error,please check your input behand.')
            else:
                print('your level is', levels)

    elif menu == 'exit':
        print('thanks for using')
        break
