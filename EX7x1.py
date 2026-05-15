
try:
    with open("name.txt", "r") as f:
        names = [line.strip() for line in f if line.strip()]

    # a. Count names
    print("Total names:", len(names))

    # b. Names starting with vowel
    vowels = ('A', 'E', 'I', 'O', 'U')
    vowel_count = sum(1 for name in names if name.upper().startswith(vowels))
    print("Names starting with vowel:", vowel_count)

    # c. Longest name
    longest = max(names, key=len)
    print("Longest name:", longest)

except FileNotFoundError:
    print("File not found") 