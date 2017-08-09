#!/usr/bin/python3
import io
import os
import subprocess
import sys
import zipfile


GRADER = os.path.join(os.path.dirname(__file__), 'grader.py')
IMPORT_DIR = os.getcwd()

def main():
  """Main routine checking each assignment"""
  files = sorted([f for f in os.listdir('.') if f.endswith('.py')])
  for assignment in files:
    student_id = assignment.split('_')[0]
    try:
      output = subprocess.check_output(
        [GRADER, IMPORT_DIR, assignment[:-3]]).decode('utf-8')      
      output = output.split('\n')
      score = output[0].split()[1]                      
      print("%s|%s|%s|'%s'" % 
        (assignment, student_id, score, '\n'.join(output)))
    except Exception as e:
      print('ERROR: Unable to grade %s' % assignment, e)


if __name__ == '__main__':
  main()
