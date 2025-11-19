# otimizacao_portfolio.py

# Fase 1: Solução Gulosa (Greedy)
def greedy_solution(capacidade, projetos):
    """
    Implementação da solução gulosa para o problema de otimização de portfólio.
    A abordagem gulosa seleciona os projetos com a maior razão entre valor e horas de especialista
    até que a capacidade total de horas seja atingida.
    """
    # Ordena os projetos pela razão Valor/Horas em ordem decrescente
    projetos_ordenados = sorted(projetos, key=lambda x: x[1] / x[2], reverse=True)
    total_valor = 0
    total_horas = 0
    selecionados = []
    
    # Itera pelos projetos ordenados e seleciona até que a capacidade seja atingida
    for nome, valor, horas in projetos_ordenados:
        if total_horas + horas <= capacidade:
            selecionados.append(nome)
            total_valor += valor
            total_horas += horas
    
    # Retorna os projetos selecionados e o valor total
    print("Seleção Gulosa:", selecionados)
    print("Valor Total:", total_valor)
    return total_valor



# Fase 2: Solução Recursiva
def max_valor_recursivo(i, capacidade, projetos):
    """
    Solução recursiva pura para o problema de otimização de portfólio.
    Explora todas as combinações possíveis de projetos, retornando o valor máximo possível.
    """
    # Caso base: se não há mais projetos ou a capacidade é 0
    if i == 0 or capacidade == 0:
        return 0
    
    # Obtém o projeto atual
    nome, valor, horas = projetos[i - 1]
    
    # Se o projeto não pode ser incluído devido à capacidade
    if horas > capacidade:
        return max_valor_recursivo(i - 1, capacidade, projetos)
    
    # Caso contrário, retorna o máximo entre:
    # 1. Não incluir o projeto
    # 2. Incluir o projeto e reduzir a capacidade
    return max(valor + max_valor_recursivo(i - 1, capacidade - horas, projetos),
               max_valor_recursivo(i - 1, capacidade, projetos))

# Fase 3: Solução com Memoização
def max_valor_memo(i, capacidade, projetos, memo):
    """
    Solução recursiva com memoização para otimização de portfólio.
    Armazena os resultados dos subproblemas em um dicionário para evitar cálculos repetidos.
    """
    # Caso base: se não há mais projetos ou a capacidade é 0
    if i == 0 or capacidade == 0:
        return 0
    
    # Verifica se o subproblema já foi resolvido e armazenado no dicionário
    if (i, capacidade) in memo:
        return memo[(i, capacidade)]
    
    # Obtém o projeto atual
    nome, valor, horas = projetos[i - 1]
    
    # Se o projeto não pode ser incluído devido à capacidade
    if horas > capacidade:
        memo[(i, capacidade)] = max_valor_memo(i - 1, capacidade, projetos, memo)
    else:
        # Caso contrário, armazena o valor máximo entre incluir ou não o projeto
        memo[(i, capacidade)] = max(valor + max_valor_memo(i - 1, capacidade - horas, projetos, memo),
                                     max_valor_memo(i - 1, capacidade, projetos, memo))
    
    return memo[(i, capacidade)]

# Fase 4: Solução Bottom-Up (Iterativa)
def max_valor_bottom_up(capacidade, projetos):
    """
    Solução iterativa com Programação Dinâmica Bottom-Up.
    Utiliza uma tabela para armazenar os resultados dos subproblemas e encontrar a solução ótima.
    """
    n = len(projetos)
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenche a tabela com os resultados dos subproblemas
    for i in range(1, n + 1):
        nome, valor, horas = projetos[i - 1]
        for c in range(capacidade + 1):
            if horas > c:
                tabela[i][c] = tabela[i - 1][c]
            else:
                tabela[i][c] = max(tabela[i - 1][c], valor + tabela[i - 1][c - horas])

    # Retorna o valor máximo encontrado na tabela
    return tabela[n][capacidade]

# Bloco de Testes
if __name__ == "__main__":
    # Caso 1: Exemplo inicial
    capacidade1 = 10
    projetos1 = [("A", 12, 4), ("B", 10, 3), ("C", 7, 2), ("D", 4, 3)]

    # Caso 2: Outro conjunto de projetos com a mesma capacidade
    capacidade2 = 10
    projetos2 = [("X", 5, 2), ("Y", 8, 5), ("Z", 10, 4), ("W", 15, 7)]

    # Caso 3: Capacidade maior e mais projetos
    capacidade3 = 20
    projetos3 = [("P", 8, 5), ("Q", 10, 3), ("R", 6, 2), ("S", 20, 8), ("T", 12, 7)]

    # Caso 4: Capacidade pequena com projetos variados
    capacidade4 = 5
    projetos4 = [("A", 10, 3), ("B", 5, 2), ("C", 4, 1)]

    # Função para testar todas as soluções
    def testar_funcoes():
        print("Teste 1 - Caso 1 (Exemplo Inicial):")
        greedy_solution(capacidade1, projetos1)
        print("Valor Máximo (Recursivo):", max_valor_recursivo(len(projetos1), capacidade1, projetos1))
        memo1 = {}
        print("Valor Máximo (Memoização):", max_valor_memo(len(projetos1), capacidade1, projetos1, memo1))
        print("Valor Máximo (Bottom-Up):", max_valor_bottom_up(capacidade1, projetos1))

        print("\nTeste 2 - Caso 2 (Outro Conjunto de Projetos):")
        greedy_solution(capacidade2, projetos2)
        print("Valor Máximo (Recursivo):", max_valor_recursivo(len(projetos2), capacidade2, projetos2))
        memo2 = {}
        print("Valor Máximo (Memoização):", max_valor_memo(len(projetos2), capacidade2, projetos2, memo2))
        print("Valor Máximo (Bottom-Up):", max_valor_bottom_up(capacidade2, projetos2))

        print("\nTeste 3 - Caso 3 (Capacidade Maior e Mais Projetos):")
        greedy_solution(capacidade3, projetos3)
        print("Valor Máximo (Recursivo):", max_valor_recursivo(len(projetos3), capacidade3, projetos3))
        memo3 = {}
        print("Valor Máximo (Memoização):", max_valor_memo(len(projetos3), capacidade3, projetos3, memo3))
        print("Valor Máximo (Bottom-Up):", max_valor_bottom_up(capacidade3, projetos3))

        print("\nTeste 4 - Caso 4 (Capacidade Pequena):")
        greedy_solution(capacidade4, projetos4)
        print("Valor Máximo (Recursivo):", max_valor_recursivo(len(projetos4), capacidade4, projetos4))
        memo4 = {}
        print("Valor Máximo (Memoização):", max_valor_memo(len(projetos4), capacidade4, projetos4, memo4))
        print("Valor Máximo (Bottom-Up):", max_valor_bottom_up(capacidade4, projetos4))

    # Executando os testes
    testar_funcoes()
