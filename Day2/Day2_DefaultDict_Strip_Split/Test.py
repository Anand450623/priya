from collections import defaultdict


if __name__ == "__main__":
    dic = {'anand': ['priya']}
    dic['anand'].append('priya2')
    print(dic)

    dic2 = {'anand': []}
    dic2['anand'].append('priya')
    dic2['anand'].append('priya2')
    print(dic2)

    dic3 = {}
    # print(dic3['anand'])

    dic4 = defaultdict(list)
    print(dic4['anand'])
