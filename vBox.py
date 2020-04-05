
import MoleKing_util as mk

AVOGRADO = 6.02214076E23
PI = 3.14159265

def splitMol(molFormula):
    atomName = ""
    num = 0
    r = False
    list1 = []
    for l in range(0, len(molFormula)):
        if molFormula[l].isupper():
            atomName = molFormula[l]
            num = 1
            r = False
            if l < len(molFormula)-1:
                if molFormula[l+1].isupper():
                    r = True
        elif molFormula[l].islower():
            atomName = atomName + molFormula[l]
        elif molFormula[l].isnumeric():
            num = int(molFormula[l])
            r = True
        if l == len(molFormula)-1:
            r = True
        if r :
            list1.append([atomName, num])
    mol = mk.Molecule()
    for i in list1:
        for j in range(0, i[1]):
            atom = mk.Atom(i[0], 0, 0, 0)
            mol.addAtom(atom)
    return mol

def catchNum(text):
    while True:
        i = input(text)
        if i.isnumeric():
            num = int(i)
            break
        else:
            print("Type a number.")
            continue
    return num

def getValues():
    valuesList = {}
    molTypes = catchNum('How many types of molecules will you have in the box? ')
    for n in range(0, molTypes):
        molFormula = input('Molecular Formula of Molecule ' + str(n+1) + ": ")
        mol = splitMol(molFormula)
        numberMol = catchNum("Number of " + str(mol) + " molecules: ")
        valuesList.update({mol: numberMol})
    return valuesList
        
def volumeSet(molecule, numberMol, density):
    return molecule.getMM() * numberMol / (AVOGRADO * density)

def calcVol(molDict):
    density = catchNum("Density of solution (g/mL): ")
    mols = list(molDict.keys())
    volume = 0
    for mol in mols:
        volume = volume + volumeSet(mol, molDict[mol], density)
    volume = volume / 1e6
    return volume / 1e-30

def sphereRadius(volume):
    return ((3 * volume) / (4 * PI)) ** (1/3)

def cubicSide(volume):
    return volume ** (1/3)

if __name__ == "__main__":
    molDict = getValues()
    volume = calcVol(molDict)
    print("The volume required for mixing with this configuration is " + str(round(volume, 3)) + " cubic Ångström")
    print("Its box can be spherical, with a radius equal to " + str(round(sphereRadius(volume), 3)) + " Ångström")
    print("Your box can be cubic, with an edge equal to " + str(round(cubicSide(volume), 3)) + " Ångström")


    
