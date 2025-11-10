import json
import os
##This script creates a dictionary that maps continents to the SWORD reach IDs for each continent.
## and saves it to a json file
path_sword = '../assets/SWORD_v16_shp/shp'
save_path = '../assets/supporting_data/sword_continents.json'
dict_sword_continents = {"AF": [], "AS": [], "EU": [], "NA": [], "SA": [], "OC": []}
#populate dictionary with sword reach ids
for continent in dict_sword_continents.keys():
    sword_folder = os.path.join(path_sword, continent)
    list_files_sword_folder = os.listdir(sword_folder)
    print(list_files_sword_folder)
    list_pfaf_ids = set([])
    for file in list_files_sword_folder:
        if file.endswith('shp'):
            pfaf_id = file.split('_v16')[0][-2:]
            list_pfaf_ids.add(pfaf_id)
    dict_sword_continents[continent] = list(list_pfaf_ids)

#save the dictionary to a file

with open(save_path, 'w') as f:
    json.dump(dict_sword_continents, f) 