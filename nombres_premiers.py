from math import*

repeter=1
combien=0
for z in range (0, 100):
    seul_ou_suite=int(input('veux tu savoir si un nombre ou une suite de nombres sont premiers ? (répondre 1 ou 2) '))
    if seul_ou_suite==2:

        nombre_a_tester=int(input("entrez le premier nombre de la suite "))
        j_usqu_a=int(input("entrez le dernier nombre de la suite "))

        nombres_premiers=[]

        for y in range (nombre_a_tester, j_usqu_a):
            nombre_a_tester=nombre_a_tester+1
            racine=(sqrt(nombre_a_tester))
            racine = floor(racine)
            test=1
            les_restes=[]
        
            for x in range (0, racine):
                test=test+1
                reste=nombre_a_tester%test
                #print (reste)
                if reste==0:
                    break
                les_restes.extend([reste])

            if len(les_restes)==racine:
                nombres_premiers.extend([nombre_a_tester])
                #print(nombre_a_tester)   sert à écrire chaque nombre premier après le test, mais ralenti le programme
                combien=combien+1

            if combien==1000:
                print(nombre_a_tester)
                combien=0
                
        premier='ta suite de nombre contient les nombres premiers %s'
        if nombres_premiers==[]:
            print("ta suite de nombres ne contient pas de nombres premiers" )
        else:
            print (premier % nombres_premiers)

    test=0
    if seul_ou_suite==1:
        nombre_a_tester=int(input("entrez le nombre à tester "))
        nombres_premiers=[]

        racine=(sqrt(nombre_a_tester))
        racine = floor(racine)
        test=1
        les_restes=[]
        
        for x in range (0, racine):
            test=test+1
            reste=nombre_a_tester%test
            if reste==0:
                break
            les_restes.extend([reste])

        if len(les_restes)==racine:
            nombres_premiers.extend([nombre_a_tester])

        pas_premier="le nombre %s n'est pas premier car il est divisible par"
        premier='le nombre %s est premier'
        if nombres_premiers==[]:
            print(pas_premier % nombre_a_tester)
            print(test)
        else:
            print (premier % nombre_a_tester)
    dmd_repeter=int(input('veux tu tester un autre nombre (si oui répondre 1, sinon 2) ? '))
    if dmd_repeter==2:
        break
