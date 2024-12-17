varosok = ["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]

varos = input("Kérem, adjon meg egy városnevet: ")


if varos in varosok:
    utana_levo_varos = varosok.index(varos)
    if utana_levo_varos + 1 < len(varosok):
        print(f"A következő város:  {varosok[utana_levo_varos + 1]}")
    else:
        print("Ez az utolsó város a listában, nincs következő város.")
if varos not in varosok:
    varosok.append(varos)    

