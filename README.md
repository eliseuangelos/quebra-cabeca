# Quebra-Cabeças

<p align="center">
  <a href="https://eliseuangelos.github.io/quebra-cabeca/" target="_blank">
    <img src="https://img.shields.io/badge/ACESSAR_O_JOGO-00D9FF?style=for-the-badge&logo=puzzle&logoColor=050505" alt="Acessar o Jogo">
  </a>
  <a href="https://eliseuangelos.github.io/" target="_blank">
    <img src="https://img.shields.io/badge/SITE_PESSOAL-111827?style=for-the-badge&logo=googlechrome&logoColor=00D9FF" alt="Site Pessoal">
  </a>
  <a href="https://github.com/eliseuangelos" target="_blank">
    <img src="https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://linkedin.com/in/eliseu-fernandes-laurindo" target="_blank">
    <img src="https://img.shields.io/badge/LINKEDIN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</p>

<p align="center"><strong>Monte imagens peça por peça com encaixes, agrupamentos e diferentes níveis de desafio.</strong></p>

---

## Sobre o projeto

**Quebra-Cabeças** é um jogo de montagem de imagens (jigsaw) executado diretamente no navegador. A aplicação apresenta uma galeria de imagens, permite selecionar a quantidade de peças e oferece uma área de jogo na qual as peças podem ser movimentadas por mouse ou toque, encaixadas em suas posições e agrupadas quando vizinhas corretas são conectadas.

Além do modo clássico, o jogo oferece um modo desafio com rotação das peças, ferramentas de referência e organização, cronômetro, efeitos sonoros e placar local. A interface permite alternar entre tema claro e escuro e adapta a área de jogo ao espaço disponível.

