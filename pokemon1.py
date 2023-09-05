import requests
#
# Nombre: Johan Emmanuel Garay Garza
# Matricula : 2001776
if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'

    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])

        if results:
            for pokemon in results:
                name = pokemon ['name']
                print (name)
