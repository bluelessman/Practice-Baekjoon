import sys
pwd_dic = dict()
n,m=map(int,sys.stdin.readline().split())
for i in range(n):
    page_input, pwd = sys.stdin.readline().split()
    pwd_dic[page_input] = pwd.rstrip()
for i in range(m):
    page_output = sys.stdin.readline().rstrip()
    print(pwd_dic[page_output])