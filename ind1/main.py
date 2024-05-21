# Узел бинарного дерева
class Node:
    value = None
    left = None
    right = None

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    root = None

    def _append(self, value, currentNode: Node):
        if value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = Node(value)
            else:
                self._append(value, currentNode.right)
        elif value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = Node(value)
            else:
                self._append(value, currentNode.left)

    def append(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._append(value, self.root)

    def _deep(self, currentNode: Node, deepValue=0) -> int:
        if currentNode.right is not None and currentNode.left is not None:
            return max(self._deep(currentNode.right, deepValue + 1), self._deep(currentNode.left, deepValue + 1))
        elif currentNode.left is not None:
            return self._deep(currentNode.left, deepValue + 1)
        elif currentNode.right is not None:
            return self._deep(currentNode.right, deepValue + 1)
        else:
            return deepValue

    def _deep_iterative(self) -> int:
        deepValue = 0
        queue = [(self.root, 0)]
        while queue:
            curNodeWithLevel = queue.pop()
            if curNodeWithLevel[1] > deepValue:
                deepValue = curNodeWithLevel[1]

            if curNodeWithLevel[0].right is not None:
                queue.append((curNodeWithLevel[0].right, curNodeWithLevel[1] + 1))

            if curNodeWithLevel[1].left is not None:
                queue.append((curNodeWithLevel[0].left, curNodeWithLevel[1] + 1))

        return deepValue

    def _countNodesOnLevel_iterative(self, levelToCheck: int) -> int:
        sum = 0
        queue = [(self.root, 0)]
        while queue:
            curNodeWithLevel = queue.pop()
            if curNodeWithLevel[1] == levelToCheck:
                sum += 1
            else:
                if curNodeWithLevel[0].right is not None:
                    queue.append((curNodeWithLevel[0].right, curNodeWithLevel[1] + 1))

                if curNodeWithLevel[1].left is not None:
                    queue.append((curNodeWithLevel[0].left, curNodeWithLevel[1] + 1))

        return sum

    def _countNodesOnLevel(self, currentNode: Node, levelToCheck: int, currentLevel: int = 0) -> int:
        if levelToCheck == currentLevel:
            return 1
        else:
            if currentNode.right is not None and currentNode.left is not None:
                return (
                        self._countNodesOnLevel(currentNode.right, levelToCheck, currentLevel + 1)
                        + self._countNodesOnLevel(currentNode.left, levelToCheck, currentLevel + 1)
                )
            elif currentNode.left is not None:
                return self._countNodesOnLevel(currentNode.left, levelToCheck, currentLevel + 1)
            elif currentNode.right is not None:
                return self._countNodesOnLevel(currentNode.right, levelToCheck, currentLevel + 1)
            else:
                return 0

    def isBalanced(self) -> bool:
        # Поиск глубины дерева
        deep = self._deep(self.root)

        print("deep", deep)

        for i in range(1, deep - 1):
            nodesOnLevel = self._countNodesOnLevel(self.root, i)
            print(nodesOnLevel, i)
            if nodesOnLevel < 2 ** i:
                return False

        return True

    def isBalanced_iterative(self) -> bool:
        # Поиск глубины дерева
        deep = self._deep_iterative()

        for i in range(1, deep - 1):
            nodesOnLevel = self._countNodesOnLevel_iterative(self.root, i)
            if nodesOnLevel < 2 ** i:
                return False

        return True


def main():
    arr = [4, 3, 2, 6, 1, 7]
    tree = BinaryTree()
    for i in arr:
        tree.append(i)

    print(tree.isBalanced())

    arr = [1, 2, 3, 4]
    tree = BinaryTree()
    for i in arr:
        tree.append(i)

    print(tree.isBalanced())

    arr = [1]
    tree = BinaryTree()
    for i in arr:
        tree.append(i)

    print(tree.isBalanced())

main()
