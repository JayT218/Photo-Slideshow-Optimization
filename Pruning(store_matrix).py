




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


# two integers into one
def concat(a, b):
     
    # Convert both the integers to string
    s1 = str(a)
    s2 = str(b)
     
    # Concatenate both strings   
    s = s1 + s2
     
    # Convert the concatenated string
    # to integer
    c = int(s)
     
    # return the formed integer
    return c 



# open test for reading
fp = open(sys.argv[1], "r")

# Read existing file with plaintext passwords
lines = [line.rstrip() for line in fp.readlines()]

fp.close()

# put photos in list
photos = []

# tags in each photos
tags = []

# put photos and tags in dictionary(ex.{1:["garden", "cat"], 2:["beach", "cat"]...})
dic = {}

# best combination
slides = ()

ID = 0
maxIF = 0
IF = 0
IFCnt = 0
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


print("photos: ", photos)
print("dic: ", dic)


# interest factor map

rows, cols = (len(photos) + 1, len(photos) + 1)
IFmap=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(None)
    IFmap.append(col)
print(IFmap)




# list out keys and values separately
dickey_list = list(dic.keys())
dicval_list = list(dic.values())

combination = permutations(photos)



# permutation
for slide in combination:
    IF = 0
    print(slide)

    # find out the interest factor in certain photo combination
    for element in range(len(slide) - 1):

        # interest factor between these two adjacent photos has not been calculated
        if IFmap[slide[element]][slide[element + 1]] == None:
            IFCnt = interestfactor(dicval_list[slide[element] - 1], dicval_list[slide[element + 1] - 1])

            # put this value in IFmap
            IFmap[slide[element]][slide[element + 1]] = IFCnt
            IFmap[slide[element + 1]][slide[element]] = IFCnt
        

        else:
            # interest factor between these two photos has been calculated before, just find this value in map
            IFCnt = IFmap[slide[element]][slide[element + 1]]


        IF = IF + IFCnt

        # find out the max interest factor and slides(photo combination)
        if IF > maxIF:
            maxIF = IF
            slides = slide

print(IFmap)

# open file for writing in utf-8 encoding type
fp = open("Slideshow.txt", "w", encoding="utf-8")

fp.write((str(len(photos))))
fp.write("\n")

for i in range(len(photos)):
    fp.write(str(slides[i]))
    fp.write("\n")

fp.close()

print("maxInterestFactor: ", maxIF)
print("slides: ", slides)

# set end 
end = time.time()

# count process time
print("Process time = %d seconds" % (end - start))


 





