import random
import pandas as pd
import os

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

sol_x = []
sol_y = []

x2 = []
y2 = []


def generate_sorted_random_numbers():
    numbers = random.sample(range(101), 3)
    sorted_numbers = sorted(numbers)
    # str_sorted_numbers = [str(num) for num in sorted_numbers]
    return sorted_numbers


def generate_random_lowercase_letter():
    random_letter = chr(random.randint(ord("a"), ord("z")))
    return random_letter


def get_random_data():
    sort_num = generate_sorted_random_numbers()
    sort_num.append(generate_random_lowercase_letter())
    return sort_num


def count_duplicate_strings(str_list1, str_list2):
    # 使用集合来存储字符串列表中的字符串
    set1 = set(str_list1)
    set2 = set(str_list2)

    # 计算交集中字符串的个数
    intersection_count = len(set1.intersection(set2))

    return intersection_count


def last_count_duplicate_characters(str1, str2):
    you_win = False
    letter_str_1 = str1[-1]
    letter_str_2 = str2[-1]
    if letter_str_1 != letter_str_2:
        return 0, 0, False

    num_str_1 = str1[:-1]
    num_str_2 = str2[:-1]

    same_num = count_duplicate_strings(num_str_1, num_str_2)
    same_letter = 1

    if (same_num > 0) & (same_letter > 0):
        you_win = True
        # if same_num > 2:
        #     print(str1, str2, same_num, same_letter, you_win)
    return same_num, same_letter, you_win


def get_fake_num_data(fake_num=100):
    all_data = []
    new_data = []
    num_dic = {0: 0, 1: 0, 2: 0, 3: 0}
    sol = 0
    bitch_data_dic = {"sol": [], "1-1": [], "2-1": [], "3-1": [], "len_num": []}
    for i in range(fake_num):
        sol_x.append(i)
        sol += 0.05
        sol = round(sol, 6)
        this_num_data = get_random_data()
        this_time_num_dic = {0: 0, 1: 0, 2: 0, 3: 0}
        for exist_data in new_data:
            same_num, same_letter, you_win = last_count_duplicate_characters(
                this_num_data, exist_data
            )
            this_time_num_dic[same_num] += 1

            if you_win:
                if same_num > 2:
                    sol = sol * 0.3
                    sol = round(sol, 6)
                all_data.remove(exist_data)
                num_dic[same_num] += 1
        # print(len(all_data))
        all_data.append(this_num_data)
        new_data = all_data.copy()
        sol_y.append(sol)
        bitch_data_dic["sol"].append(sol)
        bitch_data_dic["1-1"].append(this_time_num_dic[1])
        bitch_data_dic["2-1"].append(this_time_num_dic[2])
        bitch_data_dic["3-1"].append(this_time_num_dic[3])
        bitch_data_dic["len_num"].append(len(new_data))

    print(len(all_data))
    print(num_dic)
    print(sol)
    # 将字典转换为 DataFrame
    df = pd.DataFrame(bitch_data_dic)

    # 打印 DataFrame
    print("DataFrame:")
    print(df.info())

    # 将 DataFrame 保存为 CSV 文件
    csv_filename = f"{current_dir}/{str(fake_num)}.csv".replace(
        "/solot_data_simulated/solot_data_simulated",
        "/solot_data_simulated/output_data/",
    )
    df.to_csv(csv_filename, index=False)


get_fake_num_data(fake_num=1000000)
