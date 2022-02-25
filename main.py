open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

bal_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]

unbal_list = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.isEmpty():
            item = self[-1]
            self.__delitem__(-1)
        return item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def check(myList):
    stack = []
    for item in myList:
        if item in open_list:
            stack.append(item)
        elif item in close_list:
            pos = close_list.index(item)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


if __name__ == '__main__':
    for seq in bal_list + unbal_list:
        print(f'{seq:<30}{check(seq)}')
