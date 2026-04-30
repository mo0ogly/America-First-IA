# Project Rules

## Writing style — NO AI tics

When writing or editing text (DOCX, Markdown, code comments, commit messages):

- **NEVER use em dashes** (—). Use a comma, period, semicolon, or parentheses instead.
- **NEVER use en dashes** (–) as punctuation. Only use hyphens (-) for compound words or number ranges.
- **NEVER use arrows** (→ ← ↔). Use -> or reformulate the sentence.
- **NEVER use decorative Unicode** (• ◦ ▪ ▸ … ×). Use plain ASCII: -, ..., x.
- **NEVER use emojis** as structural markers (✅ ❌ ⚠️ 🔴). Use words: OK, NO, WARNING.
- **NEVER use curly/smart quotes** (" " ' '). Use straight quotes " or French guillemets << >>.
- Avoid filler phrases: "It's worth noting that", "It's important to note", "Interestingly", "In conclusion", "Let's dive in".
- Avoid excessive hedging: "arguably", "potentially", "it could be said that".
- Write naturally, like a competent human would. Vary sentence length. Mix short and longer sentences to create a natural rhythm.
- Do NOT write robotic ultra-short sentences ("Done. Fixed. Pushed."). That is an obvious AI pattern.
- Use simple punctuation. A period is almost always better than a semicolon.

## Language

- Default language for conversation: French
- Documents exist in 3 languages: EN, FR, BR (Portuguese Brazil)
- Code comments and commit messages: English

## CACI Dashboard

- Formula: `CACI = F^0.40 x L^0.20 x R^0.15 / E^0.25` (Power Mode)
- Intensity Mode adds `/ GDP` in denominator
- Data comes from CSV files in `caci-dashboard/public/data/`
- Key stats (from CSV): 77% US compute share, CACI US/EU ratio 3.4:1
