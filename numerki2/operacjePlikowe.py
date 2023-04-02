def wczytajZpliku(nazwa):

    with open(nazwa) as file:
        fileData = file.read()

    fileData = fileData.split("\n\n")
    data = []

    for i in range(len(fileData)):
        x = []
        base = []

        data1 = fileData[i].split('\n')

        for j in range(len(data1)):
            data2 = data1[j].split('  ')
            if len(data2) != 2:
                return
            x.append(float(data2[1]))
            row = []
            data3 = data2[0].split(',')
            for k in range(len(data3)):
                row.append(float(data3[k]))

            base.append(row)
        data.append((base,x))
    return data


# print(wczytajZpliku("uklad.txt"))