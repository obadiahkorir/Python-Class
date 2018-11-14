def hello(name):
    greeting="Hello," + name + "\n"
    greeting=greeting + "It is very nice to meet you"
    return greeting
    def main():
     yourname = input("Enter Your Name:")
    print(hello(yourname))
    main()
