import json
import statistics

b_dataset = '/Users/sergiofu/Desktop/Epicode/Python/dataset/owid-covid-data.json'

def read_json(file_path):
    """
    Legge un file JSON e inserisce i dati in un dizionario
    :param file_path: file path of json
    :return: data read from file
    """
    with open(b_dataset, 'r') as json_file:
        data = json.load(json_file)
    return data

data_1 = read_json(b_dataset)

#ISPEZIONE DEL DATASET

"""print(type(data_1)) #Verifico il tipo di file (JSON)


for k in data_1.keys(): #Individuo le chiavi del primo dizionario (contiene il codice di ogni paese del dataset)
    print(k)
    
    
for k in data_1['MEX'].keys():  #Accedo alla prima chiave per prima esplorazione
    print(k)

print(data_1['MEX']["continent"]) #Accedo alla seconda chiave di mio interesse per ulteriore esplorazione
print(data_1['MEX']["population_density"])

print(data_1['PER']["data"])

print(type(data_1['PER']['data']))  #5) La chiave "data" contiene una lista di dizionario relativi ad un giorno settimanale con associata una chiave (new cases). Esploro la lista


for elem in range(100,104):
    print(data_1['PER']['data'][elem])"""

somma = 0
for i in range(0,len(data_1['PER']['data'])):
    somma = somma + (data_1['PER']['data'][i].get('new_cases', 0))
media_1 = somma / len(data_1['PER']['data'])
print("Il numero totale dei casi è:",somma)


"""list_utility = []
for i in range(0,len(data_1['PER']['data'])):
    if (data_1['PER']['data'][i].get('new_cases', None)) != None:   #creo una lista che conterrà i parametri utili da calcolare, eliminando i campi vuoti assegnando il valore "NONE"
        list_utility.append(data_1['PER']['data'][i].get('new_cases'))
print(list_utility)"""


def media_location(loc,parametro):
    list_m= []
    for i in range(0,len(data_1[loc]['data'])):
        if (data_1[loc]['data'][i].get(parametro, None)) != None:  #definisco una funziona media per paese
            list_m.append(data_1[loc]['data'][i].get(parametro))
    media = statistics.mean(list_m)
    return media
    

loc = 'PER'
parametro = 'new_cases'
media = media_location(loc,parametro)
print("la media dei nuovi casi del Perù è:",media) 

"""paese = 'MEX'
parametro = 'new_cases'
media = media_location(loc,parametro)
print(media)"""


"""
def media_continente(m_continent,parametro_mc):
    list_2 = []
    for i in data_1:
        if data_1[i].get('continent', 'errore') == m_continent:
            for g in range(0, len(data_1[i]['data'])):                        #definisco una funziona media per continente
                if (data_1[i]['data'][g].get(parametro_mc, None)) != None:
                    list_2.append(data_1[i]['data'][g].get(parametro_mc))
    media = statistics.mean(list_2)
    return media
"""

"""
m_continente = 'North_America'
parametro_mc = 'new_cases'
media_c = media_continente(m_continente,parametro_mc)
print('North_America:', media_c)

m_continente = 'South_America'
parametro_mc = 'new_cases'
media_c = media_continente(m_continente,parametro_mc)
print('South_America:', media_c)
"""