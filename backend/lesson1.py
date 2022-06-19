dict_ex = {
    "key1":{
        "fff1":"sss",
        "fff2":"sss",
        "fff3":["fff", "ssss"],
    },
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}

print(dict_ex["key1"]["fff3"][1])

dict_homework = {
    "key1":{
        "d":44,
        "f":None,
        "s":{
            8:44,
            9:None,
            10:{"mm":["s", "GET ME", 7]},
        },
    },
    "key2":{
        "fff1":44,
        "f":None,
    },
}

print(dict_homework["key1"]["s"][10]["mm"][1])