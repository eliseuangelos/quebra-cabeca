# Quebra-Cabeças — pacote corrigido

Jogo de quebra-cabeças em HTML, CSS e JavaScript puros, sem dependências, pronto para GitHub Pages.

## Correções desta versão

- Catálogo `public/data/gallery.json` regenerado e validado.
- **A Arca de Noé.png** incluída como primeira imagem da galeria.
- Fallback embutido no `index.html`: se o JSON estiver vazio ou indisponível, o jogo tenta carregar diretamente a imagem da Arca de Noé.
- Gerador de catálogo revisado: evita duplicar a mesma arte quando ela existe em JPG e PNG com o mesmo nome-base.
- Upload local revisado: valida formato, tamanho e dimensões; apresenta mensagens mais claras; usa identificador alternativo quando SHA-256 não estiver disponível.
- Tema escuro revisado para controles nativos, campos e opções de seleção.
- Placar reorganizado com filtros responsivos e linhas de recordes alinhadas.

## Estrutura

```text
index.html
README.md
scripts/
  generate-gallery.mjs
public/
  data/
    gallery.json
  images/
    puzzles/
      A Arca de Noé.png
      A Arca de Noé.jpg
```

## Executar localmente

O catálogo é carregado com `fetch`, então não abra o HTML diretamente por `file://`.

Com Python:

```bash
python3 -m http.server 8000
```

Depois acesse `http://localhost:8000`.

## Atualizar a galeria

1. Adicione imagens JPG, JPEG, PNG, WEBP ou AVIF em `public/images/puzzles/`.
2. Execute com Node.js 18 ou superior:

```bash
node scripts/generate-gallery.mjs
```

3. Publique os arquivos atualizados no GitHub.

O script cria/atualiza `public/data/gallery.json`. Se o catálogo não puder ser carregado, o HTML possui uma alternativa direta para a Arca de Noé. Para outras imagens, mantenha o catálogo gerado atualizado.

## Publicar no GitHub Pages

Envie o conteúdo desta pasta para a raiz da branch/pasta configurada em **Settings → Pages**. Mantenha a estrutura `public/` e `scripts/` sem alterar os caminhos.

## Sobre o upload de fotos

O envio de fotos personalizadas é **local ao navegador**: a imagem é lida por uma URL temporária (`blob:`) e usada para montar o jogo. Ela não é enviada ao GitHub nem armazenada em um servidor. Isso é esperado em uma hospedagem estática sem backend. A foto fica disponível durante a sessão do navegador; o placar local guarda os resultados no `localStorage`.

## Funcionalidades preservadas

- Peças com encaixes por curvas de Bézier.
- Arrastar com mouse, toque ou caneta.
- Modo clássico e modo desafio com rotação.
- Fantasma, referência, bordas, dica, organizar e ajustar tabuleiro.
- Cronômetro, pausa e tela de vitória.
- Placar local separado em Modelos e Personalizados.
- Tema claro/escuro e respeito a movimento reduzido.

Desenvolvimento: Eliseu Fernandes Laurindo — https://eliseuangelos.github.io
