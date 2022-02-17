import os
import matplotlib.pyplot as plt
import random


def random_color():
    colors1 = '0123456789ABCDEF'
    num = "#"
    for i in range(6):
        num += random.choice(colors1)
    return num


dir_name = "./group_10-11"

dir_list = os.listdir(dir_name)
for dire in dir_list:
    # print(dire)
    day = 3650
    with open("./log_10-11/" + dire + "_cellsnumber.txt", 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            number = float(line.split(',')[1])
            if number > 999999:
                day = int(line.split(',')[0])
                break
    file_list = os.listdir(dir_name + "/" + dire)
    g_number_list = [0] * 5
    day_list_list = [0] * 5
    max_list = [0] * 5
    label_list = [''] * 5
    for file in file_list:
        day_list = list()
        g_number = list()
        number_max = 0
        with open(dir_name + "/" + dire + "/" + file, "r") as f:
            for line in f.readlines():
                line = line.strip('\n')
                g_day = float(line.split(',')[0])
                number = float(line.split(',')[1])
                if g_day > day:
                    break
                else:
                    day_list.append(g_day)
                    g_number.append(number)
                    if number > number_max:
                        number_max = number
                # if number < 1.0 and g_day < 500:
                #     print(dire + " problem!!!!!!!!! " + file)
        index = -1
        max_dis = 0
        for i in range(5):
            dis = number_max - max_list[i]
            if dis > 0 and dis > max_dis:
                max_dis = dis
                index = i

        if index >= 0:
            max_list[index] = number_max
            g_number_list[index] = g_number
            day_list_list[index] = day_list
            label_list[index] = file

    # print(max_list)
    # for i in range(len(label_list)):
    #     print("name:" + label_list[i])
    #     print("start day:" + str(day_list_list[i][0]))
    for file in file_list:
        day_list = list()
        g_number = list()
        with open(dir_name + "/" + dire + "/" + file, "r") as f:
            for line in f.readlines():
                line = line.strip('\n')
                g_day = float(line.split(',')[0])
                number = float(line.split(',')[1])
                if g_day > day:
                    break
                else:
                    day_list.append(g_day)
                    g_number.append(number)
        if len(day_list) == 0:
            continue
        if file in label_list:
            y_max = max_list[0] * 0.2
        else:
            y_max = max_list[0] * 0.1
        color = random_color()
        plt.plot(day_list, g_number, color=color)
        plt.vlines(day_list[0], ymin=0, ymax=y_max, color=color)


    # for i in range(5):
    #     label = label_list[i]
    #     label = label.replace('.txt', "")
    #     label = label.replace('r-', 'r:')
    #     label = label.replace('_b-', ' b:')
    #     color = random_color()
    #     plt.plot(day_list_list[i], g_number_list[i], color=color)
    #     plt.vlines(day_list_list[i][0], ymin=0, ymax=4000, color=color)
    plt.xlim((0, day))
    plt.xlabel("days")
    plt.ylabel("Number of tumor cells in a group")
    plt.savefig("picture_10-11/" + dire + "_all_group.jpg")
    plt.clf()
