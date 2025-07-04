import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置字体为支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
data_path = 'D:\\数据分析'
data_filenames = ['会员信息表.csv']


def collect_and_process_data():
    data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = pd.read_csv(data_file, encoding='gbk')
        print(data_arr.columns)  # 打印列名以检查
        data_arr_list.append(data_arr)
    return data_arr_list


def analyze_data(data_arr_list):
    data_arr = pd.concat(data_arr_list, ignore_index=True)

    # 检查并处理可能的空值
    data_arr = data_arr.dropna(subset=['会员等级', '年龄'])

    plt.figure(figsize=(10, 6))
    bins = range(18, 70, 5)
    hist1, bins1, _ = plt.hist(data_arr[data_arr['会员等级'] == '黄金会员']['年龄'],
                               bins=bins, color='gold', alpha=0.7, label='黄金会员')
    hist2, bins2, _ = plt.hist(data_arr[data_arr['会员等级'] == '白银会员']['年龄'],
                               bins=bins, color='silver', alpha=0.7, label='白银会员')

    # 在每个条形上添加数字
    for i in range(len(bins1) - 1):
        plt.text((bins1[i] + bins1[i + 1]) / 2, hist1[i] / 2, f'{int(hist1[i])}',
                 ha='center', va='center', fontsize=8, color='black')
        plt.text((bins1[i] + bins1[i + 1]) / 2, hist1[i] + hist2[i] / 2, f'{int(hist2[i])}',
                 ha='center', va='center', fontsize=8, color='black')

    plt.xlabel('年龄')
    plt.ylabel('会员数量')
    plt.title('会员等级与会员年龄的关系')
    plt.legend()
    plt.show()


def save_and_show_results():
    pass


def main():
    data_arr_list = collect_and_process_data()
    analyze_data(data_arr_list)


if __name__ == '__main__':
    main()