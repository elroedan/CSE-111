import csv
from datetime import datetime

def main():
    PRODUCT_NUMBER_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    AMOUNT_REQUEST_INDEX = 0
    try:
        total = 0
        subtotal = 0
        current_date_and_time = datetime.now()
        day = current_date_and_time.weekday()
        product_dictionary = read_dict('products.csv', PRODUCT_NUMBER_INDEX)
        
        print()
        print('All Products')
        print(product_dictionary)
        
        with open('request.csv', 'rt') as file:
            reader = csv.reader(file)
            next(reader)
            print()
            print('Requested item:')
            for rows in reader:
                k, v = rows
                if k in product_dictionary:
                    product_number = v[AMOUNT_REQUEST_INDEX]
                    
                    print(f'{product_dictionary[k][NAME_INDEX]}: {product_number} @ {product_dictionary[k][PRICE_INDEX]}')
        
                total += int(product_number)
                subtotal += float(product_dictionary[k][PRICE_INDEX]) * int(product_number)
                sales_tax = subtotal * 0.06
                Total = subtotal +sales_tax

        if day == 2 or day == 3:
            Discount = Total *0.9
        else: 
            Discount = Total 

        print()
        print(f'Number of items: {total}')  
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}')
        print(f'Total: {Discount:.2f}')

        print('Thank you for shopping at the Inkom Emporium')
        print(f'{current_date_and_time:%c}')
    
    except FileNotFoundError as file_err:
        print(f"Error missing file {file_err}") 
    
    except PermissionError as perm_err:
        print(f"{perm_err}")
    
    except KeyError as key_err:
        print(key_err)
        print(f"Unkown product id in the request.csv file ")
def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        next(reader)

        for row_list in reader:

           
            key = row_list[key_column_index]
            dictionary[key] = row_list

    
    return dictionary
if __name__ == '__main__':
    main()