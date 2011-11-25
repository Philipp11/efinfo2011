"""
    dijkstra-katastrophe.py  (c) 2010 by Pascal Schuppli

    Eine Minimal-Version ohne jegliche Zugriffsfunktionen auf die
    Datenstruktur und ohne Hilfsfunktionen für den Dijkstra-Algorithmus.

    Diese Version ist völlig unverständlich.
"""

orte = [
#   Name  Nachbarn             km   mark. Herkunft
    ["a", ["b", 10, "c", 5], None, False, None ],
    ["b", ["a", 10, "d", 8], None, False, None ],
    ["c", ["a",  5, "d", 7], None, False, None ],
    ["d", ["b",  8, "c", 7], None, False, None ]
]

def findeOrt(name):
    """Liefert eine Ort-Datenstruktur zurück, wenn man deren Namen kennt"""
    global orte
    for ort in orte:
        if ort[0] == name:
            return ort
    return None
                   

def dijkstra(startort, zielort):
    """Berechnet die kürzeste Route vom startort zum zielort. startort und
       zielort repräsentieren ort-Strukturen."""
    agenda = [startort]
    startort[2] = 0
    while agenda:
        aktuell = agenda[0]
        for ort in agenda:
            if ort[2] != None and ort[2] < aktuell[2]:
                aktuell = ort
                
        print "Erledige ", aktuell[0]
        while aktuell in agenda:
            agenda.remove(aktuell)
        aktuell[3] = True
        
        for i in range(0, len(aktuell[1]), 2):            
            ort = findeOrt(aktuell[1][i])
            print "  zu Ort", ort[0], 
            if not ort[3]:
                agenda.append(ort)                
                d = aktuell[2] + aktuell[1][aktuell[1].index(ort[0])+1]
                if ort[2] == None or d < ort[2]:
                    ort[2] = d
                    ort[4] = aktuell                    
                    print "Neuer kürzester Weg ist", d
                else:
                    print "Der bereits bestehende Weg ist kürzer als meiner:", d
            else:
                print "dieser Ort wurde schon von Ameisen besucht..."

    # Jetzt müssen wir nur noch die Route vom Ziel zurück zum Start finden
    aktuell = zielort
    route = [zielort]
    while aktuell != startort:
        aktuell = aktuell[4]
        route.append(aktuell)
    route.reverse()
    return (route, zielort[2])


def hauptprogramm():
    """Das Hauptprogramm demonstriert den Dijkstra-Algorithmus"""
    weg, total = dijkstra(findeOrt("a"), findeOrt("d"))
    
    print "Total", total, "km über folgende Orte:"
    for station in weg:
        print station[0], "(", station[2], "km)" 
          
if __name__ == "__main__":
    hauptprogramm()
