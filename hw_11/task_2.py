class Math:

    def addition(self, attr1, attr2):
        print(attr1 + attr2)

    def subtraction(self, attr1, attr2):
        print(attr1 - attr2)

    def multiplication(self, attr1, attr2):
        print(attr1 * attr2)

    def division(self, attr1, attr2):
        try:
            print(attr1 / attr2)
        except Exception as e:
            print(e)


example = Math()

example.addition(2, 3)
example.subtraction(3, 4)
example.multiplication(4, 5)
example.division(6, 0)