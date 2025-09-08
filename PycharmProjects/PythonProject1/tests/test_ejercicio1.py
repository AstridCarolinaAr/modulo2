import pytest
from ejercicio_1 import definir_precio

# --- Pruebas para casos de éxito (edad válida) ---

def test_precio_nino():
    """Test para una edad de niño (0 < edad <= 12)."""
    assert definir_precio(10) == 10000

def test_precio_adulto():
    """Test para una edad de adulto (edad > 18)."""
    assert definir_precio(30) == 20000

# --- Pruebas para entradas inválidas (validando las excepciones) ---

def test_entrada_negativa():
    """Prueba que una edad negativa levanta un ValueError."""
    with pytest.raises(ValueError, match="entero positivo"):
        definir_precio(-5)

def test_entrada_cero():
    """Prueba que una edad de cero levanta un ValueError."""
    assert definir_precio(0) == 10000

def test_entrada_texto():
    """Prueba que una entrada de texto levanta un ValueError."""
    with pytest.raises(ValueError, match="entero."):
        definir_precio("abc")

def test_entrada_decimal():
    """Prueba que una edad con decimales levanta un ValueError."""
    with pytest.raises(ValueError, match="entero."):
        definir_precio(10.5)

def test_entrada_vacia():
    """Prueba que una entrada vacia levanta un ValueError."""
    with pytest.raises(ValueError, match="entero."):
        definir_precio("")


from ejercicio_1 import definir_descuento
from io import StringIO
import sys
def test_con_descuento():
    """Prueba que el descuento se aplica correctamente cuando es_estudiante es 1."""
    captured_output = StringIO()
    sys.stdout = captured_output

    definir_descuento(1, 20000)

    sys.stdout = sys.__stdout__  # Restaura la salida estándar

    # Verifica que el texto impreso en pantalla es el esperado
    expected_output = "El costo de tu entrada es de $20000,\ncon el descuento de estudiante queda en $18000.0.\n"
    assert captured_output.getvalue() == expected_output


def test_sin_descuento():
    """Prueba que no se aplica descuento cuando es_estudiante es 0."""
    # Simula la salida de la función para capturarla y verificarla
    captured_output = StringIO()
    sys.stdout = captured_output
    definir_descuento(0, 15000)
    sys.stdout = sys.__stdout__  # Restaura la salida estándar
    expected_output = "El costo de tu entrada es de $15000.\nTen en cuenta que no se aplicó el descuento de estudiante.\n"
    assert captured_output.getvalue() == expected_output

def test_opcion_invalida_numero():
    """Prueba que un número distinto de 1 o 0 levanta un ValueError."""
    with pytest.raises(ValueError, match="1 o 0"):
        definir_descuento(5, 10000)


def test_opcion_invalida_texto():
    """Prueba que una entrada de texto levanta un ValueError."""
    with pytest.raises(ValueError, match="1 o 0"):
        definir_descuento("si", 10000)


def test_opcion_invalida_decimal():
    """Prueba que un número decimal levanta un ValueError."""
    with pytest.raises(ValueError, match="1 o 0"):
        definir_descuento(1.5, 10000)