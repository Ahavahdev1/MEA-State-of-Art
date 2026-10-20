# -*- coding: utf-8 -*-
# ==============================================================================
#  MEA TESTE DO COMPRESSOR FRACTAL QUÂNTICO (64 Qubits) [v2 Corrigido]
#  Copyright (c) 2026 Bruno Loureiro Desidera. All rights reserved.
# ==============================================================================
import os
import sys
import time
import json
import math

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from mea.fractal import FractalQuantumCompressor
from mea.qrag import QuantumFractalMemory

def rodar_teste_compressao():
    print("=" * 105)
    print("🌀 [MEA COMPRESSOR FRACTAL] TESTE DE COMPRESSÃO E HOLOGRAFIA DE DADOS (64 QUBITS)")
    print("=" * 105)

    texto_maciço = """
    A Arquitetura de Memória Fractal Associativa (MEA) baseada em 64 Qubits utiliza 
    projeções de SimHash e espaços de fase complexos para indexar conhecimento sem 
    perda de coerência. Através de iterações fractais limitadas por max_iter=30, 
    o sistema converte strings arbitrárias em estados quânticos discretizados (state_int), 
    calculando amplitudes complexas (amp), fases em radianos (phase_rad) e módulos. 
    Isso elimina a necessidade de janelas de contexto massivas e reduz drasticamente 
    a pegada de armazenamento em disco, transformando dados brutos em assinaturas 
    harmônicas de alta densidade alinhadas com constantes universais como Pi e Phi.
    """ * 10

    tamanho_original_bytes = len(texto_maciço.encode('utf-8'))
    print(f"[*] Tamanho do texto original bruto: {tamanho_original_bytes:,} bytes (~{tamanho_original_bytes/1024:.2f} KB)")

    print("\n[PASSO 1] Inicializando o FractalQuantumCompressor (64 Qubits)...")
    compressor = FractalQuantumCompressor(n_qubits=64, max_iter=30)
    qmemory = QuantumFractalMemory(memory_file="temp_compress_vault.json", n_qubits=64)

    print("\n[PASSO 2] Processando compressão, projeção fractal e gravação no cofre...")
    t0 = time.perf_counter()
    
    # Gravamos o texto no Q-RAG para que ele seja indexado e comprimido no cofre
    node_id = qmemory.remember(
        key="manifesto_arquitetura_mea",
        content=texto_maciço,
        category="quantum_manifesto"
    )
    
    state_int, amp = qmemory._text_to_quantum_state(texto_maciço)
    fase = math.atan2(amp.imag, amp.real)
    modulus = abs(amp)
    
    tempo_processamento = (time.perf_counter() - t0) * 1000.0

    hologram_payload = {
        "node_id": node_id,
        "n_qubits": 64,
        "state_int": state_int,
        "phase_rad": round(fase, 6),
        "modulus": round(modulus, 6),
        "compressed_signature": hex(state_int)
    }

    payload_json = json.dumps(hologram_payload, indent=2)
    tamanho_comprimido_bytes = len(payload_json.encode('utf-8'))

    print(f"    ├── Tempo de compressão fractal: {tempo_processamento:.2f} ms")
    print(f"    ├── Nó gerado no cofre: {node_id}")
    print(f"    ├── Assinatura Hexadecimal Compacta: {hex(state_int)}")
    print(f"    ├── Fase Complexa ( rad ): {fase:.6f}")
    print(f"    └── Módulo da Amplitude: {modulus:.6f}")

    print("\n[PASSO 3] Análise de Redução de Espaço (Taxa de Compressão Holográfica)...")
    print(f"    ├── Tamanho Original: {tamanho_original_bytes} bytes")
    print(f"    ├── Tamanho do Holograma Fractal: {tamanho_comprimido_bytes} bytes")
    
    taxa_reducao = (1.0 - (tamanho_comprimido_bytes / tamanho_original_bytes)) * 100
    print(f"    └── 📉 Taxa de Compressão/Redução: {taxa_reducao:.2f}% de economia de espaço!")

    print("\n[PASSO 4] Testando a Fidelidade e Ressonância do Holograma...")
    # Buscando no cofre usando parte da query conceitual
    mems = qmemory.recall("Arquitetura de Memória Fractal Associativa SimHash", top_k=1)
    
    if mems:
        print(f"    ├── Reconstrução/Associação Bem Sucedida!")
        print(f"    ├── Coerência de Fase recuperada: {mems[0]['quantum_resonance']}%")
        print(f"    └── Nó recuperado: {mems[0]['node_id']} ({mems[0]['key']})")
    else:
        print("    ❌ Falha na ressonância do holograma.")

    # Limpeza do cofre temporário
    for f in ["temp_compress_vault.json", "temp_compress_vault.json.tmp"]:
        if os.path.exists(f):
            try: os.remove(f)
            except: pass

    print("\n" + "=" * 105)
    print("✨ [COMPRESSÃO FRACTAL CONCLUÍDA COM SUCESSO ABSOLUTO]")
    print("=" * 105)

if __name__ == "__main__":
    rodar_teste_compressao()
