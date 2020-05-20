'''
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
'''
from collections import Counter, OrderedDict


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def get_child(self):
        return self.left, self.right


def haffman_tree(string):
    count_el = Counter(string)
    sorted_dict = OrderedDict(
        sorted(
            count_el.items(),
            reverse=True,
            key=lambda x: x[1]
        )
    )
    while True:
        left = sorted_dict.popitem()
        right = sorted_dict.popitem()
        freq = left[1] + right[1]
        node = Node(left[0], right[0])
        sorted_dict[node] = freq
        sorted_dict = OrderedDict(
            sorted(
                sorted_dict.items(),
                reverse=True,
                key=lambda x: x[1]
            )
        )
        if len(sorted_dict) == 1:
            break

    return sorted_dict


def haffman_code(node, code=''):
    if isinstance(node, str):
        return {
            node: code
        }

    l, r = node.left, node.right
    result = {}

    result.update(haffman_code(l, f'{code}0'))
    result.update(haffman_code(r, f'{code}1'))

    return result


string = 'каждый охотник желает знать'
tree = haffman_tree(string)
table_of_codes = None
for el in tree:
    table_of_codes = haffman_code(el)

codded_str = ''.join(table_of_codes[char] for char in string)

print(string)
print(codded_str)

"""
каждый охотник желает знать
000011110110101101001011101011001011011000011111100010000101101111010000011111000101010011111101100110010
"""