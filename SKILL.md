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

## 2. Classificar cada informação em uma das cinco relações

Esta é a etapa que diferencia digestão de resumo:

| Relação | O que fazer |
|---|---|
| **Redundante** (várias fontes dizem o mesmo) | Explica **uma vez**, na fonte mais autoritativa. Cita as outras só se agregarem número ou exemplo |
| **Complementar** (cada fonte cobre um pedaço) | **Funde num bloco só**, sem costura visível. O leitor não deve perceber que veio de lugares diferentes |
| **Ramificação** (base comum, aplicações diferentes) | Explica a base uma vez, depois as ramificações como variações |
| **Contradição** (as fontes discordam) | ⚠️ **Nunca esconda.** Dá os dois lados, diz quem tem mais peso e por quê. Contradição bem tratada é o que dá credibilidade ao estudo |
| **Único** (só uma fonte tem) | Mantém integralmente. Costuma ser o mais valioso |

**A contradição é o ouro.** Quando um praticante de 10 anos abandona uma peça do método, isso ensina mais que dez vídeos elogiando.

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

# Se o material ainda não foi coletado

Colete antes com `/consume` (vídeo, post, curso, arquivo local) ou lendo os arquivos direto.

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
