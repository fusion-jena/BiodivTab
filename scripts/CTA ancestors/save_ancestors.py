from os.path import join, realpath, exists
import json
from inc.query import runQuerySingleKey
import inc.cache

# init caches
cacheTypes1 = inc.cache.Cache('tmpTypes1', ['base'])
cacheTypes2 = inc.cache.Cache('tmpTypes2', ['base'])
cacheTypes3 = inc.cache.Cache('tmpTypes3', ['base'])

async def check_consisitant(my_dict, values):
    keys = list(my_dict.keys())
    for item in values:
        if "https://www.wikidata.org/wiki/"+item not in keys:
            raise Exception("Not consistent")


async def save_cta_types():
    with open(join(realpath('.'), 'CTA_biodivtab_WD_gt_ancestor_TEMPLATE.json'), 'r') as file:
        cta_dict = json.load(file)

    entities = list(cta_dict.keys())

    # weight 1
    res = await runQuerySingleKey(cacheTypes1, entities, """
          SELECT DISTINCT ?base ?type
          WHERE
          {
            {
              VALUES ?base { %s } .
              { ?base wdt:P31 ?type. } #  direct instanceOf P31 (most fine-grained type)             
            }
          }
        """, printIt=False)

    await check_consisitant(cta_dict, list(res.keys()))

    for base, types in res.items():
        for type in types:
            cta_dict["https://www.wikidata.org/wiki/"+base].update({'https://www.wikidata.org/wiki/'+type['type']: "1"})

    # weight 2
    res = await runQuerySingleKey(cacheTypes2, entities, """
          SELECT DISTINCT ?base ?type
          WHERE
          {
            {
              VALUES ?base { %s } .
              { 
                ?base wdt:P31 ?x. 
                ?x wdt:P279 ?type. 
              }   
              UNION
              { ?base wdt:P279 ?type .} # if base is a class then retrieves its parent directly P279           
            }
          }
        """, printIt=False)

    await check_consisitant(cta_dict, list(res.keys()))


    for base, types in res.items():
        for type in types:
            if 'https://www.wikidata.org/wiki/'+type['type'] not in cta_dict["https://www.wikidata.org/wiki/"+base]:
                cta_dict["https://www.wikidata.org/wiki/"+base].update({'https://www.wikidata.org/wiki/'+type['type']: "2"})

    # weight 3
    res = await runQuerySingleKey(cacheTypes3, entities, """
          SELECT DISTINCT ?base ?type
          WHERE
          {
            {
              VALUES ?base { %s } .
              { 
                ?base wdt:P31 ?x. 
                ?x wdt:P279 ?y. 
                ?x wdt:P279 ?type. 
              }   
              UNION
              { 
                ?base wdt:P279 ?x .
                ?x wdt:P279 ?type .
              }    
            }
          }
        """, printIt=False)

    await check_consisitant(cta_dict, list(res.keys()))

    for base, types in res.items():
        for type in types:
            if 'https://www.wikidata.org/wiki/' + type['type'] not in cta_dict["https://www.wikidata.org/wiki/" + base]:
                cta_dict["https://www.wikidata.org/wiki/" + base].update(
                    {'https://www.wikidata.org/wiki/' + type['type']: "3"})


    # Append Taxon to superkingdom,kingdom,domain
    # species
    # phylum
    # family
    # order
    # class
    # genus
    biodiv_keys = ["https://www.wikidata.org/wiki/Q19858692", "https://www.wikidata.org/wiki/Q36732",
                   "https://www.wikidata.org/wiki/Q146481","https://www.wikidata.org/wiki/Q7432",
                   "https://www.wikidata.org/wiki/Q38348", "https://www.wikidata.org/wiki/Q35409",
                   "https://www.wikidata.org/wiki/Q36602", "https://www.wikidata.org/wiki/Q37517",
                   "https://www.wikidata.org/wiki/Q34740"]
    for biodiv_k in biodiv_keys:
        # taxon
        cta_dict[biodiv_k].update({"https://www.wikidata.org/wiki/Q16521":"2"})

        # living organism class
        cta_dict[biodiv_k].update({"https://www.wikidata.org/wiki/Q21871294": "3"})

    with open(join(realpath('.'), 'CTA_biodivtab_WD_gt_ancestor.json'), 'w') as file:
        json.dump(cta_dict, file, indent=6)

