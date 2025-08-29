import math

class AntoineCalculator:
    def __init__(self):
        self.datos = [
            {"Nombre": "Acetona", "Formula": "C3H6O", "A": 14.3145, "B": 2756.22, "C": 228.060, "Tn": 56.2},
            {"Nombre": "Acido acetico", "Formula": "C2H4O2", "A": 15.0717, "B": 3580.80, "C": 224.650, "Tn": 117.9},
            {"Nombre": "Acetonitrilo", "Formula": "C2H3N", "A": 14.8950, "B": 3413.10, "C": 250.523, "Tn": 81.6},
            {"Nombre": "Benceno", "Formula": "C6H6", "A": 13.7819, "B": 2728.81, "C": 217.572, "Tn": 80.0},
            {"Nombre": "iso-Butano", "Formula": "C4H10", "A": 13.8254, "B": 2413.79, "C": 248.870, "Tn": -11.9},
            {"Nombre": "n-Butano", "Formula": "C4H10", "A": 13.6608, "B": 2154.70, "C": 238.789, "Tn": -0.5},
            {"Nombre": "1-Butanol", "Formula": "C4H10O", "A": 15.3144, "B": 3212.43, "C": 182.779, "Tn": 117.6},
            {"Nombre": "2-Butanol", "Formula": "C4H10O", "A": 15.1989, "B": 3026.03, "C": 186.590, "Tn": 99.5},
            {"Nombre": "iso-Clorobutano", "Formula": "C4H9Cl", "A": 14.6047, "B": 3026.03, "C": 186.590, "Tn": 100.0},
            {"Nombre": "tert-Butanol", "Formula": "C4H10O", "A": 14.8445, "B": 2658.29, "C": 177.650, "Tn": 82.3},
            {"Nombre": "Tetracloruro de carbono", "Formula": "CCl4", "A": 14.0572, "B": 2914.23, "C": 232.148, "Tn": 76.6},
            {"Nombre": "Clorobenceno", "Formula": "C6H5Cl", "A": 13.8635, "B": 3174.78, "C": 211.700, "Tn": 131.7},
            {"Nombre": "1-Clorobutano", "Formula": "C4H9Cl", "A": 13.7065, "B": 2723.73, "C": 201.365, "Tn": 107.8},
            {"Nombre": "Cloroformo", "Formula": "CHCl3", "A": 13.7324, "B": 2548.74, "C": 218.552, "Tn": 61.1},
            {"Nombre": "Ciclohexano", "Formula": "C6H12", "A": 13.6568, "B": 2723.44, "C": 220.618, "Tn": 80.7},
            {"Nombre": "Ciclopentano", "Formula": "C5H10", "A": 13.9727, "B": 2653.90, "C": 234.510, "Tn": 49.2},
            {"Nombre": "n-Decano", "Formula": "C10H22", "A": 13.9748, "B": 3442.76, "C": 193.838, "Tn": 174.1},
            {"Nombre": "Diclorometano", "Formula": "CH2Cl2", "A": 13.9891, "B": 2463.93, "C": 223.240, "Tn": 39.7},
            {"Nombre": "Eter dietilico", "Formula": "C4H10O", "A": 14.0735, "B": 2511.29, "C": 231.200, "Tn": 34.4},
            {"Nombre": "1,4-Dioxano", "Formula": "C4H8O2", "A": 15.0967, "B": 3579.78, "C": 240.537, "Tn": 101.3},
            {"Nombre": "n-Eicosano", "Formula": "C20H42", "A": 14.4575, "B": 4680.46, "C": 132.100, "Tn": 343.6},
            {"Nombre": "Etanol", "Formula": "C2H5OH", "A": 16.8958, "B": 3795.17, "C": 230.918, "Tn": 78.2},
            {"Nombre": "Etilbenceno", "Formula": "C8H10", "A": 13.9726, "B": 3259.93, "C": 212.300, "Tn": 136.2},
            {"Nombre": "Etilenglicol", "Formula": "C2H6O2", "A": 15.7567, "B": 4187.46, "C": 178.650, "Tn": 197.3},
            {"Nombre": "n-Heptano", "Formula": "C7H16", "A": 13.8622, "B": 3020.13, "C": 216.435, "Tn": 98.4},
            {"Nombre": "n-Hexano", "Formula": "C6H14", "A": 13.8193, "B": 2696.04, "C": 224.317, "Tn": 68.7},
            {"Nombre": "Metanol", "Formula": "CH4O", "A": 16.5785, "B": 3638.27, "C": 239.500, "Tn": 64.7},
            {"Nombre": "Acetato de metilo", "Formula": "C3H6O2", "A": 14.2456, "B": 2662.78, "C": 219.690, "Tn": 56.9},
            {"Nombre": "Metil etil cetona", "Formula": "C4H8O", "A": 14.1334, "B": 2838.24, "C": 218.690, "Tn": 79.6},
            {"Nombre": "Nitrometano", "Formula": "CH3NO2", "A": 14.7513, "B": 3331.70, "C": 227.600, "Tn": 101.2},
            {"Nombre": "n-Nonano", "Formula": "C9H20", "A": 13.9854, "B": 3311.19, "C": 202.694, "Tn": 150.8},
            {"Nombre": "iso-Octano", "Formula": "C8H18", "A": 13.6703, "B": 2896.31, "C": 220.767, "Tn": 99.2},
            {"Nombre": "n-Octano", "Formula": "C8H18", "A": 13.9346, "B": 3320.13, "C": 209.655, "Tn": 125.6},
            {"Nombre": "n-Pentano", "Formula": "C5H12", "A": 13.7667, "B": 2451.88, "C": 232.014, "Tn": 36.0},
            {"Nombre": "Fenol", "Formula": "C6H6O", "A": 14.4387, "B": 3507.80, "C": 175.400, "Tn": 181.8},
            {"Nombre": "1-Propanol", "Formula": "C3H8O", "A": 16.1154, "B": 3483.67, "C": 205.807, "Tn": 97.2},
            {"Nombre": "2-Propanol", "Formula": "C3H8O", "A": 16.6796, "B": 3640.11, "C": 219.610, "Tn": 82.2},
            {"Nombre": "Tolueno", "Formula": "C7H8", "A": 13.9320, "B": 3056.96, "C": 217.625, "Tn": 110.6},
            {"Nombre": "Agua", "Formula": "H2O", "A": 16.3872, "B": 3885.70, "C": 230.170, "Tn": 100.0},
            {"Nombre": "o-Xileno", "Formula": "C8H10", "A": 14.0413, "B": 3358.79, "C": 212.041, "Tn": 144.4},
            {"Nombre": "m-Xileno", "Formula": "C8H10", "A": 14.1387, "B": 3321.81, "C": 216.120, "Tn": 139.1},
            {"Nombre": "p-Xileno", "Formula": "C8H10", "A": 14.0579, "B": 3331.45, "C": 214.627, "Tn": 138.3}
        ]

        self.substances = {}
        for item in self.datos:
            normalized_name = self.normalize_name(item["Nombre"])
            self.substances[normalized_name] = item

    def normalize_name(self, name):
        name = name.lower()
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            ' ': '', '-': '', '_': '', '.': '', ',': ''
        }
        for old, new in replacements.items():
            name = name.replace(old, new)
        return name

    def calculate_pressure(self, A, B, C, T_celsius):
        try:
            ln_P = A - B / (T_celsius + C)
            P_kPa = math.exp(ln_P)
            return P_kPa
        except:
            return None

    def calculate_temperature(self, A, B, C, P_kPa):
        try:
            if P_kPa <= 0:
                return None
            ln_P = math.log(P_kPa)
            T_celsius = B / (A - ln_P) - C
            return T_celsius
        except:
            return None

    def show_substances(self):
        print("")
        print("=" * 60)
        print("SUSTANCIAS DISPONIBLES EN LA BASE DE DATOS")
        print("=" * 60)
        substances_list = []
        for i in range(len(self.datos)):
            item = self.datos[i]
            num_str = str(i + 1).rjust(2)
            nombre = item["Nombre"].ljust(25)
            formula = item["Formula"].ljust(10)
            tn_str = ("%6.1f" % item["Tn"]).rjust(6)
            print(num_str + ". " + nombre + " (" + formula + ") - Tn: " + tn_str + " C")
            substances_list.append((item["Nombre"], item))
        print("=" * 60)
        return substances_list

    def search_substance(self):
        print("")
        print("BUSQUEDA DE SUSTANCIA")
        search_term = input("Ingresa el nombre (o parte del nombre) de la sustancia: ").strip()
        if not search_term:
            print("Error: Debes ingresar un termino de busqueda")
            return None

        normalized_search = self.normalize_name(search_term)
        exact_match = None
        matches = []

        for norm_name, substance in self.substances.items():
            if normalized_search == norm_name:
                exact_match = (substance["Nombre"], substance)
                break
            elif normalized_search in norm_name or norm_name in normalized_search:
                matches.append((substance["Nombre"], substance))

        if exact_match:
            print("Sustancia encontrada: " + exact_match[0])
            return exact_match

        if not matches:
            print("No se encontraron sustancias que coincidan con '" + search_term + "'")
            return None

        if len(matches) == 1:
            print("Sustancia encontrada: " + matches[0][0])
            return matches[0]

        print("Se encontraron " + str(len(matches)) + " coincidencias:")
        for i in range(len(matches)):
            name = matches[i][0]
            formula = matches[i][1]["Formula"]
            print(str(i + 1) + ". " + name + " (" + formula + ")")

        try:
            choice_str = input("Selecciona el numero (1-" + str(len(matches)) + "): ")
            choice = int(choice_str)
            if choice < 1 or choice > len(matches):
                print("Numero invalido")
                return None
            selected = matches[choice - 1]
            print("Seleccionado: " + selected[0])
            return selected
        except:
            print("Por favor ingresa un numero valido")
            return None

    def show_constants(self, substance_name):
        substance_data = None
        for item in self.datos:
            if item["Nombre"] == substance_name:
                substance_data = item
                break
        if not substance_data:
            print("No se encontro la sustancia: " + substance_name)
            return

        print("")
        print("CONSTANTES DE ANTOINE PARA " + substance_data["Nombre"].upper())
        print("-" * 60)
        print("Formula quimica: " + substance_data["Formula"])
        print("T normal de ebullicion: %6.1f C" % substance_data["Tn"])
        print("Constante A: %8.4f" % substance_data["A"])
        print("Constante B: %8.2f" % substance_data["B"])
        print("Constante C: %8.3f" % substance_data["C"])
        print("-" * 60)
        print("Ecuacion: ln(P_sat/kPa) = A - B/(T/C + C)")
        print("-" * 60)

    def add_new_substance(self):
        print("")
        print("AGREGAR NUEVA SUSTANCIA")
        print("Ingresa los datos de la nueva sustancia:")

        try:
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("El nombre no puede estar vacio")
                return

            formula = input("Formula quimica: ").strip()
            if not formula:
                print("La formula no puede estar vacia")
                return

            A = float(input("Constante A: "))
            B = float(input("Constante B: "))
            C = float(input("Constante C: "))
            Tn = float(input("T normal de ebullicion (C): "))

            nueva = {
                "Nombre": nombre,
                "Formula": formula,
                "A": A,
                "B": B,
                "C": C,
                "Tn": Tn
            }
            self.datos.append(nueva)
            norm_name = self.normalize_name(nombre)
            self.substances[norm_name] = nueva

            print("Sustancia '" + nombre + "' agregada correctamente")
        except:
            print("Error al ingresar los datos")

    def perform_calculation(self, choice, substance_name, A, B, C):
        if choice == '1':
            print("")
            print("CALCULO DE PRESION DE SATURACION PARA " + substance_name.upper())
            print("Formula: ln(P_sat/kPa) = A - B/(T/C + C)")

            try:
                T_input = input("Ingresa la temperatura en C: ")
                T_celsius = float(T_input)
                P_kPa = self.calculate_pressure(A, B, C, T_celsius)
                if P_kPa is None:
                    print("Error en el calculo de presion")
                    return

                P_mmHg = P_kPa * 7.50062
                P_atm = P_kPa / 101.325
                P_bar = P_kPa / 100

                print("")
                print("RESULTADOS:")
                print("Temperatura: %6.1f C" % T_celsius)
                print("Presion de saturacion:")
                print("  kPa:  %8.3f" % P_kPa)
                print("  mmHg: %8.3f" % P_mmHg)
                print("  atm:  %8.6f" % P_atm)
                print("  bar:  %8.6f" % P_bar)
            except:
                print("Error en los datos ingresados")

        elif choice == '2':
            print("")
            print("CALCULO DE TEMPERATURA DE SATURACION PARA " + substance_name.upper())
            print("Formula: T = B/(A - ln(P)) - C")

            print("")
            print("Selecciona unidades de presion:")
            print("1. kPa")
            print("2. mmHg")
            print("3. atm")
            print("4. bar")

            try:
                unit_choice = input("Unidades (1-4): ").strip()
                pressure_input = input("Ingresa el valor de presion: ")
                pressure = float(pressure_input)

                if unit_choice == '1':
                    P_kPa = pressure
                    unit_name = "kPa"
                elif unit_choice == '2':
                    P_kPa = pressure / 7.50062
                    unit_name = "mmHg"
                elif unit_choice == '3':
                    P_kPa = pressure * 101.325
                    unit_name = "atm"
                elif unit_choice == '4':
                    P_kPa = pressure * 100
                    unit_name = "bar"
                else:
                    print("Unidad invalida")
                    return

                T_celsius = self.calculate_temperature(A, B, C, P_kPa)
                if T_celsius is None:
                    print("Error en el calculo de temperatura")
                    return

                T_kelvin = T_celsius + 273.15
                T_fahrenheit = T_celsius * 9.0 / 5.0 + 32.0

                print("")
                print("RESULTADOS:")
                print("Presion: %8.3f %s (%.3f kPa)" % (pressure, unit_name, P_kPa))
                print("Temperatura de saturacion:")
                print("  C: %8.2f" % T_celsius)
                print("  K: %8.2f" % T_kelvin)
                print("  F: %8.2f" % T_fahrenheit)
            except:
                print("Error en los datos ingresados")

    def run(self):
        print("CALCULADORA DE ANTOINE")
        print("=" * 50)
        print("Calcula presion de vapor y temperatura de saturacion")
        print("Ecuacion: ln(P_sat/kPa) = A - B/(T/C + C)")
        print("=" * 50)

        while True:
            try:
                print("")
                print("Que deseas hacer?")
                print("1. Calcular presion (dada temperatura)")
                print("2. Calcular temperatura (dada presion)")
                print("3. Ver todas las sustancias")
                print("4. Buscar sustancia")
                print("5. Agregar nueva sustancia")
                print("6. Salir")

                choice = input("Selecciona una opcion (1-6): ").strip()

                if choice == '6':
                    print("Gracias por usar la calculadora!")
                    break

                elif choice == '3':
                    self.show_substances()

                elif choice == '4':
                    result = self.search_substance()
                    if result:
                        name, data = result
                        self.show_constants(name)

                elif choice == '5':
                    self.add_new_substance()

                elif choice in ['1', '2']:
                    print("")
                    print("Como seleccionar sustancia?")
                    print("1. Ver lista completa")
                    print("2. Buscar por nombre")

                    search_choice = input("Selecciona (1-2): ").strip()

                    if search_choice == '1':
                        substances_list = self.show_substances()
                        try:
                            num_input = input("Selecciona numero (1-%d): " % len(substances_list))
                            substance_num = int(num_input)
                            if substance_num < 1 or substance_num > len(substances_list):
                                print("Numero invalido")
                                continue
                            substance_key, substance_data = substances_list[substance_num - 1]
                        except:
                            print("Por favor ingresa un numero valido")
                            continue
                    elif search_choice == '2':
                        result = self.search_substance()
                        if not result:
                            continue
                        substance_key, substance_data = result
                    else:
                        print("Opcion invalida")
                        continue

                    self.show_constants(substance_key)
                    A = substance_data["A"]
                    B = substance_data["B"]
                    C = substance_data["C"]

                    self.perform_calculation(choice, substance_key, A, B, C)

                else:
                    print("Opcion invalida. Selecciona 1-6.")

            except KeyboardInterrupt:
                print("")
                print("Programa interrumpido")
                break
            except:
                print("Error inesperado. Intenta nuevamente")


def main():
    calc = AntoineCalculator()
    calc.run()

main()