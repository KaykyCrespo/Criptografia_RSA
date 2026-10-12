# Criptografia-RSA

Projeto universitário de demonstração de criptografia RSA, com uma interface web que executa Python no navegador por meio do PyScript.

## Objetivo

Explorar conceitos de criptografia assimétrica, geração de chaves e transformação de mensagens, conectando uma implementação acadêmica em Python a uma interface em HTML, CSS e JavaScript.

**Uso educacional:** esta implementação não deve ser utilizada para proteger informações reais, senhas ou dados pessoais. Não equivale a uma biblioteca criptográfica segura para produção.

## Funcionalidades

- Interface para criptografar e descriptografar mensagens com a demonstração RSA.
- Exibição dos valores apresentados pela implementação como chaves e da mensagem cifrada.
- Transferência dos dados entre os campos de criptografia e descriptografia.
- Mensagens de validação para campos obrigatórios.
- Controles para ocultar e exibir informações na interface.

Os outros métodos exibidos na interface estão indicados como em desenvolvimento; não devem ser considerados implementados. O RSA usado aqui é uma demonstração didática, não uma implementação interoperável ou segura de RSA.

## Tecnologias

- **Python:** lógica acadêmica de criptografia.
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
| [rsa_terminal_demo.py](rsa_terminal_demo.py) | Experimento independente de linha de comando, não carregado pela página. A rotina de saída tem um erro conhecido e não é recomendada como caminho de execução. |

## Como executar a interface

### Pré-requisitos

- Navegador atualizado.
- Conexão com a internet para carregar PyScript, fontes e bibliotecas de ícones.
- Um servidor HTTP local, como a extensão **Live Server** do VS Code.

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

1. Selecione RSA na área de criptografia.
2. Digite uma mensagem fictícia, como `Mensagem de exemplo`, e clique em **ENCRIPTOGRAFAR**.
3. Confira a mensagem criptografada e os valores de chaves apresentados.
4. Use o controle de transferência de dados para preencher a área de descriptografia.
5. Na área **Descriptografar**, mantenha RSA selecionado e acione **Descriptografar** para comparar o resultado com a mensagem original. O botão de transferência preenche os campos automaticamente.

Não utilize dados confidenciais nos exemplos nem publique capturas contendo chaves ou mensagens reais.

## Limitações e pendências

- A pasta `imagens/` não está presente nesta versão. A interface principal não depende dessas imagens; `app.js` ainda contém funções do tutorial antigo que mencionam arquivos desse diretório, mas elas não são chamadas pela página atual.
- O projeto depende de uma versão antiga de pré-lançamento do PyScript (`2023.09.1.RC1`), carregada de um endereço externo. A disponibilidade e a compatibilidade precisam ser verificadas antes de uma apresentação.
- A rotina usa RSA elementar, sem padding, primos pequenos e `random`. Além de não oferecer segurança, a chave exibida como pública é `(n, p)` em vez do par RSA `(n, e)`.
- A seleção aleatória de primos pode acessar um índice fora dos limites da lista; também não garante primos distintos nem um módulo maior que todos os bytes da mensagem. Por isso, o fluxo demonstrado pode falhar em outras execuções ou mensagens.
- O teste do navegador confirmou uma ida e volta com a mensagem de exemplo, mas não cobre essas combinações aleatórias nem certifica a implementação.
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
