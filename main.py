counter = 1

while counter <= 100:
    if counter % 15 == 0:
      print(str(counter) + ' egér')
    elif counter % 5 == 0:
      print(str(counter) + ' cica')
    elif counter % 3 == 0:
      print(str(counter) + ' kutya')
    else:
      print(counter)
    counter += 1

