#! /bin/python

import requests
import sys
import json
import csv

error = 0

def updateWarframes():
    warframes_data = downloadData("https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Warframes.json")
    if error:
        return

    warframes_file_open = 0
    try:
        warframes_file = open('warframes.csv','r')
        warframes_read=csv.reader(warframes_file)
        warframes=list(warframes_read)
        warframes_file_open=1
    except:
        warframes=[]

    warframes = updateList(warframes_data,warframes)

    if warframes_file_open:
        warframes_file.close()

    warframes_file = open('warframes.csv','w')
    warframes_write = csv.writer(warframes_file)
    warframes_write.writerows(warframes)
    warframes_file.close


def updateSentinels():
    sentinels_data = downloadData(
        "https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Sentinels.json")
    if error:
        return

    sentinels_file_open = 0
    try:
        sentinels_file = open('sentinels.csv', 'r')
        sentinels_read = csv.reader(sentinels_file)
        sentinels = list(sentinels_read)
        sentinels_file_open = 1
    except:
        sentinels = []

    sentinels = updateList(sentinels_data, sentinels)

    if sentinels_file_open:
        sentinels_file.close()

    sentinels_file = open('sentinels.csv', 'w')
    sentinels_write = csv.writer(sentinels_file)
    sentinels_write.writerows(sentinels)
    sentinels_file.close


def updateSecondaries():
    secondaries_data = downloadData(
        "https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Secondary.json")
    if error:
        return

    secondaries_file_open = 0
    try:
        secondaries_file = open('secondaries.csv', 'r')
        secondaries_read = csv.reader(secondaries_file)
        secondaries = list(secondaries_read)
        secondaries_file_open = 1
    except:
        secondaries = []

    secondaries = updateList(secondaries_data, secondaries)

    if secondaries_file_open:
        secondaries_file.close()

    secondaries_file = open('secondaries.csv', 'w')
    secondaries_write = csv.writer(secondaries_file)
    secondaries_write.writerows(secondaries)
    secondaries_file.close()


def updatePrimaries():
    primaries_data = downloadData(
        "https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Primary.json")
    if error:
        return

    primaries_file_open = 0
    try:
        primaries_file = open('primaries.csv', 'r')
        primaries_read = csv.reader(primaries_file)
        primaries = list(primaries_read)
        primaries_file_open = 1
    except:
        primaries = []

    primaries = updateList(primaries_data, primaries)

    if primaries_file_open:
        primaries_file.close()

    primaries_file = open('primaries.csv', 'w')
    primaries_write = csv.writer(primaries_file)
    primaries_write.writerows(primaries)
    primaries_file.close()


def updatePets():
    pets_data = downloadData(
        "https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Pets.json")
    if error:
        return

    pets_file_open = 0
    try:
        pets_file = open('pets.csv', 'r')
        pets_read = csv.reader(pets_file)
        pets = list(pets_read)
        pets_file_open = 1
    except:
        pets = []

    pets = updateList(pets_data, pets)

    if pets_file_open:
        pets_file.close()

    pets_file = open('pets.csv', 'w')
    pets_write = csv.writer(pets_file)
    pets_write.writerows(pets)
    pets_file.close()


def updateMelees():
    melees_data = downloadData(
        "https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Melee.json")
    if error:
        return

    melees_file_open = 0
    try:
        melees_file = open('melees.csv', 'r')
        melees_read = csv.reader(melees_file)
        melees = list(melees_read)
        melees_file_open = 1
    except:
        melees = []

    melees = updateList(melees_data, melees)

    if melees_file_open:
        melees_file.close()

    melees_file = open('melees.csv', 'w')
    melees_write = csv.writer(melees_file)
    melees_write.writerows(melees)
    melees_file.close()


