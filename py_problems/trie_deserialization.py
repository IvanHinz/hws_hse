# Code a program to deserialize a Trie from a string x: string x represents a preorder traversal of
# a serialized Trie, with two additional symbols. Each character of x is either:
#  A lowercase letter 'a','b',...,'z' that represents the value of a node in the Trie.
#  The dollar symbol '$' which indicates that the previous letter is an end-of-word node.
#  The number sign symbol '#' that we will denote as a “return-to-parent” move.
# If symbol '#' appears, then the letter after '#' will be a child of the parent of the letter before '#'.
# For example, for ''ab#c'', we have that 'c' is a child of the parent of 'b' (which is 'a').
# The effect of symbol '#' can be accumulative!
# For example, for ''abc##d'', we have that 'd' will be a child of the grand-parent of 'c' (which is 'a')
# You can assume that suffix links and output links are not encoded in the string and we do not need
# to add them in the Trie.
# After the Trie is deserialized, print all patterns stored in the Trie whose prefix is an input string y.

class TrieNode:
    def __init__(self, char, parent):
        self.char = char

        self.is_end = False

        self.counter = 0

        self.children = {}

        self.parent = parent


# Trie definition
class Trie(object):
    def __init__(self, my_cur_node):
        self.output = None
        self.root = my_cur_node

    def fst(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.fst(child, prefix + node.char)

    def query(self, x):
        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.fst(node, x[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)


# be$ar$##ll$###id$##ull$##y$ - example input
def main():
    input_trie = str(input())
    target_prefix = str(input())
    my_node = TrieNode("", None)
    for i in range(len(input_trie)):
        if input_trie[i] == "#":
            if my_node.parent is not None:
                my_node = my_node.parent
        elif input_trie[i] == "$":
            my_node.is_end = True
        else:
            if not (input_trie[i] in my_node.children.keys()):
                my_node.children[input_trie[i]] = TrieNode(input_trie[i], my_node)
            my_node = my_node.children[input_trie[i]]
    while my_node.parent is not None:
        my_node = my_node.parent

    my_trie = Trie(my_node)
    query_list = my_trie.query(target_prefix)
    if len(query_list) == 0:
        print(-1)
    else:
        for elem in query_list:
            print(elem[0])


if __name__ == '__main__':
    main()
