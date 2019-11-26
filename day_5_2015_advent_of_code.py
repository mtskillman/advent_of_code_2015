storage = open('shit3.txt', 'r').readlines()

nicecounter = 0
for word in storage:
    vowelcount = 0
    twice = 0
    i = 0
    temp = ''
    badstrings = ['ab','cd','pq','xy']
    bad_flag = 0
    vowel_collection = ['a','e','i','o','u']

    substrings = {}
    substrings2 = ['33333434','333333']
    secend_condition_flag = 0
    while i < len(word):
        target = word[i]
        if i != 0:
            thing = temp + target
            if substrings2.pop() != thing:
                if thing not in substrings:
                    substrings[thing] = 1
                    substrings2.append(thing)
                else:
                    substrings[thing] += 1
                    substrings2.append(thing)
        if temp == target:
            twice = 1
        if target in vowel_collection:
            vowelcount += 1
        if i >= 2:
            if word[i-2] == target:
                secend_condition_flag = 1
        temp = target
        i += 1
        
    for item in badstrings:
        if word.find(item) != -1:
            bad_flag = 1
    random_flag = 0    
    for num in substrings.values():
        if num > 1:
            random_flag = 1
    if secend_condition_flag == 1 and random_flag == 1:
        nicecounter += 1
print(nicecounter)