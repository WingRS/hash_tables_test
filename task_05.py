import math
import random

class Node() :
    def __init__(self, key):
        self.key = key
        self.value = key
        self.nextNode = None


    def getValue(self):
        return self.value


    def setValue(self,value):
        self.value = value


    def getKey(self):
        return self.key

    def getNext(self):
        return self.nextNode

    def setNext(self, nextNode):
        self.nextNode = nextNode


class Hashing() :

    def __init__(self, size, type = 1, ):
        self.type = type
        self.size = size

    def hash_multy(self,key):
        prev_res = 0.618033*key
        our = prev_res - int(prev_res)
        return int(math.floor(self.size * our))

    def hash_divide(self,key):
        return key % self.size



class HashMap():

    def __init__(self,size, type):
        self.size = size
        self.table = [None]*size
        self.hashType = type
        self.count = 0


    def map_hash(self,key):
        if (self.hashType == 2):
            hash_num = Hashing(self.size).hash_multy(key)
        elif (self.hashType == 1):
            hash_num = Hashing(self.size).hash_divide(key)
        return hash_num


    def search(self, key):
        hash_key = self.map_hash(key)
        if(self.table[hash_key] == None) :
            return False
        else:
            x = self.table[hash_key]
            while (x != None) and (x.getKey() != key) :
                x = x.getNext()
            if(x == None):
                return False
            else:
                return True


    def add(self, value):
        hash_key = self.map_hash(value)
        if(self.table[hash_key] == None ):
            self.table[hash_key] = Node(value)
        else :
            self.count += 1
            x = self.table[hash_key]
            while  ( x.getNext()  != None ) and ( x.getKey() != value ) :
                x = x.getNext()
            if(x.getKey()  != value):
               x.setNext(Node(value))

class Research():
    def __init__(self, size, table, type = 1):
        self.type = type
        self.size = size
        self.table = table

    def linearCollision(self, key):
        i = 0
        while (i < self.size):
            index = (key + i) % self.size
            if (self.table[index] == None):
                return index
            else:
                i += 1

    def quadraticCollision(self, key):
        i = 0
        while (i<self.size):
            index = (key + i*i)%self.size
            if(self.table[index] == None):
                return index
            else:
                i += 1
    def doubleCollision(self,key, value):
        i = 0
        while(i<self.size):
            index = ( key + i* Hashing(self.size).hash_divide(value))%self.size
            if(self.table[index] == None):
                return index
            else:
                i += 1



class OpenMap() :

    def __init__(self, size, type):
        self.table = [None]*size
        self.size = size
        self.type = type
        self.count = 0

    def choose_coll(self,index,value):
        print("SIZEEEEE"+str(self.size))
        print("COLLISION "+str(index)+" value "+ str(value))
        if(self.type == 3):
            return Research(self.size,self.table).linearCollision(index)
        elif(self.type == 4):
            return Research(self.size,self.table).quadraticCollision(index)
        elif(self.type == 5):
            return Research(self.size,self.table).doubleCollision(index,value)

    def add(self, value):
        index = Hashing(self.size).hash_divide(value)
        if( self.table[index] == None):
            self.table[index] = value
        else:
            self.count += 1
            col_index = self.choose_coll(value,value)
            self.table[col_index] = value

    def search(self,value):
        i = 0
        hash_value = Hashing(self.size).hash_divide(i)
        el = self.table[hash_value]
        while i< self.size:
            if el == value :
                return True
            else:
                i+=1
                el = self.table[Hashing(self.size).hash_divide(i)]
        return False



class HashTable():
    def __init__(self,hash_type,values):
        self.hash_type = hash_type
        self.values = values
        self.hash_table = self.select_table(self.hash_type, self.select_prine(len(values)) )

    def select_table(self,hash_type, size):
        if(hash_type == 1 ) or (hash_type == 2):
            x = HashMap(size,hash_type)
        elif(hash_type == 3) or (hash_type == 4) or (hash_type == 5):
            x = OpenMap(size, hash_type)
        self.fillTable(x)
        return  x

    def fillTable(self,x):
        for i in self.values:
            x.add(i)

    def get_collisions_amount(self):
        return self.hash_table.count

    def find_sum(self,s):
        for i in self.values:
            if(self.hash_table.search(s-i)):
                return (i,s-i)
        return None
    def select_prine(self, size):
        lower = size
        upper = size+3
        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    return num

values = []
for i in range(0,100000):
    values.append(random.randint(20,500))
x = HashTable(5,values)
print(values)
for r in values:
    first = values[random.randint(0,999)]
    second = values[ random.randint(0,999)]
    sumarry = first+second
    print(x.find_sum(sumarry))






