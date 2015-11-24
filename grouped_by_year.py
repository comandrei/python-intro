import argparse

FIELDNAMES = ("NUME", "FACULTATE", "AN")


def print_students(students):
    """ This print the students groupd by year """


def group_students(csvfile):
    """ This groups students by year
    Given the file format have a look at the
    csv module - https://docs.python.org/2/library/csv.html
    """
    return {}


def main(filename):
    with open(filename) as csvfile:
        students = group_students(csvfile)

    print_students(students)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List students by year')
    parser.add_argument('filename',  type=str, help='filename to use')
    args = parser.parse_args()
    main(args.filename)