def updateArchwings():
    archwings_data = downloadData(
        "https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Archwing.json")
    if error:
        return

    archwings_file_open = 0
    try:
        archwings_file = open('archwings.csv', 'r')
        archwings_read = csv.reader(archwings_file)
        archwings = list(archwings_read)
        archwings_file_open = 1
    except:
        archwings = []

    archwings = updateList(archwings_data, archwings)

    if archwings_file_open:
        archwings_file.close()

    archwings_file = open('archwings.csv', 'w')
    archwings_write = csv.writer(archwings_file)
    archwings_write.writerows(archwings)
    archwings_file.close()


def updateArchwingMelees():
    archwing_melees_data = downloadData(
        "https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Arch-Melee.json")
    if error:
        return

    archwing_melees_file_open = 0
    try:
        archwing_melees_file = open('archwing_melees.csv', 'r')
        archwing_melees_read = csv.reader(archwing_melees_file)
        archwing_melees = list(archwing_melees_read)
        archwing_melees_file_open = 1
    except:
        archwing_melees = []

    archwing_melees = updateList(archwing_melees_data, archwing_melees)

    if archwing_melees_file_open:
        archwing_melees_file.close()

    archwing_melees_file = open('archwing_melees.csv', 'w')
    archwing_melees_write = csv.writer(archwing_melees_file)
    archwing_melees_write.writerows(archwing_melees)
    archwing_melees_file.close()


def updateArchwingGuns():
    archwing_guns_data = downloadData(
        "https://raw.githubusercontent.com/WFCD/warframe-items/development/data/json/Arch-Gun.json")
    if error:
        return

    archwing_guns_file_open = 0
    try:
        archwing_guns_file = open('archwing_guns.csv', 'r')
        archwing_guns_read = csv.reader(archwing_guns_file)
        archwing_guns = list(archwing_guns_read)
        archwing_guns_file_open = 1
    except:
        archwing_guns = []

    archwing_guns = updateList(archwing_guns_data, archwing_guns)

    if archwing_guns_file_open:
        archwing_guns_file.close()

    archwing_guns_file = open('archwing_guns.csv', 'w')
    archwing_guns_write = csv.writer(archwing_guns_file)
    archwing_guns_write.writerows(archwing_guns)
    archwing_guns_file.close()


def update():
    updateWarframes()
    updateArchwingGuns()
    updateArchwingMelees()
    updateArchwings()
    updateMelees()
    updatePets()
    updatePrimaries()
    updateSecondaries()
    updateSentinels()


