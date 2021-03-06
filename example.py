from openbabel import pybel
from nocharge import neutralize

for smi in ["CC(=O)[O-]", "C[N+](C)(C)C"]:
    mol = pybel.readstring("smi", smi).OBMol
    altered = neutralize(mol)
    if altered:
        outsmi = pybel.Molecule(mol).write("smi", opt={"n": True, "nonewline": True})
        print("{} changed to {}".format(smi, outsmi))
    else:
        print("{} was unaltered by neutralize".format(smi))
