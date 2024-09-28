# unit testing python

unit-testing-python

## comandos para ejecutar pruebas

py -m unittest discover -v -s tests

## ejecutar pruebas en especifico o por clase

py -m unittest tests.test_calculator.CalculatorTests

## ejecutar pruebas con doctest

py -m doctest src/calculator.py

## excluir los archivos de test

coverage run --source src -m unittest

## ejecutar coverage

coverage run -m unittest discover tests

## generar reporte de coverage

coverage report

## generar reporte de coverage en html

coverage html

## ejecutar pruebas con pytest

pytest tests/test_pytest.py -v
