
from itertools import permutations 
import os
import time
from tqdm import tqdm
import math
import sys




# set timer
start = time.time()

# two lists using set() method
def interestfactor(lst1, lst2):
    intersection = len(list(set(lst1) & set(lst2)))
    return min((len(lst1) - intersection), intersection, (len(lst2) - intersection))


def preparing_data(inputfile):
    
    # open test for reading
    fp = open(inputfile, "r")

    # Read existing file with plaintext passwords
    lines = [line.rstrip() for line in fp.readlines()]

    fp.close()

    # put photos in list
    photos = []

    # tags in each photos
    tags = []

    # put photos and tags in dictionary(ex.{1:["garden", "cat"], 2:["beach", "cat"]...})
    dic = {}

    ID = 0
    tagCnt = 0

    # loop through each entry in lines to put it in dictionary
    for data in lines:
        if ID != 0:
            tags = []
            tagCnt = data.split(" ")[1]
            #print(tagCnt)
            for i in range(2, int(tagCnt) + 2):
                tags.append(data.split(" ")[i])
        
            photos.append(ID)
            #print("photos: ", photos)
            dic[ID] = tags
            #print("dic: ", dic)

        ID += 1


    print("photos: ", photos) #[1 ,2,3,4,5,6....]
    print("dic: ", dic)

    return photos, dic



def without_pruning(photos, dic):

    # best combination
    slides = ()


    secondslides = ()
    thirdslides = ()


    maxIF = 0


    secondIF = 0
    thirdIF = 0


    IF = 0
    IFCnt = 0

    IFlst = []
    slideslst = []

    # list out keys and values separately
    dickey_list = list(dic.keys())
    dicval_list = list(dic.values())

    combination = permutations(photos)



    #print(combination)
    #length = sum(1 for ignore in combination)
    #print(length)
    #print(list(permutations(photos))[0])

    # permutation
    for slide in combination:
        IF = 0
        print(slide)
        # find out the interest factor in certain photo combination
        for element in range(len(slide) - 1):
            # use value in dictionary to find out the interest factor in two consecutive photos
            IFCnt = interestfactor(dicval_list[slide[element] - 1], dicval_list[slide[element + 1] - 1])
            IF = IF + IFCnt
            # find out the max interest factor and slides(photo combination)
            if IF > maxIF:
                maxIF = IF
                slides = slide

            '''if IF == 7 and secondIF != 7:
                secondIF = IF
                secondslides = slide

            if IF == 6 and thirdIF != 6:
                thirdIF = IF
                thirdslides = slide'''
                



    # open file for writing in utf-8 encoding type
    fp = open("Slideshow.txt", "w", encoding="utf-8")

    fp.write((str(len(slide))))
    fp.write("\n")

    for i in range(len(slide)):
        fp.write(str(slides[i]))
        fp.write("\n")

    fp.close()


    print("maxInterestFactor: ", maxIF)
    print("slides: ", slides)
    '''print("secondInterestFactor: ", secondIF)
    print("secondslides: ", secondslides)
    print("thirdInterestFactor: ", thirdIF)
    print("thirdslides: ", thirdslides)'''

    return maxIF, slides

    




def main():

    photos, dic = preparing_data(sys.argv[1])
    # set timer
    start = time.time()
    maxIF, slides = without_pruning(photos, dic)
    print("maxInterestFactor: ", maxIF)
    print("slides: ", slides)
    end = time.time()
    # count process time
    print("Process time = %d seconds" % (end - start))




    
 
if __name__=="__main__":
    main()