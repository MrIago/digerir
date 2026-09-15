---
name: digerir
description: Compila muitas fontes espalhadas (vídeos, PDFs, transcrições, artigos, conversas, documentos) num único estudo digerido — como se você tivesse assistido tudo, anotado, conectado os pontos e agora fosse ensinar. Elimina redundância sem perder conteúdo, organiza por profundidade em vez de por fonte, e marca explicitamente onde as fontes concordam, se complementam, se ramificam e se contradizem. Use quando o Iago pedir "digerir", "compila tudo", "junta isso num texto só", "monta um estudo/aula/livro-texto disso", "elimina as redundâncias", "conecta os pontos", ou quando uma conversa acumulou material de várias fontes e ele quer o resultado num documento único — mesmo sem citar a skill.
argument-hint: [o que compilar, ou nada se o material já está na conversa]
---

# digerir: de muitas fontes para um estudo

O pedido original, nas palavras dele:

> "Compila tudo em um único texto eliminando as redundâncias, como um estudo geral: como se eu tivesse assistido tudo, anotado, conectado os pontos, e tivesse que ensinar pra alguém. Eu não falaria o mesmo conteúdo de todos, pois cada um tem coisas iguais que não precisa repetir, ou que se conectam, ou que se complementam, ou que se contrariam. Aí dá pra montar um livro-texto / aula ensinando tudo de forma digerida e **sem perder nada**."

## O que isto NÃO é

- **Não é resumo.** Resumo encurta e perde. Digestão reorganiza e mantém tudo que ensina algo.
- **Não é lista de fontes.** "O vídeo A disse X, o vídeo B disse Y" é catálogo, não estudo. A fonte vira citação dentro do argumento, não seção.
- **Não é concatenação.** Se o resultado tem o mesmo conceito explicado duas vezes, falhou.
- **Não é curadoria.** Você não decide o que é relevante. A curadoria já aconteceu quando ele escolheu consumir aquelas fontes.

## ⛔ A regra que não se quebra: não filtrar

**"Eliminar redundância" significa desduplicar, não descartar.** O mesmo conceito aparece uma vez em vez de cinco. Todo o resto continua.

Se uma informação de qualquer fonte não aparece em lugar nenhum do output, **é bug**, não escolha editorial.

⚠️ **O erro que acontece na prática:** julgar que algo é "só implementação" e não "conceito", ou "detalhe" e não "ideia", e deixar de fora. Esse julgamento não é seu. Se a fonte gastou tempo explicando, entra.

**Verificação antes de entregar:** percorra fonte por fonte e pergunte *"tudo que esta fonte ensina está presente em algum lugar do texto?"*. Se a resposta for não para qualquer item, volte.

## O princípio que organiza tudo

**Organize por camada de profundidade, não por fonte.**

Cada camada explica a anterior e é pressuposto da seguinte. O leitor deve poder parar em qualquer ponto e ter aprendido algo completo até ali.

```
DIAGNÓSTICO ──► MÉTODO ──► APROFUNDAMENTO ──► CRÍTICAS ──► SÍNTESE
o problema      o como      os detalhes        o que falha   o que sobra
```

O nome das camadas muda com o assunto. A estrutura não.

---

# O processo, em 5 passos

## 1. Inventário (silencioso, não mostra pro usuário)

Antes de escrever, liste mentalmente:

- **Quais fontes existem** e qual o peso de cada uma (autor original > divulgador > opinião)
- **Quais conceitos aparecem** e em quantas fontes cada um aparece
- **Onde estão os números, nomes e citações literais**: esses são insubstituíveis

## 2. Classificar cada informação por RELAÇÃO com as outras fontes

Esta é a etapa que diferencia digestão de resumo. **Nenhuma relação autoriza descartar** — cada uma diz apenas *onde* a informação vai e *como* apresentá-la.

| Relação | O que fazer |
|---|---|
| **Igual** (várias fontes dizem o mesmo) | Funde numa **aparição só**, na fonte mais autoritativa. As outras entram só se agregarem número, exemplo ou formulação melhor |
| **Novo** (só uma fonte tem) | Mantém integral, e **marca como único**. Costuma ser o mais valioso do estudo |
| **Adição** (complementa sem contradizer) | Funde no mesmo bloco, citando quem acrescentou |
| **Ramificação** (base comum, aplicações diferentes) | Base uma vez, depois as variações |
| **Discordância** (as fontes divergem) | ⚠️ **Nunca esconde.** Os dois lados, com quem tem mais peso e por quê |
| **Correção** (uma fonte mostra que outra errou) | Diferente de discordar: aqui uma está factualmente errada. Aponta o erro e a correção |
| **Contribuição original** (a fonte inventou algo fora do material base) | ⚠️ **Marca explicitamente como criação da fonte.** É o tipo de item mais fácil de perder e um dos mais úteis |
| **Autocrítica** (a fonte critica o próprio método) | Dado forte, quase sempre honesto. Entra sempre |
| **Aplicação** (mesma ideia, contexto diferente) | **Não é redundância.** Mantém, mostrando que a ideia generaliza |
| **Exemplo ou caso** (instância concreta de um conceito) | Mantém. É o que faz o leitor entender de verdade |

**A discordância e a contribuição original são o ouro.** Quando um praticante de 10 anos abandona uma peça do método, ou quando alguém cria algo que o método original não tinha, isso ensina mais que dez fontes repetindo o básico.

