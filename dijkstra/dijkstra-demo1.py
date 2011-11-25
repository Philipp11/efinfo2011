"""
    dijkstra-demo1.py  (c) 2010 by Pascal Schuppli

    Eine Minimal-Version des Dijkstra-Algorithmus ohne Fehlerbehandlung
    etc, das heisst, wenn die Datenstruktur Fehler aufweist, geht alles
    den Bach runter!

    Die Lösung, das Verkehrsnetz in einer Liste von Listen zu speichern und
    die Zugriffsfunktionen von der globalen Liste "orte" abhängig zu machen,
    ist nicht besonders elegant. Insbesondere gilt es zu beachten, dass der
    Herkunftsort nicht wie die Nachbarsorte als String gespeichert wird,
    sondern dass direkt die entsprechende Ortsstruktur referenziert wird.

    Ausserdem unschön: Die km-Zahlen, Markierungen und Herkunftsangaben müssen
    vor jedem dijkstra-Lauf in den Urzustand (None, False, None) versetzt
    werden!
   
    Die print-Anweisungen in der dijkstra-Funktion dienen nur der Illustration.
"""

orte = [
#   Name  Nachbarn             km   mark. Herkunft
    ["a", ["b", 10, "c", 5], None, False, None ],
    ["b", ["a", 10, "d", 8], None, False, None ],
    ["c", ["a",  5, "d", 7], None, False, None ],
    ["d", ["b",  8, "c", 7], None, False, None ]
]

def ortsname(ort):
    """Liefert den Namen des Ortes"""
    return ort[0]

def findeOrt(name):
    """Liefert eine Ort-Datenstruktur zurück, wenn man deren Namen kennt"""
    global orte
    for ort in orte:
        if ortsname(ort) == name:
            return ort
    return None
    
def km(ort):
    """Liefert die zurückgelegte Anzahl Kilometer bis zu ort"""
    return ort[2]

def setzeKm(ort, anzahl):
    """Setze die zurückgelegte Anzahl Kilometer bis zu ort"""
    ort[2] = anzahl

def istMarkiert(ort):
    """gibt True zurück, wenn ort bereits markiert wurde, sonst False"""
    return ort[3]

def markiere(ort):
    """Markiert ort"""
    ort[3] = True

def herkunft(ort):
    """Gibt denjenigen Nachbarort zurück, von dem der kürzeste Weg zu
       diesem Ort ausgeht"""
    return ort[4]

def setzeHerkunft(ort, herkunftsort):
    """Setze den Herkunftsort, von dem der kürzeste Weg ausgeht"""
    ort[4] = herkunftsort

def nachbarn(ort):
    """Liefert eine Liste aller Nachbarsorte zurück"""
    nachbarliste = []
    for i in range(0, len(ort[1]), 2):
        nachbarliste.append(findeOrt(ort[1][i]))
    return nachbarliste

def distanz(orta, ortb):
    """Liefert die Distanz zwischen orta und ortb"""
    b = ortsname(ortb)
    if b in orta[1]:
        return orta[1][orta[1].index(b)+1]
    else:
        return None
                     

def findeNaechsten(liste):
    """Findet den Ort mit der kleinsten km-Zahl in einer liste von orten"""
    kleinstes = liste[0]
    for ort in liste:
        if km(ort) != None and km(ort) < km(kleinstes):
            kleinstes = ort
    return kleinstes

def entferneDuplikate(ort, liste):
    while ort in liste:
        liste.remove(ort)

def dijkstra(startort, zielort):
    """Berechnet die kürzeste Route vom startort zum zielort. startort und
       zielort repräsentieren ort-Strukturen."""
    agenda = [startort]
    setzeKm(startort, 0)
    while agenda:
        aktuell = findeNaechsten(agenda)
        print "Erledige ", ortsname(aktuell)
        entferneDuplikate(aktuell, agenda)
        markiere(aktuell)
        for ort in nachbarn(aktuell):
            print "  zu Ort", ortsname(ort),
            if not istMarkiert(ort):
                agenda.append(ort)
                d = km(aktuell) + distanz(aktuell, ort)
                if km(ort) == None or d < km(ort):
                    setzeKm(ort, d)
                    setzeHerkunft(ort, aktuell)
                    print "Neuer kürzester Weg ist", d
                else:
                    print "Der bereits bestehende Weg ist kürzer als meiner:", d
            else:
                print "dieser Ort wurde schon von Ameisen besucht..."

    # Jetzt müssen wir nur noch die Route vom Ziel zurück zum Start finden
    aktuell = zielort
    route = [zielort]
    while aktuell != startort:
        aktuell = herkunft(aktuell)
        route.append(aktuell)
    route.reverse()
    return (route, km(zielort))


def hauptprogramm():
    """Das Hauptprogramm demonstriert den Dijkstra-Algorithmus"""
    weg, total = dijkstra(findeOrt("a"), findeOrt("d"))
    
    print "Total", total, "km über folgende Orte:"
    for station in weg:
        print ortsname(station), "(", km(station), "km)" 
          
if __name__ == "__main__":
    hauptprogramm()
