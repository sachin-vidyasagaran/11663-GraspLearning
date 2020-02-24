'''
Sachin Vidyasagaran
4 Dec 2018

This script is used to add 2 new features to the grasping dataset, namely:
total_velocity: A measure of the net velocity of the joints
total_effort: A measure of the net effort of the joints
'''

import csv

pos = 0                                    # index of current row of the dataset

instance = list()                        # stores the current row of the dataset
avg = list()           # stores the average of all measurements of an experiment

total_velocity = 0
total_effort = 0

with open('test_dataset.csv', 'r') as readf, open('test_dataset_tot.csv', 'w', newline='') as writef:
    reader = csv.reader(readf)
    for row in reader:
        pos += 1
        if pos == 1:
            instance = row                  # assign feature names to 'instance'
            # Adding columns for Total Effort and Total Velocity
            instance.append(' total_velocity ')
            instance.append(' total_effort ')
            writer = csv.writer(writef)        # write feature names to the file
            writer.writerow(instance)
        else:
            total_velocity = 0
            total_effort = 0
            instance = row
            for i in range(len(instance)):
                instance[i] = float(instance[i])
                if i % 3 == 0 and i != 0:
                    total_effort += instance[i]    # adding up all joint efforts
                if i % 3 == 2:
                    total_velocity += instance[i]   # adding up joint velocities
            instance.append(total_velocity)
            instance.append(total_effort)
            writer = csv.writer(writef)           # write instance to a new file
            writer.writerow(instance)
        if pos == 10788:
            break