def add(arguments):
    warframes_file_r = open('warframes.csv', 'r')
    warframes_read = csv.reader(warframes_file_r)
    warframes = list(warframes_read)

    archwing_guns_file_r = open('archwing_guns.csv', 'r')
    archwing_guns_read = csv.reader(archwing_guns_file_r)
    archwing_guns = list(archwing_guns_read)

    archwing_melees_file_r = open('archwing_melees.csv', 'r')
    archwing_melees_read = csv.reader(archwing_melees_file_r)
    archwing_melees = list(archwing_melees_read)

    archwings_file_r = open('archwings.csv', 'r')
    archwings_read = csv.reader(archwings_file_r)
    archwings = list(archwings_read)

    melees_file_r = open('melees.csv', 'r')
    melees_read = csv.reader(melees_file_r)
    melees = list(melees_read)

    pets_file_r = open('pets.csv', 'r')
    pets_read = csv.reader(pets_file_r)
    pets = list(pets_read)

    primaries_file_r = open('primaries.csv', 'r')
    primaries_read = csv.reader(primaries_file_r)
    primaries = list(primaries_read)

    secondaries_file_r = open('secondaries.csv', 'r')
    secondaries_read = csv.reader(secondaries_file_r)
    secondaries = list(secondaries_read)

    sentinels_file_r = open('sentinels.csv', 'r')
    sentinels_read = csv.reader(sentinels_file_r)
    sentinels = list(sentinels_read)

    for i in range(len(arguments)):
        for j in (warframes, archwing_guns, archwing_melees, archwings, melees, pets, primaries, secondaries, sentinels):
            for k in range(len(j)):
                if arguments[i]==j[k][0]:
                    j[k][1]=1
                    break

    warframes_file_w = open('warframes.csv', 'w')
    warframes_write = csv.writer(warframes_file_w)

    archwing_guns_file_w = open('archwing_guns.csv', 'w')
    archwing_guns_write = csv.writer(archwing_guns_file_w)

    archwing_melees_file_w = open('archwing_melees.csv', 'w')
    archwing_melees_write = csv.writer(archwing_melees_file_w)

    archwings_file_w = open('archwings.csv', 'w')
    archwings_write = csv.writer(archwings_file_w)

    melees_file_w = open('melees.csv', 'w')
    melees_write = csv.writer(melees_file_w)

    pets_file_w = open('pets.csv', 'w')
    pets_write = csv.writer(pets_file_w)

    primaries_file_w = open('primaries.csv', 'w')
    primaries_write = csv.writer(primaries_file_w)

    secondaries_file_w = open('secondaries.csv', 'w')
    secondaries_write = csv.writer(secondaries_file_w)

    sentinels_file_w = open('sentinels.csv', 'w')
    sentinels_write = csv.writer(sentinels_file_w)

    warframes_write.writerows(warframes)
    archwing_guns_write.writerows(archwing_guns)
    archwing_melees_write.writerows(archwing_melees)
    archwings_write.writerows(archwings)
    melees_write.writerows(melees)
    pets_write.writerows(pets)
    primaries_write.writerows(primaries)
    secondaries_write.writerows(secondaries)
    sentinels_write.writerows(sentinels)

    warframes_file_w.close()
    archwing_guns_file_w.close()
    archwing_melees_file_w.close()
    archwings_file_w.close()
    melees_file_w.close()
    pets_file_w.close()
    primaries_file_w.close()
    secondaries_file_w.close()
    sentinels_file_w.close()

    warframes_file_r.close()
    archwing_guns_file_r.close()
    archwing_melees_file_r.close()
    archwings_file_r.close()
    melees_file_r.close()
    pets_file_r.close()
    primaries_file_r.close()
    secondaries_file_r.close()
    sentinels_file_r.close()


