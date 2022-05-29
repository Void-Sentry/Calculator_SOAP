from zeep import Client

if __name__ == '__main__':
    try:
        client  = Client('http://localhost:8000/?wsdl')
        
        while True:
            first       = input('\noperador 1: ')
            second      = input('\noperador 2: ')
            operation   = input('\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\n')
            
            if(operation == '1'): 
                print(f'\nresult: {client.service.sum(first, second)}')
            elif(operation == '2'): 
                print(f'\nresult: {client.service.sub(first, second)}')
            elif(operation == '3'): 
                print(f'\nresult: {client.service.mul(first, second)}')
            elif(operation == '4'):
                print(f'\nresult: {client.service.div(first, second)}')
            else:
                print('\nInvalid input!')

    except(KeyboardInterrupt, EOFError):
        print('GoodBye')
exit