def count_names(all_text: str) -> dict:

    with open("names.txt", "r", encoding="utf-8") as open_file:
        all_text = open_file.read().split()


    names_count = {}
    for name in all_text:
        if name in names_count:
            names_count[name] += 1
        else:
            names_count[name] = 1
 
    return names_count

def main():
    with open("names.txt", "r", encoding="utf-8") as open_file:
        all_text = open_file.read().split()
    string = all_text
    count_dict = count_names(string)

    for name, count in count_dict.items():
        print(f"{name}: {count}")

if __name__ == "__main__":
    main()