## 3. Hierarquizar por dependência

Pergunta que ordena: **"o que o leitor precisa saber antes de entender isto?"**

Isso quase nunca é a ordem em que você consumiu o material, e quase nunca é a ordem de importância. É ordem de pré-requisito.

⚠️ **O diagnóstico vem antes do método.** Explicar "como fazer" antes de "qual problema isso resolve" produz texto que se esquece.

## 4. Escrever

Regras que valem sempre:

- **Citação literal** para o que é dito melhor no original. Blockquote, com o autor nomeado. Isso ancora e dá autoridade
- **Número, n, ano, periódico** sempre que existir. "Melhora significativamente" não ensina; "IELT de 120s para 180s, n=199" ensina
- **Tabela** onde há comparação ou classificação. **Diagrama ASCII** onde há fluxo ou hierarquia
- **A fonte aparece no meio do argumento**, não como cabeçalho
- **Marca o nível de confiança**: 🟢 forte, 🟡 moderado ou inferência, 🔴 refutado ou ausente
- Toda seção termina com algo acionável ou com a implicação. Seção que só descreve é peso morto

## 5. Fechar com síntese, não com resumo

As duas últimas seções são as mais úteis do documento:

**"O que sobrevive, o que morreu"**: tabela cruzando todas as fontes:

```
🟢 Sobrevive a todas as críticas    | por quê
🔴 Morreu ou envelheceu             | quem derrubou e com que argumento
🟡 Melhorado por quem veio depois   | original, depois a versão melhor
```

**"A lição que atravessa tudo"**: o que aparece em todas as fontes, inclusive nas que discordam entre si. Isso é o núcleo duro do assunto, e é o que o leitor guarda se esquecer o resto.

---

# Quando o assunto tem aplicação pessoal

Se o material tem relação com o sistema, a rotina ou os projetos do Iago, **acrescenta um apêndice curto** cruzando o estudo com o que já existe:

```
| Peça do estudo | Nosso estado |
|---|---|
| X | ✅ já coberto em Áreas/N |
| Y | ❌ falta: e é o maior buraco |
| Z | ⛔ não implementar: obsoleto (motivo) |
```

**Isso vai no fim, nunca no meio.** O estudo tem que valer sozinho, pra qualquer leitor.

E resista a propor construir coisa nova: quase sempre a conclusão honesta é que faltam duas peças, não um sistema.

---

# O par: /consume + /digerir

**As duas skills são um fluxo de duas etapas, e é assim que devem ser usadas:**

```
/consume  ──►  muitas fontes, de uma vez
/digerir  ──►  um estudo único
```

## Por que consumir em lote é o desenho certo

Contraintuitivo, mas: **consumir muito de uma vez e digerir depois é melhor que consumir pouco.**

O FOMO de conteúdo tem duas origens, e o par resolve as duas:

| Origem do FOMO | Como o par resolve |
|---|---|
| "Preciso ver mais um pra garantir que não perdi nada" | Cobertura. Você consome todas as fontes relevantes de uma vez, e o medo de perder some porque não sobrou fonte |
| "Vi muita coisa e não consigo aplicar nada" | Síntese. O output é um documento único e acionável, não trinta vídeos soltos na memória |

**O gargalo nunca foi o volume de consumo. Foi a síntese.** Pedaço solto na cabeça gera a sensação de que falta algo; documento fechado encerra o assunto.

Isso é o mesmo mecanismo do loop aberto do GTD: o que consome atenção é o não processado, não o não consumido.

⚠️ **O critério de parada não é um número de fontes. É saturação:** pare quando as fontes novas só repetirem o que você já tem. Se a quinta fonte não acrescentou relação nova (nem complementar, nem única, nem contradição), acabou.

---

# Coletando o material

Colete com `/consume` (vídeo, post, curso, arquivo local) ou lendo os arquivos direto.

**Duas coisas que valem o esforço extra:**

- **Priorize a fonte primária.** Autor original, depois quem explica o autor, depois quem opina. Um vídeo do próprio criador do método vale cinco resumos dele
- **Procure ativamente a crítica.** Se o material é todo elogioso, o estudo fica fraco. Busque "X é ruim", "abandonei X", "melhor que X", "X não funciona"

⚠️ **Dica de ferramenta:** se o `yt-dlp` der 403 ao baixar vídeo ou pegar frame, ele está desatualizado. Atualiza com `pip install --upgrade --break-system-packages yt-dlp` e tenta de novo.

**Frames importam quando o conteúdo é visual** (interface, código na tela, diagrama). Transcrição não captura layout nem microcopy. Se o seek remoto falhar, baixa trechos curtos com `--download-sections` e extrai o frame com ffmpeg localmente.

---

# Regras de escrita

- **Zero travessão (—) e en dash (–).** Ponto, vírgula, dois-pontos ou parênteses
- Português do Brasil, direto, sem floreio
- Se algo é incerto, **diga que é incerto**. Não preencha lacuna com plausibilidade
- Se uma fonte errou (estudo mal citado, número inventado, conclusão que o desenho não sustenta), **aponte**

# Saída

Por padrão, escreve **no chat**: ele lê ali.

Salva em arquivo quando ele pedir, quando passar de ~500 linhas, ou quando for material de referência que vai ser reconsultado. Nesse caso: `.md`, e se for aprendizado durável sobre o sistema dele, o lugar é `Notas/.claude/rules/Áreas/`.
