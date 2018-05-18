# Search methods

import search

ab = (search.GPSProblem('A', 'B', search.romania))
ld = (search.GPSProblem('L', 'D', search.romania))
sp = (search.GPSProblem('S', 'P', search.romania))
on = (search.GPSProblem('O', 'N', search.romania))
cv = (search.GPSProblem('C', 'V', search.romania))
iu = (search.GPSProblem('I', 'U', search.romania))

print ("Resultado de B a A")
print (search.ramificacionYSalto(ab).path())
print (search.ramificacionYSaltoConSubestimacion(ab).path(), "\n")

print ("Resultado de D a L")
print (search.ramificacionYSalto(ld).path())
print (search.ramificacionYSaltoConSubestimacion(ld).path(), "\n")

print ("Resultado de P a S")
print (search.ramificacionYSalto(sp).path())
print (search.ramificacionYSaltoConSubestimacion(sp).path(), "\n")

print ("Resultado de N a O")
print (search.ramificacionYSalto(on).path())
print (search.ramificacionYSaltoConSubestimacion(on).path(), "\n")

print ("Resultado de V a C")
print (search.ramificacionYSalto(cv).path())
print (search.ramificacionYSaltoConSubestimacion(cv).path(), "\n")

print ("Resultado de U a I")
print (search.ramificacionYSalto(iu).path())
print (search.ramificacionYSaltoConSubestimacion(iu).path(), "\n")




"""
print search.breadth_first_graph_search(ab).path()
print search.depth_first_graph_search(ab).path()
print search.iterative_deepening_search(ab).path()
print search.depth_limited_search(ab).path()

"""

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
