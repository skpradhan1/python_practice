from trie.TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of a character 't'
    def get_index(self, t):
        return ord(t) - ord('a')
        # ord(): Given a string of length one,
        # returns an integer representing the Unicode code of the character.

    # Function to insert a key in the Trie
    def insert(self, key):
        if key is None:
            return None
        key = key.lower()
        index=0
        current = self.root
        for level in range(len(key)):
            index = self.get_index(key[level])
            if current.children[index] is None:
                current.children[index] = TrieNode(key[level])
                print(key[level] + " inserted")

            current = current.children[index]

        current.mark_as_leaf()
        print(key + " inserted")

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False
        key = key.lower()
        current = self.root
        for level in range(len(key)):
            index = self.get_index(key[level])
            if current.children[index] is None:
                return False
            current = current.children[index]
        if current is not None and current.is_end_word:
            return True
        return False

    def has_no_children(self, current_node:TrieNode):
        for i in range(len(current_node.children)):
            if current_node.children[i] is not None:
                return False
        return True
    
    def delete_helper(self, key, current_node:TrieNode, length, level):
        deleted_self = False
        if current_node is None:
            print('key does not exist')
            return deleted_self

        if length == level:
            if self.has_no_children(current_node):
                deleted_self= True
                current_node = None

            else:
                deleted_self = False
                current_node.unmark_as_Leaf()

        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(key, child_node, length, level+1)
            if child_deleted:
                current_node.children[self.get_index(key[level])] = None

                if current_node.is_end_word:
                    deleted_self = False
                elif self.has_no_children(current_node) is False:
                    deleted_self = False
                else:
                    current_node = None
                    deleted_self = True
            else:
                deleted_self = False
        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            return False
        self.delete_helper(key, self.root, len(key),0)



