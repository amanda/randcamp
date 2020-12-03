import json


def get_names_from(filename):
    with open(filename) as f:
        name_list = [x.strip() for x in f.readlines()]
    return name_list


if __name__ == "__main__":
    names = get_names_from("result.txt")
    with open("bands.json", "w") as f:
        json.dump(names, f)
