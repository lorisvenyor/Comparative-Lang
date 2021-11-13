
-- used a data structure to define a binary tree
-- a tree can be either empty or has a value with left and right subtree
-- to print out the values use Show

data BST x = Empty | Node x (BST x) (BST x)
                deriving (Show)

-- insert adds an integer x into a binary tree T to give a binary tree R.
-- if the tree is empty, make the integer the root node
-- if the integer is the same as the root, make it the root
-- if the integer is less than the root, pass the integer to the leftsubtree (recursion takes place)
-- otherwise, pass the integer to the rightsubtree (recursion takes place)
-- this will return a new bst with the added node
insert :: Ord a => a -> BST a -> BST a
insert x Empty = Node x Empty Empty
insert x (Node root leftsubtree rightsubtree)
    | x < root = Node root (insert x leftsubtree) rightsubtree
    | x > root = Node root leftsubtree (insert x rightsubtree)
    | x == root = Node x leftsubtree rightsubtree

-- search returns true if x is contained in the binary tree T.
-- if tree is empty return false
-- if the integer is equal to the root return true
-- if integer is less than the root search through the leftsubtree
-- otherwise right subtree until the integer matches the root
search :: Ord a => a -> BST a -> Bool
search x Empty = False
search x (Node root leftsubtree rightsubtree)
    | x == root = True
    | x < root = search x leftsubtree       
    | x > root = search x rightsubtree

-- inorder lists the nodes of the binary tree T using inorder traversal.
-- leftsubtree -> root -> rightsubtree
-- if tree is empty return an empty list
-- otherwise perform inorder traversal
-- go through all the nodes on both subtrees following the order left -> root -> right
inorder :: BST a -> [a]
inorder Empty = []
inorder (Node root leftsubtree rightsubtree) = inorder leftsubtree ++ [root] ++ inorder rightsubtree

-- postorder lists the nodes of the binary tree T using postorder traversal.
-- left -> right -> root
-- same method as the inorder however this time, the root is appended at the end of each recursion
postorder :: BST a -> [a]
postorder Empty = []
postorder (Node root leftsubtree rightsubtree) = postorder leftsubtree ++ postorder rightsubtree ++ [root]

-- preorder lists the nodes of the binary tree T using preorder traversal.
-- root -> left -> right
-- in this traversal, the root is appended first at each recursion
preorder :: BST a -> [a]
preorder Empty = []
preorder (Node root leftsubtree rightsubtree) = [root] ++ preorder leftsubtree ++ preorder rightsubtree
