import csv

def main():
    PRODUCT_NUMBER_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    AMOUNT_REQUEST_INDEX = 0
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
                # print(product_number)
                # print(product_dictionary[k])
    

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