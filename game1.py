import random

time = 0
win_time = 0
bot_choice = 'null'  # 初始化游戏次数、玩家胜利次数和机器人实际选择
choice = str(input('输入start开始游戏或者exit结束游戏：'))
if choice == 'start':
    print('游戏规则不用多介绍了吧，输入1代表剪刀，2代表石头，3代表布，采用五局三胜制')
    while time < 5:
        try:
            user_choice = int(input('你的选择是：'))
        except ValueError:
            print('请输入规定的内容.')
        except ():
            print('程序出现纰漏，请联系我.')
        else:
            bot_choice_number = random.choice([1, 2, 3])
            if bot_choice_number == 1:
                bot_choice = '剪刀'
            elif bot_choice_number == 2:
                bot_choice = '石头'
            elif bot_choice_number == 3:
                bot_choice = '布'  # 将机器人选择转换为可视内容
            print("电脑出的是：\n", bot_choice)
            if user_choice == 1:
                if bot_choice_number == 1:
                    print("平局，请再出一次")
                elif bot_choice_number == 2:
                    print("你输了")
                    time = time + 1
                elif bot_choice_number == 3:
                    print("你赢了！")
                    win_time = win_time + 1
                    time = time + 1
            elif user_choice == 2:
                if bot_choice_number == 2:
                    print("平局，请再出一次")
                elif bot_choice_number == 3:
                    print("你输了")
                    time = time + 1
                elif bot_choice_number == 1:
                    print("你赢了！")
                    win_time = win_time + 1
                    time = time + 1
            elif user_choice == 3:
                if bot_choice_number == 3:
                    print("平局，请再出一次")
                elif bot_choice_number == 2:
                    print("你输了")
                    time = time + 1
                elif bot_choice_number == 1:
                    print("你赢了！")
                    win_time = win_time + 1
                    time = time + 1
            else:
                print('请输入规定的内容.')
            # 以上内容为游戏主体代码
    if win_time > 2:  # 胜利条件判断
        print('恭喜你获得胜利！')
    else:
        print('很遗憾，下次再试试吧.')
elif choice == "exit":
    print('下次来玩呀~')
