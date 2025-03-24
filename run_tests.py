import subprocess

def run_tests():
    # Lista de comandos de prueba
    test_commands = [
        "python manage.py test scraper.tests.test_admin",
        "python manage.py test scraper.tests.test_forms",
        "python manage.py test scraper.tests.test_models",
        "python manage.py test scraper.tests.test_services",
        "python manage.py test scraper.tests.test_views",
    ]

    # Resumen de resultados
    total_tests = 0
    total_passed = 0
    total_failed = 0

    # Ejecutar cada comando de prueba
    for command in test_commands:
        print(f"\nEjecutando: {command}")
        try:
            # Ejecutar el comando y capturar la salida
            result = subprocess.run(command, shell=True, text=True, capture_output=True, timeout=120)

            # Mostrar la salida estándar y de error
            print(result.stdout)
            if result.stderr:
                print(result.stderr)

            # Analizar la salida para obtener el número de tests ejecutados, pasados y fallados
            if "Ran" in result.stdout:
                lines = result.stdout.splitlines()
                for line in lines:
                    if "Ran" in line:
                        # Ejemplo: "Ran 5 tests in 0.123s"
                        parts = line.split()
                        num_tests = int(parts[1])  # Número de tests ejecutados
                        total_tests += num_tests
                        if "OK" in result.stdout:
                            total_passed += num_tests
                        elif "FAILED" in result.stdout:
                            failed_part = line.split("failures=")[-1].strip(")")
                            num_failed = int(failed_part)
                            total_failed += num_failed

            # Verificar el código de salida
            if result.returncode != 0:
                print(f"El comando falló con código de salida {result.returncode}: {command}")

        except subprocess.TimeoutExpired:
            print(f"El comando se excedió del tiempo límite y fue interrumpido: {command}")
        except Exception as e:
            print(f"Error al ejecutar el comando: {command}")
            print(e)

    # Mostrar el resumen final solo si se ejecutaron tests
    if total_tests > 0:
        print("\nResumen de pruebas:")
        print(f"Total de tests ejecutados: {total_tests}")
        print(f"Total de tests pasados: {total_passed}")
        print(f"Total de tests fallados: {total_failed}")

        # Indicar si todos los tests fueron satisfactorios
        if total_failed == 0:
            print("\n✅ Todos los tests fueron satisfactorios.")
        else:
            print("\n❌ Algunos tests fallaron.")

if __name__ == "__main__":
    run_tests()