def solution(args):
    arr = args
    ans = ''
    bros = []
    for x in range(0,len(arr)):
        try:
            cur = arr[x]
            nxt = arr[x+1]
            if cur - nxt == 1 or cur - nxt == -1:
                bros.append(cur)
            elif len(bros) > 2:
                bros.append(cur)
                st = bros[0]
                en = bros[-1]
                ans_make = str(st) +"-"+ str(en)
                ans += str(ans_make)+','
                bros = []
            else:
                ans += str(cur)+','
                ans += str(nxt)+','
                bros = []

        #ans = ans[:-1]
    print(ans)

solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
