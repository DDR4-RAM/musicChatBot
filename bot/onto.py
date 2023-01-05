from owlready2 import *

keyword_list = ['musica', ' cancion', 'artista', 'ritmo', 'melodia', 'album', 'letra', 'instrumentos', 'notas',
                'genero', "musica clasica", "jazz", "Blues", "gospel", "soul", "pop", "rock and roll", "country",
                "disco", "techno", "reggae", "salsa", "flamenco", "ranchera", "hip hop/rap", "reggaeton", "metal",
                "funk", "bossa nova", "musica melodica", "rock"]

def check_onthology(input_user):
    print(input_user)
    if any(word in input_user for word in keyword_list):
        print('[O] Guide User')
        print(f"[I] Check Onthology: {input_user}")
        # onto = get_ontology("C:\\Users\\charl\\Desktop\\QUINTO_SEMESTRE\\INTELIGENCIA_ARTIFICIAL\\NEW.owl").load()
        onto = get_ontology("http://localhost:3030/test/get").load()
        print(onto.imported_ontologies)
        print("ONTO")
        sync_reasoner()
        print(onto.UNIVERSIDAD)
        print(onto.search(label="UNIVERSIDAD"))
        print(onto.graph)
        print(onto.data_properties())
        print(onto.object_properties())
        print(onto.annotation_properties())
        print(onto.search(iri="UNIVERSIDAD"))
        print(onto.search(is_a=onto.UNIVERSIDAD))
        print(onto.individuals())
        for indivi in onto.individuals():
            print(indivi)

        print(list(default_world.sparql("""
                           SELECT (COUNT(?x) AS ?nb)
                           { ?x a owl:Class . }
                    """)))
        print(list(default_world.sparql("""
                                   SELECT *
                                        WHERE {
                                          ?s ?p ?o .
                                        }
                                        LIMIT 200
                            """)))
        print(onto.properties())
        print(input_user.split(" "))
        return 0
    else:
        return 1
