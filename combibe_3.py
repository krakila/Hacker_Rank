def merge_the_tools(string, k):
    d = 0
    p = 0
    f = 0
    u = 1
    word = ''
    while d < len(string):
        while p < k:
            string1 = string
            p = f
            if string1[p] in word:
                y=0
            else:
                word += string1[p]
            if k*u - p == 1 :
                print(word)
                word = ''
                u+=1
            d+=1
            f+=1
        p = 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#AABBCAAADA 3
#AABBC
#AABBC
#AABCAAADA