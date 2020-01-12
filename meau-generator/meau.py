import json
import random

def cook(meau):
    with open(meau, 'r') as f:
        data = json.load(f)
    list = data['cook_list']
    return list

def takeOut(meau):
    with open(meau, 'r') as f:
        data = json.load(f)

    list = []
    for key in data.keys():
        list = list + data[key]
    # print(list)
    return list

def main():

    method = input("Do you want to cook at home or order some food? (input C or c for cook and O or o for making order)\n")
    while method not in ['C', 'c', 'O', 'o']:
        method = input("please input C or c for cook and O or o for making order\n")

    list = []
    if method in ['C', 'c']:
        meau = 'cook_list.json'
        list = cook(meau)
    else:
        meau = input('please input meau file address\n')
        list = takeOut(meau)
    
    num = input("How many random food do you want?\n")
    print(random.sample(list, int(num)))

if __name__ == "__main__":
    main()