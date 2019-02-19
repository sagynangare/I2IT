try:
    c=1/2
    ''' serious code '''
    
except ZeroDivisionError as zde:
    print('Opps ', zde, 'occured.')
    '''exception handled'''
else:
    'this executes only if there is no exception'''
    print('This is else block')
finally:
    print('This is finally block')
    ''' Executes anyway '''
    
