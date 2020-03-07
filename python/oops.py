class Human:
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def eat(self):
        return f"{self.name} eats rice and samber"

    def work(self):
        return f"{self.name} is now working"

    def sleep(self,time):
        return f"{self.name} sleeps {time}"


if __name__ == "__main__":
    # instantiate the object
    ob_ram = Human("ram", 25)

    # call our instance methods
    print(ob_ram.eat())
    print(ob_ram.work())
    print(ob_ram.sleep("early"))

# Output:
# ram eats rice and samber
# ram is now working
# ram sleeps early
