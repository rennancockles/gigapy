# VisionStore

Software desenvolvido como teste no processo seletivo da Gigalink. Para o desenvolvimento foram utilizados os seguintes recursos:

 * **S.O.**: Ubuntu
 * **Linguagem**: Python
 * **Banco de Dados**: MySQL
 * **Controle de Versão**: Git


## Usage

Para rodar o software basta executar o arquivo gigapy

```shell
./gigapy
```


## Info

Como se trata de um simples teste desenvolvi apenas algumas funções principais. Utilizei o banco de dados para salvar 
apenas dados de Produto, Transportadora, Fornecedor, Email e Telefone, deixando os dados de Pedido e Item apenas na 
memória.

Na classe Produto foi adicionado o campo valor para utilização como valor unitário do produto, deixando o campor valor 
da classe Item para representar um subTotal (valor_unitário * quantidade)

Utilizei umas formas básicas de validação em alguns campos, como por exemplo a utilização de regex para email e 
telefone,  e a validação de dados numéricos nos campos de valor e quantidade.
 
Por fim, existe muito mais que ainda pode ser feito no programa, mas fiz o bastante para mostrar meus conhecimentos e 
habilidades.