from util import Queue, Stack
# island count problem

def deleteOnes(grid, i, j, rows, cols):
  q = Stack()
  q.push([i, j])
  # e.g 01->  00->  01->  00->  01
  grid[i][j] = 0

  while q.size() > 0:
    node = q.pop()
    # row will be constant for a while and change
    row = node[0]
    # always change
    col = node[1]


    # rows and cols are fixed
                        #  +y              -y                 +x            -x
    for row2, col2 in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col -1)):
      # its a tuple...inside a tuple
      # if you make use of one i and not i,j
      # you get the full tuple if you declear i,j and log one u get the first value in the tuple and like wise
      
      print( row2, col2, ((row + 1, col), (row - 1, col), (row, col + 1), (row, col -1)) )
      # print(row2, col2) #fixed 
      # the <= and < is needed to prevent island[-1] which returns last of thr array.
      # which we dont want
      # print(0 <= row2 < rows, 0 <= col2 < cols, grid[row2][col2] > 0)
      if 0 <= row2 < rows and 0 <= col2 < cols and grid[row2][col2] > 0:
        # prevent moving outside from the two ends 
        # after it finds the +y -y -x x if 1 it adds to queue
        # and it runs again if it finds anything again it adds to queue
        # which is where the dfs comes in
        # we could also make use of stack to try it out....meaning work on it immediately
        print(grid[row2][col2], '->', row2, col2)
        grid[row2][col2] = 0
        q.push([row2, col2])

# islands = [[1, 0, 1, 0, 1],
#           [1, 1, 0, 0, 0],
#           [0, 1, 0, 1, 1]]

def island_counter(arr):
  rows = len(arr) 
  cols = len(arr[0])
  count = 0
  for i in range(rows):
    for j in range(cols):
      # print(i,j)
      if arr[i][j] == 1: 
        print(i,j, 'oo')
        deleteOnes(arr, i, j, rows, cols)
        count += 1
        # print(count)
  
  return count



# islands = [[0, 1, 0, 1, 0],
#         [1, 1, 0, 1, 1],
#         [0, 0, 1, 0, 0],
#         [1, 0, 1, 0, 0],
#         [1, 1, 0, 0, 0]]

# islands = [[1, 1, 0, 0, 0],
#         [1, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 0, 1, 1]
#          ]
#         #  3
# islands = [[1, 1, 1, 1, 0],
#           [1, 1, 0, 1, 0],
#           [1, 1, 0, 0, 0],
#           [0, 0, 0, 0, 0]
#            ]
#         #  1
# islands = [[1, 0, 1, 0, 1],
#            [1, 1, 0, 0, 0],
#            [0, 1, 0, 1, 1]
#          ]
#         #  3 ----turned out to be 4 looks like the youtube guy was wrong
islands = [ [0,    1,    0,    1,    0],
          [0,    0,    1,    1,    1],
          [1,    0,    0,    1,    0],
          [0,    1,    1,    0,    0],
          [1,    0,    1,    0,    1] ]
# 6
islands=[[1, 1, 0, 0, 0], 
         [0, 1, 0, 0, 1], 
         [1, 0, 0, 1, 1], 
         [0, 0, 0, 0, 0], 
         [1, 0, 1, 0, 1]]

print(island_counter(islands) ) # 4
# print(numIslands(islands))

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# print(island_counter(islands) ) # 13