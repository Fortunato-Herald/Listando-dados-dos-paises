#  pip install countryinfo

from countryinfo import CountryInfo

country =  CountryInfo(input('Digite o nome do país: '))

print(f'País: {country.name()}')
print(f'Capital: {country.capital()}')
print(f'Moedas: {country.currencies()}')
print(f'Idiomas: {country.languages()}')
print(f'Fazem Fronteira: {country.borders()}')
print(f'codigo de área: {country.calling_codes()}')
print(f'População: {country.population()}')