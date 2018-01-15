class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
def generateTree(inorder, postorder):
    if not inorder:
        return None
    data = postorder.pop()
    root = Node(data)
    index = inorder.index(data)
    root.right = generateTree(inorder[index+1:],postorder)
    root.left = generateTree(inorder[0:index], postorder)
    return root

inorder = [7,6,3,8,5,1,12,4,10,9,11]
postorder = [7,6,8,5,3,12,10,11,9,4,1]

root = generateTree(inorder,postorder)
print(root)
