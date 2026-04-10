# Making Of — Portfólio Django (Ficha 6)

> **Autor:** [Lourenço Madeira]  
> **Curso:** LEI — Lusófona  
> **Unidade Curricular:** Programação Web  


---

## Introdução

Este documento é o "diário de bordo" do processo de modelação do meu portfólio pessoal em Django.
Regista todas as decisões tomadas, erros identificados e corrigidos, e a evolução do modelo ao longo do tempo.

> **Nota sobre uso de IA:** Usei o Claude (Anthropic) como apoio para me ajudar no diagrama entidade-relação inicial e sugerir atributos para cada entidade. No entanto, todas as decisões finais foram minhas, e adaptei as sugestões ao meu caso concreto. Sou capaz de justificar cada opção tomada. Tambem usei a mesma para me auxiliar na criação mo Making of.

---

## Fotografia

![foto](media/makingof/Captura%20de%20ecrã%202026-04-07%20174115.png)

---

## Evolução do Modelo

### Versão 1 — Rascunho inicial

Na primeira versão identifiquei 7 entidades principais:
`Licenciatura`, `UnidadeCurricular`, `Projeto`, `Tecnologia`, `TFC`, `Competencia`, `Formacao`, `MakingOf`

**Problema encontrado:** Não tinha nenhum lugar para guardar informação dos docentes das UCs.  
O enunciado pedia para "identificar os docentes associados (incluindo ligação à página pessoal)".  
Inicialmente pensei em guardar o nome do docente como um campo de texto simples na entidade `UnidadeCurricular`.

---

### Versão 2 — Adição da entidade Docente

Decidi criar uma entidade separada `Docente` em vez de guardar só o nome como texto.

**Justificação:** Um docente pode lecionar várias UCs, e uma UC pode ter vários docentes.
Se guardasse apenas um campo `CharField` chamado `docente` na UC, não conseguiria representar isso corretamente — seria preciso escrever vários nomes separados por vírgulas, o que é má prática em bases de dados.
Com a entidade `Docente` e uma relação `ManyToManyField`, a estrutura fica correta e expansível.

Esta entidade serve também como **requisito adicional** pedido no enunciado.

---

### Versão 3 — Versão final 

Após validação pelo professor, o modelo ficou com 9 entidades:

```
Licenciatura → UnidadeCurricular ↔ Docente (extra)
UnidadeCurricular → Projeto ↔ Tecnologia
Competencia ↔ Projeto
Competencia ↔ Tecnologia
Formacao ↔ Competencia
TFC ↔ Tecnologia
MakingOf → (todas as entidades)
```

---

## Justificações de Modelação 



### Licenciatura

**Decisão 1 — Incluir o campo `sigla`**  
Justificação: No site da Lusófona e em contextos profissionais, os cursos são frequentemente referidos pela sigla (ex: LEI). Faz sentido guardar este campo separado do nome completo, para poder usar um ou outro conforme o contexto.

**Decisão 2 — Incluir o campo `url`**  
Justificação: O portfólio serve como cartão de visitas. Incluir o link para a página oficial do curso permite que quem visita o portfólio consulte mais informação sobre o curso, tornando o portfólio mais profissional.

---

### UnidadeCurricular

**Decisão 1 — Incluir `ano` e `semestre` separados**  
Justificação: Podia guardar apenas o semestre global (ex: semestre 3 = ano 2, semestre 1). Mas guardar `ano` e `semestre` separados torna as consultas muito mais simples — por exemplo, para mostrar todas as UCs do 2º ano basta filtrar `ano=2`.

**Decisão 2 — Incluir o campo `imagem`**  
Justificação: O enunciado pede explicitamente "Associe uma imagem a cada unidade curricular". Uma imagem representativa de cada UC torna o portfólio visualmente mais apelativo.

**Decisão 3 — Relação ManyToMany com Docente (e não ForeignKey)**  
Justificação: Uma UC pode ter vários docentes (ex: teórica e prática com professores diferentes), e um docente pode lecionar várias UCs. Por isso a relação correcta é N:N (ManyToManyField) e não 1:N (ForeignKey).

---

### Docente *(entidade adicional)*

**Decisão 1 — Criar entidade própria em vez de campo de texto**  
Justificação: Se guardasse os docentes como texto simples na UC, seria impossível pesquisar "todas as UCs de um docente" ou mostrar a página de um docente com as suas UCs. A entidade própria permite estas consultas e evita repetição de dados.

