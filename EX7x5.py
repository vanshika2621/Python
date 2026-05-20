# 5. Custom exceptions (fixed)

class FileEmptyError(Exception):
    pass

class FileNotFoundCustom(Exception):
    pass

try:
    filename = "data.txt"

    with open(filename, "r") as f:
        content = f.read()

        if not content:
            raise FileEmptyError("File is empty")

        print(content)

except FileNotFoundError:
    print("FileNotFoundCustom: File does not exist")

except FileEmptyError as e:
    print(e) 

    