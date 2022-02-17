import numpy as np
import matplotlib.pyplot as plt
import os

dir_list = os.listdir('./log_11-27')
save_path = "./picture_11-27"
if not os.path.exists(save_path):
    os.makedirs(save_path)
fig = plt.figure()
for file in dir_list:
    open_file = './log_11-27/' + file
    number = list()
    gamma = list()
    dn_dt = list()
    diameter = list()
    para_list = file.split('_')
    txt_type = para_list[-1]

    if txt_type == "cellsnumber.txt":
        with open(open_file, 'r') as f:
            for line in f.readlines():
                 line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                 number.append(float(line.split(',')[1]))
        title = "m:" + para_list[0] + " cg:" + para_list[1] + " ck:" + para_list[2] \
                + " sr:" + para_list[3] + " sB:" + para_list[4] + '\n' \
                + " lam:" + para_list[5] + " r0:" + para_list[6] + " b0:" + para_list[7]
        para_list.pop()
        pic_name = "_".join(para_list) + "_number.jpg"
        n_len = len(number)
        x = np.arange(1, n_len + 1)

        plt.plot(x, number)
        plt.title(title, pad=10)
        plt.xlabel("days")
        plt.ylabel("Number of tumor cells")
        # plt.xlim(0, 1000)
        plt.savefig(save_path + "/" + pic_name)
        plt.clf()


    elif txt_type == "dndt.txt":
        with open(open_file, 'r') as f:
            for line in f.readlines():
                 line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                 dn_dt.append(float(line.split(',')[1]))
        title = "m:" + para_list[0] + " cg:" + para_list[1] + " ck:" + para_list[2] \
                + " sr:" + para_list[3] + " sB:" + para_list[4] + '\n' \
                + " lam:" + para_list[5] + " r0:" + para_list[6] + " b0:" + para_list[7]
        para_list.pop()
        pic_name = "_".join(para_list) + "_dndt.jpg"
        n_len = len(dn_dt)
        x = np.arange(1, n_len + 1)

        plt.plot(x, dn_dt)
        plt.title(title, pad=10)
        plt.xlabel("days")
        plt.ylabel("dn/dt")
        # plt.xlim(0, 3658)
        plt.savefig(save_path + "/" + pic_name)
        plt.clf()

    elif txt_type == "gamma.txt":
        with open(open_file, 'r') as f:
            for line in f.readlines():
                 line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                 gamma.append(float(line.split(',')[1]))
        title = "m:" + para_list[0] + " cg:" + para_list[1] + " ck:" + para_list[2] \
                + " sr:" + para_list[3] + " sB:" + para_list[4] + '\n' \
                + " lam:" + para_list[5] + " r0:" + para_list[6] + " b0:" + para_list[7]
        para_list.pop()
        pic_name = "_".join(para_list) + "_gamma.jpg"
        n_len = len(gamma)
        x = np.arange(1, n_len + 1)

        plt.plot(x, gamma)
        plt.title(title, pad=10)
        plt.xlabel("days")
        plt.ylabel("Gamma")
        # plt.xlim(0, 3658)
        plt.savefig(save_path + "/" + pic_name)
        plt.clf()

    elif txt_type == "diameter.txt":
        with open(open_file, 'r') as f:
            for line in f.readlines():
                 line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                 diameter.append(float(line.split(',')[1]))
        title = "m:" + para_list[0] + " cg:" + para_list[1] + " ck:" + para_list[2] \
                + " sr:" + para_list[3] + " sB:" + para_list[4] + '\n'\
                + " lam:" + para_list[5] + " r0:" + para_list[6] + " b0:" + para_list[7]
        para_list.pop()
        pic_name = "_".join(para_list) + "_diameter.jpg"
        n_len = len(diameter)
        x = np.arange(1, n_len + 1)

        plt.plot(x, diameter)
        plt.title(title, pad=10)
        plt.xlabel("days")
        plt.ylabel("Diameter")
        # plt.xlim(0, 3658)
        plt.savefig(save_path + "/" + pic_name)
        plt.clf()




# with open('cells_number.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.strip('\n')  # 去掉列表中每一个元素的换行符
#         number.append(float(line.split(',')[1]))
#
# with open('gamma.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.strip('\n')
#         gamma.append(float(line.split(',')[1]))
#
# with open('dn_dt.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.strip('\n')
#         dn_dt.append(float(line.split(',')[1]))
#
# # 绘图
# n_len = len(number)
# x1 = np.arange(1, n_len + 1)
# fig = plt.figure()
# plt.plot(x1, number)
# plt.xlabel("days")
# plt.ylabel("Number of tumor cells")
# plt.savefig('./number.jpg')
#
# g_len = len(gamma)
# x2 = np.arange(1, g_len + 1)
# fig2 = plt.figure()
# plt.plot(x2, gamma)
# plt.xlabel("days")
# plt.ylabel("Gamma")
# plt.savefig('./gamma.jpg')
#
# d_len = len(dn_dt)
# x3 = np.arange(1, d_len + 1)
# fig3 = plt.figure()
# plt.plot(x3, dn_dt)
# plt.xlabel("days")
# plt.ylabel("dn/dt")
# plt.savefig('./dndt.jpg')
#
# plt.show()
