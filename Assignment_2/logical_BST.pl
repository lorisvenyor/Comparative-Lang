
% empty represents an empty tree (empty list)
bst(empty).
bst(_, LeftSubtree, RightSubtree):- bst(LeftSubtree), bst(RightSubtree).

% if tree is empty, make it the root base case 
insert(X, empty, bst(X, empty, empty)).
% if the integer is equal to the root. 
insert(X, bst(X, LeftSubtree, RightSubtree), bst(X, LeftSubtree, RightSubtree)).
% insert the node on the leftsubtree if it's less than the root
insert(X, bst(Root, LeftSubtree, RightSubtree), bst(Root, NewLeftSubtree, RightSubtree)) :- X < Root, insert(X, LeftSubtree, NewLeftSubtree).
% insert the node on the rightsubtree if it's greater than the root
insert(X, bst(Root, LeftSubtree, RightSubtree), bst(Root, LeftSubtree, NewRightSubtree)) :- X > Root, insert(X, RightSubtree, NewRightSubtree).


% base case if the integer is the same as the key.
search(X, bst(X,_,_)).
% if x is less than the root, search through the leftsubtree
search(X, bst(Y, LeftSubtree, _)) :- X < Y, search(X, LeftSubtree).
% otherwise search through the rightsubtree.
search(X, bst(Y, _, RightSubtree)) :- X > Y, search(X, RightSubtree).

% left -> right -> root
% so basically go to the left subtree with a list
% and then to the right subtree with a list
% then append the right list and the root
% then append both to the final list.
postorder(empty, []).
postorder(bst(Root, empty, empty), [Root]). 
postorder(bst(Root, LeftSubtree, RightSubtree), PostOrder):- 
    postorder(LeftSubtree, LList), postorder(RightSubtree, RList), append(RList, [Root], RightRoot), append(LList, RightRoot, PostOrder), !.

% leftsubtree -> root -> rightsubtree
inorder(empty, []).
inorder(bst(Root, empty, empty), [Root]).
inorder(bst(Root, LeftSubtree, RightSubtree), InOrder) :- inorder(LeftSubtree, LList), inorder(RightSubtree, RList), append([Root], RList, Result), append(LList, Result, InOrder), !.

% root -> left -> right
preorder(empty, []).
preorder(bst(Root, empty, empty), [Root]).
preorder(bst(Root, LeftSubtree, RightSubtree), PreOrder) :- preorder(LeftSubtree, LList), preorder(RightSubtree, RList), append(LList, RList, Result), append([Root], Result, PreOrder), !. 