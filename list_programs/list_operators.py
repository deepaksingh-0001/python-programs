# List Operators Program

l1 = [3, 4, 8, 0, 8, 8]
l2 = [2, 3, 4, 8]

# Concatenation
print("Concatenation :", l1 + l2)

# Repetition
print("Repetition    :", l1 * 2)

# Membership
print("Membership    :", 3 in l1)
print("Not Membership:", 5 not in l1)

# Indexing
print("Index [0] :", l1[0])
print("Index [4] :", l1[4])

#slicing
print("Slice [0:4] :", l1[0:4])
print("Slice [:3]  :", l1[:3])
print("Slice [3:]  :", l1[3:])
print("Reverse     :", l1[::-1])

# Comparison
# Comparison Operators

print("Equal :", l1 == l2)
print("Not Equal :", l1 != l2)
print("Greater :", l1 > l2)