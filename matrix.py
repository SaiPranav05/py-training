def matrix(n):
    mat=[[0]*n for _ in range(n)]
    num=1
    up=0
    down=n-1
    left=0
    right=n-1
    while num<=n*n:
        for i in range(left,right+1):
            mat[up][i]=num
            num=num+1
        up=up+1
        for i in range(up,down+1):
            mat[i][right]=num
            num=num+1
        right=right-1
        for i in range(right,left-1,-1):
            mat[down][i]=num
            num=num+1
        down=down-1
        for i in range(down,up-1,-1):
            mat[i][left]=num
            num=num+1
        left=left+1
    return mat
def print_mat(mat):
    for row in mat:
        print(' '.join(f'{num:2}' for num in row))

n=int(input())
mat=matrix(n)
print_mat(mat)