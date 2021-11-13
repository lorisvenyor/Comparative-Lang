
class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, key, val):                                                   # basic insertion for BST, of key is less than the node, sort it on the left subtree otherwise right subtree
        if node == None:
            self.root = Node(key, val)
        else:
            if key < node.key:
                if node.left == None:
                    node.left = Node(key, val)
                else:
                    self.insert(node.left, key, val)
            else:
                if node.right == None:
                    node.right = Node(key, val)
                else:
                    self.insert(node.right, key, val)

    def search(self, node, key):
        if node == None:                                                                # if node is None, return None
            return None
        elif node.key == key:                                                           # if we found the key, return the value of that node
            return node.value                                                           
        elif key < node.key:                                                            # if key is less than node.key, check left subtree
            return self.search(node.left, key)                                          
        else: 
            return self.search(node.right, key)                                         # if key is greater than node.key, check right subtree
    
    def delete(self, node, key):
        
        if node == None:                                                                
            return None
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:                                                                           # key found, key == node.key
            if node.left == None and node.right == None:                                # if there's no children ie leaf node, delete that node
                return None
            elif node.left != None and node.right != None:                              # if there's 2 children
                max_node = self.maxkey(node.left)                                       # get the max node from the left subtree or get the min from the right subtree but here im checking for the min in the left subtree            
                node.key = max_node.key                                                 # assign the maxnode key to the nodekey 
                node.left = self.delete(node.left, max_node.key)                        # delete the maxnode
            else:                                                                       # one children case
                if node.left != None:   
                    node = node.left
                else:
                    node = node.right
        
        return node                                                                     # this returns the updated node without the key

    def maxkey(self, node):                                                             # basically finding the node of the max node in left subtree, has to be in the node.right since that's where the large keys are located
        while node.right != None:
            node = node.right
        return node    
    
class Phonebook:
    def __init__(self):                                                                 # 2 BST Trees, one for name and one for number
        self._nameTree = BST()                                                          # 2 instances of bst class
        self._numTree = BST()

    def insert_entry(self, name, addr, num):                                            # insert function takes in 3 args name, addr, num
        self._nameTree.insert(self._nameTree.root, name, num)                           # so add the values to the name and num trees
        self._numTree.insert(self._numTree.root, num, (name, addr))
        print("Contact {} has been added.".format(name))

    def search_entry(self, key):                                                        # searches an entry through the phonebook, if key is digit check numbertree otherwise nametree
        if key.isdigit():
            tup =  self._numTree.search(self._numTree.root, key)                        # get the value of the node
            if tup == None:                                                             # if none, contact not found
                print("Contact {} not found.".format(key))
            else:
               print("Name: {}\nNumber: {}\nAddress: {}".format(tup[0],key, tup[1]))
        else:                                                                           # search in the name tree
            num = self._nameTree.search(self._nameTree.root, key)
            if num == None:
                print("Contact {} not found.".format(key))
            else:
                print("Name: {}\nNumber: {}".format(key, num))


    def remove_entry(self, key):                                                        # removes an entry 
        if key.isdigit():  # returns a tuple of 2                                                             # checks if the key is digit, if it is then search the key to the number tree and get the value
            key_delete = self._numTree.search(self._numTree.root, key)
            if key_delete == None:                                                      # if it returns none, it's not in the contacts
                print("Contact {} not found.".format(key))
            else:
                self._numTree.delete(self._numTree.root, key)                           # if found in the contacts, delete the contact from both trees by the value and by the key
                self._nameTree.delete(self._nameTree.root, key_delete[0]) 
                print("Contact {} has been removed".format(key))    
        else:                                                                           # if the key is alpha
            key_delete = self._nameTree.search(self._nameTree.root, key)
            if key_delete == None:
                print("Contact {} not found.".format(key))
            else:                                                                        
                self._nameTree.delete(self._nameTree.root, key)                         # delete the contact from both trees by the value and by the key
                self._numTree.delete(self._numTree.root, key_delete)
                print("Contact {} has been removed".format(key))


def main():
    # name, address, number
    tree = Phonebook()
    tree.insert_entry("Solana", "Seoul, South Korea", "0830945845")
    tree.insert_entry("Kayara", "Yemen, Yemen", "0879843473")
    tree.insert_entry("Saki", "Tokyo, Japan", "0891214398")
    tree.insert_entry("Lili", "Bangkok, Thailand", "0816789023")
    tree.insert_entry("Tilly", "Amsterdam, Netherlands", "0859802856")
    tree.insert_entry("Chae", "Melbourne, Australia", "0867234608")
    tree.insert_entry("Fritzie", "Vigan, Philippines", "0853467213")
    tree.insert_entry("Rory", "Dublin, Ireland", "0852309865")
    print("\n")
    #test cases for contacts that aren't in the phonebook
    tree.search_entry("Niall")
    tree.remove_entry("1234")
    print("\n")
    #removing an entry and searching the entry back to check if it's deleted in both trees
    tree.remove_entry("Solana")
    tree.search_entry("0830945845")
    print("\n")
    tree.search_entry("Saki")
    tree.search_entry("0853467213")
if __name__ == "__main__":
    main()
