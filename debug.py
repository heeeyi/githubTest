def p1(x, y):
    return p2(x, y) + p3(x, y)

def p2(z, w):
    return z * w

def p3(a, b):
    return p2(a) + p2(b)
'''
for i, elem in enumerate((4, 10, 1, 3)):
    print("I am in the", i ,"position and I am", elem)
'''
def search(x, seq):
    index = 0
    while index < len(seq) and  x > seq[index]:
        index += 1
    return index

def binary_search(x, seq):
    def helper(low, high):
        if low > high:
            return low
        mid = (low + high)//2
        if x <= seq[mid]:
            return helper(low, mid-1)
        else:
            return helper(mid+1, high)
    return helper(0, len(seq)-1)

def insert_list(x, lst):
    position = binary_search(x, lst)
    lst.append(None)
    for i in range(position, len(lst)-1)[::-1]:
        lst[i+1] = lst[i]
    lst[position] = x
    return lst

def insert_tup(x, tup):
    position = binary_search(x, tup)
    new = ()
    for i in range(position):
        new += (tup[i],)
    new += (x,)
    for i in range(position, len(tup)):
        new += (tup[i],)
    return new

def sort_list(lst):
    new = []
    for item in lst:
        if new == []:
            new.append(item)
        else:
            insert_list(item, new)
    return new

def sort_tup(tup):
    new = ()
    for item in tup:
        if new == ():
            new = (item,)
        else:
            new = insert_tup(item, new)
    return new

import shelf

def insert_animate(block_pos, shelf, high):
    position = 0
    target_size = shelf[block_pos].size
    while position < high and target_size > shelf[position].size:
        position +=1
    b = shelf.pop(block_pos)
    shelf.insert(position, b)  
    # optional to return shelf but we do this for debugging
    return shelf

def sort_me_animate(shelf):
    length = len(shelf)

    for i in range(length):
        insert_animate(i, shelf, i)
    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for sort_me_animate

def test_sort_me_animate():
    shelf.clear_window()
    s = shelf.init_shelf((5,2,6,9,1,4,8,3))
    print("## Q4b ##")
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 3, Block size: 4, Block size: 5, Block size: 6, Block size: 8, Block size: 9]
    shelf.clear_window()
    s = shelf.init_shelf((4, 8, 2, 9, 3, 1, 2, 3, 4, 10, 7, 5, 6))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 2, Block size: 3, Block size: 3, Block size: 4, Block size: 4, Block size: 5, Block size: 6, Block size: 7, Block size: 8, Block size: 9, Block size: 10]

# Test case to catch mutation while sorting

def test_sort_me_with_duplicates():
    shelf.clear_window()
    s = shelf.init_shelf((1,3,4,1,3,2))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 1, Block size: 2, Block size: 3, Block size: 3, Block size: 4]

# Uncomment function call to test sort_me_animate()
#test_sort_me_animate()
test_sort_me_with_duplicates()







