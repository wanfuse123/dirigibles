# Ideal gas law: PV = nRT
avogadro = 6.022140857e23

# Gas Constant. Botlzman times Avogadro
R = 8.3144598

# "Find volume of gas given `n` moles of substance at temperature `T` kelvin at pressure `P`"
def gas_volume(n, T, P):
    return n*R*T/P


def moles(totalmass, molecular):
    return totalmass/molecular

# "Find number of moles of a gas with pressure `P`, Volume `V` and `T` kelvin in temperature."
def gas_moles(P, V, T):
    return (P*V)/(R*T)


"""
Mass in grams of a gass of volume `V` temperature `celsius`, pressure `P` and mass
of each molecule of gass is `molecular_mass`
"""
def gas_mass(P, V, T, molecular_mass):
    return gas_moles(P, V, T) * molecular_mass

def pascal(bar):
    return bar*1e5

def bar(pascal):
    return pascal/1e5