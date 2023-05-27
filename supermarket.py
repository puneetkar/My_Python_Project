supermarket={
'store1':{
    'name': 'Durga General store',
    'items':[
        {'name':'store','quantity':20},
        {'name' : 'brush','quantity':30},
        {'name':'pen','quantity':30},
        ]
    },
'store2':{
            'name': 'sunny book store',
            'items':[
                    {'name':'Java','quantity':20},
                    {'name' : 'C++','quantity':30},
                    {'name':'Python','quantity':30},
    
                    ]
}
}
print('name of the store1')
print(supermarket['store1']['name'])
print(supermarket['store1']['items'])
for x in supermarket['store1']['items']:
    if x['name']=='pen':
        print(x['quantity'])
print(supermarket.get('store1').get('name'))
print('The name of all item present in store')
for d in supermarket['store2']['items']:
    if d['name']=='Java':
        print(d['quantity'])
           

