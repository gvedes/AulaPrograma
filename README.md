# Estoque Web

Uma aplicação web de gerenciamento de estoque desenvolvida com **Django** e estilizada com **Bulma CSS**.

## 📋 Descrição

A aplicação permite gerenciar:
- **Produtos**: Criar, listar, atualizar e deletar produtos com informações de nome, cor, descrição, preço e quantidade.
- **Entradas**: Registrar entradas de produtos no estoque (aumento de quantidade).
- **Saídas**: Registrar saídas de produtos do estoque (diminuição de quantidade).

A aplicação valida automaticamente que não haja saídas com quantidade maior que o estoque disponível.

## 🚀 Tecnologias

- **Backend**: Django 5.2.8
- **Frontend**: Bulma CSS 0.9.4
- **Database**: SQLite3
- **Python**: 3.12.3

## 📦 Dependências

As dependências principais estão em `requirements.txt`:
- Django
- asgiref
- sqlparse

## 🔧 Instalação e Configuração

### 1. Clonar o repositório
```bash
git clone https://github.com/gvedes/AulaPrograma.git
cd AulaPrograma
