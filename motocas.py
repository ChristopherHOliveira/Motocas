# importing the classes Garage and Motoca
from motorcycle import Garage, Motoca

# importing the csv module
import csv

# instantiating a Garage object
garage = Garage()

print('\n============== Motocas v1.0 ==============\n')

# opening the .csv and storing the data in 'csvfile' variable
with open('data_motocas.csv', newline='') as csvfile:
    # read the data through reader function
    reader = csv.reader(csvfile)
    headers = next(reader)

    # for each row in the data
    for row in reader:
        # instantiate a Motoca object considering each field value as a parameter
        # and add it to a list of objects stored in a property of a Garage object
        garage._motocas.append(Motoca(row[0],
                                      float(row[1]),
                                      float(row[2]),
                                      float(row[3]),
                                      float(row[4]),
                                      float(row[5])))

# counting the objects uploaded
num_obj = 0
for m in garage._motocas:
    num_obj += 1

print(f'{num_obj} objects uploaded successfully from database.')

answer = 'm'

while answer == 'm' or answer == 'M' or answer == 'a' or answer == 'A':
    # command menu
    answer = input('\nType:\n\n'
                   '[M] to show the current Motocas\n'
                   '[A] to add a new Motoca\n'
                   '[D] to delete a Motoca\n'
                   '[Q] to quit\n\n'
                   '>>> ')

    # validating allowed commands
    while answer != 'm' and answer != 'M' and answer != 'a' and answer != 'A' and answer != 'd' and answer != 'D' and answer != 'q' and answer != 'Q':
        answer = input('\nINVALID COMMAND!\n\n'
                       'Type:\n\n'
                       '[M] to show the current Motocas\n'
                       '[A] to add a new Motoca\n'
                       '[D] to delete a Motoca\n'
                       '[Q] to quit\n\n'
                       '>>> ')

    # print a dictionary containing all attributes of stored Motocas
    if answer == 'M' or answer == 'm':
        for m in garage._motocas:
            print(vars(m))

    # add a new Motoca
    elif answer == 'A' or answer == 'a':
        # recieve the input data
        add_model = input('\nModel (name - year): ')
        add_cv = float(input('Power (cv): '))
        add_rpm_cv = float(input('Peak power rpm (/1000): '))
        add_tork = float(input('Tork (kgf.m): '))
        add_rpm_tork = float(input('Peak tork rpm (/1000): '))
        add_kg = float(input('Weight (kg): '))

        # instantiate the new object Motoca()
        garage.add_motoca(add_model, add_cv, add_rpm_cv, add_tork, add_rpm_tork, add_kg)

        # write the data to the DB (*.csv), as a new row
        with open('data_motocas.csv', 'a+', newline='') as csvfile:
            # write the data through writer and writerow functions
            writer = csv.writer(csvfile)
            new_row = [add_model, add_cv, add_rpm_cv, add_tork, add_rpm_tork, add_kg]
            writer.writerow(new_row)

    # delete a Motoca <<<<<< EM DESENVOLVIMENTO
    elif answer == 'd' or answer == 'D':
        # exhibiting the Motocas position in garage
        c = 1
        for m in garage._motocas:
            print(f'Position: {c} Motoca: {vars(m)}\n'
                  '=========================================')
            c += 1

        #
        position_del1 = int(input('\nType a Motoca position to delete: '))

        position_del2 = input('\nAre you sure you want to delete the Motoca below?\n\n'
                              f'{vars(garage._motocas[position_del1 -1])}\n\n'
                              '[Y] yes\n'
                              '[N] no\n\n'
                              '>>> ')

    # quit
    else:
        exit()
