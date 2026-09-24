class DocumentReadError(Exception):
    pass

filename = input("Enter a filename: ")

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise DocumentReadError("File not found")
    except PermissionError:
        raise DocumentReadError("Permission denied")
    except UnicodeDecodeError:
        raise DocumentReadError("This is not a utf-8 encoded file")

try:
    content = read_file(filename)
except DocumentReadError as e:
    print(e)
else:
    print(content)