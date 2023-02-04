import threading
import time
from pymantic import sparql

def request1():
    server1 = sparql.SPARQLServer('http://192.168.100.77:9999/blazegraph/sparql')
    global result1
    print('Request 1 started')
    # 1 one-level
    #result1 = server1.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_id "Object_10000"}')
    # 2 one-level
    #result1 = server1.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_option_id "Option_15"}')
    # 3 one-level
    #result1 = server1.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_option_id ?Option_id. FILTER (?Option_id = "Option_9" || ?Option_id = "Option_10")}')
    # 4 one-level
    #result1 = server1.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT (count(distinct ?Object) as ?count) WHERE {?Object my:has_option_id ?Option_id. FILTER (?Option_id = "Option_9" || ?Option_id = "Option_15")}GROUP BY ?Option_id')
    #5 one-level
    #result1 = server1.query('PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_option_id ?Option_id. FILTER contains(?Option_id, "_200")}')

    # 1 3-2-2
    result1 = server1.query(
        'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_id "Object_10000"}')
    # 2 3-2-2
    #result1 = server1.query('PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT * WHERE {?Object my:has_parent_id/my:has_parent_id/my:linked_to ?Core_2_Level_2. ?Option my:has_parent_id/my:has_parent_id ?Core_2_Level_2. ?Option my:has_id "Option_15". }LIMIT 100')
    # 3 3-2-2
    #result1 = server1.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT * WHERE {?Object my:has_parent_id/my:has_parent_id/my:linked_to ?Core_2_Level_2. ?Option my:has_parent_id/my:has_parent_id ?Core_2_Level_2. ?Option my:has_id ?Option_id. FILTER (?Option_id = "Option_8" || ?Option_id = "Option_11")}')
    # 4 3-2-2
    #result1 = server1.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT (count(distinct ?Object) as ?count) WHERE {?Object my:has_parent_id/my:has_parent_id/my:linked_to ?Core_2_Level_2. ?Option my:has_parent_id/my:has_parent_id ?Core_2_Level_2. ?Option my:has_id ?Option_id. FILTER (?Option_id = "Option_8" || ?Option_id = "Option_11")}GROUP BY ?Option_id')
    # 5 3-2-2
    #result1 = server1.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_parent_id/my:has_parent_id/my:linked_to ?Option_2. ?Option my:has_parent_id/my:has_parent_id ?Option_2. ?Option my:has_id ?Option_id. FILTER contains(?Option_id, "_201")}LIMIT 100')

    print('Request 1 finished')


def request2():
    server2 = sparql.SPARQLServer('http://192.168.100.72:9999/blazegraph/sparql')
    global result2
    print('Request 2 started')
    # 1 one-level
    #result2 = server2.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_id "Object_10000"}')
    # 2 one-level
    #result2 = server2.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_option_id "Option_15"}')
    # 3 one-level
    #result2 = server2.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_option_id ?Option_id. FILTER (?Option_id = "Option_9" || ?Option_id = "Option_10")}')
    # 4 one-level
    #result2 = server2.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT (count(distinct ?Object) as ?count) WHERE {?Object my:has_option_id ?Option_id. FILTER (?Option_id = "Option_9" || ?Option_id = "Option_15")}GROUP BY ?Option_id')
    #5 one-level
    #result2 = server2.query('PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_option_id ?Option_id. FILTER contains(?Option_id, "_200")}')

    # 1 3-2-2
    result2 = server2.query(
        'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_id "Object_10000"}')
    # 2 3-2-2
    #result2 = server2.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT * WHERE {?Object my:has_parent_id/my:has_parent_id/my:linked_to ?Core_2_Level_2. ?Option my:has_parent_id/my:has_parent_id ?Core_2_Level_2. ?Option my:has_id "Option_15". }LIMIT 100')
    # 3 3-2-2
    #result2 = server2.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT * WHERE {?Object my:has_parent_id/my:has_parent_id/my:linked_to ?Core_2_Level_2. ?Option my:has_parent_id/my:has_parent_id ?Core_2_Level_2. ?Option my:has_id ?Option_id. FILTER (?Option_id = "Option_8" || ?Option_id = "Option_11")}')
    # 4 3-2-2
    #result2 = server2.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT (count(distinct ?Object) as ?count) WHERE {?Object my:has_parent_id/my:has_parent_id/my:linked_to ?Core_2_Level_2. ?Option my:has_parent_id/my:has_parent_id ?Core_2_Level_2. ?Option my:has_id ?Option_id. FILTER (?Option_id = "Option_8" || ?Option_id = "Option_11")}GROUP BY ?Option_id')
    # 5 3-2-2
    #result2 = server2.query(
    #    'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema> PREFIX my: <http://127.0.0.1/bg/ont/test1#> SELECT ?Object WHERE {?Object my:has_parent_id/my:has_parent_id/my:linked_to ?Option_2. ?Option my:has_parent_id/my:has_parent_id ?Option_2. ?Option my:has_id ?Option_id. FILTER contains(?Option_id, "_201")}LIMIT 100')
    print('Request 2 finished')


t0 = int(time.time() * 1000)
tn = t0
print("Started")

x = threading.Thread(target=request1)
x.start()

y = threading.Thread(target=request2)
y.start()

x.join()
y.join()

#for b in result1['results']['bindings']:
#    print(b)
for b in result2['results']['bindings']:
    print(b)

t1 = int(time.time() * 1000)
print("\nFinished. Time: " + str(t1-t0) + " ms.")