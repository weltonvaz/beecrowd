def troco_possivel(valor_compra: int, valor_pago: int) -> bool:
  """
  Verifica se é possível devolver o troco exato de uma compra utilizando apenas duas notas.

  Argumentos:
    valor_compra (int): O valor da compra.
    valor_pago (int): O valor pago pelo cliente.

  Retorno:
    bool: True se for possível devolver o troco exato, False caso contrário.
  """
  troco = valor_pago - valor_compra

  if troco == 0:
    return True

  notas_disponiveis = [100, 50, 20, 10, 5, 2]

  for nota in notas_disponiveis:
    if troco >= nota:
      troco -= nota
      if troco == 0:
        return True

  return False

import pytest

def test_troco_possivel_exemplos_corretos():
  casos_de_teste = [
    (11, 23),
    (500, 650),
    (9948, 9963),
    (12, 20),
    (24, 50),
    (0, 10),
  ]

  for valor_compra, valor_pago in casos_de_teste:
    assert troco_possivel(valor_compra, valor_pago) is True

def test_troco_possivel_exemplos_incorretos():
  casos_de_teste = [
    (100, 600),
    (1, 2),
    (2, 4),
    (0, 0),
  ]

  for valor_compra, valor_pago in casos_de_teste:
    assert troco_possivel(valor_compra, valor_pago) is False

def test_troco_possivel_valor_compra_negativo():
  with pytest.raises(ValueError):
    troco_possivel(-10, 20)

def test_troco_possivel_valor_pago_negativo():
  with pytest.raises(ValueError):
    troco_possivel(10, -20)

def test_troco_possivel_valor_pago_menor_que_valor_compra():
  with pytest.raises(ValueError):
    troco_possivel(20, 10)
