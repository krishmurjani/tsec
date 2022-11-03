import numpy as np
n = int(input ("Enter the number of websites: ")) 
relation = np.empty((n, n))
for i in range (0, n):
  print ( f"Enter '1' if website {i} contains a hyperlink directing to following website (s) else enter '0': ")
  for j in range (0, n):
    x = int(input(f"website {j}: ")) 
    relation[i, j] = x 
    
print(relation) 
pageRank = []

for i in range (0, n): 
  pageRank.append(1/n)

print("Initially the page rank for each page is: ", pageRank)

m = 0
while m < 3:
  m = m + 1
  for i in range (0, n): 
    temp = [] 
    for j in range (0, n):
      if relation [j][i] == 1:
        count = 0 
        for k in range (0, n):
            if relation [j][k] == 1: 
                count = count + 1 
                y = pageRank[j]/count
    temp.append (y)
    # print (temp)
  pageRank[i] = sum(temp)
  print(f"The new Page Ranks after iteration {m} are: ", pageRank)

print(f"Website {pageRank.index(max(pageRank))+1} has the highest page rank whereas Website {pageRank.index(min(pageRank)) +1} has the lowest page rank.")