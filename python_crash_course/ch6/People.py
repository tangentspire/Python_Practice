Sean = {
        'Name' : 'Sean Venard',
        'Sex' : 'Male',
        'Age' : '28'
        }

Claire = {
        'Name' : 'Claire Venard',
        'Sex' : 'Female',
        'Age' : '26'
        }

People = [Sean, Claire]


for person in People:
    print(f"{person}/'s information is:")
    
    for key, value in Person:
        print(f"{key} : {value}")
