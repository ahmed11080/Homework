nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("Before: ", nums)
def removeddup():
    newlist=[]
    for items in nums:
        if items not in newlist:
            newlist.append(items)
    print("After: ", newlist)

removeddup()
