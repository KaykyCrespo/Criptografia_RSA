# Criptografia-RSA

Projeto universitário de demonstração de criptografia RSA, com uma interface web que executa Python no navegador por meio do PyScript.

## Objetivo

Explorar conceitos de criptografia assimétrica, geração de chaves e transformação de mensagens, conectando uma implementação acadêmica em Python a uma interface em HTML, CSS e JavaScript.

**Uso educacional:** esta implementação não deve ser utilizada para proteger informações reais, senhas ou dados pessoais. Não equivale a uma biblioteca criptográfica segura para produção.

## Funcionalidades

- Criptografia e descriptografia RSA didáticas.
- Cifras simétricas implementadas em Python puro, sem bibliotecas externas: DES, Twofish-128 e SAFER K-64.
- DES, Twofish e SAFER usam CBC com padding PKCS#7, chave e IV aleatórios; chave e IV são exibidos em hexadecimal para permitir a transferência entre os painéis.
- Simulação textual das etapas conceituais de um handshake TLS. Ela não cria certificados, segredos, conexão ou tráfego TLS real, e não cifra mensagens.
- Transferência dos dados entre os campos, validação de entradas e controles para revelar os resultados.

O RSA e as cifras são demonstrações educacionais, não implementações para proteger dados reais.

## Tecnologias

- **Python:** implementações didáticas com módulos da biblioteca padrão; nenhuma dependência criptográfica externa.
- **PyScript:** execução de Python e interação com a página no navegador.
- **HTML e CSS:** estrutura e apresentação da interface.
- **JavaScript:** interações da interface.
- **Bootstrap Icons e Google Fonts:** ícones e fontes carregados externamente.

## Organização dos arquivos

| Arquivo | Responsabilidade |
| --- | --- |
| [index.html](index.html) | Página principal e carregamento dos recursos. |
| [styles.css](styles.css) | Estilos responsivos da interface. |
| [app.js](app.js) | Interações da interface e avisos dos métodos ainda indisponíveis. |
| [rsa_web.py](rsa_web.py) | Lógica Python integrada ao navegador via PyScript. |
| [cipher_methods.py](cipher_methods.py) | DES, Twofish-128 e SAFER K-64, CBC/PKCS#7 e sequência descritiva da simulação TLS. |
| [test_cipher_methods.py](test_cipher_methods.py) | Vetores conhecidos e testes de ida e volta das cifras simétricas. |
| [rsa_terminal_demo.py](rsa_terminal_demo.py) | Experimento independente de linha de comando, não carregado pela página. A rotina de saída tem um erro conhecido e não é recomendada como caminho de execução. |

## Como executar a interface

### Pré-requisitos

- Navegador atualizado.
- Conexão com a internet para carregar PyScript, fontes e bibliotecas de ícones.
- Um servidor HTTP local, como a extensão **Live Server** do VS Code.
- Não é necessário instalar pacotes Python para os métodos deste projeto.

### Com Live Server

1. Clone ou baixe o repositório e abra a pasta no VS Code.
2. Instale a extensão Live Server, caso ainda não esteja disponível.
3. Clique com o botão direito em `index.html` e selecione **Open with Live Server**.
4. Aguarde o carregamento do PyScript no navegador. A versão usada pela página e os recursos visuais externos precisam de conexão com a internet.

### Alternativa com Python 3

Na pasta do projeto, execute:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Abra <http://localhost:8000/index.html>. Para encerrar o servidor, pressione `Ctrl+C` no terminal.

`rsa_web.py` depende do ambiente do navegador e não deve ser executado diretamente com `python rsa_web.py`.

## Exemplo de uso

1. Selecione RSA, DES, Twofish ou SAFER e escreva uma mensagem fictícia.
2. Clique em **Criptografar**. Para DES, Twofish e SAFER, a chave e o IV são mostrados em hexadecimal.
3. Use o botão de transferência para preencher a área de descriptografia com o texto cifrado, a chave e o IV.
4. Selecione o mesmo método na segunda área e clique em **Descriptografar**.
5. Para TLS, selecione essa opção e execute a simulação do handshake. Essa ação apenas apresenta etapas conceituais.

Não utilize dados confidenciais nos exemplos nem publique capturas contendo chaves ou mensagens reais.

### Testes das cifras

Com Python 3 instalado, execute na pasta do projeto:

```sh
python -m unittest test_cipher_methods.py
```

Os testes incluem vetores conhecidos de DES, Twofish-128 e SAFER K-64 e verificam o retorno de mensagens UTF-8 em CBC.

## Limitações e pendências

- A pasta `imagens/` não está presente nesta versão. A interface principal não depende dessas imagens; `app.js` ainda contém funções do tutorial antigo que mencionam arquivos desse diretório, mas elas não são chamadas pela página atual.
- O projeto depende de uma versão antiga de pré-lançamento do PyScript (`2023.09.1.RC1`), carregada de um endereço externo. A disponibilidade e a compatibilidade precisam ser verificadas antes de uma apresentação.
- RSA usa primos pequenos, `random`, não aplica padding e apresenta `(n, p)` como chave pública, em vez do par RSA `(n, e)`.
- A seleção aleatória de primos pode acessar um índice fora dos limites da lista; também não garante primos distintos nem um módulo maior que todos os bytes da mensagem. Por isso, o fluxo demonstrado pode falhar em outras execuções ou mensagens.
- DES está obsoleto e possui chave efetiva de apenas 56 bits. CBC com padding não autentica o ciphertext; nenhuma cifra simétrica desta demonstração deve proteger dados reais.
- Twofish-128 e SAFER K-64 passaram vetores conhecidos e testes locais, mas continuam sendo implementações acadêmicas próprias, sem análise de segurança ou proteção contra ataques por canal lateral.
- A opção TLS é apenas uma simulação de passos conceituais, não uma implementação do protocolo.
- O teste no navegador confirmou a ida e volta dos quatro métodos de cifra para uma mensagem UTF-8 fictícia; isso não certifica segurança.
- `rsa_terminal_demo.py` contém uma rotina de descriptografia que tenta chamar `.append()` no resultado convertido para `bytes`; o script de terminal pode falhar ao concluir a saída.
- Capturas de tela foram omitidas porque os arquivos de imagem originais não estão no repositório.

## Autoria

Responsável por esta versão: **Kayky Crespo dos Santos**.

Colaboradores creditados na versão acadêmica original:

- Kayky Crespo
- Caio Pacheco
- Lucas Jesus
- Guilherme Nobre
- Gabriel Cipriano

## Cuidados com o repositório

Não versione credenciais, chaves privadas reais, arquivos `.env`, ambientes virtuais ou caches. O `.gitignore` ajuda a prevenir inclusões acidentais, mas não remove arquivos já rastreados nem segredos do histórico.

Caso uma credencial seja publicada, revogue ou substitua a credencial antes de tratar sua remoção do histórico.

Registre apenas alterações reais, com mensagens que expliquem sua finalidade, como `docs: documenta execução e limitações do projeto RSA`. Preserve os créditos dos colaboradores e não crie commits apenas para aumentar o gráfico de contribuições.
