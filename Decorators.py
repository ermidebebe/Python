def decorator(orignal):
    def support():
        print("Code before the Orignal code")
        orignal()
        print("code after the orignal code")
    return support
@decorator
def main():
    print("this is the main code")
main()

