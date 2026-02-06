# 📺 Catálogo de Séries — API com FastAPI

## 🧠 Como foi meu processo

Alguns pontos importantes do meu processo:

- Sou iniciante em desenvolvimento
- Pensar sozinho o que fazer e como estruturar ainda é desafiador
- Consigo entender melhor a lógica quando vejo o código e acompanho o fluxo
- Usei bastante sugestões inline do editor para conseguir avançar
- Tive dúvidas, como:  
    
- Como os arquivos se conectam entre si
- Por que algumas funções existem mesmo sem serem chamadas diretamente pelas rotas
- Qual função deveria ser usada em cada caso (ex: leitura de dados)
    
- Em momentos fiquei confuso e precisei revisar, mas essas dúvidas ajudaram a entender melhor a separação de responsabilidades e organização.

## 🗂️ Organização do projeto

O projeto foi organizado em pastas para facilitar o entendimento e a manutenção:

- routes/ → definição das rotas da API
- app/ → modelos de dados e validação
- data/ → arquivos de persistência

Essa parte foi a que mais passei tempo pensando como estruturar
Quis fazer uma organização mais complexa, porém não tive visão para fazer isso de forma eficiente, então optei por uma estrutura mais simples, mas que ainda assim separa algumas responsabilidades.
A organização me ajuda a enxergar melhor o papel de cada parte do sistema, mesmo que eu ainda não tenha total clareza de como tudo se conecta.

## 📌 Aprendizados principais

- Entender melhor como APIs são estruturadas
- Trabalhar com validação de dados usando Pydantic
- Diferenciar persistência em arquivo e em banco de dados
- Criar rotas HTTP com tratamento de erros
  
## 🤯 Maior desafio

Foi entender que o SQLite e o JSON não são usados ao mesmo tempo, mas sim como opções de persistência. No início, fiquei confuso achando que ambos deveriam ser usados juntos, mas depois entendi que são alternativas para armazenar os dados.

## 📎 Observação final

Este repositório faz parte do meu processo de aprendizado em programação do zero.
Foi um processo de muitas tentativas, ajustes, dúvidas e evolução.

## 📝 Nota sobre autoria

Este README foi redigido com apoio de uma ferramenta de IA, com base nas minhas próprias explicações, dúvidas e reflexões durante o desenvolvimento do projeto, e revisado por mim para garantir que represente fielmente meu processo de aprendizado.