import csv

with open("csv_db.txt", "r") as f:
  csv.next();  #przeskakuje piersza linie (naglowek)
  csv_reader = csv.reader(f)
  print(csv_reader)

  for line in csv_reader:
    print(line[2]);
 
  f.seek(0)

  with open("csv_db2.txt", "w") as f_out:

    cvs_writer = csv.witer(f_out, delimiter="-")
    for line in csv_reader:
      csv_writer.witerow(line)  #  gdy w danych jest - to obejmownane w ""



cvs.DictReader()
print(line['name'])

filed_names = ["name", "surname", "email"]
csv.DictWriter(f_out, field_names, delimiter='\t')
csv.writeheader()



