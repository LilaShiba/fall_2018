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
    ans1_l = len(ans1)
    ans2_l = len(ans2)
    ans3_l = len(equal_boys)
    length = ans1_l + ans2_l + ans3_l
    # ans hash
    ans_hash = [ans1, ans2, equal_boys]
    print(ans_hash)
    # make strings
    print(length)
    ans = make_strings(ans_hash, length)
    # give the good stuff
    print(ans_hash)
    ans = ans[:-1]
    print(ans)
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
    return hash1_more, hash2_more, equal_hash

def make_strings(ans_hash, ans_hash_len):
    #TODO find highest val in hashy boy
    str = ''
    count = 0
    while count < ans_hash_len:
        highest = find_highest(ans_hash)
        for hashy in ans_hash:
            for x, y in hashy.items():
                if y >= highest:
                    # find value
                    highest = y
                    # find key
                    letter = x
                    # find index value of hash
                    location = ans_hash.index(hashy)
                    # make string
                    if location == 0:
                        pre = "1:"
                    elif location == 1:
                        pre = "2:"
                    else:
                        pre = "=:"
                    # TODO remove key:value from ans_hash
                    mid = letter_print(highest, letter)
                    str+=  pre+mid+'/'
                    hashy[x] = 0
                    count = count + 1
    return str

def letter_print(n,letter):
    ans = ''
    count = 0
    while count < n:
        ans += letter
        count = count + 1
    return ans

def find_highest(ans_hash):
    highest = 0
    for hashy in ans_hash:
        for x, y in hashy.items():
            if y > highest:
                highest = y
    return highest



#mix("Are they here e e e", "ewrwerwerw, they are here q q q")

mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &","my frie n d Joh n has ma n y ma n y frie n ds n&")
#"1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
mix("codewars", "codewars")

#"1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
