from trie.TrieNode import TrieNode
from trie.Trie import Trie

def is_formation_possible(dictionary, word):
    # Write your code here
    for i in range(len(word)):
        word1 = word[0:i]
        word2 = word [i:len(word)]
        if word1 in dictionary and word2 in dictionary:
            return True

    return  False

dictionary = ["the", "hello", "there", "answer", "any",
                     "by", "world", "their", "abc"]
word = "helloworld"

print(is_formation_possible(dictionary, word))