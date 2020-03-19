import json
dict = {'name': 'Adithya',
        'age': 25,
        'Education' :'Graduate',
        'Majors':['CS','Physics','Maths'],
        'CGPA':7,
        'Gender': 'Male',
        'Phone':99999999,
        'Address': 'Bengaluru'
}
json_obj = json.dumps(dict)
print(json_obj)

# Write to a file
with open('output.json', 'w') as json_file:
  json.dump(json_obj, json_file)
# Read from the file
with open('output.json') as r:
  data = json.load(r)

print(data)