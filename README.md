# SuperaDesafio-Python

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

