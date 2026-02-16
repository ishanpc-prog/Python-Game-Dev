set1 = {1,2,3,4,5}
#sets are unorderd
#everything in a set is unique
#you can add and remove elements
set2 = {22,1,34,2,5}
my_set = set([])
my_set.add(3)
my_set.add(2)
my_set.add(1)
my_set.add(0)
print(my_set)
my_set.remove(0)
print(my_set)
#my_set.remove(67)
my_set.discard(67)
#if you try to remove something that does not exist it will give error but with discard it wont
# union operation
#set1 u set2 = {1,2,3,4,5,22,34}
#intersection = common elements between two sets
set3 = {1,2,5} #it is the intersection of s1 and s2
#difference of set1 and set2 is the elements that exist in set1 but not in set2
#set1-set2 = {3,4}
#symetric difference is union of sets minus intersection of sets
set4 = {3,4,22,34}
print(set1.union(set2)) #union
print(set1.intersection(set2)) #intersection
print(set1.difference(set2)) #difference
print(set1.symmetric_difference(set2)) #symetric difference