**Acesse:** [eliseuangelos.github.io/quebra-cabeca](https://eliseuangelos.github.io/quebra-cabeca/)

## Objetivos do site

- Oferecer uma atividade interativa de raciocínio visual, percepção espacial e concentração.
- Reproduzir a experiência de montar um quebra-cabeça tradicional em uma interface web.
- Proporcionar opções de dificuldade por meio da quantidade e da orientação das peças.
- Funcionar em computadores e dispositivos com tela sensível ao toque.
- Compartilhar um projeto de estudo que explora interatividade, geometria, responsividade e experiência de usuário.

## Funcionalidades

### Galeria de imagens

- Galeria com imagens cadastradas no projeto.
- Busca por nome para localizar imagens disponíveis.
- Miniaturas com carregamento sob demanda (`loading="lazy"`).
- Nome da imagem exibido sem depender da extensão do arquivo.
- Pré-visualização da imagem antes do início da partida.

### Montagem do quebra-cabeça

- Seleção entre diferentes quantidades de peças: 12, 24, 48, 72, 100, 150 ou 200.
- Organização automática das linhas e colunas considerando a proporção da imagem.
- Peças com contornos complementares e encaixes geométricos.
- Distribuição das peças na área de jogo.
- Movimentação por mouse, toque ou caneta compatível.
- Encaixe automático quando a peça se aproxima da posição correta.
- Agrupamento de peças vizinhas para movimentação conjunta.

### Modos e ferramentas

- **Modo clássico:** montagem sem rotação inicial das peças.
- **Modo desafio:** peças iniciam com rotações; cada peça pode ser girada em passos de 90 graus e só se encaixa na orientação correta.
- **Modo fantasma:** apresenta a imagem de referência de forma translúcida sobre a área do tabuleiro, com ajuste de transparência.
- **Referência:** permite consultar e ampliar a imagem completa.
- **Bordas:** facilita a identificação das peças externas.
- **Dica:** destaca a região de destino da peça selecionada.
- **Organizar:** reorganiza a distribuição das peças soltas.
- **Ajustar:** altera a escala da área de montagem.
- **Cronômetro, pausa e reinício** da partida.
- **Efeito sonoro** com controle para ativar ou desativar o som.
- Tela de conclusão com animação de comemoração.
- **Placar local**, com filtros por imagem, quantidade de peças e modalidade.

## Controles

- Arraste as peças com o mouse ou o dedo.
- No modo desafio, use o botão **Girar**, a tecla `R`, duplo clique ou dois toques sobre a peça selecionada.
- Use `Tab` para alternar o foco entre as peças soltas e `Shift + Tab` para retornar aos controles.
- As setas do teclado movimentam a peça em foco; `Shift` permite passos maiores.

## Catálogo de imagens: funcionamento atual

As imagens da galeria são cadastradas manualmente no vetor `FILES`, localizado no arquivo `index.html`. Cada registro contém um identificador, o nome que será mostrado na tela e o caminho da imagem dentro de `public/images/puzzles/`. A ordem dos registros define a ordem de exibição.

Atualmente, a galeria inclui **A Arca de Noé**, **Davi e Golias**, **Daniel na Cova dos Leões** e **Crianças Brincando**. As miniaturas usam carregamento lento nativo do navegador.

> **Nota técnica:** a versão pública analisada não utiliza um catálogo JSON, não examina automaticamente a pasta de imagens e não consulta a API do GitHub para descobrir novos arquivos. Para adicionar ou reordenar uma imagem, é necessário atualizar o vetor `FILES` em `index.html` e publicar a alteração.

## Tecnologias e recursos

| Tecnologia ou recurso | Aplicação |
|---|---|
| HTML5 | Estrutura da galeria, dos controles e da área de jogo. |
| CSS3 | Layout, temas, animações, encaixes visuais e responsividade. |
| JavaScript | Geração das peças, movimentação, encaixe, agrupamento e regras. |
| Pointer Events | Entrada de mouse, toque e caneta. |
| `clip-path` e curvas Bézier | Geometria visual dos contornos e encaixes das peças. |
| `loading="lazy"` | Carregamento sob demanda das miniaturas. |
| localStorage | Persistência local do tema, som e resultados do placar. |
| GitHub Pages | Hospedagem estática do jogo. |

## Privacidade e armazenamento

A aplicação executa a lógica do jogo no navegador. O placar e as preferências são armazenados localmente por meio do `localStorage` do dispositivo. Por isso, os resultados não representam uma classificação centralizada entre diferentes aparelhos e podem ser perdidos quando os dados locais do site forem apagados.

## Execução local

Como o jogo carrega imagens por caminhos relativos, recomenda-se iniciar um servidor HTTP local:

```bash
git clone https://github.com/eliseuangelos/quebra-cabeca.git
cd quebra-cabeca
python3 -m http.server 8000
```

Depois, acesse `http://localhost:8000/` no navegador.

## Sobre o autor

Sou **Eliseu Fernandes Laurindo**, profissional com experiência administrativa e operacional, estudante autodidata e entusiasta de tecnologia e inteligência artificial. Meu contato com HTML e CSS começou por volta de 2010, acompanhado de estudos iniciais de JavaScript. Na adolescência, eu já experimentava estruturas de jogos digitais; posteriormente, atuei como tutor em um MMORPG internacional e multiplataforma, mantive uma fanpage própria e desenvolvi scripts e calculadoras para a comunidade.

Atualmente, utilizo essa experiência como ponto de partida para aprender, testar ideias e desenvolver ferramentas digitais voltadas a necessidades de estudo ou utilidade compartilhada. **Não sou desenvolvedor profissional nem possuo formação acadêmica específica em desenvolvimento de software**; este projeto integra minha jornada prática de aprendizagem. Ferramentas de inteligência artificial são utilizadas como apoio à pesquisa, ao planejamento e à revisão, sem substituir a validação do resultado.

- **Projeto:** [Quebra-Cabeças](https://eliseuangelos.github.io/quebra-cabeca/)
- **Site pessoal:** [eliseuangelos.github.io](https://eliseuangelos.github.io/)
- **GitHub:** [github.com/eliseuangelos](https://github.com/eliseuangelos)
- **LinkedIn:** [linkedin.com/in/eliseu-fernandes-laurindo](https://linkedin.com/in/eliseu-fernandes-laurindo)

---

<p align="center"><em>“Quanto mais aumenta nosso conhecimento, mais evidente fica nossa ignorância.”</em><br><strong>John F. Kennedy</strong></p>
