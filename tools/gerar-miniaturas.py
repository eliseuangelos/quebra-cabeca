#!/usr/bin/env python3
"""
Gera as miniaturas (WebP) usadas nos cards da galeria.

Como usar (na pasta do projeto):
    python3 -m pip install pillow        # só na primeira vez
    python3 tools/gerar-miniaturas.py

O que faz:
  1. Lê as imagens de public/images/puzzles/ (png, jpg, jpeg, webp).
  2. Cria public/images/thumbs/<mesmo-nome>.webp (lado maior = 360 px).
     Miniaturas que já estão em dia são ignoradas; use --forcar para refazer todas.
  3. Mostra o bloco pronto para colar no vetor FILES do index.html
     para as imagens que ainda não estão cadastradas.

As imagens originais NÃO são alteradas.
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow não encontrado. Instale com:  python3 -m pip install pillow")

RAIZ = Path(__file__).resolve().parent.parent
ORIGENS = RAIZ / "public" / "images" / "puzzles"
DESTINO = RAIZ / "public" / "images" / "thumbs"
INDEX = RAIZ / "index.html"
EXTENSOES = {".png", ".jpg", ".jpeg", ".webp"}
LADO_MAIOR = 360   # px; cobre telas de alta densidade (2x) com folga nos cards
QUALIDADE = 75     # WebP; equilíbrio entre nitidez e peso (~25 a 30 KB por miniatura)


def tamanho(num_bytes):
    return f"{num_bytes / 1048576:.1f} MB" if num_bytes >= 1048576 else f"{num_bytes / 1024:.0f} KB"


def para_rgb(img):
    """Converte para RGB; se houver transparência, compõe sobre fundo branco."""
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
        fundo = Image.new("RGB", img.size, (255, 255, 255))
        fundo.paste(img, mask=img.getchannel("A"))
        return fundo
    return img.convert("RGB")


def gerar(origem, destino):
    with Image.open(origem) as img:
        img = para_rgb(ImageOps.exif_transpose(img))
        img.thumbnail((LADO_MAIOR, LADO_MAIOR), Image.LANCZOS)
        img.save(destino, "WEBP", quality=QUALIDADE, method=6)


def cadastradas():
    """Caminhos de src já presentes no vetor FILES do index.html."""
    if not INDEX.exists():
        return set()
    return set(re.findall(r"src\s*:\s*['\"]([^'\"]+)['\"]", INDEX.read_text(encoding="utf-8")))


def js(texto):
    """Escapa o texto para uso entre aspas simples em JavaScript."""
    return texto.replace("\\", "\\\\").replace("'", "\\'")


def slug(texto):
    """Minúsculas, sem acentos, só letras/números separados por hífen."""
    base = unicodedata.normalize("NFD", texto)
    base = "".join(c for c in base if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", base).strip("-") or "imagem"


def bloco(arquivo):
    nome = arquivo.stem.replace("-", " ").replace("_", " ").strip()
    nome = nome[:1].upper() + nome[1:]
    caminho = "public/images/puzzles/" + quote(arquivo.name)
    return (
        " {\n"
        f"  id:'{slug(arquivo.stem)}',\n"
        f"  name:'{js(nome)}',\n"
        f"  src:'{caminho}'\n"
        " },"
    )


def main():
    ap = argparse.ArgumentParser(description="Gera as miniaturas da galeria.")
    ap.add_argument("--forcar", action="store_true", help="refaz todas as miniaturas")
    args = ap.parse_args()

    if not ORIGENS.is_dir():
        sys.exit(f"Pasta não encontrada: {ORIGENS}")
    imagens = sorted(p for p in ORIGENS.iterdir() if p.suffix.lower() in EXTENSOES)
    if not imagens:
        sys.exit("Nenhuma imagem encontrada em public/images/puzzles/.")

    vistos = {}
    for arq in imagens:
        vistos.setdefault(arq.stem.lower(), []).append(arq.name)
    for nomes in vistos.values():
        if len(nomes) > 1:
            print(f"ATENÇÃO: {', '.join(nomes)} têm o mesmo nome e dividiriam a mesma miniatura. Renomeie um deles.")

    DESTINO.mkdir(parents=True, exist_ok=True)
    feitas = puladas = 0
    for arq in imagens:
        dest = DESTINO / (arq.stem + ".webp")
        if not args.forcar and dest.exists() and dest.stat().st_mtime >= arq.stat().st_mtime:
            puladas += 1
            continue
        gerar(arq, dest)
        feitas += 1
        print(f"  {arq.name} ({tamanho(arq.stat().st_size)}) -> thumbs/{dest.name} ({tamanho(dest.stat().st_size)})")

    print(f"\nMiniaturas: {feitas} geradas, {puladas} já em dia.")

    ja = cadastradas()
    novas = [a for a in imagens if "public/images/puzzles/" + quote(a.name) not in ja]
    if novas:
        print("\nImagens ainda não cadastradas no vetor FILES (index.html).")
        print("Cole o bloco abaixo e ajuste o campo name (acentos e maiúsculas):\n")
        print("\n".join(bloco(a) for a in novas))


if __name__ == "__main__":
    main()
