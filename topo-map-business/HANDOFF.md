# Topo Map Business — Session Handoff
*Last updated: March 1, 2026 | For continuation in a fresh Claude session*

---

## What This Business Is

You have a proprietary rendering engine that generates visually rich, artistic topographic maps for any coordinates worldwide, with any color scheme. You want to turn this into a passive side business selling custom topo map art.

The research is done. The product is validated. You have a Printify account with products already created. The next step is completing one piece of missing data, then starting to sell.

---

## What's Already Done

### Research report
`report.md` in this repo is a complete 8-section business research report covering:
1. POD canvas vendors & verified pricing (Printify + Printful, Gelato, Gooten estimates)
2. Embroidery on demand (short answer: not viable for wall art yet)
3. Customer segments & go-to-market sizing
4. Distribution strategy (Etsy → Shopify → configurator phased rollout)
5. Competitive landscape (Mapiful, Topographia Design, Etsy sellers)
6. Operations & infrastructure stack
7. Financial model / P&L with verified unit economics
8. Summary & prioritized action plan

A formatted Word version also exists at `mnt/outputs/topo-map-business-report.docx` (39KB, 843 paragraphs).

### Verified Printify pricing (already in report)
Captured directly from your Printify account in an authenticated browser session (Feb 2026):
- All 60 sizes + prices for **Jondo Matte Canvas Stretched 1.25"** (standard + Premium)
- All 6 economy shipping tiers for Jondo (US, 4–8 business days)
- Starting prices for all canvas products in your account
- Premium plan discount verified at exactly **25% off** (not just "~20%")

### Your existing Printify products
Your account already has 3 products set up:
- **Matte Canvas, Framed (Multi-color)** — teal topo art with purple heart location marker (Jondo, Trending label)
- Softcover journal
- Scented candles

The **framed canvas is your hero product** — gift-ready, attractive framing in black/white/natural/brown, strongly positioned for the gifting and outdoor segments.

---

## What's NOT Done Yet — The One Blocker

### Framed canvas per-size pricing

**What we need:** The full price table for the **Jondo Matte Canvas, Framed Multi-color** (Printify product #944 / #1174) — all sizes with standard price, Premium price, and shipping tiers.

**What we have:** Only the starting price ($22.19 standard / $15.84 Premium). The shipping tiers in the report for the framed canvas are marked as *estimates*.

**Why it matters:** You specifically said the framed canvas feels like the most complete, attractive product (especially in black or white). Before optimizing your pricing and Etsy listings around it, you need the actual per-size costs.

**Why it's not done:** Browser automation was broken during this session. Every time Claude attempted to use the browser tools, a "Claude log in to your subscription" popup appeared in the headless browser and blocked all actions. Web search and WebFetch don't work either (Printify.com is blocked by the network egress proxy).

---

## How to Fix the Browser Automation Issue

The next Claude session will need to pull framed canvas pricing from your Printify account. Here's what to try:

### Option A — Just log in and share the data manually (fastest)
1. Go to printify.com and log in
2. Open the **Matte Canvas, Framed (Multi-color)** product catalog page
3. Take a screenshot of the pricing table showing all sizes
4. Paste it into the next Claude session

This bypasses the automation issue entirely and gets you the data in under 5 minutes.

### Option B — Let Claude try browser automation again
In the next session, tell Claude: *"I'm logged in to Printify. Please navigate to my Printify catalog and pull the framed canvas pricing."*

The headless browser (Claude in Chrome) should be able to access your browser session. If the "log in to your subscription" popup appears again:
- Dismiss/close it
- Tell Claude to try again immediately after
- The popup seems to appear when browser automation is first initiated; a second attempt may succeed

### Option C — Provide the data from Printify's UI
The data Claude needs from Printify:
1. Go to: `https://printify.com/app/products/944/generic-brand/matte-canvas-framed-multi-color`
2. Click through each popular size and note the price
3. Or open the Shipping tab for the framed canvas and screenshot the shipping tiers

The most useful sizes to capture: 9×12", 12×16", 12×18", 16×20", 18×24", 20×24", 24×30"

---

## What to Do in the Next Session

### Priority 1: Get framed canvas pricing
Use one of the options above. Once you have:
- Per-size prices (standard + Premium) for key sizes
- Shipping tiers for the framed canvas

...Claude can update Section 1.4 of the report with real framed canvas COGS and update the P&L model accordingly.

### Priority 2: Walk through the report together
You said: *"Can we talk through each section together? I want to make sure I understand it but also iterate as needed."*

This hasn't happened yet. The report is complete enough to walk through section by section and identify what to adjust, especially around:
- Which sizes to focus on for Etsy listings
- Whether to lead with framed or unframed canvas
- Pricing strategy for your first 10–15 listings
- What the first week of Etsy setup actually looks like

### Priority 3 (optional): Start Etsy setup
Once pricing is confirmed, the next concrete action is:
1. Create your Etsy shop (if not already done)
2. Connect Printify to Etsy
3. Create your first 3–5 listings (framed canvas at key sizes)
4. Write listing titles targeting gifting + outdoor search terms

---

## Key Numbers to Keep in Mind

**Framed canvas (estimates — need verification):**
- Starting price: $22.19 standard / $15.84 Premium (25% off)
- Shipping: estimated ~$8.99–$11.79 economy for popular sizes
- Suggested retail: $79–$99 (12×9"), $99–$129 (16×20"), $139–$169 (24×30")
- Estimated margin at Premium: ~75–80%

**Stretched canvas (verified):**
- 16×20" sweet spot: $25.76 standard / $19.20 Premium + $8.99 shipping
- Suggest retail: $79–99 → ~72–78% margin with Premium at Etsy
- 18×24" sweet spot: $29.21 / $21.77 Premium + $11.79 shipping
- Suggested retail: $99–$119 → ~72–78% margin

**Printify Premium:** $29/mo. Pays for itself at 5 orders of 16×20". Breakeven: 4–5 orders/month even with Shopify added.

---

## Files in This Repo

| File | What it is |
|------|-----------|
| `HANDOFF.md` | This document |
| `report.md` | Full 8-section business research report (markdown) |
| `mnt/outputs/topo-map-business-report.docx` | Formatted Word version of the report (39KB) |
| `mnt/outputs/topo-map-business-report.js` | Node.js script that generates the Word doc (uses `docx` npm library) |

---

## Technical Notes (for Claude, not for Teera)

The Word doc generation script is at `/sessions/zen-laughing-allen/topo-map-business-report.js` (in the VM, not this repo). Key implementation details:
- Uses `docx` npm library
- `makeTable()` helper handles string, array, or bare TextRun objects as cell values
- `ShadingType.CLEAR` (not SOLID) for table shading
- `WidthType.DXA` for all table widths
- Page size: US Letter (12240 × 15840 DXA)
- Output: `/sessions/zen-laughing-allen/mnt/outputs/topo-map-business-report.docx`

DOM selector that worked for scraping Printify pricing tables: `pfy-variants-table-title-row`

Printify.com is blocked by the network egress proxy (`EGRESS_BLOCKED`) — use browser automation, not WebFetch.
