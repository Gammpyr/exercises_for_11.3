def merge_dicts(dict1, dict2):
    result = dict1
    result.update(dict2)
    return result

my_dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict2 = {
  "brand": "Ford2",
  "model2": "Mustang2",
  "year2": 19642
}
print(merge_dicts(my_dict1, my_dict2))