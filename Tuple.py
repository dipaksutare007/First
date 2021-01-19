t = ()
print(t,type(t))

t1= tuple()
print(t,type(t1))

t2 = (10)        #  this is output is integer
print(type(t2))


t2 = (10,)        #  this is output is tuple
print(type(t2))

t3 = (10,20,30,)  # it is support homo Ginus
print(t3)

t4=(10,2.3,'hi')  # it is Support hetroginius
print(t4)


t5=(10,20,30,40,50,10,10)
print(t5)
print(t5[2::])

print(t5[2::2])

# t5[0]=100  Tuple is immutable we can not delete insert update value of Tuple

#List is mutable ..Mean we can Insert,update,delete

#Mothod



for i in dir(t):
    if '_' not in i:
        print(i)

print(t5.count(10))

print(t5.index(10,2))




