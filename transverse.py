

mine = [
'dep0,parent0,item0',
    ['dep1,parent0,item0','dep1,parent2,item1'],
    ['dep1,parent0'],
    ['dep1,parent0']
]
def recurse(recursable):

    main_list = []

    is_list  = lambda x: isinstance(x, list)
    is_dict  = lambda x: isinstance(x, dict)
    is_tuple = lambda x: isinstance(x, tuple)
    is_many  = lambda y: is_list(y) or is_tuple(y) or is_dict(y)

    def main(many,depth=0):            

        if is_many(many):
            depth += 1
            for item in many:
                if is_many(item):
                    main(item)
                else:
                    main_list.append(f'{depth}  {item}')
        else:
            main_list.append(many)
        depth -= 1
    main(recursable)
    return main_list
            
print(recurse(mine))      
