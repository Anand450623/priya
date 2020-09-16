from collections import defaultdict
ml_model = {}
total_words = {}


def train_using_default_dict(path):

    data = list()
    with open(path, "r") as f:
        for line in f:
            data.append(line)

    dic1 = defaultdict(list)
    for chat in data:
        dic1[chat.split(":")[0]].append(chat.split(":")[1])

    # write logic to get frequency of each word said by a person and count of total word said by a person
    # store the result in ml_model and total_words respectively

    '''
        
        Expected Result:
        
        ml_model = 
        {
            'A': {'hi,': 1, 'hello': 1, 'no,': 1, "i'm": 1, 'busy.': 1}, 
            'B': {'can': 1, 'we': 1, 'meet?': 1, 'no': 1, 'problem.': 1}
        }
        
        total_words = 
        {
            'A': 5, 
            'B': 5
        }
        
    '''

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

    # write logic to get frequency of each word said by a person and count of total word said by a person
    # store the result in ml_model and total_words respectively

    '''

        Expected Result:

        ml_model = 
        {
            'A': {'hi,': 1, 'hello': 1, 'no,': 1, "i'm": 1, 'busy.': 1}, 
            'B': {'can': 1, 'we': 1, 'meet?': 1, 'no': 1, 'problem.': 1}
        }

        total_words = 
        {
            'A': 5, 
            'B': 5
        }

    '''

    return dic1
