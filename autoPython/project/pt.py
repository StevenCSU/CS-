# pt.py - print table content in an organized format

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [getLen(t) for t in table]
    colHeight = len(table[0])
    m = ''
    for j in range(colHeight):
        for i in range(len(colWidths)):
            m += table[i][j].rjust(colWidths[i])
            m += ' '
        m += '\n'
    print(m)

# def printTable(table):
#     colWidths = [getLen(t) for t in table]
#     colHeight = len(table[0])
#     for j in range(colHeight):
#         m = ''
#         for i in range(len(colWidths)):
#             m = m + table[i][j].rjust(colWidths[i]) + " "
#         print(m)
#     print(m)

def getLen(table):
    max = len(table[0])
    for _ in table:
        if len(_) > max:
            max = len(_)
    return max

printTable(tableData)