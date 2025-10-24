import json

file_name = "data.json"

data = {'chart_title': 'Groceries Data',
        'data_points': [{'item': 'Apples', 'value': 5}, {'item': 'Bacon', 'value': 2},
                        {'item': 'Milk', 'value': 9}, {'item': 'Pringles', 'value': 1},
                        {'item': 'Bread', 'value': 4}, {'item': 'Rice', 'value': 8},
                        {'item': 'Steaks', 'value': 10}, {'item': 'Tide Pods', 'value': 7}]}

with open(file_name, 'w') as f:
    json.dump(data, f, indent=4)
