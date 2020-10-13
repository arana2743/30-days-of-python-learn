import json


def add_employees(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    print('Initial salary list : %s' % salaries)
    salaries[name] = salary
    print('Post adding salary list : %s' % salaries)
    return json.dumps(salaries)

salaries = '{ "Alfred": 300, "Jane": 400}'
new_salaries = add_employees(salaries,"Me", 800)
decoded_salaries = json.loads(new_salaries)

print(decoded_salaries["Me"])
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
