from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS

g = Graph()
g.parse('https://www.wikidata.org/wiki/Special:EntityData/Q2831.ttl')

print(f'GRAPH LENGTH: {len(g)}')
