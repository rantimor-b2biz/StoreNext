#!/usr/bin/env node
// generate-visual.js — StoreNext LinkedIn visual generator
// Usage: node T-tools/generate-visual.js <week-folder-path>
// Reads visual-data.json, writes visual.svg + visual.png

const fs   = require('fs');
const path = require('path');

const folderPath = process.argv[2];
if (!folderPath) {
  console.error('Usage: node T-tools/generate-visual.js <week-folder-path>');
  process.exit(1);
}

const dataPath = path.join(folderPath, 'visual-data.json');
if (!fs.existsSync(dataPath)) {
  console.error(`Missing visual-data.json in ${folderPath}`);
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
const svg  = buildSVG(data);

const svgPath = path.join(folderPath, 'visual.svg');
const pngPath = path.join(folderPath, 'visual.png');

fs.writeFileSync(svgPath, svg, 'utf8');
console.log(`SVG written: ${svgPath}`);

// Convert to PNG via sharp
try {
  const sharp = require('sharp');
  sharp(Buffer.from(svg))
    .resize(1200, 628)
    .png()
    .toFile(pngPath)
    .then(() => console.log(`PNG written: ${pngPath}`))
    .catch(err => { console.error('sharp error:', err.message); process.exit(1); });
} catch (e) {
  console.log('sharp not available — SVG only. Run: npm install sharp');
}

// ---------------------------------------------------------------------------

function esc(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function buildSVG(d) {
  const W = 1200, H = 628;

  // headline: string or array of strings
  const lines = Array.isArray(d.headline) ? d.headline : [d.headline];

  // vertical centering for headline block
  const lineHeight   = 72;
  const blockHeight  = lines.length * lineHeight;
  const midY         = 290; // visual center (slightly above true center)
  const firstLineY   = midY - (blockHeight / 2) + lineHeight;

  const headlineLines = lines.map((line, i) =>
    `<text x="600" y="${firstLineY + i * lineHeight}" font-size="68" font-weight="700"
       fill="#FFFFFF" text-anchor="middle" font-family="'Inter',Arial,sans-serif">${esc(line)}</text>`
  ).join('\n    ');

  const subY = firstLineY + lines.length * lineHeight + 28;

  return `<svg width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   style="stop-color:#3C2C4C;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#2a1f38;stop-opacity:1"/>
    </linearGradient>
    <pattern id="dots" x="0" y="0" width="200" height="200" patternUnits="userSpaceOnUse">
      <circle cx="40"  cy="60"  r="2" fill="#7CCBC3" opacity="0.15"/>
      <circle cx="160" cy="140" r="2" fill="#7CCBC3" opacity="0.15"/>
      <circle cx="80"  cy="160" r="2" fill="#7CCBC3" opacity="0.15"/>
      <circle cx="120" cy="40"  r="2" fill="#7CCBC3" opacity="0.10"/>
      <line x1="40" y1="60" x2="80"  y2="160" stroke="#7CCBC3" stroke-width="1" opacity="0.07"/>
      <line x1="80" y1="160" x2="160" y2="140" stroke="#7CCBC3" stroke-width="1" opacity="0.07"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="${W}" height="${H}" fill="url(#bg)"/>
  <rect width="${W}" height="${H}" fill="url(#dots)"/>

  <!-- Subtle diagonal lines -->
  <line x1="60"  y1="126" x2="420" y2="230" stroke="#7CCBC3" stroke-width="2" opacity="0.07"/>
  <line x1="980" y1="80"  x2="580" y2="460" stroke="#7CCBC3" stroke-width="2" opacity="0.07"/>

  <!-- Stat (top left) -->
  <text x="80" y="106" font-size="52" font-weight="700" fill="#7CCBC3"
    font-family="'Inter',Arial,sans-serif">${esc(d.stat)}</text>
  <text x="80" y="140" font-size="22" font-weight="400" fill="#7CCBC3"
    font-family="'Inter',Arial,sans-serif" opacity="0.85">${esc(d.stat_suffix)}</text>

  <!-- Headline -->
  ${headlineLines}

  <!-- Subheading -->
  <text x="600" y="${subY}" font-size="30" font-weight="600"
    fill="#FFFFFF" text-anchor="middle" opacity="0.80"
    font-family="'Inter',Arial,sans-serif">${esc(d.subheading)}</text>

  <!-- Bottom bar -->
  <line x1="80" y1="546" x2="${W - 80}" y2="546" stroke="#E85252" stroke-width="3"/>
  <text x="80" y="594" font-size="20" font-weight="600" fill="#FFFFFF"
    font-family="'Inter',Arial,sans-serif" opacity="0.90">${esc(d.tagline)}</text>
  <text x="${W - 90}" y="594" font-size="30" font-weight="700" fill="#7CCBC3"
    text-anchor="end" font-family="'Inter',Arial,sans-serif">STORENEXT</text>
  <rect x="${W - 80}" y="568" width="26" height="26" fill="#E85252" rx="2"/>
</svg>`;
}
