from trie.TrieNode import TrieNode
from trie.Trie import Trie

def find_words_helper(node:TrieNode, result, prefix):
    word = prefix+node.char
    if node.is_end_word:
        result.append(word)
    for i in range(len(node.children)):
        if node.children[i] is not None:
            child_node = node.children[i]
            find_words_helper(child_node, result, word)


def find_all_words(root:TrieNode):
    if root is None:
        return None
    result = []
    find_words_helper(root,result,'')

    return result

keys = ["the", "bat", "bbt"]
output = ["Not present in the trie", "Present in the trie"]

t = Trie()
print("Keys to insert: ")
print(keys)

# Construct Trie
for i in range(len(keys)):
    t.insert(keys[i])

print("here all words - ",find_all_words(t.root))

