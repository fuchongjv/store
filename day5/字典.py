prov = {"010": "北京", "020": "上海", "030": "深圳"}

keys = prov.keys()
for key in keys:
    value = prov[key]
    print(key, "=", value)
