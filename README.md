# Quebra-Cabeças

Jogo de quebra-cabeças (jigsaw) em HTML, CSS e JavaScript puros, sem dependências, pronto para hospedagem estática no GitHub Pages.

## Funcionalidades

- Peças com encaixes, desenhadas com `clip-path: path()`.
- Arrastar com mouse, toque ou caneta; encaixe automático e agrupamento de peças vizinhas.
- Modo clássico e modo desafio, com rotação de 90°.
- Modo fantasma, imagem de referência ampliável, bordas, dica, organizar e ajustar tabuleiro.
- Cronômetro com pausa, tela de vitória, tema claro/escuro e respeito a movimento reduzido.
- Placar local (`localStorage`), separado em Modelos e Personalizados.
- Envio de foto própria (JPG, PNG, WEBP ou AVIF, até 15 MB), processada no próprio navegador.
- Efeito sonoro de vitória (Web Audio, sem arquivos), com botão **Som** no topo; a preferência fica em `jigsaw.audio.v1`.
- Galeria com links de imagem cadastrados manualmente no `index.html`, sem catálogo JSON e sem consulta à API do GitHub.

## Estrutura

```text
index.html                  # aplicação e lista manual de imagens
public/images/puzzles/      # imagens usadas na galeria
```

## Adicionar, remover ou reordenar imagens

1. Coloque a imagem em `public/images/puzzles/`.
2. Abra `index.html` e procure por `const FILES = [`.
3. Adicione um objeto com `id`, `name` e `src`.
4. Em `src`, informe o caminho relativo completo do arquivo, codificando espaços e caracteres especiais na URL.
5. Salve o arquivo. A ordem dos objetos em `FILES` é a ordem da galeria.

Exemplo:

```javascript
const FILES=[
 {
  id:'a-arca-de-noe',
  name:'A Arca de Noé',
  src:'public/images/puzzles/A%20Arca%20de%20No%C3%A9.png'
 },
 {
  id:'criancas-brincando-no-parque',
  name:'Crianças Brincando no Parque',
  src:'public/images/puzzles/Crian%C3%A7as%20Brincando%20no%20Parque.png'
 },
 {
  id:'minha-nova-imagem',
  name:'Minha Nova Imagem',
  src:'public/images/puzzles/Minha%20Nova%20Imagem.jpg'
 }
];
```

Os exemplos acima incluem as duas imagens já cadastradas e uma terceira imagem ilustrativa. Troque o terceiro registro pelo nome e caminho reais do arquivo que você adicionar. O nome mostrado na galeria é o valor de `name`; ele não precisa incluir a extensão.

O arquivo precisa existir exatamente no caminho informado. Os arquivos guardados na pasta, mas não cadastrados em `FILES`, não aparecem na galeria.

## Sobre o carregamento das miniaturas

As miniaturas usam `loading="lazy"` e `decoding="async"`, recursos nativos do navegador. Não há `IntersectionObserver` personalizado, leitura de `gallery.json` nem consulta à API do GitHub para descobrir as imagens. A imagem original continua sendo utilizada na montagem do quebra-cabeça.

## Processamento de fotos (notas técnicas)

- O original nunca é alterado. Se a foto já cabe nos limites, é usada como está; senão gera-se uma cópia JPEG (0,90, fundo branco) só para o jogo.
- Limites: celular 2.048 px no maior lado e ~4 MP; computador 2.560 px. Os dois limites valem ao mesmo tempo e a proporção é preservada.
- Ordem: validar → SHA-256 (em blocos de 1 MiB, mesmo id `u-<hex>` do placar) → decodificar. O hash nunca coexiste com a imagem decodificada.
- Uma foto por vez; timeout de 30 s com cancelamento (`AbortController`). `createImageBitmap` não é cancelável: ao expirar, o bitmap atrasado é fechado e o resultado descartado.
- URLs temporárias ficam num gerenciador central (donos `up` e `game`). No console, `__qc.urls()` deve ser 1 com uma foto selecionada e 0 sem nenhuma.
- **Limites reais:** `createImageBitmap` com `resizeWidth/Height` pode decodificar em resolução cheia internamente, conforme o navegador; a orientação EXIF depende de o navegador aplicá-la em `<img>`/`createImageBitmap`; o fallback sem `createImageBitmap` decodifica a imagem inteira.

## Executar localmente

Abra o projeto por um servidor HTTP local. Por exemplo, com Python:

```bash
python -m http.server 8000
```

Depois, acesse `http://localhost:8000`.

## Créditos

Desenvolvimento: Eliseu Fernandes Laurindo — https://eliseuangelos.github.io
