import csv


def atualiza_dados(valor_liquido):
    print ("Valor a ser atualizado" +valor_liquido)


with open('Exportar_custodia_2019-01-09.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        elif line_count == 1:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[0]+ " - "+row[1]+ " - "+row[7])
            if row[1] == "BTG PACTUAL ABSOLUTO INSTITUCIONAL FIQ DE FIA":
                 atualiza_dados(row[7])
            line_count += 1
    print(f'Processed {line_count} lines.')


