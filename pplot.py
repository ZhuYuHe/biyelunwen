import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
# font = FontProperties(fname="/System/Library/Assets/com_apple_MobileAsset_Font5/fe548b971e5f16935cdcecfc29727ea44e91cf5c.asset/AssetData/FTFANGSO.tff")

import re
# plt.rcParams['font.sans-serif']=['STangsong']
pattern = re.compile('\d')

user = []
idle = []

with open("data.txt", encoding='utf-8') as f:
    for line in f:
        arr = line.split()
        if not pattern.match(arr[1]):
            user.append(arr[2])
            idle.append(arr[-1])

x = list(range(len(user)))

plt.title("实验期间服务器CPU使用情况")
plt.xlabel('时间/s')
plt.ylabel("百分比")

plt.plot(x, user, label="user")
plt.plot(x, idle, label="idle")
plt.legend()

plt.show()