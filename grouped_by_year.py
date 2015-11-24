import argparse
import collections
import csv

FIELDNAMES = ("NUME", "FACULTATE", "AN")


def print_students(students):
    for an, students in students.iteritems():
        print an
        for student in students:
            nume, facultate = student["NUME"], student["FACULTATE"]
            print "\t {} -- {} ".format(nume, facultate)


def group_students(csvfile):
    students = collections.defaultdict(list)
    reader = csv.DictReader(csvfile, fieldnames=FIELDNAMES)
    for row in reader:
        students[row['AN']].append(row)
    return students


def main(filename):
    with open(filename) as csvfile:
        students = group_students(csvfile)

    print_students(students)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List students by year')
    parser.add_argument('filename',  type=str, help='filename to use')
    args = parser.parse_args()
    main(args.filename)
