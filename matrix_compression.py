
#########  Madhur Sharma  ############
def no_of_digit(x):
    cnt=0
    while x>0:
        x=int(x/10)
        cnt+=1
    return cnt
def compress(arr):
    comp_arr=[]
    dat_arr=[]
    for x in arr:
        tmp_dat=[]
        num=0
        for y in x:
            n = no_of_digit(y)
            num = num *( 10**n) + y;
            tmp_dat.append(n)
        
        comp_arr.append(num)
        dat_arr.append(tmp_dat)
    return [comp_arr,dat_arr]


def modify(x,y):
    sz = 10 ** (no_of_digit(x)-y)
    return x%sz,int(x/sz)

def decompress(comp,dat):
    org_mat=[]
    for i in range(0,len(comp)):
        tmp=[]
        for x in dat[i]:
            comp[i],n = modify(comp[i],x)
            tmp.append(n)
        org_mat.append(tmp)
    return org_mat
        

arr = [[11,2,322],[245,4,12]]
comp_arr = compress(arr)
print(comp_arr[0])
print(decompress(comp_arr[0],comp_arr[1])) 
    
