##  Cálculo de Média de Notas

---

Temos um problema de programação simples, porém fundamental: desenvolver um algoritmo capaz de receber as notas de um aluno e calcular sua média final. 

O objetivo não é apenas resolver o problema, mas resolvê-lo seguindo um padrão rigoroso de qualidade de software.

---

##  O Problema
Escreva uma função que receba uma lista de notas (números reais) e retorne a média aritmética dessas notas. O código deve ser capaz de lidar com a possibilidade de a lista estar vazia para evitar erros de execução.

##  Fluxo de Avaliação

---

Todas as soluções submetidas ou propostas para este problema devem ser avaliadas sob os três pilares abaixo:

### 1. Precisão Lógica
 **O que avalia:** O código faz o que é suposto fazer de forma correta e matemática?
 **Critérios de aprovação:**
  - A soma das notas e a divisão pela quantidade de notas estão corretas.
  - O sistema não quebra se receber uma lista sem notas (evita o erro de "Divisão por Zero").
  - O sistema lida corretamente com números decimais (ponto flutuante).

### 2. Clareza e Eficiência
 **O que avalia:** O código é legível por humanos e gentil com a máquina?
 **Critérios de aprovação:**
  - Variáveis possuem nomes descritivos (ex: `soma_notas` em vez de `x`).
  - O código não utiliza loops desnecessários (complexidade de tempo $O(n)$ ou equivalente nativo).
  - Possui comentários apenas onde necessário para explicar o "porquê", não o "o quê".

### 3. Taxa de Alucinação
 **O que avalia:** A solução resolve *apenas* o problema proposto, sem inventar requisitos?
 **Critérios de aprovação (Taxa 0% desejada):**
  - Não importa bibliotecas externas pesadas (como `numpy` ou `pandas`) para um problema que pode ser resolvido com código nativo simples.
  - Não cria interfaces gráficas, conexões com banco de dados ou requisições web, a menos que explicitamente solicitado.
  - Mantém a fidelidade estrita à entrada (lista de notas) e saída (média).

---

2. Exemplo de um Código Funcion em Python.

def calcular_media(notas: list[float]) -> float:
    """
    Calcula a média aritmética de uma lista de notas.
    
    Args:
        notas (list[float]): Uma lista contendo as notas do aluno.
        
    Returns:
        float: A média das notas. Retorna 0.0 se a lista estiver vazia.
    """
    # Verificação de segurança para evitar divisão por zero
    if not notas:
        return 0.0
    
    # Lógica central: soma total dividida pela quantidade de itens
    soma_total = sum(notas)
    quantidade_notas = len(notas)
    
    return soma_total / quantidade_notas


# --- Testes de Validação ---
if __name__ == "__main__":
    # Teste 1: Fluxo normal
    notas_aluno = [8.5, 9.0, 7.5, 10.0]
    print(f"Notas: {notas_aluno} | Média: {calcular_media(notas_aluno)}") 
    # Saída esperada: 8.75

    # Teste 2: Lista vazia (Testando a Precisão Lógica)
    notas_vazias = []
    print(f"Notas: {notas_vazias} | Média: {calcular_media(notas_vazias)}") 
    # Saída esperada: 0.0

## Como este código pode atender o meu fluxo de avaliação

---

1. **Precisão Lógica:** Utiliza as funções matemáticas corretas e trata ativamente o erro clássico de divisão por zero (if not notas: return 0.0).

2. **Clareza e Eficiência:** Usa Tipagem (list[float], -> float), docstrings claras e as funções nativas altamente otimizadas do Python (sum() e len()).

3. **Taxa de Alucinação (0%):** Não importou o math, não criou classes desnecessárias (class Aluno:), nem pediu input() do usuário no meio da função matemática. Resolveu estritamente o problema dado.

---
