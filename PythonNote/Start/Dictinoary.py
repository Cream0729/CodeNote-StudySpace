# Tips: Key must be only
new_dict = {"wood": 16, "coco": 3.5, "chip": 299, "wood": 15}
print(new_dict)
for x in new_dict:
    # key : value
    print(x, ':', new_dict[x])
print()

my_dict = {
    "user1": {
        "cod1": 100,
        "cod2": 80,
        "cod3": 60
    },
    "user2": {
        "cod1": 100,
        "cod2": 80,
        "cod3": 50
    },
    "user3": {
        "cod1": 90,
        "cod2": 80,
        "cod3": 60
    }
}

print(my_dict, '\n')
# add k-v
my_dict["user4"] = {"cod1": 100, "cod2": 75, "cod3": 60}
print(my_dict, '\n')

my_dict.pop("user2")
print(my_dict, '\n')

print("All the keys:", my_dict.keys())
print("length:", len(my_dict))
print(max(my_dict), min(my_dict))
print()

print(sorted(my_dict))