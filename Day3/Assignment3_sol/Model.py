from collections import defaultdict


def train_using_default_dict(path):

    data = list()
    with open(path, "r") as f:
        for line in f:
            data.append(line)

    dic1 = defaultdict(list)
    for chat in data:
        dic1[chat.split(":")[0]].append(chat.split(":")[1])

    return dic1


def train_without_using_default_dict(path):

    data = list()
    with open(path, "r") as f:
        for line in f:
            data.append(line)

    dic1 = {}
    for chat in data:
        chat_split = chat.split(":")
        if chat_split[0] in dic1:
            dic1[chat_split[0]].append(chat_split[1])
        else:
            dic1[chat_split[0]] = [chat_split[1]]

    return dic1
