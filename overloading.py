class Greetings():
    def Hello(self,name=None,age=None):
        if name is None and age is None:
            print("Hello")
        elif name is not  None and age is None:
            print(f"Hello {name}")
        elif name is not None and age is not None:
            print(f"Hello {name} with {age}age")
greet=Greetings()
greet.Hello()
greet.Hello("Ava")
greet.Hello("Ava",26)
