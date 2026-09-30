# PalmerPenguinsM2.py
# J. Andrew Yurick
# September 30, 2026
# Calculates and displays Palmer Penguin statistics.

# import modules
import math

# constants representing the species and count
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"
NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151
TOTAL_SPECIES = 3

# calculate dataset statistics
total_penguins = NUM_CHINSTRAP + NUM_GENTOO + NUM_ADELIE
average_penguins = total_penguins / TOTAL_SPECIES
chinstrap_percent = (NUM_CHINSTRAP / total_penguins) * 100
gentoo_percent = (NUM_GENTOO / total_penguins) * 100
adelie_percent = (NUM_ADELIE / total_penguins) * 100
average_penguins_rounded_up = math.ceil(average_penguins)

# output the species names with introductory text
print("Introducing the Palmer Penguins:")
print()
print("\t" + SP_CHINSTRAP + "!")
print("\t" + SP_GENTOO + "!")
print("and last but not least...")
print("\t" + SP_ADELIE + "!")
print()

# output dataset statistics
print("There are a total of " + str(TOTAL_SPECIES) +
      " penguin species in this dataset.")
print("There are a total of " + str(total_penguins) +
      " penguins in the dataset.")
print("The average number of penguins per species is " +
      str(average_penguins) + ".")
print("The average rounded up is " +
      str(average_penguins_rounded_up) + " penguins.")
print()

# output count and percentage for each species
print(SP_CHINSTRAP + ": " + str(NUM_CHINSTRAP) + 
      " (" + str(chinstrap_percent) + "%)") 
print(SP_GENTOO + ": " + str(NUM_GENTOO) + 
      " (" + str(gentoo_percent) + "%)") 
print(SP_ADELIE + ": " + str(NUM_ADELIE) + 
      " (" + str(adelie_percent) + "%)") 

