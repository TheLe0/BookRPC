Universidade de Caxias do Sul

Área de Ciências Exatas e Engenharias

Cidade Universitária / Campus Universitário da Região dos Vinhedos

Disciplina: CIC4004 – Programação Concorrente, Paralela e Distribuída

Professores: André Martinotto e Daniel Notari

Especificação do Trabalho I – 2020-4

O trabalho consiste no desenvolvimento de um programa servidor que implemente um Sistema de Consulta de Livros, sendo acessado via Sockets e via RPC (RMI). Os dados estão organizados em um arquivo SQL gerado através do SGBDR PostgreSQL. A estrutura dos dados envolve: Código do livro, Título do livro, Autor do livro, Edição do livro e Ano de Publicação. As informações dos livros deverão ser persistidas em arquivos ou em um banco de dados.

As operações possíveis são:

* Criar livro: recebe como parâmetro as informação do livro e retorna se foi possível inserir o livro ou uma mensagem de erro.
* Consultar livro: deverá permitir consultas pelo nome do autor (completo e parcial) e pelo título do livro (completo e parcial). No caso de consultas pelo nome parcial, deverá retornar todos os livros que atendam a consultam em ordem alfabética pelo nome. Caso o contato não exista, imprima uma mensagem de erro.
* Consultar por ano e número da edição: deverá retornar o nome de todos os livros em ordem alfabética pelo nome.
* Remover livro: deve permitir a remoção do livro através do título completo. Caso o contato não exista, imprima uma mensagem de erro.
* Alteração do Livro: deverá permitir alterações por nome e título completo do livro, edição e ano de publicação. Caso o contato não exista, imprima uma mensagem de erro.

