# Teste Prático — Desenvolvedor(a) Júnior Python/Django

## 1. Objetivo do teste

Este teste tem como objetivo avaliar sua capacidade de realizar uma pequena evolução em um projeto Django já existente, de forma funcional, organizada e coerente.

No dia a dia do MB, grande parte do trabalho envolve:
- entender requisitos simples de negócio
- alterar código existente
- ajustar models, views, templates e queries
- implementar mudanças com cuidado
- validar o comportamento da funcionalidade
- explicar com clareza o que foi feito

Este teste foi pensado para simular esse tipo de cenário de forma objetiva e justa.

---

## 2. Contexto

Você recebeu um projeto Django base já funcional com um módulo de clientes.

Atualmente:
- existe um model `Cliente`
- existe uma listagem de clientes
- os clientes cadastrados aparecem normalmente na tela

Precisamos evoluir esse projeto para permitir a **inativação e reativação de clientes**, além de ajustar a listagem para respeitar essa regra.

---

## 3. Desafio

Implementar a funcionalidade de **inativação de clientes**, fazendo com que clientes inativos não apareçam na listagem padrão.

---

## 4. Requisitos obrigatórios

### 4.1. Alteração no model
1. Adicionar ao model `Cliente` o campo `ativo`
2. Exibir apenas clientes ativos por padrão
3. Permitir visualizar todos os clientes com filtro opcional
4. Criar forma de inativar e reativar clientes
5. Criar pelo menos 2 testes automatizados
6. Atualizar o `seed_clientes` para gerar uma massa de dados
7. Separe o backend do frontend, para boas práticas de desenvolvimento:
- O frontend será feito em um novo projeto que irá acessar as informações deste projeto;
- O frontend deve ser feito em Angular e consumir endpoints do backend;
- Pode utilizar no backend o DRF (Django Rest Framework) para criação dos endpoints;
8. A melhor solução para este teste não é a mais complexa e sim:
- a mais simples;
- a mais clara;
- a mais funcional;
- a mais organizada;
9. Ao final, atualize este README com uma seção chamada "O que foi implementado", descrevendo brevemente:
- o que você fez;
- eventuais decisões tomadas;
- qualquer observação importante sobre sua implementação;
- como rodar o projeto completo, dividido em backend e frontend.
10. Você pode utilizar IA como apoio no desenvolvimento, porém esperamos que você:
- entenda o que implementou
- consiga explicar suas escolhas
- consiga responder perguntas simples sobre o próprio código
11. Junto com a entrega faça um vídeo de no máximo 10 minutos explicando o que foi feito, junto com as envidências do software rodando.

---

## 5. Bônus inicial:


```python
## Como rodar o projeto
```bash
python -m venv .venv
source .venv/bin/activate
pip install django
pip install djangorestframework
pip install django-cors-headers
python manage.py migrate
python manage.py runserver
```

## 6. O que foi implementado:

Foram realizadas evoluções no projeto Django original para permitir a inativação e reativação de clientes, além de preparar a aplicação para uma arquitetura com backend e frontend separados.

1. Alterações no model

Foi adicionado o campo ativo no model Cliente, permitindo controlar se um cliente está ativo ou inativo no sistema.

Clientes são criados como ativos por padrão

Clientes inativos permanecem armazenados no banco, mas não aparecem na listagem padrão

2. Ajuste na listagem de clientes

A listagem foi alterada para respeitar o status do cliente:

Por padrão, apenas clientes ativos são exibidos

Foi implementado um filtro opcional que permite visualizar todos os clientes, incluindo os inativos

Exemplo de uso do filtro:

/clientes/?mostrar_inativos=1
3. Inativação e reativação de clientes

Foram criadas rotas para alterar o status do cliente:

Inativar cliente

Reativar cliente

A alteração modifica o campo ativo do registro, preservando o histórico do cliente no banco de dados.

4. Atualização do seed de dados

O script seed_clientes foi atualizado para:

incluir o campo ativo

gerar massa de dados com clientes ativos e inativos

Isso facilita validar o comportamento da listagem e dos filtros.

5. Testes automatizados

Foram adicionados testes automatizados para validar regras principais do sistema:

clientes inativos não aparecem na listagem padrão

o filtro opcional permite visualizar todos os clientes

Os testes utilizam o framework de testes padrão do Django.

6. Separação entre backend e frontend

O projeto foi reorganizado para permitir uma arquitetura desacoplada.

Estrutura atual:

test_ms/
    backend/
        Django API
    frontend/
        Angular application

O backend será responsável por expor os dados via API, enquanto o frontend Angular consumirá esses endpoints.

Essa separação segue boas práticas modernas de desenvolvimento web, permitindo evolução independente entre as camadas.

# MS Test – API de Clientes

API simples para gerenciamento de clientes, permitindo listar, inativar e reativar registros.

1. Listar clientes
```
GET /api/clientes/
```
Opcional:
```
GET /api/clientes/?mostrar_inativos=1
```
2. Inativar cliente
```
PATCH /api/clientes/{id}/inativar/
```
Exemplo:
```
PATCH /api/clientes/1/inativar/
```
3. Reativar cliente
```
PATCH /api/clientes/{id}/reativar/
```
Exemplo:
```
PATCH /api/clientes/1/reativar/
```

## Frontend – Principais Decisões Técnicas

O frontend foi desenvolvido com **Angular utilizando componentes standalone**, priorizando simplicidade estrutural, reatividade e alinhamento com práticas modernas do framework.

### Arquitetura

A aplicação adota uma separação clara de responsabilidades:

* **Component**: controla o estado da interface e lê parâmetros da URL.
* **Service**: realiza a comunicação com a API.
* **Backend/API**: responsável pelas regras de negócio e persistência.

### Gerenciamento de Estado

O estado da lista de clientes é gerenciado com **Signals**, permitindo atualização automática da interface sempre que os dados mudam, sem necessidade de manipulação manual de change detection.

### Integração com a URL

O filtro de clientes inativos é controlado por **query parameters** (`?mostrar_inativos=1`).
O componente observa alterações na URL e recarrega os dados conforme necessário, permitindo:

* compartilhamento de links com filtros aplicados
* consistência após recarregar a página
* navegação alinhada ao histórico do navegador

### Comunicação com a API

O service encapsula a lógica de chamada da API e constrói a URL conforme o filtro selecionado, mantendo o componente desacoplado da lógica de requisição.

### Atualização de Dados

Após ações como ativar ou inativar clientes, a lista é recarregada preservando o filtro atual, garantindo consistência entre interface e dados retornados pela API.

---

Essa abordagem resulta em um frontend **simples, reativo e fácil de manter**, com uma estrutura adequada para evolução futura da aplicação.