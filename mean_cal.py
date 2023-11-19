# 打开文本文件
with open('metric_cc_ssim_250000.txt', 'r') as file:
    # 读取文件中的内容并分割成数字列表
    numbers = [float(x) for x in file.read().split()]

# 计算平均值
if numbers:
    average = sum(numbers) / len(numbers)
    print(f'平均值: {average:.2f}')
else:
    print('文件中没有有效的数字可供计算平均值。')
