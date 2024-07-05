import unittest
from unittest.mock import patch
from io import StringIO
import sys
from datetime import date

# Função que será testada
def calcular_dias_para_o_natal(mes, dia):
    christmas = date(2016, 12, 25)
    current_date = date(2016, mes, dia)
    delta = (christmas - current_date).days
    
    if delta == 0:
        return "E natal!"
    elif delta == 1:
        return "E vespera de natal!"
    elif delta < 0:
        return "Ja passou!"
    else:
        return f"Faltam {delta} dias para o natal!"

class TestNatal(unittest.TestCase):
    
    @patch('sys.stdin', StringIO("12 25\n12 24\n12 26\n12 20\n"))
    def test_script(self):
        expected_output = "E natal!\nE vespera de natal!\nJa passou!\nFaltam 5 dias para o natal!\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            import main  # Executa o script principal
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_calcular_dias_para_o_natal(self):
        self.assertEqual(calcular_dias_para_o_natal(12, 25), "E natal!")
        self.assertEqual(calcular_dias_para_o_natal(12, 24), "E vespera de natal!")
        self.assertEqual(calcular_dias_para_o_natal(12, 26), "Ja passou!")
        self.assertEqual(calcular_dias_para_o_natal(12, 20), "Faltam 5 dias para o natal!")

if __name__ == "__main__":
    unittest.main()
