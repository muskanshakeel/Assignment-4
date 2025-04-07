def main():
    earth_weight_input = input("Enter a weight on Earth: ")

    earth_weight = float(earth_weight_input)

    planet = input("Enter a planet: ")

    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    if planet in gravity_factors:
        factor = gravity_factors[planet]
        planet_weight = round(earth_weight * factor, 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Unknown planet entered.")

main()
