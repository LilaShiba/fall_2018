def solution(args):
    args =  args
    arr = args
    ans = ''
    bros = []
    try:
        for x in range(0,len(arr)):
            cur = arr[x]
            nxt = arr[x+1]
            if cur - nxt == 1 or cur - nxt == -1:
                bros.append(cur)
            elif len(bros) >= 2:
                bros.append(cur)
                print("I am bro in if", bros)
                st = bros[0]
                en = bros[-1]
                ans_make = str(st) +"-"+ str(en)
                ans += str(ans_make)+','
                bros = []
            elif len(bros) == 1:
                pre = str(arr[x - 1])
                ans += pre + ','
                ans += str(cur)+','
                bros = []
            else:
                ans += str(cur)+','
                bros = []
                print('woof')
    except:
        if arr[-2] - arr[-1] == 1 or arr[-2] - arr[-1] == -1 and len(bros) >= 2:
            bros.append(arr[-2])
            bros.append(arr[-1])
            st = bros[0]
            en = bros[-1]
            ans_make = str(st) +"-"+ str(en)
            ans += str(ans_make)+','
            bros = []
        elif len(bros) == 1:
            pre = str(arr[-2])
            ans += pre + ','
            ans += str(arr[-1])+','
            bros = []
        else:
            ans += str(arr[-1])+','
            bros = []
    ans = ans[:-1]
    print(ans)
    return(ans)

solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
# '-6,-3-1,3-5,7-11,14,15,17-20'
