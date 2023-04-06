def TopView(root):
  if root is None:
    return 
  queue=[(root,0)]
  d={}
  while queue:
    i,j=queue.pop(0)
    if j not in d:
      d[j]=i.info
    queue.append((root.left,j-1))
    queue.append((root.right,j+1))
  for i in sorted(d):
    print(d[i],end=' ')
