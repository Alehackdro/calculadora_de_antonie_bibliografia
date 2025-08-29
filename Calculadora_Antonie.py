import math

class AntoineCalculator:
    def __init__(self):
        self.datos = [
            {"Nombre": "Acetona", "Formula": "C₃H₆O", "A": 14.3145, "B": 2756.22, "C": 228.060, "Tn": 56.2},
            {"Nombre": "Ácido acético", "Formula": "C₂H₄O₂", "A": 15.0717, "B": 3580.80, "C": 224.650, "Tn": 117.9},
            {"Nombre": "Acetonitrilo", "Formula": "C₂H₃N", "A": 14.8950, "B": 3413.10, "C": 250.523, "Tn": 81.6},
            {"Nombre": "Benceno", "Formula": "C₆H₆", "A": 13.7819, "B": 2728.81, "C": 217.572, "Tn": 80.0},
            {"Nombre": "iso-Butano", "Formula": "C₄H₁₀", "A": 13.8254, "B": 2413.79, "C": 248.870, "Tn": -11.9},
            {"Nombre": "n-Butano", "Formula": "C₄H₁₀", "A": 13.6608, "B": 2154.70, "C": 238.789, "Tn": -0.5},
            {"Nombre": "1-Butanol", "Formula": "C₄H₁₀O", "A": 15.3144, "B": 3212.43, "C": 182.779, "Tn": 117.6},
            {"Nombre": "2-Butanol", "Formula": "C₄H₁₀O", "A": 15.1989, "B": 3026.03, "C": 186.590, "Tn": 99.5},
            {"Nombre": "iso-Clorobutano", "Formula": "C₄H₉Cl", "A": 14.6047, "B": 3026.03, "C": 186.590, "Tn": 100.0},
            {"Nombre": "tert-Butanol", "Formula": "C₄H₁₀O", "A": 14.8445, "B": 2658.29, "C": 177.650, "Tn": 82.3},
            {"Nombre": "Tetracloruro de carbono", "Formula": "CCl₄", "A": 14.0572, "B": 2914.23, "C": 232.148, "Tn": 76.6},
            {"Nombre": "Clorobenceno", "Formula": "C₆H₅Cl", "A": 13.8635, "B": 3174.78, "C": 211.700, "Tn": 131.7},
            {"Nombre": "1-Clorobutano", "Formula": "C₄H₉Cl", "A": 13.7065, "B": 2723.73, "C": 201.365, "Tn": 107.8},
            {"Nombre": "Cloroformo", "Formula": "CHCl₃", "A": 13.7324, "B": 2548.74, "C": 218.552, "Tn": 61.1},
            {"Nombre": "Ciclohexano", "Formula": "C₆H₁₂", "A": 13.6568, "B": 2723.44, "C": 220.618, "Tn": 80.7},
            {"Nombre": "Ciclopentano", "Formula": "C₅H₁₀", "A": 13.9727, "B": 2653.90, "C": 234.510, "Tn": 49.2},
            {"Nombre": "n-Decano", "Formula": "C₁₀H₂₂", "A": 13.9748, "B": 3442.76, "C": 193.838, "Tn": 174.1},
            {"Nombre": "Diclorometano", "Formula": "CH₂Cl₂", "A": 13.9891, "B": 2463.93, "C": 223.240, "Tn": 39.7},
            {"Nombre": "Éter dietílico", "Formula": "C₄H₁₀O", "A": 14.0735, "B": 2511.29, "C": 231.200, "Tn": 34.4},
            {"Nombre": "1,4-Dioxano", "Formula": "C₄H₈O₂", "A": 15.0967, "B": 3579.78, "C": 240.537, "Tn": 101.3},
            {"Nombre": "n-Eicosano", "Formula": "C₂₀H₄₂", "A": 14.4575, "B": 4680.46, "C": 132.100, "Tn": 343.6},
            {"Nombre": "Etanol", "Formula": "C₂H₅OH", "A": 16.8958, "B": 3795.17, "C": 230.918, "Tn": 78.2},
            {"Nombre": "Etilbenceno", "Formula": "C₈H₁₀", "A": 13.9726, "B": 3259.93, "C": 212.300, "Tn": 136.2},
            {"Nombre": "Etilenglicol", "Formula": "C₂H₆O₂", "A": 15.7567, "B": 4187.46, "C": 178.650, "Tn": 197.3},
            {"Nombre": "n-Heptano", "Formula": "C₇H₁₆", "A": 13.8622, "B": 3020.13, "C": 216.435, "Tn": 98.4},
            {"Nombre": "n-Hexano", "Formula": "C₆H₁₄", "A": 13.8193, "B": 2696.04, "C": 224.317, "Tn": 68.7},
            {"Nombre": "Metanol", "Formula": "CH₄O", "A": 16.5785, "B": 3638.27, "C": 239.500, "Tn": 64.7},
            {"Nombre": "Acetato de metilo", "Formula": "C₃H₆O₂", "A": 14.2456, "B": 2662.78, "C": 219.690, "Tn": 56.9},
            {"Nombre": "Metil etil cetona", "Formula": "C₄H₈O", "A": 14.1334, "B": 2838.24, "C": 218.690, "Tn": 79.6},
            {"Nombre": "Nitrometano", "Formula": "CH₃NO₂", "A": 14.7513, "B": 3331.70, "C": 227.600, "Tn": 101.2},
            {"Nombre": "n-Nonano", "Formula": "C₉H₂₀", "A": 13.9854, "B": 3311.19, "C": 202.694, "Tn": 150.8},
            {"Nombre": "iso-Octano", "Formula": "C₈H₁₈", "A": 13.6703, "B": 2896.31, "C": 220.767, "Tn": 99.2},
            {"Nombre": "n-Octano", "Formula": "C₈H₁₈", "A": 13.9346, "B": 3320.13, "C": 209.655, "Tn": 125.6},
            {"Nombre": "n-Pentano", "Formula": "C₅H₁₂", "A": 13.7667, "B": 2451.88, "C": 232.014, "Tn": 36.0},
            {"Nombre": "Fenol", "Formula": "C₆H₆O", "A": 14.4387, "B": 3507.80, "C": 175.400, "Tn": 181.8},
            {"Nombre": "1-Propanol", "Formula": "C₃H₈O", "A": 16.1154, "B": 3483.67, "C": 205.807, "Tn": 97.2},
            {"Nombre": "2-Propanol", "Formula": "C₃H₈O", "A": 16.6796, "B": 3640.11, "C": 219.610, "Tn": 82.2},
            {"Nombre": "Tolueno", "Formula": "C₇H₈", "A": 13.9320, "B": 3056.96, "C": 217.625, "Tn": 110.6},
            {"Nombre": "Agua", "Formula": "H₂O", "A": 16.3872, "B": 3885.70, "C": 230.170, "Tn": 100.0},
            {"Nombre": "o-Xileno", "Formula": "C₈H₁₀", "A": 14.0413, "B": 3358.79, "C": 212.041, "Tn": 144.4},
            {"Nombre": "m-Xileno", "Formula": "C₈H₁₀", "A": 14.1387, "B": 3321.81, "C": 216.120, "Tn": 139.1},
            {"Nombre": "p-Xileno", "Formula": "C₈H₁₀", "A": 14.0579, "B": 3331.45, "C": 214.627, "Tn": 138.3}
        ]
        
        # Crear diccionario para búsquedas más eficientes
        self.substances = {}
        for item in self.datos:
            # Normalizar nombres para búsqueda (sin tildes, minúsculas)
            normalized_name = self.normalize_name(item["Nombre"])
            self.substances[normalized_name] = item

    def normalize_name(self, name):
        """Normaliza nombres para búsquedas (sin tildes, espacios, guiones)"""
        # Diccionario de reemplazos para caracteres especiales
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u',
            ' ': '', '-': '', '_': '', '.': '', ',': ''
        }
        
        normalized = name.lower()
        for old, new in replacements.items():
            normalized = normalized.replace(old, new)
        return normalized

    def calculate_pressure(self, A, B, C, T_celsius):
        """
        Calcula presión usando la ecuación de Antoine
        ln(P^sat/kPa) = A - B/(T/°C + C)
        """
        try:
            ln_P = A - B / (T_celsius + C)
            P_kPa = math.exp(ln_P)
            return P_kPa
        except Exception as e:
            raise ValueError(f"Error en el cálculo de presión: {e}")

    def calculate_temperature(self, A, B, C, P_kPa):
        """
        Calcula temperatura usando la ecuación de Antoine despejada
        T = B/(A - ln(P)) - C
        """
        try:
            if P_kPa <= 0:
                raise ValueError("La presión debe ser mayor que 0")
            ln_P = math.log(P_kPa)
            T_celsius = B / (A - ln_P) - C
            return T_celsius
        except Exception as e:
            raise ValueError(f"Error en el cálculo de temperatura: {e}")

    def show_substances(self):
        """Muestra todas las sustancias disponibles"""
        print("\n" + "="*80)
        print("📋 SUSTANCIAS DISPONIBLES EN LA BASE DE DATOS")
        print("="*80)
        
        substances_list = []
        for i, item in enumerate(self.datos, 1):
            print(f"{i:2d}. {item['Nombre']:<25} ({item['Formula']:<10}) - Tn: {item['Tn']:>6.1f}°C")
            substances_list.append((item['Nombre'], item))
        
        print("="*80)
        return substances_list

    def search_substance(self):
        """Busca una sustancia por nombre"""
        print("\n🔍 BÚSQUEDA DE SUSTANCIA")
        search_term = input("Ingresa el nombre (o parte del nombre) de la sustancia: ").strip()
        
        if not search_term:
            print("❌ Debes ingresar un término de búsqueda")
            return None
        
        # Normalizar término de búsqueda
        normalized_search = self.normalize_name(search_term)
        
        # Buscar coincidencias exactas primero
        for normalized_name, substance in self.substances.items():
            if normalized_search == normalized_name:
                print(f"✅ Sustancia encontrada: {substance['Nombre']}")
                return substance['Nombre'], substance
        
        # Buscar coincidencias parciales
        matches = []
        for normalized_name, substance in self.substances.items():
            if normalized_search in normalized_name or normalized_name in normalized_search:
                matches.append((substance['Nombre'], substance))
        
        if not matches:
            print(f"❌ No se encontraron sustancias que coincidan con '{search_term}'")
            return None
        elif len(matches) == 1:
            substance_name, substance_data = matches[0]
            print(f"✅ Sustancia encontrada: {substance_name}")
            return substance_name, substance_data
        else:
            print(f"\n🔍 Se encontraron {len(matches)} coincidencias:")
            for i, (name, data) in enumerate(matches, 1):
                print(f"{i}. {name} ({data['Formula']})")
            
            try:
                choice = int(input(f"\nSelecciona el número (1-{len(matches)}): "))
                if 1 <= choice <= len(matches):
                    substance_name, substance_data = matches[choice - 1]
                    print(f"✅ Seleccionado: {substance_name}")
                    return substance_name, substance_data
                else:
                    print(f"❌ Número inválido. Debe estar entre 1 y {len(matches)}")
                    return None
            except ValueError:
                print("❌ Por favor ingresa un número válido")
                return None

    def show_constants(self, substance_name):
        """Muestra las constantes de Antoine para una sustancia"""
        # Buscar la sustancia
        substance_data = None
        for item in self.datos:
            if item['Nombre'] == substance_name:
                substance_data = item
                break
        
        if not substance_data:
            print(f"❌ No se encontró la sustancia: {substance_name}")
            return
        
        print(f"\n📊 CONSTANTES DE ANTOINE PARA {substance_data['Nombre'].upper()}")
        print("-" * 60)
        print(f"Fórmula química: {substance_data['Formula']}")
        print(f"Temperatura normal de ebullición: {substance_data['Tn']:.1f} °C")
        print(f"Constante A: {substance_data['A']:.4f}")
        print(f"Constante B: {substance_data['B']:.2f}")
        print(f"Constante C: {substance_data['C']:.3f}")
        print("-" * 60)
        print("Ecuación de Antoine: ln(P^sat/kPa) = A - B/(T/°C + C)")
        print("-" * 60)

    def add_new_substance(self):
        """Permite agregar una nueva sustancia a la base de datos"""
        print("\n➕ AGREGAR NUEVA SUSTANCIA")
        print("Ingresa los datos de la nueva sustancia:")
        
        try:
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío")
                return
            
            formula = input("Fórmula química: ").strip()
            if not formula:
                print("❌ La fórmula no puede estar vacía")
                return
            
            A = float(input("Constante A: "))
            B = float(input("Constante B: "))
            C = float(input("Constante C: "))
            Tn = float(input("Temperatura normal de ebullición (°C): "))
            
            # Agregar a la base de datos
            nueva_sustancia = {
                "Nombre": nombre,
                "Formula": formula,
                "A": A,
                "B": B,
                "C": C,
                "Tn": Tn
            }
            
            self.datos.append(nueva_sustancia)
            normalized_name = self.normalize_name(nombre)
            self.substances[normalized_name] = nueva_sustancia
            
            print(f"✅ Sustancia '{nombre}' agregada correctamente a la base de datos")
            
        except ValueError as e:
            print(f"❌ Error al ingresar los datos: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    def perform_calculation(self, choice, substance_name, A, B, C):
        """Realiza el cálculo seleccionado"""
        if choice == '1':  # Calcular presión
            print(f"\n🌡️  CÁLCULO DE PRESIÓN DE SATURACIÓN PARA {substance_name.upper()}")
            print("Fórmula: ln(P^sat/kPa) = A - B/(T/°C + C)")
            
            try:
                T_celsius = float(input(f"\nIngresa la temperatura en °C: "))
                
                P_kPa = self.calculate_pressure(A, B, C, T_celsius)
                P_mmHg = P_kPa * 7.50062  # Conversión kPa a mmHg
                P_atm = P_kPa / 101.325   # Conversión kPa a atm
                P_bar = P_kPa / 100       # Conversión kPa a bar
                
                print(f"\n📊 RESULTADOS:")
                print(f"Temperatura: {T_celsius:.1f} °C")
                print(f"Presión de saturación:")
                print(f"  • {P_kPa:.3f} kPa")
                print(f"  • {P_mmHg:.3f} mmHg")
                print(f"  • {P_atm:.6f} atm")
                print(f"  • {P_bar:.6f} bar")
                
            except ValueError as e:
                print(f"❌ {e}")
            except Exception as e:
                print(f"❌ Error en el cálculo: {e}")
                
        elif choice == '2':  # Calcular temperatura
            print(f"\n💨 CÁLCULO DE TEMPERATURA DE SATURACIÓN PARA {substance_name.upper()}")
            print("Fórmula despejada: T = B/(A - ln(P)) - C")
            
            print("\nSelecciona las unidades de presión:")
            print("1. kPa")
            print("2. mmHg") 
            print("3. atm")
            print("4. bar")
            
            try:
                unit_choice = input("Unidades (1-4): ").strip()
                pressure = float(input("Ingresa el valor de presión: "))
                
                # Convertir a kPa
                if unit_choice == '1':  # kPa
                    P_kPa = pressure
                    unit_name = "kPa"
                elif unit_choice == '2':  # mmHg
                    P_kPa = pressure / 7.50062
                    unit_name = "mmHg"
                elif unit_choice == '3':  # atm
                    P_kPa = pressure * 101.325
                    unit_name = "atm"
                elif unit_choice == '4':  # bar
                    P_kPa = pressure * 100
                    unit_name = "bar"
                else:
                    print("❌ Unidad inválida")
                    return
                
                T_celsius = self.calculate_temperature(A, B, C, P_kPa)
                T_kelvin = T_celsius + 273.15
                T_fahrenheit = T_celsius * 9/5 + 32
                
                print(f"\n📊 RESULTADOS:")
                print(f"Presión: {pressure:.3f} {unit_name} ({P_kPa:.3f} kPa)")
                print(f"Temperatura de saturación:")
                print(f"  • {T_celsius:.2f} °C")
                print(f"  • {T_kelvin:.2f} K")
                print(f"  • {T_fahrenheit:.2f} °F")
                
            except ValueError as e:
                print(f"❌ {e}")
            except Exception as e:
                print(f"❌ Error en el cálculo: {e}")

    def run(self):
        """Ejecuta el programa principal"""
        print("🧪 CALCULADORA DE ANTOINE")
        print("=" * 50)
        print("Calcula presión de vapor y temperatura de saturación")
        print("usando la ecuación de Antoine: ln(P^sat/kPa) = A - B/(T/°C + C)")
        print("=" * 50)

        while True:
            try:
                print("\n¿Qué deseas hacer?")
                print("1. Calcular presión (dada temperatura)")
                print("2. Calcular temperatura (dada presión)")
                print("3. Ver todas las sustancias disponibles")
                print("4. Buscar sustancia específica")
                print("5. Agregar nueva sustancia")
                print("6. Salir")

                choice = input("\nSelecciona una opción (1-6): ").strip()

                if choice == '6':
                    print("¡Gracias por usar la calculadora de Antoine!")
                    break
                elif choice == '3':
                    self.show_substances()
                    continue
                elif choice == '4':
                    result = self.search_substance()
                    if result:
                        substance_key, substance_data = result
                        self.show_constants(substance_key)
                    continue
                elif choice == '5':
                    self.add_new_substance()
                    continue
                elif choice in ['1', '2']:
                    print("\n¿Cómo quieres seleccionar la sustancia?")
                    print("1. Ver lista completa")
                    print("2. Buscar por nombre")
                    
                    search_choice = input("Selecciona (1-2): ").strip()
                    
                    if search_choice == '1':
                        substances_list = self.show_substances()
                        try:
                            substance_num = int(input(f"\nSelecciona el número de sustancia (1-{len(substances_list)}): "))
                            if substance_num < 1 or substance_num > len(substances_list):
                                print(f"❌ Número inválido. Debe estar entre 1 y {len(substances_list)}")
                                continue
                            substance_key, substance_data = substances_list[substance_num - 1]
                        except ValueError:
                            print("❌ Por favor ingresa un número válido")
                            continue
                    elif search_choice == '2':
                        result = self.search_substance()
                        if not result:
                            continue
                        substance_key, substance_data = result
                    else:
                        print("❌ Opción inválida")
                        continue

                    self.show_constants(substance_key)
                    A = substance_data['A']
                    B = substance_data['B']
                    C = substance_data['C']
                    
                    # Realizar el cálculo
                    self.perform_calculation(choice, substance_key, A, B, C)

                else:
                    print("❌ Opción inválida. Por favor selecciona una opción del 1 al 6")

            except KeyboardInterrupt:
                print("\n\n👋 Programa interrumpido por el usuario")
                break
            except Exception as e:
                print(f"❌ Error inesperado: {e}")
                print("Por favor intenta nuevamente")

# Función principal para ejecutar el programa
def main():
    calculator = AntoineCalculator()
    calculator.run()

if __name__ == "__main__":
    main()