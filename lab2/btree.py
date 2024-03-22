from collections import deque

D = 2

class Node:
    def __init__(self, parent=None, leaf=False):
        self.keys = []
        self.children = [] if not leaf else None
        self.parent = parent
        self.leaf = leaf

    def split(self):
        right_node = Node(leaf=self.leaf)
        mid_idx = len(self.keys) // 2
        goes_up = self.keys[mid_idx]

        new_root = Node()
        if self.parent is None:
            new_root.keys.append(goes_up)
            right_node.keys = self.keys[mid_idx + 1:]
            self.keys = self.keys[:mid_idx]
            new_root.children = [self, right_node]
            for child in new_root.children:
                child.parent = new_root
        return new_root

    def insert(self, key):
        if self.leaf:
            self.keys.append(key)
            self.keys.sort()
            if len(self.keys) > D * 2:
                return self.split()
            return self
        else:
            index = 0
            while index < len(self.keys) and key >= self.keys[index]:
                index += 1
            if self.children and index < len(self.keys) + 1:  # Check if the node has children
                new_root = self.children[index].insert(key)
                if new_root:  # If the child node split, handle the split
                    if self.parent is None:  # If current node is root, update root
                        self.parent = new_root
                    else:  # Otherwise, split recursively
                        return new_root.split()

    def search(self, key):
        if key in self.keys:
            return True
        elif self.leaf:
            return False
        else:
            index = 0
            while index < len(self.keys) and key > self.keys[index]:
                index += 1
            if self.children and index < len(self.keys) + 1:  # Check if the node has children
                return self.children[index].search(key)
            else:
                return False


class BPlusTree:
    def __init__(self):
        self.root = Node(leaf=True)

    def insert(self, key):
        self.root = self.root.insert(key)


    def search(self, key):
        return self.root.search(key)

    def print_tree(self):
        if self.root is None:
            return

        queue = deque([self.root])

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                print(node.keys, end=" ")

                if not node.leaf and node.children:
                    for child in node.children:
                        queue.append(child)

            print("\n")


def main():
    B = BPlusTree()

    for i in range(5):
        B.insert((i, "value"))

    B.print_tree()


if __name__ == '__main__':
    main()
