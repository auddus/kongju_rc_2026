class MyList:
    def __init__(self):
        self.myVariable = "Hello World"
        self.myVariable2 = "Hello World 2"
        self.mylist = list()

    def append(self, ele):
        self.mylist.append(ele)



def main():
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    print(list_a + list_b)
    print(list_a)
    list_a.extend(list_b)
    print(list_a)

    list_b.append(7)
    list_b.append(8)
    print(list_b)
    list_b.insert(1, 4.5)
    print(list_b)
    myList_a = MyList()
    myList_a.append("myung")
    myList_a.append("myList_a.myVariable, myList_a.myVariable2")


if __name__ == "__main__":
    main()
