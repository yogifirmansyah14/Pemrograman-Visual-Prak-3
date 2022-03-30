# Moch Yogi Firmansyah
# 20051397044
# MI 2020 B

class stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def IsEmpty(self):
        return self.items == []

    def peek (self):
        if not self.IsEmpty():
            return self.items[-1]

    def get_stack (self):
        return self.items

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.IsEmpty():
        rev_str = input_str[::-1]
        if (rev_str == input_str):
            print ("Palindrom")
            break
        else :
            print ("Bukan Palindrom")
            break
    return rev_str


stack = stack()
input_str = "rusak"
print("Jika dibalik menjadi : ",reverse_string(stack, input_str))