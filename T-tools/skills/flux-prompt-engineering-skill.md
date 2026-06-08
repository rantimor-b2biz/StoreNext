# FLUX Prompt Engineering Skill
# StoreNext Edition

**Used by:** Artist Agent
**Model:** `black-forest-labs/flux-1.1-pro` via Replicate
**Purpose:** Generate reliable, high-quality realistic images on the first or second attempt

---

## The Core Formula

```
[Shot type] + [Subject + key detail] + [Angle/composition] + [Lighting] + [Atmosphere] + [Style modifiers] + [What's NOT in it]
```

---

## Client-Specific Style Profile: StoreNext

**Brand mood:** Corporate, data-forward, enterprise trust. Clean precision. CFO/Procurement audience.

**Default style modifiers:**
```
corporate photography, enterprise aesthetic, clean and precise,
professional lighting, ultra-realistic, high contrast, no people, no text
```

**Color palette:**
- Deep navy blue / dark corporate tones
- Clean white / steel gray accents
- Precise, structured compositions
- Avoid: warm tones, casual settings, anything startup-looking

**Metaphors that resonate with CFO/Procurement ICP:**
- Supply chain / logistics imagery (warehouses, networks, flow)
- Financial precision (scales, graphs made physical, ledgers)
- Control room / command center scenes
- Infrastructure (bridges, servers, systems)
- Procurement cycle (handshakes replaced by structural metaphors)

---

## Formula Components

### Shot Types
| Option | When to Use |
|--------|------------|
| `Corporate architectural photography` | Offices, infrastructure |
| `Industrial documentary photograph` | Supply chain, operations |
| `Editorial business photography` | Conceptual, B2B |
| `Aerial cinematic photograph` | Scale, overview, systems |
| `Medium format film photograph` | Premium, precise |

### Lighting for StoreNext
| Phrase | Mood |
|--------|------|
| `cold blue corporate overhead lighting` | Enterprise, clinical precision |
| `clean diffused professional light` | Trustworthy, neutral |
| `dramatic directional light, deep shadows` | Authority, scale |
| `warm boardroom light` | Decision-making, executive |

---

## Iteration Protocol

| Problem | Fix |
|---------|-----|
| Too warm / casual | Add "cold corporate blue tones", remove warm descriptors |
| Too abstract | Make subject more literal and physical |
| Looks startup, not enterprise | Add "Fortune 500 corporate aesthetic, established institution" |
| Too empty / minimal | Add background elements: "large open warehouse", "server room depth" |

**Rule:** Change ONE element per iteration.

---

## API Call Template

```python
import replicate, os, urllib.request
from dotenv import load_dotenv
load_dotenv(r'C:\Users\rant\Documents\ran-workspace\T-tools\api-credentials.env')

output = replicate.run(
    "black-forest-labs/flux-1.1-pro",
    input={
        "prompt": """[YOUR PROMPT HERE]""",
        "aspect_ratio": "16:9",
        "output_format": "png",
        "output_quality": 95,
        "safety_tolerance": 2,
        "prompt_upsampling": True
    }
)
url = str(output)
out_path = r"C:\Users\rant\Documents\ran-workspace\StoreNext\O-output\[WEEK]\[FOLDER]\visual\[name].png"
urllib.request.urlretrieve(url, out_path)
print("Saved:", out_path)
```

---

## Lessons Learned

*Update this table after every visual session.*

| Session | Prompt Issue | What Fixed It |
|---------|-------------|---------------|
| — | — | — |

---

*Flux Prompt Engineering Skill — StoreNext Edition*
*Last updated: 2026-03-16*
