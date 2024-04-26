"""
This module provides functionality to store the results in a csv file

Author: Kumar
Created Date: 24/Apr/2024
"""
import csv
import os

RESULTS_FILE_PATH="results.csv"
def write_result(principal,interest_rate,time,invevstment_type,future_value):
    """
    This function writes the result to csv file
    """
    file_exists=False
    if os.path.exists(RESULTS_FILE_PATH):
        file_exists=True
    
    with open(RESULTS_FILE_PATH,'a', newline='', encoding='utf-8') as file:
        results_writer=csv.writer(file)
        if not file_exists:
            results_writer.writerow(['principal','interest_rate','time','invevstment_type','future_value'])
        
        results_writer.writerow([principal,interest_rate,time,invevstment_type,future_value])
    
    


def read_result():
    """
    This function writes the result to csv file
    """
    with open(RESULTS_FILE_PATH,'r') as reader:
        result_reader=csv.reader(reader,delimiter=',')
        for reacord in result_reader:
            # to do skip 1st record as it is header
            yield reacord