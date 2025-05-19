def write_to_file(filename):
    data = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(data + '\n')
def append_to_file(filename):
    additional_data = input("Enter text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(additional_data + '\n')
def read_file(filename):
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
def main():
    filename = 'output.txt'
    write_to_file(filename)
    append_to_file(filename)
    read_file(filename)
if __name__ == '__main__':
    main()