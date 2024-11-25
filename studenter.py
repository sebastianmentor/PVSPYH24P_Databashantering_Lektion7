import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

collections = mydb['studenter']


def lägg_till_student():
    namn = input('Ange namn: ')
    ålder = int(input('Ange ålder: '))
    utbildning = input('Ange utbildning: ')
    ämnen = input('Ange ämnen som ska läsas: ').split()

    ny_student = {f'name':namn,
                  'age':ålder,
                  'education':utbildning,
                  'courses':ämnen}
    
    resultat = collections.insert_one(ny_student)
    print(f'Ny student tillagd med id {resultat.inserted_id}')


def uppdatera_student():
    namn = input("Ange id: ")

    s = collections.find_one({'name':namn})
    if s:
        lägg_till_kurser = input("Vill du lägga till kurser?(y/n)")
        if lägg_till_kurser == 'y':        
            print('Nuvarande ämnen:')
            for ämne in s['courses']:
                print(ämne)
            while True:
                ny_kurs = input('Ange ny kurs eller q för att avsluta: ')
                if ny_kurs == 'q': break
                
                s['courses'].append(ny_kurs)
            
            collections.update_one({'name':namn},
                                   {'$set':{'courses': s['courses']}})


def visa_alla_studenter():
    for student in collections.find():
        print(f"{student['_id']}")
        print(f'{student['name']} är {student['age']} gammal och läser utbildningen {student['education']}')
        if student['courses']:
            print('Kurser som ska läsas är:')
            for kurs in student['courses']:
                print(f"\t{kurs}")


while True:
    print("1. Lägg till Student")
    print("2. Uppdatera Student")
    print("3. Visa alla Studenter")
    print("0. Avlsuta")

    meny_val = input('Ange val: ')

    match meny_val:
        case '1': lägg_till_student()
        case '2': uppdatera_student()
        case '3': visa_alla_studenter()
        case '0': break
        case _: print('Ogiltligt val!')