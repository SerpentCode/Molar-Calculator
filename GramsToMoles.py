x = int(input("Amount of material: "))
y = input("(M)ole or (G)ram: ")
v = int(input("How many molecules are there in the atom: "))
elements = { 
    "H" : 1.0079,
    "He" : 4.0026,
    "Li" : 6.941,
    "Be" : 9.0122,
    "B" : 10.811,
    "C" : 12.011,
    "N" : 14.0067,
    "O" : 15.9994,
    "F" : 18.9984,
    "Ne" : 20.1797,
    "Na" : 22.9898,
    "Mg" : 24.3050,
    "Al" : 26.9815,
    "Si" : 28.0855,
    "P" : 30.9738,
    "Cl" : 25.4527,
    "Ar" : 39.948,
    "K" : 39.098,
    "Ca" : 40.078,
    "Sc" : 44.9559,
    "Ti" : 47.88,
    "V" : 50.9415,
    "Cr" : 51.9961,
    "Mn" : 54.9380,
    "Fe" : 55.847,
    "Co" : 58.9332,
    "Ni" : 58.6934,
    "Cu" : 63.546,
    "Zn" : 65.39,
    "Ga" : 69.723,
    "Ge" : 72.61,
    "As" : 74.9216,
    "Ge" : 72.61,
    "Se" : 78.96,
    "Br" : 79.904,
    "Kr" : 83.80,
    "Rb" : 85.468,
    "Sr" : 87.62,
    "Y" : 88.9059,
    "Zr" : 91.224,
    "Nb" : 92.9064,
    "Mo" : 95.94,
    "Tc" : 98.9072,
    "Ru" : 101.07,
    "Rh" : 102.9055,
    "Pd" : 106.42,
    "Ag" : 107.8682,
    "Cd" : 112.411,
    "In" : 114.82,
    "Sn" : 118.710,
    "Sb" : 121.76,
    "Te" : 127.60,
    "I" : 126.0945,
    "Xe" : 131.29,
    "Cs" : 132.905,
    "Ba" : 137.327,
}

if v == 1:
    atom1 = input("Enter in atom 1: ")
    z = elements[atom1]
elif v == 2:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    z = elements[atom1] + elements[atom2]
elif v == 3:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    z = elements[atom1] + elements[atom2] + elements[atom3]
elif v == 4:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4]
elif v == 5:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5]
elif v == 6:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6]
elif v == 7:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7]
elif v == 8:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8]
elif v == 9:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    atom9 = input("Enter in atom 9: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8] + elements[atom9]
elif v == 10:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    atom9 = input("Enter in atom 9: ")
    atom10 = input("Enter in atom 10: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8] + elements[atom9] + elements[atom10]
elif v == 11:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    atom9 = input("Enter in atom 9: ")
    atom10 = input("Enter in atom 10: ")
    atom11 = input("Enter in atom 11: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8] + elements[atom9] + elements[atom10] + elements[atom11]
elif v == 12:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    atom9 = input("Enter in atom 9: ")
    atom10 = input("Enter in atom 10: ")
    atom11 = input("Enter in atom 11: ")
    atom12 = input("Enter in atom 12: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8] + elements[atom9] + elements[atom10] + elements[atom11] + elements[atom12]
elif v == 13:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    atom9 = input("Enter in atom 9: ")
    atom10 = input("Enter in atom 10: ")
    atom11 = input("Enter in atom 11: ")
    atom12 = input("Enter in atom 12: ")
    atom13 = input("Enter in atom 13: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8] + elements[atom9] + elements[atom10] + elements[atom11] + elements[atom12] + elements[atom13]
elif v == 14:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    atom9 = input("Enter in atom 9: ")
    atom10 = input("Enter in atom 10: ")
    atom11 = input("Enter in atom 11: ")
    atom12 = input("Enter in atom 12: ")
    atom13 = input("Enter in atom 13: ")
    atom14 = input("Enter in atom 14: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8] + elements[atom9] + elements[atom10] + elements[atom11] + elements[atom12] + elements[atom13] + elements[atom14]
elif v == 15:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    atom9 = input("Enter in atom 9: ")
    atom10 = input("Enter in atom 10: ")
    atom11 = input("Enter in atom 11: ")
    atom12 = input("Enter in atom 12: ")
    atom13 = input("Enter in atom 13: ")
    atom14 = input("Enter in atom 14: ")
    atom15 = input("Enter in atom 15: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8] + elements[atom9] + elements[atom10] + elements[atom11] + elements[atom12] + elements[atom13] + elements[atom14] + elements[atom15]
elif v == 16:
    atom1 = input("Enter in atom 1: ")
    atom2 = input("Enter in atom 2: ")
    atom3 = input("Enter in atom 3: ")
    atom4 = input("Enter in atom 4: ")
    atom5 = input("Enter in atom 5: ")
    atom6 = input("Enter in atom 6: ")
    atom7 = input("Enter in atom 7: ")
    atom8 = input("Enter in atom 8: ")
    atom9 = input("Enter in atom 9: ")
    atom10 = input("Enter in atom 10: ")
    atom11 = input("Enter in atom 11: ")
    atom12 = input("Enter in atom 12: ")
    atom13 = input("Enter in atom 13: ")
    atom14 = input("Enter in atom 14: ")
    atom15 = input("Enter in atom 15: ")
    atom16 = input("Enter in atom 16: ")
    z = elements[atom1] + elements[atom2] + elements[atom3] + elements[atom4] + elements[atom5] + elements[atom6] + elements[atom7] +elements[atom8] + elements[atom9] + elements[atom10] + elements[atom11] + elements[atom12] + elements[atom13] + elements[atom14] + elements[atom15] + elements[atom16]


if y.upper() == "G":
    conversion = x / z
    print("Weight in Moles: ", str(conversion))
else:
    conversion = x * z
    print("Wieght in Grams: ", str(conversion))