# Hash type #3: Open Address Hash with Linear Func
# Load time: 0.034 ms
# Number of collisions: 0
# Sum 36 not found - OK
# Fail! You didn't find sum 134
# Sum 108 not found - OK
# Fail! You didn't find sum 117
# Fail! You didn't find sum 105
# Fail! You didn't find sum 86
# Fail! You didn't find sum 98
# Fail! You didn't find sum 88
# Fail! You didn't find sum 60
# Fail! You didn't find sum 40
# Average time for sum search is 0.093 ms
# Hash type #4: Open Address Hash with Quadratic Func
# Load time: 0.027 ms
# Number of collisions: 0
# Sum 36 not found - OK
# Fail! You didn't find sum 134
# Sum 108 not found - OK
# Fail! You didn't find sum 117
# Fail! You didn't find sum 105
# Fail! You didn't find sum 86
# Fail! You didn't find sum 98
# Fail! You didn't find sum 88
# Fail! You didn't find sum 60
# Fail! You didn't find sum 40
# Average time for sum search is 0.080 ms
# Hash type #5: Open Address Hash with Double Func
# Load time: 0.049 ms
# Number of collisions: 0
# Sum 36 not found - OK
# Fail! You didn't find sum 134
# Sum 108 not found - OK
# Fail! You didn't find sum 117
# Fail! You didn't find sum 105
# Fail! You didn't find sum 86
# Fail! You didn't find sum 98
# Fail! You didn't find sum 88
# Fail! You didn't find sum 60
# Fail! You didn't find sum 40
# Average time for sum search is 0.098 ms
# Input size 10 processing time 5.185 ms
# Data size: 1000. Number of sums: 10

# Hash type #3: Open Address Hash with Linear Func
# Load time: 3.693 ms
# Number of collisions: 149
# Sum 879751 not found - OK
# Sum 1822307 not found - OK
# Sum 1240913 not found - OK
# Fail! You didn't find sum 1243385
# Fail! You didn't find sum 1311544
# Fail! You didn't find sum 839105
# Fail! You didn't find sum 891483
# Fail! You didn't find sum 1386859
# Fail! You didn't find sum 1311003
# Fail! You didn't find sum 724100
# Average time for sum search is 4.888 ms
# Hash type #4: Open Address Hash with Quadratic Func
# Load time: 2.310 ms
# Number of collisions: 149
# Sum 879751 not found - OK
# Sum 1822307 not found - OK
# Sum 1240913 not found - OK
# Fail! You didn't find sum 1243385
# Fail! You didn't find sum 1311544
# Fail! You didn't find sum 839105
# Fail! You didn't find sum 891483
# Fail! You didn't find sum 1386859
# Fail! You didn't find sum 1311003
# Fail! You didn't find sum 724100
# Average time for sum search is 4.564 ms
# Hash type #5: Open Address Hash with Double Func
# Load time: 2.540 ms
# Number of collisions: 166
# Sum 879751 not found - OK
# Sum 1822307 not found - OK
# Sum 1240913 not found - OK
# Fail! You didn't find sum 1243385
# Fail! You didn't find sum 1311544
# Fail! You didn't find sum 839105
# Fail! You didn't find sum 891483
# Fail! You didn't find sum 1386859
# Fail! You didn't find sum 1311003
# Fail! You didn't find sum 724100
# Average time for sum search is 4.594 ms
# Input size 1000 processing time 199.416 ms
# Data size: 100000. Number of sums: 10

# Hash type #3: Open Address Hash with Linear Func
# Load time: 224.547 ms
# Number of collisions: 17106
# Fail! You didn't find sum 758052
# Fail! You didn't find sum 1092119
# Fail! You didn't find sum 1040353
# Fail! You didn't find sum 888014
# Fail! You didn't find sum 991665
# Fail! You didn't find sum 657724
# Fail! You didn't find sum 1239007
# Fail! You didn't find sum 408463
# Fail! You didn't find sum 1099474
# Fail! You didn't find sum 255695
# Average time for sum search is 163.610 ms
# Hash type #4: Open Address Hash with Quadratic Func
# Load time: 248.007 ms
# Number of collisions: 17102
# Fail! You didn't find sum 758052
# Fail! You didn't find sum 1092119
# Fail! You didn't find sum 1040353
# Fail! You didn't find sum 888014
# Fail! You didn't find sum 991665
# Fail! You didn't find sum 657724
# Fail! You didn't find sum 1239007
# Fail! You didn't find sum 408463
# Fail! You didn't find sum 1099474
# Fail! You didn't find sum 255695
# Average time for sum search is 179.356 ms
# Hash type #5: Open Address Hash with Double Func
# Load time: 322.254 ms
# Number of collisions: 17096
# Fail! You didn't find sum 758052
# Fail! You didn't find sum 1092119
# Fail! You didn't find sum 1040353
# Fail! You didn't find sum 888014
# Fail! You didn't find sum 991665
# Fail! You didn't find sum 657724
# Fail! You didn't find sum 1239007
# Fail! You didn't find sum 408463
# Fail! You didn't find sum 1099474
# Fail! You didn't find sum 255695
# Average time for sum search is 177.967 ms
# Input size 100000 processing time 7247.375 ms
# Collisions overall statistics:
# Type 1: 0 (0.00%), 141 (14.10%), 15308 (15.31%). Avg: 9.80%
# Type 2: 1 (10.00%), 150 (15.00%), 15115 (15.12%). Avg: 13.37%
# Type 3: 0 (0.00%), 149 (14.90%), 17106 (17.11%). Avg: 10.67%
# Type 4: 0 (0.00%), 149 (14.90%), 17102 (17.10%). Avg: 10.67%
# Type 5: 0 (0.00%), 166 (16.60%), 17096 (17.10%). Avg: 11.23%
# Your total grade is 50