tableData = [
          ['apples','oranges','cherries','banana'],
          ['Alice','Bob','Carol','David'],
          ['dog','cats','moose','goose']]
def printTable(list_list_values):
  colWidth = [0] * len(list_list_values)
  for i in range(len(list_list_values)):
    for j in range(len(list_list_values[i])):
      if(colWidth[i] < len(list_list_values[i][j])):
        colWidth[i] = len(list_list_values[i][j])
  print(colWidth)
  i = 0;
  for j in range(len(list_list_values[i])):
    tabLine = "";
    for i in range(len(list_list_values)):
      tabLine += (list_list_values[i][j].rjust(colWidth[i]))
      tabLine += " | "
    print(tabLine)

printTable(tableData)

