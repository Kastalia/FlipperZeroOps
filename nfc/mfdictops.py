import os


def compare_dicts(path_dict_main, path_dict_user, path_dict_new):
    dict_main = open(path_dict_main, "r").read()
    dict_user = open(path_dict_user, "r").read()
    dict_new = open(path_dict_new, "r").read()

    dict_main_lst = dict_main.strip().replace("\n\n", "\n").split("\n")
    dict_user_lst = dict_user.strip().replace("\n\n", "\n").split("\n")
    dict_new_lst = dict_new.strip().replace("\n\n", "\n").split("\n")

    keys_old = set()
    keys_new = set()

    for key in [*dict_main_lst, *dict_user_lst]:
        if key.startswith(("#", "*", " ")) or key == "":
            continue
        else:
            keys_old.add(key)

    for key in dict_new_lst:
        if key.startswith(("#", "*", " ")) or key == "":
            continue
        else:
            keys_new.add(key)

    keys_old_uniq = set(keys_old).difference(keys_new)
    keys_old_uniq_str = "\n".join(keys_old_uniq)

    keys_new_uniq = set(keys_new).difference(keys_old)
    keys_new_uniq_str = "\n".join(keys_new_uniq)

    print(f"Уникальные в старых ключах:\n{keys_old_uniq_str}")
    print(f"\n\nУникальные в новых ключах:\n{keys_new_uniq_str}")

def add_new_keys(path_dict_main, path_dict_user, path_dict_new):
    remove_duplicates(path_dict_new)

    dict_main = open(path_dict_main, "r").read()
    dict_user = open(path_dict_user, "r").read()
    dict_new = open(path_dict_new, "r").read()

    dict_user = dict_user.strip()

    dict_main_lst = dict_main.strip().replace("\n\n", "\n").split("\n")
    dict_user_lst = dict_user.split("\n")
    dict_new_lst = dict_new.strip().split("\n")

    keys_old = set()

    for key in [*dict_main_lst, *dict_user_lst]:
        if key.startswith(("#", "*", " ")) or key == "":
            continue
        else:
            keys_old.add(key)

    comment = ""
    prev_line_with_key = False
    new_keys = ""
    n_new_keys = 0
    for line in dict_new_lst:
        if line.startswith(("#", "*", " ")) or line == "":
            if prev_line_with_key is True:
                comment = ""
            comment += f"{line}\n"
            prev_line_with_key = False
            continue
        else:
            key = line
            if key not in keys_old:
                if comment:
                    new_keys += comment
                    comment = ""
                new_keys += f"{key}\n"
                n_new_keys += 1
            prev_line_with_key = True



    dict_user += dict_user + "\n\n" + new_keys
    dict_user = dict_user.strip().replace("\n\n\n", "\n\n")

    os.remove(path_dict_user)
    open(path_dict_user, "w").write(dict_user)
    print(f"Added {n_new_keys} new keys")
    #print(new_keys)

def remove_duplicates(*paths_dict):
    keys = set()

    for path_dict in paths_dict:
        dict = open(path_dict, "r").read()

        dict = dict.strip().split("\n")
        dict_clear = ""

        n_duplicates = 0
        for line in dict:
            if line.startswith(("#", "*", " ")) or line == "":
                dict_clear += f"{line}\n"
                continue
            else:
                if line in keys:
                    n_duplicates += 1
                    continue
                else:
                    dict_clear += f"{line}\n"
                    keys.add(line)


        os.remove(path_dict)
        open(path_dict, "w").write(dict_clear)
        print(f"Removed {n_duplicates} duplicate from dictionary {path_dict}")

if __name__ == "__main__":
    pass