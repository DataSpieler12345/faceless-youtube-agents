# Script to Slides

You are converting a narration script into a structured slides JSON that the YT Video Factory pipeline can process.

## Input

A narration script (plain text) + video configuration:
- **style**: text-heavy | documentary | 3d-render | sketch | anime
- **title**: The video title
- **description**: YouTube description
- **tags**: YouTube tags

## Rules

### Slide Duration
- Each slide covers 3-4 seconds of voiceover (target ~8-10 words per slide at 2.5 words/sec)
- Split narration at sentence boundaries — never mid-sentence
- If a sentence is long (>12 words), it gets its own slide
- If two short sentences total <10 words, combine them into one slide

### Image Prompts

**For "text-heavy" style:**
- Start every prompt with: `"A wide 16:9 bold modern flat illustration."`
- Include a 5-color design system (pick once, use for all slides):
  - Background hex, Primary hex, Secondary hex, Accent hex, Text hex
- Reference EVERY hex by value in the prompt (e.g., `"#E94560"` not `"primary"`)
- Describe exact text placement: `"Large white (#FFFFFF) bold text reading 'THE FUTURE IS NOW' centered"`
- Include visual elements that support the text
- Add continuity references between slides

**For all other styles (no text in image):**
- Start every prompt with the style prefix from config
- Describe a vivid, cinematic scene that illustrates the narration
- NO text, NO words, NO labels in the image
- Focus on emotion, atmosphere, and visual storytelling
- Maintain visual continuity (consistent color palette, recurring motifs)
- Each image should stand alone as a compelling visual

### Thumbnail Prompt
- Generate ONE attention-grabbing thumbnail prompt
- Must include the video title text baked in (large, bold, readable)
- Use contrasting colors, dramatic composition
- Single focal point + title text
- Resolution: 1280x720

### Narration
- Copy EXACTLY from the source script — do not rewrite
- Split at sentence boundaries only

## Output Format

Write the output as `slides.json` in the run directory. Exact structure:

```json
{
  "title": "The Video Title",
  "description": "YouTube video description (2-3 sentences)",
  "tags": ["tag1", "tag2", "tag3"],
  "style": "documentary",
  "design_system": {
    "background": "#0A0A0A",
    "primary": "#E94560",
    "secondary": "#1A1A2E",
    "accent": "#16213E",
    "text": "#FFFFFF"
  },
  "thumbnail_prompt": "A wide 16:9 dramatic thumbnail showing...",
  "slides": [
    {
      "slide_number": 1,
      "narration": "The exact voiceover text for this slide.",
      "image_prompt": "A wide 16:9 photorealistic cinematic photograph. A vast server room...",
      "duration": 4
    },
    {
      "slide_number": 2,
      "narration": "Next sentence of voiceover.",
      "image_prompt": "A wide 16:9 photorealistic cinematic photograph. Close-up of...",
      "duration": 3
    }
  ]
}
```

### Duration Calculation
For each slide: `duration = max(3, min(10, round(word_count / 2.5)))`

### Quality Checks Before Output
1. All narration segments concatenated = original script (no words added or lost)
2. Every slide has 3-10 second duration
3. Image prompts are 3-6 sentences each (detailed enough for good generation)
4. Thumbnail prompt includes title text
5. design_system is included (even for non-text styles, for visual consistency)
6. No slide has more than ~25 words of narration (split if longer)
