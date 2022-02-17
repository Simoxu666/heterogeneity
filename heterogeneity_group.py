# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:57:24 2021

"""
import os
import math
import random

# os.getcwd()
# os.chdir('E:\WangHaofan\Study3')
save_root = './log_11-27'
if not os.path.exists(save_root):
    os.makedirs(save_root)


class Group:  # 定义类,类名Group
    def __init__(self, r, b, n, start):
        self.r = r  # 类属性r
        self.b = b  # 类属性β
        self.n = [n]  # 类属性n
        self.start_time = start  # 类属性start,开始时刻t

    def __str__(self):
        s = "族群细胞数量：" + str(self.n)
        return s

    def mutated(self, n):
        self.n[-1] = self.n[-1] - n

    def grow(self, n):
        self.n[-1] = n

    def day_grow(self, n):
        self.n.append(n)

    def cure(self):
        cure_n = self.n[-1] * self.b
        if cure_n > 1:
            self.n[-1] = cure_n
        elif self.n[-1] > 1:
            self.n[-1] = 1

    def __eq__(self, other):  # 这一段函数用来判断同一天突变的多个细胞是否属于同一族群
        if not isinstance(other, Group):
            raise TypeError('=运算要求目标是Group')
        if type(self) == type(other) and self.r == other.r and self.b == other.b:
            return True
        else:
            return False


# 等间距分割函数，传入参数：起点，终点，步数(几等份)
def linspace(start, end, step):
    insist = list()
    if step == 1:
        insist.append(end)
        return insist
    lin = end - start
    increase = lin/(step - 1)
    t = start
    for i in range(step - 1):
        insist.append(t)
        t = t + increase
    insist.append(end)
    return insist

cure_mark = False
k = 1e6
diameter_each_cell = 12e-4  # 每个肿瘤细胞的直径设置为12e-4cm，即12微米
volume_each_cell = 1 / 6 * math.pi * diameter_each_cell ** 3  # 每个肿瘤细胞的体积，单位：立方厘米

end_diameter = (volume_each_cell * k * 6 / math.pi) ** (1 / 3)  # 肿瘤长到K时（即终点时）的直径，单位：cm

years = 10  # 推算年数
number_data_point = years * 365
'''
m_list = linspace(1/800, 1/800, 1)  # 计算gamma斜率的参数之一
cg_list = linspace(0.0000000850, 0.0000000850, 1)  # 计算gamma斜率的参数之一
ck_list = linspace(0.85, 0.85, 1)  # 计算gamma斜率的参数之一，小k即等于ck*大k
sr_list = linspace(0.01, 0.02, 1)  # 每次r突变带来的生长优势
sB_list = linspace(0.02, 0.02, 1)  # 每次β突变带来的生长优势
lmd_list = linspace(0.004, 0.004, 1) # 每天每个细胞发生有意义突变事件（不管几次）的概率
r0_list = linspace(0.15, 0.15, 1)  # 初始族群的r值
b0_list = linspace(0.15, 0.15, 1)  # 初始族群的β值
'''
m_list = [5e-5]
cg_list = [1e-12]  # 计算gamma斜率的参数之一
ck_list = [0.75]  # 计算gamma斜率的参数之一，小k即等于ck*大k
sr_list = [0.06]  # 每次r突变带来的生长优势
sB_list = linspace(0.01, 0.1, 10)  # 每次β突变带来的生长优势
lmd_list = linspace(0.001, 0.014, 10)  # 每天每个细胞发生有意义突变事件（不管几次）的概率
r0_list = [0.03]  # 初始族群的r值
b0_list = [0.9]  # 初始族群的β值
# m_list = [1e-8]
# cg_list = [5e-10]  # 计算gamma斜率的参数之一
# ck_list = [0.8166666666666667]  # 计算gamma斜率的参数之一，小k即等于ck*大k
# sr_list = [0.03]  # 每次r突变带来的生长优势
# sB_list = [0.05]  # 每次β突变带来的生长优势
# lmd_list = [0.05]  # 每天每个细胞发生有意义突变事件（不管几次）的概率
# r0_list = [0.03]  # 初始族群的r值
# b0_list = [0.75]  # 初始族群的β值
# m_start = 0.0001
# m_list = [m_start * 0.1, m_start * 0.2, m_start * 0.3, m_start * 0.5, m_start * 2]  # 计算gamma斜率的参数之一
# cg_list = [1e-8]  # 计算gamma斜率的参数之一
# ck_list = [0.816666666666667]  # 计算gamma斜率的参数之一，小k即等于ck*大k
# sr_list = [0.025]  # 每次r突变带来的生长优势
# sB_list = [0.025]  # 每次β突变带来的生长优势
# lmd_list = [0.002]  # 每天每个细胞发生有意义突变事件（不管几次）的概率
# r0_list = [0.05]  # 初始族群的r值
# b0_list = [0.15]  # 初始族群的β值
# m_list = [0.003]  # 计算gamma斜率的参数之一
# cg_list = [1.1e-5]  # 计算gamma斜率的参数之一
# ck_list = [0.14]  # 计算gamma斜率的参数之一，小k即等于ck*大k
# sr_list = [0.05]  # 每次r突变带来的生长优势
# sB_list = [0.05]  # 每次β突变带来的生长优势
# lmd_list = [0.01]  # 每天每个细胞发生有意义突变事件（不管几次）的概率
# r0_list = [0.03]  # 初始族群的r值
# b0_list = [0.03]  # 初始族群的β值
# m_list = [0.0016]  # 计算gamma斜率的参数之一
# cg_list = [8e-7]  # 计算gamma斜率的参数之一
# ck_list = [0.04]  # 计算gamma斜率的参数之一，小k即等于ck*大k
# sr_list = [0.05]  # 每次r突变带来的生长优势
# sB_list = [0.05]  # 每次β突变带来的生长优势
# lmd_list = [0.01]  # 每天每个细胞发生有意义突变事件（不管几次）的概率
# r0_list = [0.03]  # 初始族群的r值
# b0_list = [0.03]  # 初始族群的β值
# m_start = [0.003]
# m_list = m_start
# cg_list = [1.1e-5]  # 计算gamma斜率的参数之一
# ck_list = [0.14]  # 计算gamma斜率的参数之一，小k即等于ck*大k
# sr_list = [0.05]  # 每次r突变带来的生长优势
# sB_list = [0.05]  # 每次β突变带来的生长优势
# lmd_list = [0.01]  # 每天每个细胞发生有意义突变事件（不管几次）的概率
# r0_list = [0.03]  # 初始族群的r值
# b0_list = [0.03]  # 初始族群的β值
# m_list = [0.00166666666666668]  # 计算gamma斜率的参数之一
# cg_list = [1.1e-07]  # 计算gamma斜率的参数之一
# ck_list = [0.3]  # 计算gamma斜率的参数之一，小k即等于ck*大k
# sr_list = [0.03]  # 每次r突变带来的生长优势
# sB_list = [0.02333333333333]  # 每次β突变带来的生长优势
# lmd_list = [0.005]  # 每天每个细胞发生有意义突变事件（不管几次）的概率
# r0_list = [0.3]  # 初始族群的r值
# b0_list = [0.025]  # 初始族群的β值
# m_list = [5e-5]  # 计算gamma斜率的参数之一
# cg_list = [1e-12]  # 计算gamma斜率的参数之一
# ck_list = [0.75]  # 计算gamma斜率的参数之一，小k即等于ck*大k
# sr_list = [0.06]  # 每次r突变带来的生长优势
# sB_list = linspace(0.01, 0.1, 10)  # 每次β突变带来的生长优势
# lmd_list = [0.001] # 每天每个细胞发生有意义突变事件（不管几次）的概率
# r0_list =[0.03]  # 初始族群的r值
# b0_list = [0.9]  # 初始族群的β值
#parameter = [0, 0, 0, 0, 0, 0, 0, 0]
for m in m_list:
    #parameter[0] = m
    for cg in cg_list:
        #parameter[1] = cg
        for ck in ck_list:
            #parameter[2] = ck
            for sr in sr_list:
                #parameter[3] = sr
                for sB in sB_list:
                    #parameter[4] = sB
                    for lmd in lmd_list:
                        #parameter[5] = lmd
                        for r0 in r0_list:
                            #parameter[6] = r0
                            for b0 in b0_list:
                                #parameter[7] = b0

                                dn_dt = []  # 记录数目对时间导数的列表
                                gamma = [1]  # 记录gamma的列表,初始gamma等于1
                                number = [1]  # 记录总的肿瘤细胞数量的列表
                                diameter = [(volume_each_cell * 1 * 6 / math.pi) ** (1 / 3)] # 记录总的肿瘤直径的列表
                                group_list = []  # 族群列表，其中的每个element是一个族群，也即一个类
                                g = Group(r0, b0, 1, 1)  # 初始族群参数，四个参数分别对应r,b,n和start
                                group_list.append(g)  # 将该族群添加进列表
                                current_n_end = 1  # 最开始为1个肿瘤细胞(进入for循环前)，从这个值开始进入for循环

                                for day in range(1, number_data_point):
                                    number_groups = len(group_list)  # 找出当天初始时刻有多少个族群
                                    current_n_int_initial = 0  # current_n_int_initial为当天初始时刻瘤体内总共有多少整数个细胞,以下的for循环结束后，计算出该值
                                    for g in group_list:
                                        n_temp = math.floor(g.n[-1])
                                        current_n_int_initial += n_temp  # current_n_int_initial为当天初始时刻瘤体内总共有多少整数个细胞，此时值已算出
                                    current_n_initial = current_n_end  # 找出当天初始时刻瘤体内总共有多少个细胞,也等于前一天结束时的值，前一天结束时的值在for循环的最后有代码进行计算
                                    gamma_slope = cg * current_n_initial * (1 - current_n_initial / (
                                                ck * k * math.exp(-m * (day - 1))))  # 计算当日gamma的斜率
                                    # gamma_slope = cg * current_n_initial * (1 - current_n_initial / (ck * k))  # 计算当日gamma的斜率
                                    gamma_temp = gamma[day - 1] + gamma_slope  # 计算当日的gamma
                                    if gamma_temp < 1:
                                        gamma_temp = 1  # 如果gamma小于1,那么就将其直接调整为1
                                    gamma.append(gamma_temp)  # 将当天的gamma值添加进列表

                                    number_mutated_cell = math.floor(current_n_int_initial * lmd)  # 计算当日的变异细胞个数，取底
                                    # temp_total_number = math.floor(current_n_initial)#找到当前模型里共有多少个完整的整数个的细胞，算法待商酌
                                    r_or_b = 0  # 标记变异类型 1表示r变异 0表示β变异
                                    mutated_count = 0

                                    Index_mutated_cells = random.sample(range(1, current_n_int_initial + 1),
                                                                        number_mutated_cell)  # 变异细胞的序号（假定每个细胞都按序编了号，从1开始）
                                    for ind in Index_mutated_cells:
                                        count = 0
                                        for grp in group_list:
                                            count += 1
                                            ind -= math.floor(grp.n[-1])
                                            if ind <= 0:  # 当随机数被减到小于等于0说明找到了所在的族群，族群细胞数 n - ran 代表变异的是 第几个细胞ran=0代表最后一个细胞变异
                                                parent_i = count - 1
                                                real_ind_in_grp = ind - 1
                                                break
                                        mu_ran = random.random()  # 确定变异类型的随机数
                                        if mu_ran < 3 / 4:  # r突变的概率是β突变概率的3倍，所以这么设置
                                            r_or_b = 1
                                        else:
                                            r_or_b = 0
                                        # 处理r和b值
                                        if r_or_b == 1:  # 让别人更能看得明白的写法
                                            new_r = group_list[parent_i].r * (1 + sr)
                                            new_b = group_list[parent_i].b
                                        else:
                                            new_r = group_list[parent_i].r
                                            new_b = group_list[parent_i].b * (1 + sB)
                                        group_list[parent_i].mutated(1)  # 变异了之后原来族群的细胞数相应减少1个
                                        if group_list[parent_i].n[-1] == 0:  # 判断减少了细胞之后族群是不是没有细胞了，没有应该把族群删除
                                            del group_list[parent_i]
                                            number_groups = len(group_list)  # 更新族群数目
                                        # elif group_list[parent_i].n < 0: #这种情况在当前代码逻辑里不可能出现
                                        # 下面的代码属于判断当前这个变异的细胞是不是属于已经存在的任何一个族群，如果是，则应该归到一个族群中
                                        temp_g = Group(new_r, new_b, 1, day)  # 出来一个“暂时的”新族群
                                        group_list.append(temp_g)  # 将这个“暂时的”新族群增加进列表
                                        for grp2 in group_list[0:len(group_list) - 1]:  # 最后新加的那个族群不纳入循环，所以减1
                                            if temp_g == grp2:  # 一旦新增的“暂时的”族群跟前面任意一个族群相等，即r跟β均相等
                                                grp2.grow(grp2.n[-1] + 1)  # 则将其归入前面出现过的族群中
                                                del group_list[len(group_list) - 1]  # 从列表里删除这个“暂时的”族群
                                                # number_groups = len(group_list) #更新族群数目
                                                break  # 跳出循环
                                        # 如果for循环完了之后，没有执行if内的语句，则“暂时的”族群变为“永久的”族群保留下来
                                    number_groups = len(group_list)  # 更新族群数目
                                    # 以下代码开始计算每个族群的增长
                                    current_n_end = 0  # 将current_n_end清零，通过以下的for循环重新计算current_n_end
                                    for grp3 in group_list:
                                        slope = grp3.r * grp3.n[-1] * (1 - (current_n_initial / k) ** grp3.b) ** gamma[
                                            day - 1]
                                        new_n = grp3.n[-1] + slope
                                        grp3.day_grow(new_n)
                                        current_n_end += new_n
                                    number.append(current_n_end)
                                    current_diameter = (volume_each_cell * current_n_end * 6 / math.pi) ** (1 / 3)
                                    # if not cure_mark and current_diameter > 0.04:
                                    #     cure_mark = True
                                    #     current_n_end = 0
                                    #     for grp in group_list:
                                    #         grp.cure()
                                    #         current_n_end += grp.n[-1]
                                    #     number[-1] = current_n_end
                                    #     gamma[-1] = 2.2
                                    diameter.append(current_diameter)
                                    t_dn_dt = current_n_end - current_n_initial
                                    # if t_dn_dt < 0:
                                    #     t_dn_dt = 0
                                    dn_dt.append(t_dn_dt)
                                    if current_n_end >= k:
                                        break
                                    print("Day:{}, cells number:{}, groups number:{}, diameter:{}".format(day, current_n_end,
                                                                                             number_groups, current_diameter))


                                name = str(m) + '_' + str(cg) + '_' + str(ck) + '_' + str(sr) + '_' + str(sB) + '_' + str(lmd) + '_' + str(r0) + '_' + str(b0) + '_'
                                # 以下代码为保存数据
                                with open(save_root + "/" + name + 'groups.txt', 'w') as f:
                                    for i in range(len(group_list)):
                                        f.write("{},{},{},{}\n".format(group_list[i].r, group_list[i].b, group_list[i].n[-1],
                                                                       group_list[i].start_time))
                                with open(save_root + "/" + name + 'cellsnumber.txt', 'w') as f:
                                    for i in range(len(number)):
                                        f.write("{},{}\n".format(i + 1, number[i]))
                                with open(save_root + "/" + name + 'diameter.txt', 'w') as f:
                                    for i in range(len(diameter)):
                                        f.write("{},{}\n".format(i + 1, diameter[i]))
                                with open(save_root + "/" + name + 'gamma.txt', 'w') as f:
                                    for i in range(len(gamma)):
                                        f.write("{},{}\n".format(i + 1, gamma[i]))
                                with open(save_root + "/" + name + "dndt.txt", 'w') as f:
                                    for i in range(len(dn_dt)):
                                        f.write("{},{}\n".format(i + 1, dn_dt[i]))

                                g_save_root = "./group_10-11/" + name[:-1]
                                if not os.path.exists(g_save_root):
                                    os.makedirs(g_save_root)
                                for grp in group_list:
                                    name = "r-" + str(grp.r) + "_b-" + str(grp.b) + ".txt"
                                    with open(g_save_root + "/" + name, 'w') as f:
                                        day = grp.start_time
                                        for n in grp.n:
                                            f.write("{}, {}\n".format(day, n))
                                            day = day + 1
