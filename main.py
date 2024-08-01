
import re

# store elements and their atomic weights in a dictionary
# key: Atomic Symbol, value: Atomic Weight
# first 3 rows of periodic table included for now
periodic_table = {
    "H": 1.008, "He": 4.003,
    "Li": 6.940, "Be": 9.012,  "B" : 10.810, "C" : 12.011, "N": 14.007, "O": 15.999, "F" : 18.998, "Ne": 20.180,
    "Na": 22.99, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.060, "Cl": 35.450, "Ar": 39.948
}


def molecular_weight(chemical_formula):
    mw = 0
    molecules = re.findall(r'([A-Z][a-z]?)([\d]*)', chemical_formula)
    for molecule in molecules:
        aw = atomic_weight(molecule[0])
        if molecule[1] == '':
            stoichiometry = 1
        else:
            stoichiometry = int(molecule[1])
        mw += aw*stoichiometry
    return mw


def atomic_weight(element):
    return periodic_table.get(element)


if __name__ == '__main__':

    print(molecular_weight(input("Enter a chemical formula (including up to element Ar): ")))

