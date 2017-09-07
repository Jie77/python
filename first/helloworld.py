str = "x.nowcoder.com"
arr = list(str)
nstr = input()
narr = list(nstr)
def initdic(arr):
    dic = {}
    for i in arr:
        dic[i] = 0
    for i in arr:
        dic[i] = dic[i]+1
    return
dic = initdic(arr)
ndic = initdic(narr)
if dic['y'] in dic:
    print ("jcc")
else:
    print("ccdssc")
