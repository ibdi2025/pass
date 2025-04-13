Cielom projektu 'Pass' je Python program na vytvaranie uzivatelskych uctov a ich zapisovanie do suboru 'pass.txt'. 
Program bude vo finlnej verzii poskytovat nasledovne funkcionality:

(parrent class)
- vytvorenie alebo otvorenie suboru (def)
- vstup uzivatelskeho mena (def)
- kontrola uzivatelskeho mena oproti suboru - databaze uzivatelov/hashov (def)
    - ak uzivatel existuje, program sa ukonci
- vstup uzivatelskeho hesla
- vytvorenie hashu hesla (def->child class->return to parrent class)
- zapis mena a hashu do suboru - databazy uzivatelov/hashov (def)
- kontrola uzivatelskeho hesla/hashu (def->child class->return to parrent class)
- nasledna akcia ak je sa heslo/hash zhoduje