# 3. City data processing

try:
    with open("city.txt", "r") as f:
        cities = [line.strip().split() for line in f if line.strip()]

    total_area = 0

    print("All city details:")
    for city in cities:
        name, pop, area = city[0], float(city[1]), float(city[2])
        print(name, pop, area)
        total_area += area

    print("\nCities with population > 10 lakhs:")
    for city in cities:
        if float(city[1]) > 10:
            print(city[0])

    print("\nTotal area:", total_area)

except Exception as e:
    print("Error:", e) 


    