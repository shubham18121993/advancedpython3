import csv


def main():
    print('Starting CSV Exmaple')
    print(csv.list_dialects())

    print('Crearting CSV file')
    with open('sample.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['She Loves You', 'Sept 1963'])
        writer.writerow(['I Want to Hold Your Hand', 'Dec 1963'])
        writer.writerow(['Cant Buy Me Love', 'Apr 1964'])
        writer.writerow(['A Hard Days Night', 'July 1964'])

    print('-' * 100)

    print('Starting to read csv file')
    with open('sample.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Process each row in the csv file
        for row in reader:
            row_length = len(row)
            print('row_length', row_length)
            for i in range(row_length):
                # Each element in the row can be accessed via an index
                print(row[i], end=', ')
            print()
    print('Done Reading')

if __name__ == '__main__':
    main()