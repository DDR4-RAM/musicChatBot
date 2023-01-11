from owlready2 import *

keyword_list = ['musica', ' cancion', 'artista', 'ritmo', 'melodia', 'album', 'letra', 'instrumentos', 'notas',
                'genero', "musica clasica", "jazz", "Blues", "gospel", "soul", "pop", "rock and roll", "country",
                "disco", "techno", "reggae", "salsa", "flamenco", "ranchera", "hip hop/rap", "reggaeton", "metal",
                "funk", "bossa nova", "musica melodica", "rock", "michael jackson", "canciones", "obras", "chopin", 
                "tonos", "continuos", "platillos", "tonos", "compases", "amalgama"]

onto = get_ontology("http://localhost:3030/MusicBot").load()

# SIN INFERENCIA

queryConcepts     = '''SELECT ?class WHERE { ?class a owl:Class }'''
queryCompositions = '''SELECT ?song WHERE { ?song a <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#ComposicionMusical> }'''
queryProperties   = '''SELECT ?property WHERE { ?property rdfs:domain <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#ComposicionMusical> }'''
querySubclasses   = '''SELECT ?subclass WHERE {?subclass rdfs:subClassOf <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#ComposicionMusical> }'''

queryCompNames = '''SELECT ?name WHERE {
  ?individual rdf:type <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#ComposicionMusical> 
  ?individual <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#Nombre> ?name .
  }
'''
queryIndividuals = '''SELECT ?name WHERE {
  ?individual <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#Nombre> ?name .
  }
'''
queryMJSongs = '''SELECT ?name WHERE {
  ?individual rdf:type <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#ComposicionMusical>
  ?individual <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#compuestaPor> <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#MichealJackson>
  ?individual <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#Nombre> ?name .
  }
'''
queryMJWorks = '''SELECT ?name WHERE {
  ?individual <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#compuestaPor> <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#MichealJackson>
  ?individual <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#Nombre> ?name .
  }
'''
queryChopin = '''SELECT ?name WHERE {
  ?individual <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#compuestaPor> <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#Chopin> .
  ?individual <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#Nombre> ?name .
  }
'''

# INFERENCIA

queryCTRelatedIndividuals = '''SELECT ?individuo WHERE { <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#TonoContinuo> ?propiedad ?individuo .}'''
queryClasicRelatedIndividuals = '''SELECT ?individuo WHERE { <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#Clasica> ?propiedad ?individuo .}'''
queryPlatillosRelatedIndividuals = '''SELECT ?individuo WHERE { <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#Platillos> ?propiedad ?individuo .}'''
queryAlternedToneRelatedIndividuals = '''SELECT ?individuo WHERE { <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#TonoAlterno> ?propiedad ?individuo .}'''
queryAmalgamaCompassesRelatedIndividuals = '''SELECT ?individuo WHERE { <http://www.semanticweb.org/charl/ontologies/2023/0/music_onto#CompasesAmalgama> ?propiedad ?individuo .}'''

def getAnswer(header, query):
    buffer = header
    for data_set in default_world.sparql(query):
        if hasattr(data_set[0], 'name'):
            buffer += data_set[0].name + ", "
        else:
            buffer += str(data_set[0]) + ", "
    buffer = buffer[:-2] + "."
    return buffer          

# print("Individuos:")
# for individual in default_world.sparql(queryIndividuals):
#     print(individual[0])

# print("\nCanciones de Michael Jackson:")
# for song in default_world.sparql(queryMJSongs):
#     print(song[0])

# print("\nObras de Michael Jackson:")
# for songs in default_world.sparql(queryMJWorks):
#     print(songs[0])

# print("\nCanciones de Chopin:")
# for songs in default_world.sparql(queryChopin):
#     print(songs[0])

# print("\nCompos Nombre:")
# for comp_name in default_world.sparql(queryCompNames):
#     print(comp_name[0])

# print("\nConceptos:")
# for concept in default_world.sparql(queryConcepts):
#     print(concept[0].name)

# print("\nCompos:")
# for composition in default_world.sparql(queryCompositions):
#     print(composition[0].name)

# print("\nPropiedades:")
# for prop in default_world.sparql(queryProperties):
#     print(prop[0].name)

# print("\nSubclasess:")
# for composiciones in default_world.sparql(querySubclasses):
#     print(composiciones[0].name)


def check_onthology(input_user):
    print(input_user)
    match = [word for word in keyword_list if word in input_user]
    if match:
        match = match[0]
        response = ""
        print('[O] Guide User')
        print(f"[I] Check Onthology: {input_user}")

        onto = get_ontology("http://localhost:3030/MusicBot").load()

        if input_user == "que canciones conoces?":
            response = getAnswer("Las canciones que conozco son: ",queryCompNames)
        elif input_user == "que canciones conoces de michael jackson?":
            response = getAnswer("Las canciones que conozco de Michael Jackson son: ",queryMJSongs)
        elif input_user == "que obras conoces de michael jackson?":
            response = getAnswer("Las obras que conozco son: ",queryMJWorks)
        elif input_user == "que sabes de musica?":
            response = getAnswer("Sé sobre los siguientes temas sobre música: ", queryIndividuals)
        elif match == "chopin":
            response = getAnswer("Aquí tienes algunas obras de Chopin: ", queryChopin)
        elif input_user == "que conceptos hay en musica?":
            response = getAnswer("Puedes aprender algo sobre los siguientes conceptos: ", queryConcepts)
        elif input_user == "que conceptos de canciones conoces?":
            response = getAnswer("Conozco los siguientes conceptos de canciones: ", queryCompositions)
        elif input_user == "que datos sobre la musica puedo encontrar?":
            response = getAnswer("Puedes encontrar las siguientes propiedades: ", queryProperties)
        elif input_user == "que subclasificaciones puedo encontrar en la musica?":
            response = getAnswer("Las subclasificaciones que tengo en música son: ", querySubclasses)
        elif input_user == "con que se relacionan los tonos continuos?":
            sync_reasoner()
            response = getAnswer("Aquí tienes algunas relacionees de los tonos continuos: ", queryCTRelatedIndividuals)
        elif input_user == "con que se relaciona la musica clasica?":
            sync_reasoner()
            response = getAnswer("La música se relaciona con los siguientes conceptos: ", queryClasicRelatedIndividuals)
        elif input_user == "con que se relacionan los platillos de bateria?":
            sync_reasoner()
            response = getAnswer("Los platillos de batería se relacionan con los siguientes conceptos: ", queryPlatillosRelatedIndividuals)
        elif input_user == "con que se relacionan los tonos alternos?":
            sync_reasoner()
            response = getAnswer("Aquí tienes algunas relaciones de los tonos alternos: ", queryAlternedToneRelatedIndividuals)
        elif input_user == "con que se relacionan los compases amalgama?":
            sync_reasoner()
            response = getAnswer("Los compases amalgama se relacionan con los siguientes conceptos: ", queryAmalgamaCompassesRelatedIndividuals)
        else:
            return None
        
        print(f'''[Response] {response}''')
        print(input_user.split(" "))
        return response
    else:
        return None
