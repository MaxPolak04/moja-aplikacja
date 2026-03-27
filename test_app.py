from app import dodaj, odejmij, pomnoz, podziel

def test_dodaj():
    assert dodaj(2, 3) == 5
    
def test_odejmij():
    assert odejmij(5, 2) == 3
    
def test_pomnoz():
    assert pomnoz(2, 4) == 8
    
def test_podziel():
    assert podziel(10, 2) == 5
    assert podziel(0, 5) == 0
    assert podziel(7, 0) == "Blad: dzielenie przez zero"
    
if __name__ == "__main__":
    test_dodaj()
    test_odejmij()
    test_pomnoz()
    test_podziel()
    print("Wszystkie testy OK")
    