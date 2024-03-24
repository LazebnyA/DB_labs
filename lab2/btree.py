from collections import deque

D = 2


class Node:
    def __init__(self, parent=None, leaf=False):
        self.keys = []
        self.children = [] if not leaf else None
        self.parent = parent
        self.leaf = leaf

    def split(self):
        right_node = Node(leaf=True)
        mid_idx = len(self.keys) // 2
        goes_up = self.keys[mid_idx]

        if self.parent is None:
            new_root = Node()
            new_root.keys.append(goes_up)
            right_node.keys = self.keys[mid_idx + 1:]
            self.keys = self.keys[:mid_idx]

            self.parent = new_root

            if not self.leaf:
                children_mid_idx = len(self.children) // 2
                right_node.children = self.children[children_mid_idx+1:]
                self.children = self.children[:children_mid_idx]

                right_node.parent = new_root
                right_node.leaf = False

            new_root.children = [self, right_node]

            for child in new_root.children:
                child.parent = new_root

            return new_root
        else:
            self.parent.keys.append(goes_up)
            self.parent.keys.sort()
            right_node.keys = self.keys[mid_idx + 1:]
            right_node.parent = self.parent
            self.keys = self.keys[:mid_idx]
            self.parent.children += [right_node]

    def insert(self, key):
        if self.leaf:
            self.keys.append(key)
            self.keys.sort()
            if len(self.keys) > D * 2:
                return self.split()
        else:
            index = 0
            while index < len(self.keys) and key >= self.keys[index]:
                index += 1

            # Check if the current node is a leaf
            if self.children[index].leaf:
                # If it's a leaf node, insert the key directly
                self.children[index].keys.append(key)
                self.children[index].keys.sort()
                if len(self.children[index].keys) > D * 2:
                    self.children[index].split()
            else:
                # If it's an internal node, continue traversal
                self.children[index].insert(key)
                if len(self.children[index].keys) > D * 2:
                    self.children[index]()

            if len(self.keys) > D * 2:
                return self.split()

        return self


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

    for i in range(1, 18):
        B.insert((i, f"value {i}"))

    B.print_tree()


if __name__ == '__main__':
    main()

# при перенесенні значення в корінь, треба його копіювати (залишати в ноді)
# при вставці значення 17 воно не опускається до листів

#ліве піддерево показується а праве ні.!!!

