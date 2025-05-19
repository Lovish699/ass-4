def read_file(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
read_file("sample.txt")