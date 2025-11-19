# 📊 Otimização de Portfólio de Projetos  
### FIAP – Engenharia de Software  
### Disciplina: Dynamic Programming | Prof. Marcelo Amorim  

---

## 📘 Introdução
Este projeto aborda o problema de **Otimização de Portfólio de Projetos**, onde uma empresa precisa selecionar o melhor conjunto de projetos considerando uma capacidade limitada de **Horas-Especialista**. O problema é uma aplicação direta do **0/1 Knapsack Problem**, e foi resolvido em **quatro fases**: Estratégia Gulosa, Recursiva Pura, Programação Dinâmica com Memoização e Programação Dinâmica Bottom-Up. Cada abordagem foi estudada, implementada e comparada quanto ao desempenho, precisão e comportamento diante de casos reais de teste.

---

## 🏗️ Fases Implementadas

### 📌 **Fase 1 – Estratégia Gulosa (Greedy)**
- Seleciona projetos com maior razão **Valor/Horas**.  
- Muito rápida e simples, porém **não garante a solução ótima**.  
- Falhou em dois dos quatro casos de teste.  

---

### 📌 **Fase 2 – Solução Recursiva Pura**
- Explora **todas as combinações** de projetos.  
- Sempre encontra o valor ótimo.  
- Complexidade exponencial **O(2ⁿ)** → inviável para muitos projetos.  

---

### 📌 **Fase 3 – Programação Dinâmica com Memoização**
- Otimiza a recursiva armazenando subproblemas já calculados.  
- Mantém precisão e reduz drasticamente o tempo de execução.  
- Complexidade **O(n × C)** → já eficiente.  

---

### 📌 **Fase 4 – Programação Dinâmica Bottom-Up (Iterativa)**
- Preenche uma tabela iterativa avaliando todas as capacidades e projetos.  
- **Mais eficiente e estável** entre todas as abordagens.  
- Não usa recursão e garante a solução ótima.  
- Considerada **a melhor solução do projeto**.  

---

## 🧪 Casos de Teste – Resumo dos Resultados

| Caso | Greedy | Recursiva | Memoização | Bottom-Up | Ótimo? |
|------|--------|------------|-------------|------------|---------|
| 1    | 29     | 29         | 29          | 29         | ✔      |
| 2    | 15 ❌  | 20          | 20          | 20         | ✔      |
| 3    | 48     | 48          | 48          | 48         | ✔      |
| 4    | 14 ❌  | 15          | 15          | 15         | ✔      |

✔ As três abordagens de Programação Dinâmica encontraram o valor ótimo  
❌ A abordagem Gulosa falhou em encontrar o ótimo em 2 dos 4 testes  

---

## 🏁 Melhor Solução do Projeto

### 🥇 **Programação Dinâmica Bottom-Up (Fase 4)**

A abordagem Bottom-Up é a melhor solução porque:

- Garante o valor ótimo em todos os casos.
- É a abordagem mais rápida e eficiente.
- Requer menos memória que a recursiva com memoização.
- Não utiliza recursão, evitando estouro de pilha e facilitando manutenção.
- É a mais adequada para aplicações reais em empresas com muitos projetos.

---

## 📚 Requisitos Atendidos

- ✔ Implementação correta das 4 fases (Greedy, Recursiva, Memoização, Bottom-Up)  
- ✔ Uso adequado de memoização (Fase 3)  
- ✔ Construção completa da tabela de DP (Fase 4)  
- ✔ Testes realizados com 4 casos diferentes  
- ✔ Demonstração de falha da abordagem Gulosa  
- ✔ Código amplamente comentado e explicativo  
- ✔ Documentação completa e clara conforme solicitado  

---

## 👩‍💻 Integrantes do Grupo

- **Eduardo Dallabella - 556803**  
- **Heloísa Real - 554535**  
- **Mariana Dourado - 550494**  

---

## 📄 Licença
Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina **Dynamic Programming – FIAP**.

