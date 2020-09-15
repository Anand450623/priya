from collections import defaultdict


if __name__ == "__main__":

    # ordinary dictionary generally/usually contains only one item for key
    dic = {'anand': 'priya'}
    print(dic)

    dic['anand'] = 'priya2'
    print(dic)

    # defaultdict dictionary is data structure used if we want to store some complex structure as value for a key
    d_dic = defaultdict(list)
    d_dic['anand'].append('priya')
    print(d_dic)

    d_dic['anand'].append('priya2')
    d_dic['anand'].append('priya3')
    print(d_dic)

    # Here, in the above example list can be replaced by set, dict or anything which suits to need of developer...
