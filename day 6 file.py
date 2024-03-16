# ! ------> day 6

# s1 = input("enter string:")
  fst = s1[0].upper()
  lst = s1[-1].upper()
  print(fst+s1[1:len(s1)-1]+lst)



 n = 128
 temp = n
 f1 = 0
 while n!=0:
     rem = n%10
     check temp % rem
     if check!=0
         f1 = 1
       n = n//10


 if f1==0:
     print("yes")
 else:
     print("no")



# ! --------> set


# ? charctristics of set
 1.) set can be created using {}
 2.) the elements inside set are not indexed
 3.) does not allow duplicate values
 4.) it unordered
 5.) heterogenous
 6.) mutable or changable

 # Eg:1
  s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck",'e'}
  # print(s1)

# * Eg:2
  s2 = {5, 8, 98, [9, 0]}
  print(s2)----> error

# * Eg:3
# min(),max(),len()


# * Eg:4
# ? to add element inside set


 s1 = {8, 78, 67, 'u'}
# add()
  s1.add(43)
  print(s1)

# update()
  s1.update([9,0])
  print(s1)

# ? To delete element inside set
  s1 = {8, 78, 67,'u'}

  pop() # to delete one element randomly
  s1.pop()
  print(s1)


# remove()
  s1.remove(978)
  print(s1)


# discard()
  s1.discard(8967)
  print(s1)

# clear()
 l1 = {}
 print(type(l1)) ----> datatype is dict

# s1 = set() #  to create empty set
  print(type(s1))

# s1 = {8, 9, 0}
 s1.clear()
 print(s1)

# del s1
# print(s1)

# * join the  sets
 s1 = {9, 0, 8}
 s2 = {9.90, "card", 't',56}
# # union()--> to combine 2  sets
# s3 = s1.union(s2)
 print(s3)


# * intersection() ---> to get common elements inside set
# s1 = {4, 5, 6}
# s2 = {5, 6, 7, 8}
# print(s1.intersection(s2))


# * difference()
 s1 = {4, 5, 6}
 s2 = {5, 6, 7, 8}
 print(s1.difference(s2))
  print(s2.difference(s1))
print(s1.symmetric_difference(s2))



# isdidjoit(), issubset(), issuperset()
# s1 = {8, 9, o}
# s2 = {6, 7, 5, 8, 9, 0}

# print(s1.issubset(s2))
# print(s2.issubset(s1))

# !-----> problem:1
 s1 = {1, 2, 3, 4, 5}
 s2 = {3, 2, 7, 8, 9}


 for val in s1:
     if val in s2:
         str1 = "its joint set"
  print(str1)

# ! --------> dictionary
  eg:1
  d1 = {1:100,'a':200,4.5:"hello"}
  print(d1)
  print(len(d1))

# ? char of dictionary
 1.) have to be surronded by{}
 2.) It have to be in the form of key, value pair
 3.) It is mutable
 4.) duplicate keys are not allowed,duplicate values are allowed
 5.) It is unindexed
 6.) It is ordered
 7.) key does not allow mutable datatypes,values allow mutable datatype

  d1 = {1:100,2:200,3:300, 4:400}
# * to access elements in dictionary

# print(d1)
# or
# To access the values, have to use key
# print(d1[1]) # o/p ---->100




# ? some common functins
# len(),min(),max()
# print(min(d1))
# print(max(d1))



# clear(), del

# join 2 dictionary
 d1 = {1:100,2:200,3:300,4:400}




 # * Iterating dictiuonary
  for val in d1:# to iterate keys alone
      print(val)

# for val in d1.values(): # to iterate values alone
  print(val)


# # to get both key and values
# for key,val in d1.items():
#    print(key,val)


  
# !-----------> problem:1
 n = int(input("Enter num of times :"))
 integer = []
 float_value = []
 string=[]

 for val in range(n):
     value= eval(input("enter the value:")
     if type(value)==int:
      integer.append(value)
    elif type(value) == float:
              float_value,append(value)
    elif type(value)== str:
        string.append(value)
        else: print("pls provide data in int,flaot,string")
 print(integer)
 print(float_value)
 print(string)



 Return a set of elements present in set A or B,but not both
 set1 = [10, 20, 30, 40, 50]
 set2 = [30, 40, 50, 60, 70]
 o/p
 [20, 70, 10, 60]



 
 
# ! ---------> problem:3
 l1 = [1, 2, 3, 4] # key
 l2 = ["a", "b", "c", "d"] # value
# ? o/p -----> {1:'a',2:'b',3;'c',4:'d'}



# # ! or
# c = 0
  for val in set1, set2:
     c= c+1
     if c==1:
         for element in val:
              if element not in set2















  















     
