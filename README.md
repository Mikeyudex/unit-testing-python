# unit testing python

unit-testing-python

## comandos para ejecutar pruebas

py -m unittest discover -v -s tests

## ejecutar pruebas en especifico o por clase

py -m unittest tests.test_calculator.CalculatorTests

## ejecutar pruebas con doctest

py -m doctest src/calculator.py
