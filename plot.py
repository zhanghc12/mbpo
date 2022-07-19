import os
import os
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn
import numpy as np

sns.set()
fig, axes = plt.subplots(1, 2, figsize=(20, 6.5))
axes = axes.reshape(-1)
le = []

line_labels = ['baseline', 'ir']
fontsize = 22
colorplus = ["#2CAFAC", "#FB5607"]

env = 'HalfCheetah'

dirname = '/Users/peixiaoqi/Documents/mbpo/'
baseline_dirname = dirname + 'baseline/'
ir_dirname = dirname + 'ir/'

all_names = [[], []]
all_names[0] = []
all_names[1] = []

for l1 in os.listdir(baseline_dirname):
    if env in l1:
        all_names[0].append(dirname + '/' + l1)

for l1 in os.listdir(ir_dirname):
    if env in l1:
        all_names[1].append(dirname + '/' + l1)


print(len(all_names[0]))
print(len(all_names[1]))

total_length = 200
average_num = 10
print(all_names)
for k, all_names_per_version in enumerate(all_names):
    seg_data = []
    for file_name in all_names_per_version:
        seed_data_value = []
        with open(file_name, 'r') as f:
            logs = f.readlines()
            for log in logs[1:]:
                seed_data_value.append(float(log.split(' ')[1]))
        seed_data_value = np.convolve(seed_data_value, np.ones(average_num) / average_num, mode='valid')
        seg_data.append(seed_data_value)

    mean_data = []
    std_data = []

    # print(len(seg_data[0]))
    for i in range(total_length):
    # for i in range(len(seg_data[0])):
        print(i)
        vals = []
        for j in range(len(seg_data)):
            vals.append(seg_data[j][i])

        mean = np.mean(vals)
        std = np.sqrt(np.var(vals))
        mean_data.append(mean)
        std_data.append(std)
    print(np.mean(mean_data[-50:]))
    upper_data = np.array(mean_data) + np.array(std_data)
    lower_data = np.array(mean_data) - np.array(std_data)

    # plt.plot(base_data[0][0], mean_data)
    # plt.fill_between(base_data[0][0], lower_data, upper_data, color='lightblue',alpha=0.25)
    l1 = axes[0].plot(range(len(mean_data)), mean_data, color=colorplus[k])[0]#, label=env+'-'+ratios[k])
    print(len(mean_data), len(lower_data), len(upper_data))
    axes[0].fill_between(range(len(lower_data)),lower_data, upper_data, color=colorplus[k], alpha=0.15)
    le.append(l1)

axes[0].set_xlabel('Iterations', fontsize=fontsize)
axes[0].set_ylabel('Return', fontsize=fontsize)
axes[0].set_title(env, fontsize=30)


fig.legend(le, line_labels, fontsize=22, loc="upper center", ncol=5)
fig.savefig('ir.png', bbox_inches='tight')
plt.show()
