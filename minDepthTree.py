queue=[]
        if root is None:
            return 0
        if root is not None:
            queue.append(root)
        depth=1
        while queue:
            s=len(queue)
            for i in range(s):
                cur=queue.pop(0)
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            depth+=1
        return depth
