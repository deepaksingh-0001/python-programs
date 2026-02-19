# List Methods Program

l1 = [9, 7, 5, 1, 6, 8]
l2 = [2, 3, 4, 0]

l1.append(10)            # adds an element at the end of the list
print("Append :", l1)

l1.insert(2, 100)        # inserts an element at the given index
print("Insert :", l1)

l1.extend(l2)            # adds elements of another list to the current list
print("Extend :", l1)

l1.remove(10)            # removes the specified value from the list
print("Remove :", l1)

l1.pop(2)                # removes the element at the given index
print("Pop :", l1)

print("Count(8) :", l1.count(8))   # counts how many times the element appears
print("Index(4) :", l1.index(4))   # returns the index of the element

l1.sort()                # sorts the list in ascending order
print("Sort :", l1)

l1.reverse()             # reverses the list
print("Reverse :", l1)

l1.clear()               # removes all elements from the list
print("Clear :", l1)