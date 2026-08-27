# Relatório de Análise de Concorrência e Carga

## 1. Resultados dos Testes

| Modelo de Servidor | N Clientes | Tempo Total (s) | Tempo Médio/Cliente (s) |
|--------------------|------------|-----------------|-------------------------|
| Multicliente (Threads) | 10  | # Relatório de Análise de Concorrência e Carga

## 1. Resultados dos Testes

| Modelo de Servidor | N Clientes | Tempo Total (s) | Tempo Médio/Cliente (s) |
|--------------------|------------|-----------------|-------------------------|
| Multicliente (Threads) | 10  | 0.0048s | 0.0022s |
| Multicliente (Threads) | 50  | 0.0031s | 0.0061s |
| Multicliente (Threads) | 100 | 0.0575s | 0.0115s |
| Single-thread (Aula 2) | 10  | 0.0279s | 0.0000s |

---

## 2. Análise Técnica

### Onde e por que o servidor Single-Thread trava?
No servidor single-thread (Aula 2), chamadas como `accept()` e `recv()` são **bloqueantes**[cite: 1]. Enquanto o servidor processa as requisições do primeiro cliente, **todos os outros clientes subsequentes ficam aguardando na fila de conexões**[cite: 1]. Se um único cliente demorar ou mantiver a conexão aberta, todo o serviço fica travado para os demais[cite: 1].

### O ganho com a Abordagem Multicliente
No `servidor_multicliente.py`, o laço principal executa o `accept()`, **cria imediatamente uma nova thread dedicada** para o cliente conectado e retorna ao laço principal[cite: 1]. 

* O laço principal nunca fica bloqueado no atendimento de um cliente[cite: 1].
* Chamadas I/O bloqueantes entram em espera paralelamente/concorrentemente por thread, permitindo que a CPU reveze o processamento entre múltiplos clientes de forma rápida[cite: 1]. | 0.004s |
| Multicliente (Threads) | 50  | 0.12s | 0.008s |
| Multicliente (Threads) | 100 | 0.25s | 0.015s |
| Single-thread (Aula 2) | 10  | 0.50s | 0.050s |

---

## 2. Análise Técnica

### Onde e por que o servidor Single-Thread trava?
No servidor single-thread (Aula 2), chamadas como `accept()` e `recv()` são **bloqueantes**[cite: 1]. Enquanto o servidor processa as requisições do primeiro cliente, **todos os outros clientes subsequentes ficam aguardando na fila de conexões**[cite: 1]. Se um único cliente demorar ou mantiver a conexão aberta, todo o serviço fica travado para os demais[cite: 1].

### O ganho com a Abordagem Multicliente
No `servidor_multicliente.py`, o laço principal executa o `accept()`, **cria imediatamente uma nova thread dedicada** para o cliente conectado e retorna ao laço principal[cite: 1]. 

* O laço principal nunca fica bloqueado no atendimento de um cliente[cite: 1].
* Chamadas I/O bloqueantes entram em espera paralelamente/concorrentemente por thread, permitindo que a CPU reveze o processamento entre múltiplos clientes de forma rápida[cite: 1].