# SuperaDesafio-Python


# Título do Projeto

## Execução 

Não foi possível containerizar as aplicações. Mas, para fazer o banco de dados funcionar com os requesitos da aplicação, use os comandos:

`docker pull postgres`

`sudo docker run -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres` 

`docker exec -it <POSTGRES_CONTAINER_ID> bash`

` psql -U postgres` 

`CREATE DATABASE db_ps_supera;`

Todos os requesitos do back-end foram atendidos. Entretanto, parte do front-end, não. Como a parte de checkout e feedbacks visuais de remoções e adições de itens. Print das telas:

*PRINTS*

###  Informações adicionais
Pensei em usar alguma função como `LOAD DATA` presente em alguns outros banco de dados para a inserção automática do JSON. Mas, como não foi possivel, decidi adicionar manualmente os itens. Talvez uma forma de deixar esse processo automático seria fazer um loop que leria os dados do arquivo e com um `IF NOT EXISTS` adiociona-los para o banco.

Usei no front-end desse projeto alguns arquivos que criei em um outro projeto pessoal. 

Na parte do front-end criei uma pasta ` fake_cdn` para simular a existência de um CDN e não inserir as imagens diretas no banco.

Toda a parte lógica do back-end está no arquivo `views.py` dentro da pasta `api`

## Documentação da API

  ```
    POST api/signup/
  ``` 


| Parâmetros   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `{name ,email, password}` | `json` | Cria o usuário|


```
  POST api/get-token/
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{email, password}`      | `json` | Recebe o token de autenticação|


```
 POST api/cart/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
|    `{id_product}`   | `json` |Adiciona um produto baseado no ID no carrinho do usuário|

```
 DELETE api/cart/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{id_product}`      | `json` |Retira do carrinho um produto baseado no ID|

```
 POST cart/transactions/view/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{}`      | `json` |Retorna todos os items comprados pelo usuário|

```
 POST api/cart/checkout/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{}`      | `json` |Efetua checkout do carrinho do usuário e o deleta da tabela Cart|


```
 GET api/filter/price/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{}`      | `json` |Recebe todos os produtos ordenados por `price`|

```
 POST api/filter/score/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{}`      | `json` |Recebe todos os produtos ordenados por `score`|

```
 POST api/filter/name/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{}`      | `json` |Recebe todos os produtos ordenados por `name`|

