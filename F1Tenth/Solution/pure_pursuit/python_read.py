#!/usr/bin/env python3
import csv

file_path = '/Users/knowbutdontknow/Downloads/csv_sim.csv' 

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def main():
    csv_data = read_csv_file(file_path)
    
    while csv_data:
        print(csv_data[0])
        csv_data = csv_data[1:] 
    
if __name__ == '__main__':
    main()
