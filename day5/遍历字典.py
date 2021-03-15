dict1 = {"k1": "v1", "k2": "v2", "k3": "v3"}

keys = dict1.keys()
for key in keys:
    zhi = dict1[key]
    print(key, "=", zhi)

dict1["k4"] = "v4"
print(dict1)