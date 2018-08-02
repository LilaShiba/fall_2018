# https://www.codewars.com/kata/strings-mix
hash1 = {}
hash2 = {}
def mix(s1, s2):
    # turn into a sorted array
    args1 = list(s1)
    args1 = sorted(args1, key=str)
    args2 = list(s2)
    args2 = sorted(args2, key=str)
    # populate hash with key values
    hash1_check = county_boy(args1, hash1)
    hash2_check = county_boy(args2, hash2)
    # organize what hash has more and equal amount and normalize keys
    ans_unformated = set_norm(hash1_check, hash2_check)
    # seperate ans_unformated
    ans1 = ans_unformated[0]
    ans2 = ans_unformated[1]
    equal_boys = ans_unformated[2]
    # make strings
    ans = make_strings(ans1,ans1,equal_boys)
    # check hashes
    print("I am hash1 check", hash1_check)
    print("I am hash2 check", hash2_check)
    print("I am ans1", ans1)
    print("I am ans2", ans2)
    print("I am equal", equal_boys)
    # give the good stuff
    return ans


def county_boy(args, hashy):
    guide = ['a','b','c','d','e','f','g','h',
            'i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x',
            'y','z']
    # filter for reqs
    for x in args:
        if x in guide:
            count = args.count(x)
            if count > 1:
                hashy[x] = count
    return hashy

def set_norm(hash1, hash2):
    # set norm for hashes: all contain = keys
    for key in hash2:
        if key in hash1:
            pass
        else:
            hash1[key] = 0
    for key in hash1:
        if key in hash2:
            pass
        else:
            hash2[key] = 0
    # compare args
    hash1_more = {k: hash1[k] for k in hash1 if k in hash2 and hash1[k] > hash2[k]}
    hash2_more = {k: hash2[k] for k in hash2 if k in hash1 and hash2[k] > hash1[k]}
    equal_hash = {k: hash2[k] for k in hash2 if k in hash1 and hash2[k] == hash1[k]}
    print("this is hash1", hash1_more)
    print("this is hash2", hash2_more)
    print("this is equal hash", equal_hash)
    return hash1_more, hash2_more, equal_hash

def make_strings(ans1, ans2, equal_boys):
    pass




mix("Are they here e e e", "yes, they are here q q q")
