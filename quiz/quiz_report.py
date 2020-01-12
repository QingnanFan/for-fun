import sys
import random
import re

class classfang:
    def __init__(self, bufferPoolSize, policyName):
        print("in class fang")





def CanBeUsedInMain():
    print("This function can be used in main")

def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

def is_TF(str):
    for s in ['t', 'T', 'F', 'f']:
        if s == str:
            return True
    return False

###################################################################################################
#  Main
#


def main():
    file_address = ""
    word_list = []

    if(len(sys.argv) == 1):
        # 在这里也可以引导用户输入文件地址
        print('please add the address of vocabulary list at the end of command')
        sys.exit()
    elif(len(sys.argv) > 2):
        print('The input parameters are wrong!!!')
        sys.exit()
    elif(len(sys.argv) == 2):
        file_address = sys.argv[1]
    else:
        print("unexpected error")
    


    try:
        input_file = open(file_address, "r")
    except IOError as e:
        print("Couldn't open or write to file (%s)", e)
        sys.exit()

    for line in input_file:
        # print(line.split())
        count = 0
        chinese_explaination = ""
        for word in line.split():
            if is_contains_chinese(word):
                count = count + 1
                chinese_explaination = chinese_explaination + " " + word
        # print('number of chinese explaination:' + str(count))

        for word in line.split():
            if not is_contains_chinese(word):
                word_list.append([word, chinese_explaination])

    # print(word_list)

    input_size = input('please input the test size')
    test_size = 0
    while True:
        
        if(not input_size.isdigit()):
            input_size = input('the input should be an integer')
        elif(int(input_size) < 0):
            input_size = input('test size should larger than 0')
        else:
            break
        
    test_size = int(input_size)
        
    wrong_list = []

    while test_size > 0:
        curr_word = random.choice(word_list)
        print(curr_word[0])
        # print("")
        input('press enter when you are ready')
        print(curr_word[1])
        is_correct = input('Input T or F indicate whether you are currect or wrong')
        while(not is_TF(is_correct)):
            is_correct = input('Input should be t, T, f or F. Please input again.')
        if is_correct == 'f' or is_correct == 'F':
            wrong_list.append(curr_word)
        test_size = test_size - 1

    print("-----------wrong word list-----------")
    for wrong in wrong_list:
        print(wrong)


if __name__ == "__main__":
    main()