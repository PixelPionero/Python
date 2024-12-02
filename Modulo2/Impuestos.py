from colorama import Fore, Style, init # type: ignore

# Inicializa Colorama
init(autoreset=True)

def calcular_deducciones(salario_mensual):
    # Definir tasas de deducción
    tasa_impuesto_renta = 0.10  # 10%
    tasa_seguro = 0.16          # 16%
    tasa_pension = 0.07         # 7%

    # Calcular deducciones
    impuesto_renta = salario_mensual * tasa_impuesto_renta
    seguro = salario_mensual * tasa_seguro
    pension = salario_mensual * tasa_pension

    # Calcular salario neto
    salario_neto = salario_mensual - (impuesto_renta + seguro + pension)

    return impuesto_renta, seguro, pension, salario_neto

def mostrar_resultados(salario_mensual, deducciones):
    impuesto_renta, seguro, pension, salario_neto = deducciones

    print(Fore.CYAN + "=" * 30)
    print(Fore.GREEN + "Cálculo de Deducciones")
    print(Fore.CYAN + "=" * 30)
    print(f"{Fore.YELLOW}Salario Mensual: ${salario_mensual:.2f}")
    print(f"{Fore.RED}Impuesto sobre la Renta (10%): ${impuesto_renta:.2f}")
    print(f"{Fore.BLUE}Seguro (16%): ${seguro:.2f}")
    print(f"{Fore.MAGENTA}Pensión (7%): ${pension:.2f}")
    print(Fore.CYAN + "=" * 30)
    print(f"{Fore.GREEN}Salario Neto: ${salario_neto:.2f}")
    print(Fore.CYAN + "=" * 30)

def main():
    try:
        salario_mensual = float(input(Fore.CYAN + "Ingrese su salario mensual: $"))
        deducciones = calcular_deducciones(salario_mensual)
        mostrar_resultados(salario_mensual, deducciones)
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()
