countries = ['United Kingdom', 'Turkey', 'Australia', 'Ghana','Nigeria','New Zealand']
countries1 = list(('United Kingdom', 25, False))
countries2 = ['United Kingdom', 25, False]

print(countries)                # butun hepsini gosterir
print(countries[1])             # 1. siradaki
print(countries[1][3])          # 1. siradaki ulkenin 3. siradaki harfini gosterir
print(countries[2:])            # 2. siradakinden sonrakileri gosterir
print(countries[2:4])           # 2 ile 4 arasindakileri gosterir
print(type(countries))          # countries in bir liste oldugunu gosterir 
countries[0] = 'United States'  # United Kingdom u united state e degistirir
print(countries[-2])            # listeyi tersted siralar
print(len(countries))           # listede kac tane eleman oldugunu gosterir
print(type(countries1))
print(type(countries2))