def read_file():
    f = open('test.txt', 'r')
    text = f.read()
    print('Text from file is : ' + str(text))
    f.close()

def append_file():
    f = open('test.txt', 'a+')
    text = input('Enter text to feed to the file:\n')
    f.write(str(text) + '\n')

def main():
    read_file()
    append_file()

if __name__ == '__main__':
    main()