'''
Sachin Vidyasagaran
17 Oct 2018

This script is used to clean the shadow_robot_dataset in order to run a machine
learning algorithm for predicting the robustness of a grip
'''

import csv

m_count = 0       # counts the number of measurements taken for every experiment
pos = 0                                    # index of current row of the dataset
m_num = 0              # index of column numer of the measurement_number feature

instance = list()                        # stores the current row of the dataset
avg = list()           # stores the average of all measurements of an experiment

with open('original_shadow_robot_dataset.csv', 'r') as readf, open('cleaned_dataset.csv', 'w', newline='') as writef:
    reader = csv.reader(readf)
    for row in reader:
        pos += 1
        if pos == 1:
            # Identify the position of the measurement number
            for i in range(len(row)):
                if row[i] == ' measurement_number':
                    m_num = i
            instance = row                  # assign feature names to 'instance'
            writer = csv.writer(writef)        # write feature names to the file
            writer.writerow(instance)
        else:
            instance = row
            for i in range(len(instance)):
                if i != 0:
                    instance[i] = float(instance[i])
            if row[m_num] == 0:
                if pos != 2:
                    for i in range(len(avg)):            # divide avg by m_count
                        if i != 0:
                            avg[i] /= m_count
                    writer = csv.writer(writef)        # write avg to a new file
                    writer.writerow(avg)
                avg = instance
                m_count = 1
            else:
                for i in range(len(avg)):                  # add instance to avg
                    if i != 0:
                        avg[i] += instance[i]
                m_count += 1
        if pos == 992642:
            for i in range(len(avg)):                    # divide avg by m_count
                if i != 0:
                    avg[i] /= m_count
            writer = csv.writer(writef)                # write avg to a new file
            writer.writerow(avg)
