import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5000
MENSAGENS_POR_CLIENTE = 5

def cliente_worker(id_cliente, resultados_tempos):
    """Lógica de um cliente individual."""
    inicio = time.time()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        
        for i in range(MENSAGENS_POR_CLIENTE):
            msg = f"Cliente {id_cliente} - mensagem {i}"
            s.sendall(msg.encode('utf-8'))
            resposta = s.recv(1024)
            
        s.close()
        fim = time.time()
       
        resultados_tempos.append(fim - inicio)
    except Exception as e:
        print(f"Erro no cliente {id_cliente}: {e}")

def executar_teste_carga(num_clientes):
    """Dispara N clientes simultâneos via Threads e mede o tempo."""
    threads = []
    tempos_clientes = []
    
    print(f"\n--- Iniciando teste com {num_clientes} clientes ---")
    tempo_inicio_total = time.time()

    
    for i in range(num_clientes):
        t = threading.Thread(target=cliente_worker, args=(i, tempos_clientes))
        threads.append(t)
        t.start()

   
    for t in threads:
        t.join()

    tempo_fim_total = time.time()
    tempo_total = tempo_fim_total - tempo_inicio_total
    tempo_medio = sum(tempos_clientes) / len(tempos_clientes) if tempos_clientes else 0

    print(f"Tempo total: {tempo_total:.4f}s")
    print(f"Tempo médio por cliente: {tempo_medio:.4f}s")
    
    return tempo_total, tempo_medio

if __name__ == "__main__":
    
    for n in [10, 50, 100]:
        executar_teste_carga(n)
        time.sleep(1)  # Pausa entre cenários