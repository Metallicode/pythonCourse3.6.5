import csv
##with open('file.csv', newline='') as f:
##    reader = csv.reader(f)
##    for row in reader:
##        print(row[0])
##
##print("\n")
##
##
##with open('file.csv', newline='') as f:
##    reader = csv.DictReader(f)
##    for row in reader:
##        print(row["fruits"])



##with open('file.csv', 'a', newline='') as f:
##    writer = csv.writer(f)
##    writer.writerows([["tamar", "sausage", "wine","tofu cheese"]])
    

with open('s.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

 
##
##
##with open('some.csv', 'w', newline='') as f:
##    writer = csv.writer(f)
##    writer.writerows([["hi", "ty", "kk"],["gfff"],["er"]])
##
##
##
###save objects
##class Cdr():
##
##    def __iter__(self):
##        return iter([self.name, self.my_value, self.my_datetime])
##
##
###from another class
##with open(self.file_name, 'wb') as csv_file:
##    wr = csv.writer(csv_file, delimiter=',')
##    for cdr in cdr_list:
##        wr.writerow(list(cdr))  # @Shankar suggestion
