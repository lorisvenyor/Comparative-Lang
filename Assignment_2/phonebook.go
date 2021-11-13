package main

import (
	"fmt"
	"unicode"
)

type Node struct {
	key   string
	value []string
	left  *Node
	right *Node
}

type phonebook struct {
	nametree *Node
	numtree  *Node
}

func check_int(str string) bool {
	for _, i := range str {
		if !unicode.IsDigit(i) {
			return false
		}
	}
	return true
}

func (tree *phonebook) insert_entry(name string, addr string, num string) {
	if tree.nametree == nil || tree.numtree == nil {
		tree.nametree = &Node{key: name, value: []string{num}}
		tree.numtree = &Node{key: num, value: []string{name, addr}}
	} else {
		tree.nametree.insert(name, []string{num})
		tree.numtree.insert(num, []string{name, addr})
	}
	fmt.Printf("Contact %s has been added.\n", name)
}

func (node *Node) insert(key string, val []string) {
	if key < node.key {
		if node.left == nil {
			node.left = &Node{key: key, value: val}
		} else {
			node.left.insert(key, val)
		}
	} else {
		if node.right == nil {
			node.right = &Node{key: key, value: val}
		} else {
			node.right.insert(key, val)
		}
	}
}

func (tree *phonebook) search_entry(key string) {
	if check_int(key) {
		num := tree.numtree.search(key)
		if num != nil {
			fmt.Printf("Name: %s\nNumber: %s\nAddress: %s\n", num.value[0], key, num.value[1])
		} else {
			fmt.Printf("Contact %s not found.\n", key)
		}
	} else {
		name := tree.nametree.search(key)
		if name != nil {
			fmt.Printf("Name: %s\nNumber: %s\n", key, name.value[0])
		} else {
			fmt.Printf("Contact %s not found.\n", key)
		}
	}
}

func (node *Node) search(key string) *Node {
	if node == nil {
		return nil
	}
	if key == node.key {
		return node
	}
	if key < node.key {
		return node.left.search(key)
	} else {
		return node.right.search(key)
	}
}

func (tree *phonebook) remove_entry(key string) {

	if check_int(key) { //returns a list of 2 which has the name and addr
		key_delete := tree.numtree.search(key)
		if key_delete == nil {
			fmt.Printf("Contact %s not found.\n", key)
		} else {
			tree.numtree.delete(key)
			tree.nametree.delete(key_delete.value[0])
			fmt.Printf("Contact %s removed.\n", key)
		}
	} else { //returns a list of 1 element which contains a number
		key_delete := tree.nametree.search(key)
		if key_delete == nil {
			fmt.Printf("Contact %s not found.\n", key)
		} else {
			tree.nametree.delete(key)
			tree.numtree.delete(key_delete.value[0])
			fmt.Printf("Contact %s removed.\n", key)
		}
	}
}

func (node *Node) delete(key string) *Node {
	if node == nil {
		return nil
	}
	if key < node.key {
		node.left = node.left.delete(key)
	} else if key > node.key {
		node.right = node.right.delete(key)
	} else if key == node.key {
		if node.left == nil && node.right == nil {
			return nil
		} else if node.left != nil && node.right != nil {
			max_node := node.left.max_node(node.left)
			node.key = max_node.key
			node.left = node.left.delete(max_node.key)
		} else {
			if node.left != nil {
				node = node.left
			} else {
				node = node.right
			}
		}
	}
	return node
}

func (node *Node) max_node(key *Node) *Node {
	for {
		if node.right != nil {
			node = node.right
		} else {
			break
		}
	}
	return node
}

func main() {
	// name, address, number
	tree := &phonebook{}
	tree.insert_entry("Solana", "Seoul, South Korea", "0830945845")
	tree.insert_entry("Kayara", "Yemen, Yemen", "0879843473")
	tree.insert_entry("Saki", "Tokyo, Japan", "0891214398")
	tree.insert_entry("Lili", "Bangkok, Thailand", "0816789023")
	tree.insert_entry("Tilly", "Amsterdam, Netherlands", "0859802856")
	tree.insert_entry("Chae", "Melbourne, Australia", "0867234608")
	tree.insert_entry("Fritzie", "Vigan, Philippines", "0853467213")
	tree.insert_entry("Rory", "Dublin, Ireland", "0852309865")
	fmt.Println()
	// test cases for contacts that aren't in the phonebook
	tree.search_entry("Niall")
	tree.remove_entry("1234")
	fmt.Println()
	// removing an entry and searching the entry back to check if it's deleted in both trees
	tree.remove_entry("Solana")
	tree.search_entry("0830945845")
	fmt.Println()
	tree.search_entry("Saki")
	tree.search_entry("0853467213")
}
