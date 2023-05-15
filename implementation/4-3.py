data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) +1
dx = [-1,1,-1,1]
dy = [-1,1,1,-1]

check = 0
for i in range(4):
    row_next = row + 2 * dx[i]
    col_next = col + dy[i]
    if row_next <=8 and 1<= row_next and col_next <=8 and 1 <= col_next:
        check +=1
    row_next = row + dx[i]
    col_next = col + 2 * dy[i]
    if row_next <=8 and 1<= row_next and col_next <=8 and 1 <= col_next:
        check +=1
print(check)
