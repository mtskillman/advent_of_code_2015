import hashlib
#print((hashlib.md5("abcdef609043".encode())).hexdigest())

def hash_check(secret_key, num):
    combined_form = secret_key + str(num)
    thing = hashlib.md5(combined_form.encode()).hexdigest()
    thing = str(thing)
    counter = 0
    for char in thing[0:6]:
        if char == '0':
            counter += 1
    if counter == 6:
        print(num)
        return(thing)
    else: 
        #print(f'running.... {num}')
        return None

num = 0
while hash_check("yzbqklnj", num) == None:
    num += 1
