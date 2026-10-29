def calcular_media(notas: list[float]) -> float:
  """
  Calcula a média aritmética de uma lista de notas.

  Args:
      notas (list[float]): Lista contendo as notas do aluno.

  Returns:
      float: Média das notas.
      Retorna 0.0 caso a lista esteja vazia.
  """

  # Evita divisão por zero caso nenhuma nota seja informada
  if not notas:
      return 0.0

  soma_notas = sum(notas)
  quantidade_notas = len(notas)

  return soma_notas / quantidade_notas

if __name__ == "__main__":