def delete(arguments):
    warframes_file_r = open('warframes.csv', 'r')
    warframes_read = csv.reader(warframes_file_r)
    warframes = list(warframes_read)

    archwing_guns_file_r = open('archwing_guns.csv', 'r')
    archwing_guns_read = csv.reader(archwing_guns_file_r)
    archwing_guns = list(archwing_guns_read)

    archwing_melees_file_r = open('archwing_melees.csv', 'r')
    archwing_melees_read = csv.reader(archwing_melees_file_r)
    archwing_melees = list(archwing_melees_read)

    archwings_file_r = open('archwings.csv', 'r')
    archwings_read = csv.reader(archwings_file_r)
    archwings = list(archwings_read)

    melees_file_r = open('melees.csv', 'r')
    melees_read = csv.reader(melees_file_r)
    melees = list(melees_read)

    pets_file_r = open('pets.csv', 'r')
    pets_read = csv.reader(pets_file_r)
    pets = list(pets_read)

    primaries_file_r = open('primaries.csv', 'r')
    primaries_read = csv.reader(primaries_file_r)
    primaries = list(primaries_read)

    secondaries_file_r = open('secondaries.csv', 'r')
    secondaries_read = csv.reader(secondaries_file_r)
    secondaries = list(secondaries_read)

    sentinels_file_r = open('sentinels.csv', 'r')
    sentinels_read = csv.reader(sentinels_file_r)
    sentinels = list(sentinels_read)

    for i in range(len(arguments)):
        for j in (warframes, archwing_guns, archwing_melees, archwings, melees, pets, primaries, secondaries, sentinels):
            for k in range(len(j)):
                if arguments[i]==j[k][0]:
                    j[k][1]=0
                    break

    warframes_file_w = open('warframes.csv', 'w')
    warframes_write = csv.writer(warframes_file_w)

    archwing_guns_file_w = open('archwing_guns.csv', 'w')
    archwing_guns_write = csv.writer(archwing_guns_file_w)

    archwing_melees_file_w = open('archwing_melees.csv', 'w')
    archwing_melees_write = csv.writer(archwing_melees_file_w)

    archwings_file_w = open('archwings.csv', 'w')
    archwings_write = csv.writer(archwings_file_w)

    melees_file_w = open('melees.csv', 'w')
    melees_write = csv.writer(melees_file_w)

    pets_file_w = open('pets.csv', 'w')
    pets_write = csv.writer(pets_file_w)

    primaries_file_w = open('primaries.csv', 'w')
    primaries_write = csv.writer(primaries_file_w)

    secondaries_file_w = open('secondaries.csv', 'w')
    secondaries_write = csv.writer(secondaries_file_w)

    sentinels_file_w = open('sentinels.csv', 'w')
    sentinels_write = csv.writer(sentinels_file_w)

    warframes_write.writerows(warframes)
    archwing_guns_write.writerows(archwing_guns)
    archwing_melees_write.writerows(archwing_melees)
    archwings_write.writerows(archwings)
    melees_write.writerows(melees)
    pets_write.writerows(pets)
    primaries_write.writerows(primaries)
    secondaries_write.writerows(secondaries)
    sentinels_write.writerows(sentinels)

    warframes_file_w.close()
    archwing_guns_file_w.close()
    archwing_melees_file_w.close()
    archwings_file_w.close()
    melees_file_w.close()
    pets_file_w.close()
    primaries_file_w.close()
    secondaries_file_w.close()
    sentinels_file_w.close()

    warframes_file_r.close()
    archwing_guns_file_r.close()
    archwing_melees_file_r.close()
    archwings_file_r.close()
    melees_file_r.close()
    pets_file_r.close()
    primaries_file_r.close()
    secondaries_file_r.close()
    sentinels_file_r.close()



# TODO add more functions
# TODO error handling
def parse_arguments():
    # grab arguments from command line
    arguments = sys.argv
    arguments.pop(0)

    if len(arguments) == 0:
        # TODO call help function
        print("TODO")
    else:
        # if arguments begin with not a function then we call the default function
        if not arguments[0][0] == '-':
            function_arguments = []
            # get arguments we need to pass to default function
            for i in range(len(arguments)):
                if arguments[i][0] == '-':
                    break
                function_arguments.append(arguments[i])
                # TODO call default action aka add
        # scan through arguments searching for functions
        for i in range(len(arguments)):
            global error
            if error:
                break
            if arguments[i][0] == '-':
                function_arguments = []
                # get arguments we need to pass to function
                for j in range(i + 1, len(arguments)):
                    if arguments[j][0] == '-':
                        break
                    function_arguments.append(arguments[j])
                # call functions
                if arguments[i] == "-u" or arguments[i] == "--update":
                    if len(function_arguments):
                        print("Update function doesn't accept any arguments, aborting")
                        error = 1
                        break
                    update()
                elif arguments[i] == "-a" or arguments[i] == "--add":
                    if not len(function_arguments):
                        print("No arguments provided, aborting")
                        error = 1
                        break
                    add(function_arguments)
                elif arguments[i] == "-d" or arguments[i] == "--delete":
                    if not len(function_arguments):
                        print("No arguments provided, aborting")
                        error = 1
                        break
                    delete(function_arguments)
                else:
                    print("Invalid function, aborting")
                    error = 1


def downloadData(url):
    try:
        data = requests.get(url)
        return json.loads(data.text)
    except:
        print("Cannot access remote data, Aborting.")
        global error
        error = 1
        return []


def updateList(data,list):
    for i in range(len(data)):
        if len(list)>i:
            if not list[i][0]==data[i]['name']:
                list.insert(i,[data[i]['name'],0])
        else:
            list.append([data[i]['name'],0])
    return list



parse_arguments()
