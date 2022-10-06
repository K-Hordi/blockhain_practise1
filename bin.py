from array import array
import datetime
import random
key_lenghts = 8,16,32,64,128,256,512,1024,2048,4096 

keys = {}

def binary_key_gen(len):
    val = [str(random.randint(0,1)) for n in range(int(len))]
    key = "".join(val)
    return key

for len in key_lenghts:
    key = binary_key_gen(len)
    new_key={len:bin(int(key,2))}
    keys.update(new_key)
    ##print(f"Generated key for length {len} is : {bin(int(key,2))}")

def brutforce(len, key):
    time_start = datetime.datetime.now()
    for i in range(pow(2,len)):        
        if bin(i)==bin(int(key,2)):
            print(f"Matched key  {bin(i)}")
            print(f"Original key {key}")
            break  
    time_stop = datetime.datetime.now()
    timer = (time_stop - time_start).microseconds
    print(f"For length {int(len)} brutforcing time is {timer*0.001} milliseconds\n")

for l, k in keys.items():
    brutforce(int(l),k)