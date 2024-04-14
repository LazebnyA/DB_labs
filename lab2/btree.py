from collections import deque

D = 2
max_depth = 4
max_keys = 4
max_leaves = max_keys ** max_depth


def hash_function(word):
    dictionary = {
        'А': 1, 'Б': 1, 'В': 1, 'Г': 2, 'Д': 2, 'Е': 2, 'Є': 2,
        'Ж': 3, 'З': 3, 'И': 3, 'І': 3, 'Ї': 3, 'Й': 3,
        'К': 4, 'Л': 4, 'М': 5, 'Н': 5, 'О': 6, 'П': 6,
        'Р': 7, 'С': 7, 'Т': 8, 'У': 8, 'Ф': 8, 'Х': 9,
        'Ц': 9, 'Ч': 9, 'Ш': 9, 'Щ': 9, 'Ь': 9, 'Ю': 9,
        'Я': 9
    }

    word = word.upper()

    code = ''
    int_hash = 0
    for i, char in enumerate(word):
        if i < 3:
            if char not in dictionary.keys():
                continue
            code += str(dictionary.get(char))  # перекодовуємо кожну букву в хеш
        else:
            int_hash += ord(char) % max_leaves
    code += '0' * (10 - len(code))  # додаємо нулі до коду, щоб отримати 10 значень

    code = int(code) + int_hash

    return code


class Node:
    def __init__(self, parent=None, leaf=False, next_sibling=None):
        self.keys = []
        self.leaf = leaf
        self.parent = parent
        self.children = [] if not leaf else None
        self.next_sibling = next_sibling

    def get_keys(self):
        return self.keys

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
            self.next_sibling = right_node

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

            if self.children[index].leaf:
                self.children[index].keys.append(key)
                self.children[index].keys.sort()
                if len(self.children[index].keys) > D * 2:
                    self.children[index].split()
            else:
                self.children[index].insert(key)
                if len(self.children[index].keys) > D * 2:
                    self.children[index]()

            if len(self.keys) > D * 2:
                return self.split()

        return self

    def search_object(self, key):
        if self.leaf and key in [pair[0] for pair in self.keys]:
            return self

        if not self.leaf:
            index = 0
            while index < len(self.keys) and key >= self.keys[index]:
                index += 1
            if self.children and index < len(self.keys) + 1:
                return self.children[index].search_object(key)

        return False

    def search_page(self, key):

        page_obj = self.search_object(key)
        if page_obj:
            for pair in page_obj.keys:
                if pair[0] == key:
                    return pair[1]
        return False

    def search_all_after(self, key):

        fst_page = self.search_object(key)
        el_idx = [pair[0] for pair in fst_page.keys].index(key)
        lst_of_pages = [pair[1] for pair in fst_page.keys[el_idx:]]

        current_page = fst_page.next_sibling
        while True:
            if current_page is None or current_page is False:
                break
            lst_of_pages.append([pair[1] for pair in current_page.keys])
            current_page = current_page.next_sibling

        return lst_of_pages

    def del_by_key(self, key):
        leaf_object = self.search_object(key)

        if leaf_object:
            keys_lst = [pair[0] for pair in leaf_object.keys]
            if key in keys_lst:
                el_idx = keys_lst.index(key)
                del leaf_object.keys[el_idx]
        return False


class BPlusTree:
    def __init__(self):
        self.root = Node(leaf=True)

    def insert(self, key):
        self.root = self.root.insert(key)

    def search(self, key):
        return self.root.search_page(key)

    def search_after(self, key):
        return self.root.search_all_after(key)

    def delete(self, key):
        return self.root.del_by_key(key)

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

    names_with_numbers = [
        ("Соколовський Ігор Петрович", ["+380123456789", "+380987654321"]),
        ("Козловський Андрій Володимирович", ["+380234567890"]),
        ("Павлюченко Олександр Олександрович", ["+380345678901", "+380876543210"]),
        ("Поляковський Михайло Іванович", ["+380456789012"]),
        ("Коваленко Ольга Сергіївна", ["+380567890123", "+380765432109"]),
        # ("Міщенко Тетяна Вікторівна", ["+380678901234"]),
        # ("Івановський Валерій Петрович", ["+380789012345", "+380654321098"]),
        # ("Сидорович Юрій Віталійович", ["+380890123456"]),
        # ("Петрович Ігор Васильович", ["+380901234567", "+380543210987"]),
        # ("Мельничук Ірина Андріївна", ["+380012345678"]),
        # ("Григорович Наталія Олександрівна", ["+380123456789", "+380432109876"]),
        # ("Ткаченко Олексій Сергійович", ["+380234567890"]),
        # ("Шевченко Віктор Миколайович", ["+380345678901", "+380321098765"]),
        # ("Бондаренко Оксана Петрівна", ["+380456789012"]),
        # ("Лисенко Василь Ігорович", ["+380567890123"]),
        # ("Кравченко Олена Володимирівна", ["+380678901234"]),
        # ("Сидоренко Владислав Олексійович", ["+380789012345", "+380210987654"]),
        # ("Гриценко Іван Юрійович", ["+380890123456"]),
        # ("Іванченко Тетяна Михайлівна", ["+380901234567"]),
        # ("Павленко Дмитро Олегович", ["+380012345678"]),
        # ("Ткачук Людмила Вікторівна", ["+380123456789", "+380654321098"]),
        # ("Іваненко Юлія Олегівна", ["+380234567890"]),
        # ("Петренко Олександр Миколайович", ["+380345678901"]),
        # ("Михайленко Вікторія Володимирівна", ["+380456789012", "+380987654321"]),
        # ("Дмитренко Ігор Олександрович", ["+380567890123"]),
        # ("Василенко Ірина Анатоліївна", ["+380678901234"]),
        # ("Кондратенко Олександр Вікторович", ["+380789012345"]),
        # ("Карпенко Юрій Петрович", ["+380890123456"]),
        # ("Коваленко Олексій Андрійович", ["+380901234567"]),
        # ("Литвиненко Надія Миколаївна", ["+380012345678"]),
        # ("Романенко Марина Сергіївна", ["+380123456789"]),
        # ("Шевельов Сергій Валерійович", ["+380234567890"]),
        # ("Гончаренко Ірина Петрівна", ["+380345678901"]),
        # ("Семененко Олег Михайлович", ["+380456789012"]),
        # ("Черненко Оксана Іванівна", ["+380567890123"]),
        # ("Гладченко Віталій Володимирович", ["+380678901234"]),
    ]

    for name, number in names_with_numbers:
        hashed_name = hash_function(name)
        print(f"Ім'я: {name},\nНомер телефону: {number}.\nХеш-код: {hashed_name}\n")

        B.insert((hashed_name, (name, number)))

    print("_" * 100)

    B.print_tree()

    print("_" * 100)

    print(B.delete(4610000530))
    print(B.delete(4630000763))

    print("_" * 100)

    B.print_tree()


if __name__ == '__main__':
    main()
