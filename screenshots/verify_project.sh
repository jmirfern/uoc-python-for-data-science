#!/bin/bash
# Script per capturar pantallazos de verificació del projecte PAC4

PROJECT_ROOT="/Users/allianz/Documents/Formación/Máster Data Science/Programación para la ciencia de datos/uoc-python-for-data-science"
SCREENSHOTS_DIR="${PROJECT_ROOT}/screenshots"

cd "$PROJECT_ROOT"

# Activar el entorno virtual
source .venv/bin/activate

echo "=========================================="
echo "Captura 1: Estructura de carpetes"
echo "=========================================="
echo ""
echo "Mostrant l'estructura de directoris del projecte:"
echo "Comando: tree -L 2 -I '__pycache__|*.pyc|.venv'"
tree -L 2 -I '__pycache__|*.pyc|.venv' 2>/dev/null || find . -maxdepth 2 -not -path '*/\.*' | head -30

echo ""
echo "=========================================="
echo "Captura 2: Ajuda del programa"
echo "=========================================="
cd src
python main.py --help

echo ""
echo "=========================================="
echo "Captura 3: Executar exercici 1 (parcial)"
echo "=========================================="
echo "Executant: python main.py -ex 1"
echo ""
python main.py -ex 1 2>&1 | tail -20

echo ""
echo "=========================================="
echo "Captura 4: Llistar fitxers generats"
echo "=========================================="
echo "Gràfiques generades a img/:"
ls -lh ../img/grafica_*.png 2>/dev/null | awk '{print $9, "(" $5 ")"}'

echo ""
echo "=========================================="
echo "Captura 5: Tests executats"
echo "=========================================="
cd ../tests
echo "Executant tests de l'exercici 6:"
python -m unittest tests_ex6.TestEx6 -v 2>&1 | tail -15

echo ""
echo "=========================================="
echo "Captura 6: Informació del projecte"
echo "=========================================="
echo "Fitxer README.md:"
head -30 ../README.md

echo ""
echo "=========================================="
echo "Captura 7: Linting amb Pylint"
echo "=========================================="
cd "$PROJECT_ROOT"
echo "Alumne: Jonathan_Mir"
echo "Comanda: pylint src tests"
pylint src tests

echo ""
echo "=========================================="
echo "Verificació completada"
echo "=========================================="
