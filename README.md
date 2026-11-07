# Quebra-Cabeças

Jogo de quebra-cabeças (jigsaw) em HTML, CSS e JavaScript puros, sem dependências, pronto para hospedagem estática (GitHub Pages, raiz ou subdiretório).

## Funcionalidades
- Peças reais com encaixes (curvas de Bézier compartilhadas entre vizinhas), desenhadas com `clip-path: path()`.
- Arrastar com mouse, toque ou caneta (Pointer Events); encaixe automático com tolerância configurável (`CFG.tol`); peças vizinhas formam grupos.
- Modo clássico e modo desafio (rotação de 90°: tecla `R` ou botão Girar; só encaixa na orientação correta). Desafio vem desligado.
- Modo fantasma (imagem translúcida de 20% a 40% alinhada ao tabuleiro), imagem de referência ampliável, bordas, dica, organizar e ajustar tabuleiro.
- Cronômetro com pausa, tela de vitória com confetes, tema claro/escuro e respeito a movimento reduzido.
- Placar local (`localStorage`), separado em Modelos e Personalizados, com top 10 por imagem, quantidade de peças e modo.
- Envio de foto própria (JPG, PNG, WEBP, AVIF, até 15 MB), processada só no navegador; o placar usa o SHA-256 do arquivo como identificador.

## Estrutura
```
index.html                  # aplicação (CSS e JS inline)
scripts/generate-gallery.mjs
public/data/gallery.json    # gerado pelo script
public/images/puzzles/      # imagens do catálogo
```

## Adicionar imagens e atualizar o catálogo
1. Copie as imagens (JPG, JPEG, PNG, WEBP ou AVIF) para `public/images/puzzles/`. Coloque também `A Arca de Noé.png`: ela sempre será a primeira da galeria.
2. Rode `node scripts/generate-gallery.mjs` (Node 18 ou superior). O script é idempotente e avisa se `A Arca de Noé.png` estiver ausente.
3. O nome exibido é o nome do arquivo sem a extensão, com acentos preservados.

## Executar localmente
Use um servidor estático (o catálogo é carregado com `fetch`, então `file://` não funciona):
`python3 -m http.server 8000` e abra `http://localhost:8000`.

## Publicar no GitHub Pages
Envie o projeto ao repositório, abra Settings > Pages e escolha a branch e a pasta raiz. Todos os caminhos são relativos, então funciona em `usuario.github.io/repositorio/`.

## Como funciona
- **Grade:** escolhe colunas e linhas que deixam as peças o mais próximo possível de um quadrado, informa a quantidade real e nunca distorce a imagem (o tabuleiro tem a proporção da foto).
- **Geometria:** cada aresta interna tem sentido de encaixe e pequenas variações aleatórias (semente por partida). Peças vizinhas usam a mesma curva, uma percorrida em sentido inverso, então os recortes sempre se complementam. Bordas externas são retas.
- **Rotação:** a peça gira em torno do próprio centro; o encaixe e o agrupamento só valem com rotação 0°.
- **Distribuição:** as peças são espalhadas fora do tabuleiro, sempre dentro da área visível, e reposicionadas se a tela mudar de tamanho.

## Limitações conhecidas
Sem salvamento automático de partidas em andamento, sem bandejas de peças com rolagem e sem miniaturas redimensionadas (o navegador reduz as imagens originais).

## Créditos
Desenvolvimento: Eliseu Fernandes Laurindo — https://eliseuangelos.github.io
