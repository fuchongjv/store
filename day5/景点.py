version = {
    "北京": {
        "昌平": {
            "天通苑": ["海底捞", "呷哺"],
            "龙泽": ["永辉超市"]
        },
        "海淀": {
            "公主坟": ["军事博物馆", "中华世纪园"],
            "科普场馆": ["中国科技馆", "北京天文馆"],
            "高校": ["北京大学", "清华大学", "民族大学"]
        },
        "朝阳": {
            "龙城": ["鸟化石国家地质公园", "朝阳南北塔"],
            "双塔": ["朝阳凌河公园", "朝阳凤凰山"]
        }
    },
    "上海": {
        "黄浦": {
            "商业街": ["南京路", "淮海路"],
            "人文": ["上海大剧院", "上海城隍庙"],
        },
        "静安": {
            "景点": ["静安寺", "毛泽东故居"],
            "商场": ["上海商场", "芮欧百货"]
        }

    }
}


###### 打印城市函数
def printPlace(choice):
    for i in choice:
        print("\t\t", i)


# 打印选项
for con in version:
    print(con)
# 获取用户想去的城市
choise = input("请输入您想要去的城市>>>:")

# 判断是否存在该城市
while True:
    if choise in version:
        if choise == 'q':
            break

        # 打印当前选项的子城市
        printPlace(version[choise])
        # 输入二级城市
        choise2 = input("请继续输入想去的地方：")
        if choise2 == 'q':
            break
        if choise2 in version[choise]:
            # 输入三级城市
            printPlace(version[choise][choise2])  # 北京,昌平
            choise3 = input("请继续输入三级城市>>>:")
            if choise3 == 'q':
                break
            if choise3 in version[choise][choise2]:
                printPlace(version[choise][choise2][choise3])
            i = input("您是否想要退出？是  |  否>>>:")
            if i == "是":
                break
