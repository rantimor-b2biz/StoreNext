const https = require('https');
const fs = require('fs');
const path = require('path');

// Gemini API Configuration
const API_KEY = 'AIzaSyCpSiZgWZoHWfdg1rU2TCHosTYkr0pirX0';
const API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent';

// Detailed prompt for LinkedIn visual
const prompt = `Create a professional LinkedIn post visual image (1200x628 pixels) for a B2B Enterprise software company called StoreNext.

Requirements:
- Background: Gradient from dark purple (#3C2C4C) to darker purple (#2a1f38)
- Main text color: White (#FFFFFF)
- Accent color: Turquoise (#7CCBC3)
- Red accent color: #E85252

Content to include:
- Large stat at top: "500+ Suppliers"
- Main headline centered: "Email chaos at Enterprise scale"
- Subheading: "The system is broken."
- Bottom tagline: "Rethinking Procurement at Scale"
- Company name: "STORENEXT" in turquoise
- Professional, clean design - no clutter
- Subtle network/supply chain visual elements in the background
- Red horizontal divider line separating sections

Style: Corporate, professional, modern B2B, enterprise-focused
The image should appeal to procurement leaders and CFOs
No logos or external branding - just clean typography and design
Make it look like a premium LinkedIn post that would generate engagement`;

async function generateImage() {
  try {
    console.log('Generating LinkedIn Post Visual with Gemini API...');
    console.log('(This may take 30-60 seconds)');
    
    const payload = {
      contents: [
        {
          parts: [
            {
              text: prompt
            }
          ]
        }
      ],
      generationConfig: {
        temperature: 0.7,
        top_p: 0.95,
        top_k: 64,
        max_output_tokens: 1024
      }
    };

    const options = {
      hostname: 'generativelanguage.googleapis.com',
      path: `/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    };

    return new Promise((resolve, reject) => {
      const req = https.request(options, (res) => {
        let data = '';
        
        res.on('data', (chunk) => {
          data += chunk;
        });

        res.on('end', () => {
          if (res.statusCode === 200) {
            try {
              const response = JSON.parse(data);
              console.log('Gemini API Response:');
              console.log(JSON.stringify(response, null, 2));
              resolve(response);
            } catch (e) {
              reject(new Error('Failed to parse Gemini response: ' + e.message));
            }
          } else {
            reject(new Error(`Gemini API Error (${res.statusCode}): ${data}`));
          }
        });
      });

      req.on('error', (error) => {
        reject(error);
      });

      req.write(JSON.stringify(payload));
      req.end();
    });
  } catch (error) {
    console.error('Error:', error.message);
    throw error;
  }
}

// Run the generator
generateImage()
  .then((response) => {
    console.log('\n✅ Image generation request sent successfully!');
    console.log('\nNote: Gemini is a text-based model.');
    console.log('For actual image generation, we should use:');
    console.log('- Google Gemini Image Generation (different API)');
    console.log('- Or: Replicate + Stable Diffusion');
    console.log('- Or: DALL-E via OpenAI API');
  })
  .catch((error) => {
    console.error('Error generating image:', error.message);
    process.exit(1);
  });
