import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 设置字体为支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
data_path = 'D:\\数据分析'
data_filenames = ['会员消费表.csv']

def collect_data():
    data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        try:
            data_arr = pd.read_csv(data_file, encoding='utf-8')
        except UnicodeDecodeError:
            data_arr = pd.read_csv(data_file, encoding='gbk')
        data_arr_list.append(data_arr)
    return data_arr_list

def process_data(data_arr_list):
    clothes_style_list = []
    for data_arr in data_arr_list:
        # 假设衣服款式在名为'款号'的列中
        clothes_style = data_arr['款号']
        clothes_style_list.append(clothes_style)
    return clothes_style_list

def analyze_data(clothes_list):
    all_styles = np.concatenate(clothes_list)
    unique_styles, counts = np.unique(all_styles, return_counts=True)
    most_popular_style = unique_styles[np.argmax(counts)]
    max_count = np.max(counts)
    print(f"卖得最多的款式是: {most_popular_style}，销售数量为: {max_count}")
    # 对销售数量进行降序排序
    sorted_indices = np.argsort(-counts)
    sorted_styles = unique_styles[sorted_indices]
    sorted_counts = counts[sorted_indices]
    # 只保留前20名的数据
    sorted_styles = sorted_styles[:20]
    sorted_counts = sorted_counts[:20]
    return sorted_styles, sorted_counts

def show_results(sorted_styles, sorted_counts):
    plt.figure(figsize=(10, 8))
    plt.barh(sorted_styles, sorted_counts, color='skyblue')
    plt.xlabel('销量')
    plt.title('各款式衣服的销量从大到小排序（前二十名）')
    plt.gca().invert_yaxis()  # 反转y轴，使销量最多的款式在顶部
    plt.show()

def main():
    # 数据获取
    data_arr_list = collect_data()
    # 数据处理
    clothes_list = process_data(data_arr_list)
    # 数据分析
    sorted_styles, sorted_counts = analyze_data(clothes_list)
    # 数据展示
    show_results(sorted_styles, sorted_counts)

if __name__ == '__main__':
    main()