**Decisão 2 — Incluir `url_pagina`**  
Justificação: O enunciado pede explicitamente "ligação à página pessoal no site da Lusófona". Este campo permite que o visitante do portfólio aceda ao perfil oficial do docente.

---

### Projeto

**Decisão 1 — Incluir `url_github`**  
Justificação: O enunciado refere que o link para o repositório GitHub é "muito importante para entrevistas de emprego". É um dos campos mais importantes do portfólio, pois demonstra código real.

**Decisão 2 — Relação ForeignKey com UnidadeCurricular**  
Justificação: Cada projeto foi desenvolvido no âmbito de uma UC específica (ex: este portfólio é da UC de PW). Um projeto pertence a uma UC, mas uma UC pode ter vários projetos — relação 1:N, logo ForeignKey.

**Decisão 3 — Incluir `video_demo`**  
Justificação: Um vídeo de demonstração do projeto é muito mais expressivo do que apenas uma imagem ou descrição. Em entrevistas de emprego, mostrar o projeto a funcionar é uma vantagem.

---

### Tecnologia

**Decisão 1 — Incluir `nivel_interesse` como IntegerField (1 a 5)**  
Justificação: O enunciado pede "uma forma de representar o nível de interesse ou preferência". Optei por uma escala numérica de 1 a 5 porque é simples de usar no template (ex: mostrar estrelas), fácil de ordenar e comparar.

**Decisão 2 — Incluir `categoria`**  
Justificação: Há muitos tipos de tecnologias (linguagens, frameworks, bases de dados, ferramentas). Ter uma categoria permite agrupar e filtrar as tecnologias no portfólio, tornando a apresentação mais organizada.

---

### TFC

**Decisão 1 — Incluir `interesse` como BooleanField**  
Justificação: O enunciado pede "uma forma de classificar ou destacar os TFCs de maior interesse". Um campo booleano simples (True/False) permite marcar os favoritos e mostrá-los em destaque no portfólio.

**Decisão 2 — Organizar por `ano`**  
Justificação: Os TFCs são mais relevantes quando apresentados cronologicamente. Com o campo `ano` posso ordenar facilmente com `order_by('ano')`.

---

### Competencia

**Decisão 1 — Incluir `nivel` como CharField com escolhas**  
Justificação: Nos CVs as competências têm sempre um nível associado (Básico, Intermédio, Avançado). Este campo permite apresentar as competências de forma profissional, à semelhança de um CV real.

**Decisão 2 — Relação ManyToMany com Tecnologia e com Projeto**  
Justificação: Uma competência pode ser demonstrada em vários projetos (ex: "Programação em Python" aparece em vários projetos). E um projeto demonstra várias competências. O mesmo raciocínio se aplica às tecnologias.

---

### Formacao

**Decisão 1 — Incluir `data_inicio` e `data_fim` separados**  
Justificação: Com dois campos de data, posso ordenar cronologicamente (`order_by('data_inicio')`), calcular a duração da formação, e apresentar o percurso de forma timeline no portfólio.

**Decisão 2 — Incluir `certificado_url`**  
Justificação: Formações com certificado online (ex: Coursera, Udemy) têm um URL de verificação do certificado. Incluir este link torna a informação verificável por potenciais empregadores.

---

### MakingOf

**Decisão 1 — Incluir `entidade_relacionada` como CharField**  
Justificação: Cada entrada do Making Of documenta o processo de modelação de uma entidade específica. Este campo permite filtrar o Making Of por entidade — por exemplo, mostrar só os registos relacionados com a entidade `Projeto`.

**Decisão 2 — Incluir `uso_ia`**  
Justificação: O enunciado pede explicitamente que o uso de IA seja documentado. Este campo regista se e como foi usada IA em cada fase, garantindo transparência no processo.

---

## Erros Identificados e Correções

| # | Erro | Correção |
|---|---|---|
| 1 | Inicialmente guardei o nome do docente como texto simples (`CharField`) dentro da UC | Criei a entidade `Docente` com relação `ManyToManyField` |
| 2 | Não tinha nenhum campo para guardar imagens nas entidades que pediam (UC, Projeto, Tecnologia) | Adicionei `ImageField` nas entidades correspondentes e instalei o `pillow` |
| 3 | Na entidade `Formacao`, só tinha a data de fim, não conseguia ordenar cronologicamente de forma fiável | Adicionei `data_inicio` e passei a ordenar por este campo |
| 4 | A entidade `TFC` não tinha relação com `Tecnologia`, mas os TFCs usam tecnologias específicas | Adicionei relação `ManyToManyField` entre `TFC` e `Tecnologia` |

---

