# First
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.value

# Second
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.value

# Third
def sum_tree(root):
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

if __name__ == "__main__":
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        root = insert(root, v)

    max_value = find_max(root)
    print(f"Найбільше значення в дереві: {max_value}")

    min_value = find_min(root)
    print(f"Найменше значення в дереві: {min_value}")

    total_sum = sum_tree(root)
    print(f"Сума всіх значень у дереві: {total_sum}")
