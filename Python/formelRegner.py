# Dictionary over alle formler
from webbrowser import get


formulas = {
    'A':'l*l',
    'V':'l*l*l',
    'rho':'m/V',
    'l':'',
    't':'',
    'F':'',
    'rho_gas':'(M/R)*(p/T)',
    'E':'',
    'E_Foton':'h*f',
    'f':'c/λ',
    'T':'',
    'λ':'c*f',
    'Q':'',
    'P':'E/t',
    'U':'E/Q',
    'I':'Q/t',
    'Pascal':'F/A',
    'F_op':'P_Væske*V_Genstand*g',
    'h':'',
    'c':'',
    'm':'n*M',
    'n':'m/M',
    'M':'m/n',
    'F_t':'m*g',
    'g':'',
    'specifik varmekapacitet':'c*m*ΔT',
    'L_s':'Q/m',
    'L_f':'Q/m',
    'eta':'E_Udnyttet/E_Tilført',
    'U':'I*R'
}

def ConvertFormulaToSymbols(formular):
    convertedFormular = formular.split('/')
    convertedFormular += formular.split('*')
    return convertedFormular

def FindMissingValues(formular, arrGivenValues):
    missingValues = []
    convertedFormula = ConvertFormulaToSymbols(formular)
    for symbol in convertedFormula:
        if symbol in formulas and missingValues.count(symbol) == 0 and arrGivenValues.count(symbol) == 0:
            missingValues.append(symbol)
    return missingValues    

knownValues = []
neededValues = []

givenValues = input('Hvilke værdier har du? (Separer med mellemrum)')
knownValues = givenValues.split()
neededValues.append(input('Hvilken værdi skal du bruge?'))

neededFormulas = []
for neededValue in neededValues:
    currentFormula = formulas.get(neededValue)
    neededFormulas.append(currentFormula)
    currentNeededValues = FindMissingValues(currentFormula, knownValues)
    if not currentNeededValues:
        knownValues.append(neededValue)
        neededValues.remove(neededValue)
    else:
        for currentNeededValue in currentNeededValues:
            neededValues.append(currentNeededValue)

print(neededFormulas)