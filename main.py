import random
jifen=0
while True:
    # 生成随机目标数字
    target_number = random.randint(1, 100)
    print("欢迎来到猜数字游戏！请输入1到100之间的数字进行猜测，输入0退出游戏。")
    count=0
    # 使用while循环等待用户输入
    while True:
        guess = int(input("请输入你的猜测："))
        count += 1
        # 判断猜测的数字
        if guess == 0:
            print("游戏结束，下次再挑战吧！")
            break
        elif guess < target_number:
            print("太小了，请再试一次")
            continue
        elif guess > target_number:
            print("太大了，请再试一次")
            continue
        else:
            print("恭喜，你猜对了！")
            huode=100-count*5
            jifen+=huode
            print("本次一共猜了",count,"次，","获得",huode,"分.""累计",jifen,"分")
            break
