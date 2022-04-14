import json
from os.path import join, realpath

if __name__ == '__main__':
    gt = join(realpath('.'), 'gt', 'CTA_biodivtab_2021_WD_gt_ancestor.json')
    with open(gt, 'r', encoding='utf-8') as file:
        json_obj = json.load(file)

    for k, v in json_obj.items():
        # rename keys
        new_key = k.replace('https://www.wikidata.org/wiki/', 'https://www.wikidata.org/entity/')
        json_obj[new_key] =  json_obj.pop(k)
        # rename nested keys
        for nested_k, nested_v in v.items():
            new_nested_k = nested_k.replace('https://www.wikidata.org/wiki/', 'https://www.wikidata.org/entity/')
            v[new_nested_k] = v.pop(nested_k)

    for k, v in json_obj.items():
        print(k)
        print(v)
    with open('new_ancestors.json', 'w', encoding='utf-8') as file:
        json.dump(json_obj,file, indent=4)