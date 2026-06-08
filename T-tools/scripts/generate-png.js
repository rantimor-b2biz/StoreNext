const fs = require('fs');
const path = require('path');

// Create a complete LinkedIn post image as PNG
// Using raw PNG format construction

function createLinkedInPNG() {
  const width = 1200;
  const height = 628;
  
  // We'll create base64 SVG embedded in data URL
  const svg = `<svg width="1200" height="628" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 628">
    <defs>
      <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#3C2C4C;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#2a1f38;stop-opacity:1" />
      </linearGradient>
      <pattern id="networkPattern" x="0" y="0" width="200" height="200" patternUnits="userSpaceOnUse">
        <circle cx="40" cy="60" r="2" fill="#7CCBC3" opacity="0.15"/>
        <circle cx="160" cy="140" r="2" fill="#7CCBC3" opacity="0.15"/>
        <circle cx="80" cy="160" r="2" fill="#7CCBC3" opacity="0.15"/>
        <line x1="40" y1="60" x2="80" y2="160" stroke="#7CCBC3" stroke-width="1" opacity="0.08"/>
      </pattern>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        text { font-family: 'Inter', sans-serif; }
      </style>
    </defs>
    <rect width="1200" height="628" fill="url(#bgGradient)"/>
    <rect width="1200" height="628" fill="url(#networkPattern)"/>
    <line x1="60" y1="126" x2="400" y2="220" stroke="#7CCBC3" stroke-width="2" opacity="0.08"/>
    <line x1="960" y1="94" x2="600" y2="470" stroke="#7CCBC3" stroke-width="2" opacity="0.08"/>
    <text x="80" y="120" font-size="56" font-weight="700" fill="#7CCBC3">500+ Suppliers</text>
    <text x="600" y="240" font-size="64" font-weight="700" fill="#FFFFFF" text-anchor="middle">Email chaos</text>
    <text x="600" y="315" font-size="64" font-weight="700" fill="#FFFFFF" text-anchor="middle">at Enterprise</text>
    <text x="600" y="390" font-size="64" font-weight="700" fill="#FFFFFF" text-anchor="middle">scale</text>
    <text x="600" y="460" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="middle" opacity="0.95">The system is broken.</text>
    <line x1="80" y1="510" x2="1120" y2="510" stroke="#E85252" stroke-width="3"/>
    <text x="80" y="575" font-size="20" font-weight="600" fill="#FFFFFF">Rethinking Procurement at Scale</text>
    <text x="1015" y="575" font-size="32" font-weight="700" fill="#7CCBC3" text-anchor="end">STORENEXT</text>
    <rect x="1050" y="545" width="30" height="30" fill="#E85252" rx="2"/>
  </svg>`;

  const outputPath = path.join(__dirname, 'week1-visual-FINAL.png');
  
  // Save SVG for reference
  fs.writeFileSync(
    path.join(__dirname, 'week1-visual-for-conversion.svg'),
    svg,
    'utf8'
  );

  console.log('SVG created: week1-visual-for-conversion.svg');
  console.log('To convert to PNG, use: https://convertio.co/svg-png/');
  console.log('Or: npx sharp week1-visual-for-conversion.svg week1-visual-FINAL.png');
  
  return outputPath;
}

createLinkedInPNG();
