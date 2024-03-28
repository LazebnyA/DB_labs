from collections import deque

D = 2


def hash_function(word):
    dictionary = {
        'А': 1, 'Б': 1, 'В': 1, 'Г': 2, 'Д': 2, 'Е': 2, 'Є': 2,
        'Ж': 3, 'З': 3, 'И': 3, 'І': 3, 'Ї': 3, 'Й': 3,
        'К': 4, 'Л': 4, 'М': 5, 'Н': 5, 'О': 6, 'П': 6,
        'Р': 7, 'С': 7, 'Т': 7, 'У': 7, 'Ф': 8, 'Х': 8,
        'Ц': 8, 'Ч': 8, 'Ш': 8, 'Щ': 9, 'Ь': 9, 'Ю': 9,
        'Я': 9
    }

    if len(word) > 10:
        word = word[:10]

    code = ''
    for char in word:
        code += str(dictionary.get(char.upper()))  # перекодовуємо кожну букву в хеш
    code += '0' * (10 - len(code))  # додаємо нулі до коду, щоб отримати 10 значень

    return int(code)


class Node:
    def __init__(self, parent=None, leaf=False):
        self.keys = []
        self.children = [] if not leaf else None
        self.parent = parent
        self.leaf = leaf

    def split(self):
        right_node = Node(leaf=True)
        mid_idx = len(self.keys) // 2

        if self.leaf:
            goes_up = self.keys[mid_idx][0]
        else:
            goes_up = self.keys[mid_idx]

        if not self.leaf:
            right_node.leaf = False
            right_node.keys = self.keys[mid_idx + 1:]

            children_mid_idx = len(self.children) // 2
            right_node.children = self.children[children_mid_idx:]

            for child in self.children[children_mid_idx:]:
                child.parent = right_node

            self.children = self.children[:children_mid_idx]
        else:
            right_node.keys = self.keys[mid_idx:]

        self.keys = self.keys[:mid_idx]

        if self.parent is None:
            new_root = Node()
            new_root.keys.append(goes_up)

            self.parent = new_root

            new_root.children = [self, right_node]

            for child in new_root.children:
                child.parent = new_root

            return new_root
        else:
            self.parent.keys.append(goes_up)
            self.parent.keys.sort()
            right_node.parent = self.parent

            self_idx = self.parent.children.index(self)
            self.parent.children.insert(self_idx + 1, right_node)

    def insert(self, key):
        if self.leaf:
            self.keys.append(key)
            self.keys.sort()
            if len(self.keys) > D * 2:
                return self.split()
        else:
            index = 0
            while index < len(self.keys) and key[0] >= self.keys[index]:
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
        i = 0
        while queue:
            level_size = len(queue)
            i += 1
            print(f"Level: {i}")
            for j in range(level_size):
                node = queue.popleft()
                print(f"Node {j + 1}: {node.keys}")

                if not node.leaf and node.children:
                    for child in node.children:
                        queue.append(child)

            print("\n")


def main():
    B = BPlusTree()

    names = [
        "Ковальчук",
        "Шевченко",
        "Петренко",
        "Коваль",
        "Мельник",
        "Бондаренко",
        "Лисенко",
        "Кравченко",
        "Сидоренко",
        "Григоренко",
        "Іваненко",
        "Павленко",
        "Ткаченко",
        "Іванов",
        "Поліщук",
        "Гончаренко",
        "Романенко",
        "Дмитренко",
        "Семененко",
        "Василенко",
        "Ярошенко",
        "Олійник",
        "Кучеренко",
        "Черненко",
        "Гладченко",
        "Шевельов",
        "Гаврилюк",
        "Поляков",
        "Кондратенко",
        "Карпенко"
    ]

    for name in names:
        hashed_name = hash_function(name)
        print(f"Ім'я: {name}, Хеш-код: {hashed_name}")

        B.insert((hashed_name, name))

    B.print_tree()


if __name__ == '__main__':
    main()

# при перенесенні значення в корінь, треба його копіювати (залишати в ноді)
# в нелистових нодах не повинно бути значень у ключів (просто ключі)

# якщо goes up з не листової ноди, воно не копіює значення вверх, а переносить його

# попрацювати над прінтом дерева
