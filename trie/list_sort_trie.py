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


def sort_list(arr):
    trie = Trie()
    for key in arr:
        trie.insert(key)

    result = []
    find_words_helper(trie.root,result,'')

    return result

keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

print(sort_list(keys))