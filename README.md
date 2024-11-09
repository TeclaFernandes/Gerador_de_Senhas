# Gerador de Senhas

Este projeto é um aplicativo simples em Python, com uma interface gráfica desenvolvida em Tkinter, que gera uma senha baseada na data atual.

## Como funciona

A senha é gerada ao multiplicar o dia, o mês e o ano da data atual (no formato DD/MM/AAAA). Cada vez que o botão "Gerar Senha" é pressionado, a senha é calculada e exibida na tela.

## Tecnologias utilizadas

- **Python 3.x**
- **Tkinter:** Biblioteca padrão para criação de interfaces gráficas em Python.

## Funcionalidades

- **Gerar Senha:** Calcula uma senha com base na data atual e exibe o resultado na tela.

## Requisitos

- Python 3.x

## Como executar

1. Clone este repositório em seu ambiente local:

```bash
git clone https://github.com/seu_usuario/nome_do_repositorio.git
```
2. Navegue até o diretório do projeto:

```bash
cd nome_do_repositorio
```
3. Execute o código:

```bash
python nome_do_arquivo.py
```
Uma janela será aberta com o botão "Gerar Senha". Clique no botão para gerar e visualizar a senha baseada na data atual.

## Estrutura do Código

- **Função** `gerar_senha():` Calcula a senha multiplicando o dia, mês e ano da data atual.
- **Função** `exibir_senha():` Chama `gerar_senha()` e exibe o resultado na interface.
- **Interface Gráfica:** Utiliza o Tkinter para criar uma janela simples com um botão e uma área de texto para exibir a senha.

## Exemplo de Saída

Se a data atual for 09/11/2024, a senha gerada será:

```yaml
09 * 11 * 2024 = 200376
```
> Nota: A senha muda diariamente, de acordo com a data atual.

## Licença
Este projeto é licenciado sob a Licença MIT.

