# PAC4 - Anàlisi de Dades de LaLiga (1995-2025)

## Descripció del Projecte

Aquest projecte és una anàlisi exhaustiva de les dades històriques de la Lliga Espanyola de Futbol des de 1995 fins a 2025. El projecte s'ha desenvolupat com a part de la quarta activitat d'avaluació continuada (PAC4) de l'assignatura "Programació per a la Ciència de Dades" del Màster en Ciència de Dades Aplicada de la UOC.

El projecte inclou anàlisis estadístiques completes sobre:
- Càrrega i anàlisi exploratòria de dades (EDA)
- Distribució de gols locals i visitants
- Partits jugats per equip
- Resultats de partits (victòries, empats, derrotes)
- Classificació històrica acumulada (1995-2025)
- Podi dels millors equips
- Gràfics de connexions entre equips

## Estructura del Projecte

```
.
├── src/
│   ├── main.py                 # Punt d'entrada principal
│   ├── config.py               # Configuració global del projecte
│   ├── exercises/              # Mòduls dels exercicis
│   │   ├── __init__.py
│   │   ├── ex1.py             # Càrrega i EDA
│   │   ├── ex2.py             # Partits totals
│   │   ├── ex3.py             # Distribució de gols
│   │   ├── ex4.py             # Resultats FTR
│   │   ├── ex5.py             # Classificació global
│   │   ├── ex6.py             # Summary i Podi
│   │   └── ex7.py             # Gràfics de connexions
│   ├── data/                   # Datasets
│   └── img/                    # Gràfiques generades
├── tests/
│   └── tests_ex6.py           # Tests de l'exercici 6
├── doc/                        # Documentació generada
├── screenshots/                # Captures de pantalla
├── requirements.txt            # Dependències del projecte
├── README.md                   # Aquest fitxer
└── LICENSE                     # Llicència del projecte

```

## Requisits del Sistema

- Python 3.8 o superior
- pip (gestor de paquets de Python)

## Instal·lació

### 1. Clonar o descarregar el projecte

```bash
cd /ruta/al/projecte
```

### 2. Crear un entorn virtual (recomanat)

```bash
python3 -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# o
.venv\Scripts\activate  # En Windows
```

### 3. Instal·lar les dependències

```bash
pip install -r requirements.txt
```

## Ús

### Executar tots els exercicis (1-7)

```bash
cd src
python main.py
# o explícitament
python main.py -ex 7
```

### Executar exercicis específics

```bash
# Només l'exercici 1
python main.py -ex 1

# Exercicis 1-3
python main.py -ex 3

# Exercicis 1-5
python main.py -ex 5
```

### Obtenir ajuda

```bash
python main.py -h
# o
python main.py --help
```

### Exemple de sortida

```
======================================================================
PAC4 - LaLiga Data Analysis Project (1995-2025)
Alumne: Jonathan_Mir
======================================================================

======================================================================
EXERCICI 1
======================================================================

Carregant el dataset i realitzant l'anàlisi exploratòria...

Primers valors del dataset:
    Date  HomeTeam  AwayTeam  FTHG  FTAG  FTR
0   08/08/1995  Real Madrid  Barcelona    1    2    A
...
```

## Verificació de Qualitat del Codi

### Verificar amb Pylint

```bash
pylint src/exercises/ex*.py src/main.py --disable=line-too-long
```

### Verificar amb Black (formatador)

```bash
black src/ --check
```

### Verificar amb Flake8

```bash
flake8 src/ --max-line-length=100
```

## Execució de Tests

### Executar tots els tests

```bash
cd tests
python -m pytest tests_ex6.py -v
# o amb unittest
python -m unittest tests_ex6.py -v
```

### Executar tests específics

```bash
python -m pytest tests_ex6.py::TestEx6::test_fun_total_goals -v
```

### Cobertura de tests

```bash
pip install coverage
coverage run -m pytest tests/tests_ex6.py
coverage report -m
```

## Generació de Documentació

### Generar documentació amb Sphinx

```bash
pip install sphinx
cd doc
sphinx-quickstart
# Seguir les instruccions
```

### Generar documentació amb pdoc

```bash
pip install pdoc
pdoc src/exercises/ -o doc/
```

## Dependències del Projecte

- **pandas**: Manipulació i anàlisi de dades
- **matplotlib**: Creació de visualitzacions
- **networkx**: Anàlisi i visualització de grafs
- **ipython**: Suport per a Jupyter notebooks
- **jupyter**: Entorn de notebooks interactius

Per veure les versions específiques, consulteu [requirements.txt](requirements.txt).

## Informació de l'Alumne

- **Nom**: Jonathan_Mir
- **Assignatura**: 22.503 · Programació per a la Ciència de Dades
- **Grau**: Màster en Ciència de Dades Aplicada
- **Universitat**: UOC - Universitat Oberta de Catalunya

## Informació sobre els Exercicis

### Exercici 1 (0.4p): Càrrega i EDA
- Càrrega del dataset
- Eliminació de columnes innecessàries
- Anàlisi exploratòria de dades
- Visualització de la distribució de gols

### Exercici 2 (0.6p): Partits Totals
- Càlcul de partits jugats per equip
- Identificació d'equips a primera divisió
- Gràfica de partits per equip

### Exercici 3 (0.6p): Distribució de Gols
- Càlcul de la distribució de gols locals i visitants
- Visualització mitjançant gràfiques de barres

### Exercici 4 (0.6p): Resultats FTR
- Anàlisi de victòries, derrotes i empats
- Càlcul del percentatge de victòries locals

### Exercici 5 (0.6p): Classificació Global
- Càlcul de punts acumulats
- Determinació del guanyador històric

### Exercici 6 (0.6p): Summary i Podi
- Creació del dataframe summary
- Visualització del podi històric
- Tests unitaris inclosos

### Exercici 7 (0.6p): Gràfics de Connexions
- Creació del graf de connexions entre equips
- Visualització de relacions entre els 5 millors equips

### Exercici 8 (2p): Projecte Python Modular
- Organització del codi en mòduls
- Implementació de main.py amb arguments CLI
