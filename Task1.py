def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

read_file('sample.txt')
