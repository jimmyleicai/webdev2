with open('data.csv' , 'r') as f:
    header = f.readline()
    content = f.readlines()
    print(header)
