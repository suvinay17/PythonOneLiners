def main():
    x = input()
    palindrome(x)

def palindrome(x):
    print(x == x[::-1])


if __name__ == "__main__":
    main()
