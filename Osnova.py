# Naučili se bomo osnov v pythonu

#---------------------------------------------------------------------------------------------------------------------------
# 1.) 
# Prva najbolj prepoznavna osnova je osnova PRINT , s to kodo bomo lahko na zaslonu prikazali kar smo zapisali v vrstici print.
print("Pozdravljen")

# Rezultat je viden v terminalu
#---------------------------------------------------------------------------------------------------------------------------

# Ločimo en primer od drugega z kodo PRINT(), ali pa z kakšni črticami, to je seveda odvisno od naše želje
print("-------------------------------------------")

#---------------------------------------------------------------------------------------------------------------------------
# 2.)
# Koda INPUT, je namenjena izpisu podatkov, kakor koda print, le da nam ta koda omagoča še v terminalu vpisovanje podatkov.
input("Kako ti je ime? ")
#---------------------------------------------------------------------------------------------------------------------------
print("-------------------------------------------")
#---------------------------------------------------------------------------------------------------------------------------
# 3.)
# Koda IF, je namenjena če je pravilno,potem..., to kombiniramo z ostalimi kodami. Še prej moramo kodo INPUT poimnenovati, 
# da bo program lahko vedel na kaj se vzirati.
print("Pozdravljen ")
ime= input("Kako ti je ime? (PREVERJANJE IMENA) ") 
if ime=="Primož":
    print("Sprejeto! ")
else:
    print("Zavrnjeno")

#---------------------------------------------------------------------------------------------------------------------------
print("-------------------------------------------")