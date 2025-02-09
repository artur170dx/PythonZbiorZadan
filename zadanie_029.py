# Kasia postanowiła w 2022 roku zaznaczać dni, w których udało jej się pilnować diety, 
# jak również te, w których jej się to nie udało. Dla każdego dnia roku, numerowa
# nego od 1 do 365, utwórz dla Kasi listę i skopiuj do niej następujące wartości, gdzie 
# 1 to wartość True, a 0 to wartość False (plik 29_dieta.txt).  
# Każda cyfra (0 lub 1) to kolejny dzień udany (1) lub nieudany (0). Utwórz odpo
# wiednią listę zawierającą wyżej wymienione dane. Odpowiedz na następujące pytania:  
#  Przez ile dni w roku Kasia odnosiła sukces dietetyczny? [1]  
#  Ile było okresów trwających przynajmniej pięć dni z rzędu, które stanowiły 
# porażkę dietetyczną? Podaj numer dnia w roku rozpoczynającym każdy 
# z okresów [4]. 

year = [1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0, 
0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0, 
1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0, 
0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1, 
0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,1, 
0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0, 
1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1, 
0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,0,0, 
1,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1]

print(f"Number of success days: {year.count(1)}")

fail_period_start_days = []
zero_count = 0
period_added = False

for day, diet in enumerate(year):
    if diet == 0:
        zero_count += 1
    else:
        zero_count = 0
    if zero_count ==5:
            fail_period_start_days.append(day - zero_count + 2)

print("First days of failing period: ", fail_period_start_days)