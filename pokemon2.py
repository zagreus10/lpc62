import requests
#
# Nombre : Johan Emmanuel Garay Garza
# Matricula : 2001776
# Script en python que consult el API de Pokemon
# para listar los nombres de pokemon pero se le agrego
# interaccion para que listaras mas pokemons segun se vaya requiriendo.
# Contribuyo: Johan Emmanuel Garay Garza
# Fecha: 04 de Septiembre de 2023

def get_pokemons (url='https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset':offset} if offset else {}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
        next = input ("¿Continuar listando? [Y/N]").lower()
        if next == 'y':
            get_pokemons(offset=offset+20)
if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    get_pokemons()
