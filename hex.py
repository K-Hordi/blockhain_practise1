import string
import random
import datetime

key_lenghts = 8,16,32,64,128,256,512,1024,2048,4096 


print("Number of variants:")
for len in key_lenghts:
    print(f"For length {len} bits, number of unique keys is {pow(2,len)}\n")

keys = {}
print("\n\n\n")
##print("Keys:")

def gen_key(len):
    val = [random.choice(string.hexdigits) for n in range(int(len/4))]
    key = "".join(val)
    return key

for len in key_lenghts:
    key = gen_key(len)
    new_key={len:hex(int(key,16))}
    keys.update(new_key)
   ## print(f"Generated key for length {len} is : {hex(int(key,16))}")
    
def brutforce(len, key):
    time_start = datetime.datetime.now()
    end_key= '0x'+('f'*int(len/4))
    for i in range(int(end_key,16)):
        
        if hex(i)==key:
            print(f"Matched key  {hex(i)}")
            print(f"Original key {key}")
            break  
    time_stop = datetime.datetime.now()
    timer = (time_stop - time_start).microseconds
    print(f"For length {int(len)} brutforcing time is {timer*0.001} milliseconds\n")
    

for l, k in keys.items():
    brutforce(int(l),k)

