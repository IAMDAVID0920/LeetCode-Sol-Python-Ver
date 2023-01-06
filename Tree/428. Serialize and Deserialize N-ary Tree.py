# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        :type root: Node
        :rtype: str
        """
        res = []

        def dfs(node):
            if node is None:
                return
            res.append(str(node.val))
            for child in node.children:
                dfs(child)
            res.append("N")

        dfs(root)
        return ",".join(res)


    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        """
        if not data:    return None
        tokens = deque(data.split(","))
        root = Node(int(tokens.popleft()), [])

        def dfs(node):
            if not tokens:
                return
            while tokens[0] != "N":
                value = tokens.popleft()
                child = Node(int(val), [])
                node.children.append(child)
                dfs(child)
            tokens.popleft() # get rid/discard all the "N"
        dfs(root)
        return root
