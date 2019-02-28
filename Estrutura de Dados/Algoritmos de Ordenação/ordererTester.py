#!/usr/bin/python3

import numpy as np
import inquirer as inq
from pprint import pprint as prt

from insetionSort import InsertionSorter
from selectionSort import SelectionSorter


questions = [
    inq.List('sorter',
             message="Qual algoritmo de ordenação deseja testar?",
             choices=["Insertion Sort", "Selection Sort"]
             ),
    inq.List('arraySize',
             message="Qual o tamanho do array?",
             choices=[10, 30, 50, 100, 1000, 10000]
             ),
    inq.List('arrayMax',
             message="Qual o valor máximo para os números do array?",
             choices=[10, 50, 100, 1000]
             ),
    inq.List('numTests',
             message="Quantos testes fazer?",
             choices=[1, 10, 100]
             ),
    inq.List('verbose',
             message="Verbose?",
             choices=['Não', 'Sim']
             )
]


def run(options):
    for i in range(options['numTests']):
        testArray = np.random.randint(
            options['arrayMax'], size=options['arraySize'])

        if options['sorter'] == "Insertion Sort":
            mySorter = InsertionSorter(testArray)

        else:
            mySorter = SelectionSorter(testArray)

        res = mySorter.sort()
        ref = np.sort(testArray)

        if options['verbose'] == "Sim":
            print('')
            print(' --- Generated array:')
            prt(testArray)

            print(' --- My sort result:')
            prt(res)

            print(' --- Expected result:')
            prt(ref)

        if (np.array_equal(res, ref)):
            print('[ Test ' + str(i+1) + ' ] PASSED!')

        else:
            print('[ Test ' + str(i+1) + ' ] FAILED!')
            exit(-1)


if __name__ == "__main__":
    options = inq.prompt(questions)
    run(options)
