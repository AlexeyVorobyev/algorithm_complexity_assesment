import timeit


class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def completionTree(root, e):
    if not root.left:
        root.left = Tree(e)
    elif not root.right:
        root.right = Tree(e)
    else:
        if iterative_count_nodes(root.left) <= iterative_count_nodes(root.right):
            completionTree(root.left, e)
        else:
            completionTree(root.right, e)


def obh_recurs(t, k):
    if t:
        k = 1 + obh_recurs(t.left, k) + obh_recurs(t.right, k)
    return k


def iterative_count_nodes(root):
    if root is None:
        return 0
    stack = []
    count = 0
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            count += 1
            current = current.right
        else:
            break
    return count


def countVertex2(root):
    if not root:
        return 0
    return 1 + countVertex1(root.left) + countVertex1(root.right)


def countVertex1(root):
    if not root:
        return 0
    return countVertex2(root.right) + countVertex2(root.left) + 1


def indirCount(root):
    return countVertex1(root)


t = Tree(0)
root = t
for i in range(1, 5000):
    completionTree(root, i)

k = 0
start = timeit.default_timer()
print('Рекурсивный метод:' + str(obh_recurs(root, k)))
finish = timeit.default_timer()
print('Время работы обхода дерева рекурсивно: {:.20f} секунд'.format(finish - start))

start = timeit.default_timer()
print('Итеративный метод:' + str(iterative_count_nodes(root)))
finish = timeit.default_timer()
print('Время работы итеративного подсчета узлов: {:.20f} секунд'.format(finish - start))

print('Косвенная рекурсия:' + str(indirCount(root)))
