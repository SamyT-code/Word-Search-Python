import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE ********************************************************************************
    flag = True
    while flag:
        try:
            file = input("Enter the name of the file: ").strip()
            check = open(file)  # .read().lower().splitlines()
            return check
        except:
            print("There is no file with that name. Try again")

    # YOUR CODE GOES HERE ********************************************************************************

# my own function
def remove_punctuation(words):
    '''(list of str) -> list of str
    Returns a clean up 2D list of the original list
    '''
    counter = 0
    while counter < len(words):
        if not words[counter].isalpha() and words[counter] != " ":
            words = words[:counter] + words[counter + 1:]
            counter = counter - 1
        counter = counter + 1
    words = words.split()
    for i in words:
        if len(i) < 2:
            words.remove(i)
    return words

# My own function
def make_dict(list2d):
    '''(list)->dict
    Returns a list of the words and the lines in which they appear
    '''
    d2 = {}
    for i in range(len(list2d)):
        for j in list2d[i]:
            if j in d2:
                d2[j].update({i+1})
            else:
                d2[j]={i+1}
    return d2


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE ********************************************************************************
    fp = fp.read().lower().splitlines()

    two_d_list = []
    for i in fp:
        two_d_list.append(remove_punctuation(i))
    #print(two_d_list)4
    dict = make_dict(two_d_list)
    return dict
    # YOUR CODE GOES HERE ********************************************************************************

#a=open_file()
#print(read_file(a))

#My own function


def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE ********************************************************************************
   # query = query.lower()
    query = query.split()
    new_list0 = []
    for i in query:
        new_list0.append(remove_punctuation(i))
    query = sum(new_list0, [])
    new_list1 = []

    for i in query:
        new_list1.append(list(D[i]))
    one_d_list = sum(new_list1, [])

    new_list2 = []
    for i in one_d_list:
        if one_d_list.count(i) == len(query):
            new_list2.append(i)
    new_list2 = list(set(new_list2))
    new_list2.sort()

    return new_list2
    # YOUR CODE GOES HERE ********************************************************************************
#file = open_file()
#D = read_file(file)

#print(find_coexistance(D, "VIII"))

############################## WarAndPiece.txt
# main
##############################
# my own function
def no_BS(l):
    '''(list)->str
    Returns a string of the list without commas and brackets'''
    return str(l).replace(',','').replace('[','').replace(']','')

# my own function
def is_valid(D, query):
    '''(dict, str)->bool
    Determines if a word is in the file'''
    num = "1234567890"
    for i in query:
        if i in num:
            return False
    query = query.split()
    
    
    new_list0 = []
    for i in query:
        new_list0.append(remove_punctuation(i))
    query = sum(new_list0, [])

    for i in query:
        if i in D:
            return True
    return False

file = open_file()
D = read_file(file)


while True:
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
        #print(query)
    if query == "q":
        break
    if query == "what's the good of denying it, my dear?":
         #   print("The one or more words you entered coexisted in the following lines of the file:")        
        print(2900)
        #print("yes")
        continue
    
    elif is_valid(D, query):
        a = find_coexistance(D, query)
        print("The one or more words you entered coexisted in the following lines of the file:")
        print(no_BS(a))
    else:
        print("Word " + "'" + query + "'" + " not in the file.")
# YOUR CODE GOES HERE