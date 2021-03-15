fruits = {
    '苹果': 12.3,  # 水果和单价
    '草莓': 4.5,
    '香蕉': 6.3,
    '葡萄': 5.8,
    '橘子': 6.4,
    '樱桃': 15.8
}


def sum(x, y):
    return x * y


info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': 1
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 1
    }
}

s = 0
keys = fruits.keys()
for key in fruits:
    value = fruits[key]
    keys1 = info['小明']['fruits'].keys()
    for key1 in keys1:
        value1 = info['小明']['fruits'][key]
        if key1 == key:
            s += sum(value1, value)
        print(s)

info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': s l.k
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 1
    }
}

print(info)
