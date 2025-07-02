

## ✅ `README.md`

```markdown
# 🌀 Compilador NinLang - Analisador Léxico e Sintático

Este projeto implementa um analisador léxico e sintático para a linguagem fictícia **NinLang**, inspirada nos selos de mão do universo Naruto.

Trabalho desenvolvido para a disciplina de Compiladores, com base em regras gramaticais e exemplos práticos.

---

## 🔧 Tecnologias Utilizadas

- Python 3
- PLY (Python Lex-Yacc): biblioteca que simula o funcionamento de `Flex` e `Bison`.

---

## 📁 Estrutura do Projeto

```

```
Trabalho de Compiladores/
├── analisador\_lexico.py          # Lexer com reconhecimento de tokens e palavras reservadas
├── analisador\_sintatico.py       # Parser com árvore sintática abstrata (AST)
├── main.py                       # Interface principal de análise
├── programas\_exemplo/
│   ├── exemplo1.nl
│   ├── exemplo2.nl
│   ├── exemplo3.nl
│   └── exemplo4.nl
├── reconhecimentos/              # Geração automática dos tokens
└── README.md
```

````

---

## ▶️ Como Executar

### 1. Instale o PLY

No terminal ou prompt de comando:

```bash
pip install ply
````

---

### 2. Execute o analisador

No diretório raiz do projeto, use:

```bash
python main.py programas_exemplo/exemplo1.nl
```

> Substitua `exemplo1.nl` pelo arquivo desejado.

---

## 📌 O que o programa faz

* Realiza análise léxica, listando todos os tokens reconhecidos.
* Executa a análise sintática com base na gramática da NinLang.
* Informa se a sintaxe está válida ou inválida.
* Gera um arquivo `.txt` com os tokens reconhecidos na pasta `reconhecimentos/`.

---

## 🧪 Exemplos

### ✅ `exemplo1.nl`: declaração, atribuição e condição

```ninlang
Carneiro chakra Galo 100;
Tigre "Chakra atual:";
Tigre chakra;
Rato chakra > 50 {
    Tigre "Pode usar jutsu";
} Dragao {
    Tigre "Chakra insuficiente";
}
```

---

### ✅ `exemplo2.nl`: laço de repetição

```ninlang
Macaco contador Galo 0;
Cao limite Galo 3;

Cavalo contador < limite {
    Tigre contador;
    contador Galo contador Boi 1;
}
```

---

### ✅ `exemplo3.nl`: entrada de dados

```ninlang
Carneiro nome;
Cobra nome;
Tigre "O nome digitado foi:";
Tigre nome;
```

---

### ✅ `exemplo4.nl`: código completo com tudo

```ninlang
Macaco i Galo 0;
Macaco soma Galo 0;
Macaco limite;
Cobra limite;

Tigre "Contando até:";
Tigre limite;

Cavalo i < limite {
    i Galo i Boi 1;
    soma Galo soma Boi i;

    Rato i % 2 == 0 {
        Tigre "Número par:";
        Tigre i;
    } Dragao {
        Tigre "Número ímpar:";
        Tigre i;
    }
}

Tigre "Soma total:";
Tigre soma;
```

---

## ✍️ Desenvolvido por

* Igor Rafael Marcelo Morais
* Disciplina: ECOM06A– Compiladores
* Professor: Thatyana de Faria Piola Seraphim
* Período: 2025.1

```
