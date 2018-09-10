#https://www.codewars.com/kata/range-extraction/train/python
# woops, made this just check if i and i+1 are more than 3 a part
def solution(args):
    arr = sorted(args, key=int)
    ans = ''
    for x in range(0,len(arr)):
        try:
            current = arr[x]
            nxt = arr[x+1]
            nxt3 = arr[x+2]
            if current - nxt > 2 or current - nxt < -2:
                add_me = str(arr[x])+'-'+str(arr[x+1])+','
                ans += add_me
                nxt = nxt3
            else:
                ans += str(arr[x])+','
        except:
            pass
    ans = ans[:-1]
    print(ans)
    return ans

solution([-6,-3,-2,-1,0,0,3,4,5,7,8,9,10,11,18,18,19,20])
