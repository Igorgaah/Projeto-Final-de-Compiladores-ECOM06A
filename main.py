from analisador_lexico import lexer
from analisador_sintatico import parser
import sys
import os

def analisar_arquivo(caminho_entrada, caminho_saida):
    with open(caminho_entrada, 'r', encoding='utf-8') as f:
        codigo = f.read()

    print(f"\n📥 Analisando: {caminho_entrada}")

    # Etapa 1: Análise Léxica
    lexer.input(codigo)
    tokens_reconhecidos = []

    print("\n🔍 Tokens reconhecidos:")
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_info = f"[{tok.type}] {tok.value}"
        tokens_reconhecidos.append(token_info)
        print(token_info)

    # Salva tokens reconhecidos em arquivo
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tokens_reconhecidos))

    print(f"\n✅ Tokens salvos em: {caminho_saida}")

    # Etapa 2: Análise Sintática
    print("\n🧠 Análise Sintática:")
    try:
        resultado = parser.parse(codigo)
        print("✅ Sintaxe válida!")
    except Exception as e:
        print(f"❌ Erro de sintaxe: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo_fonte.nl>")
        sys.exit(1)

    entrada = sys.argv[1]
    nome_base = os.path.basename(entrada).replace(".nl", "")
    saida = f"reconhecimentos/tokens_{nome_base}.txt"

    os.makedirs("reconhecimentos", exist_ok=True)

    analisar_arquivo(entrada, saida)
