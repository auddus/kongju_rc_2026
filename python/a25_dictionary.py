def main():
    dict_a = {"a": "aa"}
    dict_a = dict()
    print(type(dict_a))

    dict_a["b"] = "bbb"
    print(dict_a)
    print(dict_a["a"], dict_a["b"], dict_a.get("c"))

    print(dict_a.pop("a"))
    print(dict_a)


    dict_a["a"] = "aa"
    dict_a["b"] = "bbb"
    dict_a["c"] = "cccc"
    dict_a['d'] = "ddddd"
    
    for key in dict_a:
        print(key, dict_a[key])

    for key, value in dict_a.items():
        print(key, value)

    print(dict_a.keys())
    print(dict_a.values())

