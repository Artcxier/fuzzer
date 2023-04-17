import requests
import string
import random

# lista dostępnych metod HTTP
HTTP_METHODS = ["GET", "POST", "PUT", "DELETE"]

# lista dostępnych typów zawartości
CONTENT_TYPES = ["application/json", "application/xml", "text/html", "text/plain"]

# lista dostępnych ciągów znaków do testowania
CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation

# adres URL lub adres IP serwera docelowego
TARGET_URL = "http://example.com"

# liczba iteracji fuzzer'a
NUM_ITERATIONS = 1000

def generate_payload(length):
    """Generuje losowy ciąg znaków o zadanej długości"""
    return ''.join(random.choice(CHARACTER_SET) for _ in range(length))

def fuzz():
    """Wykonuje losowe testy"""
    # wybierz losową metodę HTTP
    method = random.choice(HTTP_METHODS)

    # wybierz losowy typ zawartości
    content_type = random.choice(CONTENT_TYPES)

    # wygeneruj losowy ciąg znaków
    payload = generate_payload(10)

    # wybierz losową ścieżkę docelową
    path = generate_payload(5)

    # utwórz łącze URL
    url = f"{TARGET_URL}/{path}"

    # utwórz nagłówki żądania HTTP
    headers = {
        "Content-Type": content_type
    }

    # wykonaj żądanie HTTP
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=payload, headers=headers)
        elif method == "PUT":
            response = requests.put(url, data=payload, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
    except:
        # obsłuż błędy połączenia
        print(f"Nie udało się nawiązać połączenia z {url}")
        return

    # wyświetl wyniki testu
    print(f"{method} {url} ({content_type}): {response.status_code}")
    print(response.text)

# wykonaj serię testów
for i in range(NUM_ITERATIONS):
    fuzz()