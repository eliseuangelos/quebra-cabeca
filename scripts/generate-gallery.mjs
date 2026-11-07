#!/usr/bin/env node
// Gera public/data/gallery.json a partir de public/images/puzzles/
// Uso: node scripts/generate-gallery.mjs   (sem dependências; idempotente)
import { readdir, readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dir = path.join(root, 'public/images/puzzles');
const out = path.join(root, 'public/data/gallery.json');
const FIRST = 'A Arca de Noé.png'; // sempre o primeiro item do catálogo
const EXT = /\.(jpe?g|png|webp|avif)$/i;
const nfc = (s) => s.normalize('NFC');

// Lê largura e altura direto do cabeçalho do arquivo (PNG, JPEG, WEBP, AVIF)
function dims(b) {
  if (b.toString('latin1', 1, 4) === 'PNG') return [b.readUInt32BE(16), b.readUInt32BE(20)];
  if (b[0] === 0xff && b[1] === 0xd8) {
    let i = 2;
    while (i + 9 < b.length) {
      if (b[i] !== 0xff) { i++; continue; }
      const m = b[i + 1];
      if (m === 0xff) { i++; continue; }
      if (m === 1 || (m >= 0xd0 && m <= 0xd9)) { i += 2; continue; }
      if (m >= 0xc0 && m <= 0xcf && ![0xc4, 0xc8, 0xcc].includes(m)) return [b.readUInt16BE(i + 7), b.readUInt16BE(i + 5)];
      i += 2 + b.readUInt16BE(i + 2);
    }
  }
  if (b.toString('latin1', 0, 4) === 'RIFF' && b.toString('latin1', 8, 12) === 'WEBP') {
    const t = b.toString('latin1', 12, 16);
    if (t === 'VP8X') return [1 + b.readUIntLE(24, 3), 1 + b.readUIntLE(27, 3)];
    if (t === 'VP8 ') return [b.readUInt16LE(26) & 0x3fff, b.readUInt16LE(28) & 0x3fff];
    if (t === 'VP8L') { const v = b.readUInt32LE(21); return [(v & 0x3fff) + 1, ((v >> 14) & 0x3fff) + 1]; }
  }
  const k = b.indexOf('ispe');
  if (k > 0 && b.toString('latin1', 4, 8) === 'ftyp') return [b.readUInt32BE(k + 8), b.readUInt32BE(k + 12)];
  return null;
}

await mkdir(dir, { recursive: true });
await mkdir(path.dirname(out), { recursive: true });

const files = (await readdir(dir)).filter((f) => EXT.test(f));
// Prioridade para FIRST; depois ordem alfabética natural
files.sort((a, b) =>
  (nfc(b) === nfc(FIRST)) - (nfc(a) === nfc(FIRST)) ||
  nfc(a).localeCompare(nfc(b), 'pt', { numeric: true, sensitivity: 'base' }));

const ids = new Set();
const list = [];
for (const f of files) {
  const name = nfc(f).replace(EXT, ''); // extensão removida só do nome exibido
  const base = name.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase()
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'imagem';
  let id = base, n = 2;
  while (ids.has(id)) id = `${base}-${n++}`;
  ids.add(id);
  const d = dims(await readFile(path.join(dir, f)));
  const [width, height] = d || [null, null];
  list.push({
    id, name, filename: f,
    src: 'public/images/puzzles/' + encodeURIComponent(f), // relativo ao index.html
    width, height,
    orientation: d ? (width > height * 1.05 ? 'landscape' : height > width * 1.05 ? 'portrait' : 'square') : null,
    featured: nfc(f) === nfc(FIRST),
    order: list.length,
  });
}

await writeFile(out, JSON.stringify(list, null, 2) + '\n');
console.log(`${list.length} imagem(ns) registrada(s) em ${path.relative(root, out)}`);
if (!files.some((f) => nfc(f) === nfc(FIRST)))
  console.warn(`ATENÇÃO: "${FIRST}" não foi encontrado em public/images/puzzles/. Adicione o arquivo e rode o script novamente.`);
