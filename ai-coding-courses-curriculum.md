# AI Coding Courses — Master Curriculum

*Source of truth for course content. Reference this document when producing website copy, slide decks, session outlines, or marketing materials.*

**Last updated:** March 2026
**Audience:** Non-technical white collar professionals
**Format:** 60–90 minute sessions, in-person or virtual

---

## Overview

Two courses are offered as a progressive track:

| Course | Level | Sessions | Goal |
|--------|-------|----------|------|
| **Intro to Vibe Coding** | Beginner | 2–3 sessions | Build and deploy a simple web app using only plain English |
| **Intermediate Vibe Coding** | Intermediate | 3–4 sessions | Set up a real developer workflow with GitHub, Cursor, and basic AI agents |

Students can take each course standalone or as a sequence. No coding experience is required for either course. Intro is the recommended starting point for anyone who has never built with AI tools before.

---

---

# Course 1: Intro to Vibe Coding

## Course Description

"Vibe coding" is the practice of building software by describing what you want in plain English — no programming knowledge required. This course is about experiencing that firsthand. Students will leave having actually shipped something: a working app or game, live on the internet, built entirely through conversation with AI.

The goal is not to learn to code. The goal is to discover how much you can create just by knowing what you want and being able to describe it.

## Who This Is For

White collar professionals who are curious about AI tools but haven't built anything yet. No technical background required. If you can write an email, you can take this course.

## Learning Outcomes

By the end of this course, students will be able to:

- Understand what vibe coding is and why it's meaningful right now
- Choose the right AI tool for a given task
- Build a working web app or interactive experience from scratch using only natural language
- Deploy a project so it has a real, shareable URL
- Apply an iterative "describe → see → improve" loop to keep making something better

## Course Philosophy

This course treats the student as the product manager and the AI as the developer. The core skill being trained is **intent communication** — the ability to describe what you want clearly enough that AI can build it. Students who leave this course feeling the "shock" of having created something real, with no code, are primed to go further.

---

## Session 1: What Is Vibe Coding? (Your First App in 60 Minutes)

**Duration:** 60–90 minutes
**Goal:** Students build their first working app live, in the session.

### Why now?

- Brief framing: AI tools have crossed a threshold where non-technical people can build real things
- The transition from "copy-pasting AI outputs blindly" to actually directing the AI with intention
- What's possible today vs. even 12 months ago
- The "shocking" feeling of creating something that exists — and why it matters

### Mental model: You're the PM, AI is the dev

- You don't need to know how to code; you need to know what you want
- Your job is to communicate intent clearly — think less "make it more fun" and more concrete descriptions
- How communicating with AI is like working with a designer or developer: specificity gets results
- Design inspiration as a tool: screenshots, references, and visual language help the AI understand your vision (Dribbble, screenshots of apps you like)

### Tour of the landscape

A brief overview of the main platforms — when to use which, and what makes each one distinct:

| Tool | Best for | Notes |
|------|----------|-------|
| **Claude Artifacts** | Quick one-off experiments, games, interactive tools | No deployment needed; runs right in the chat; great starting point |
| **Lovable** | Full web apps with a nice UI | Polished output; adds its own branding by default; good for prototypes |
| **V0** (by Vercel) | UI components and clean front-end work | Strong design sensibility; integrates with Vercel for easy deploy |
| **Bolt** | Fast full-stack app prototyping | Quick to get a working app; good for slightly more complex builds |
| **Base44** | Simple apps and internal tools | Clean interface; good for business-oriented tools |
| **Replit** | Code + run in the browser | More hands-on; good when you want to see and optionally edit code |

The key insight: these tools are all variations on the same idea. Pick one and learn it well rather than juggling all of them.

### Live exercise: Build something right now

Students choose one of the following (or bring their own idea):

- A simple game (trivia, word game, tile puzzle)
- A personal landing page or portfolio
- A tool they actually want to use (habit tracker, simple calculator, idea journal)

Walk through the process together:

1. Start with a plain-English description of what you want
2. Let the AI generate a first version
3. Look at it with a critical eye and describe what to change
4. Iterate 2–3 times in session

**The "just start" lesson:** 90% of building with AI is easy and fast. The last 10% is where the real problem-solving happens — and that's where the learning is.

### Key concept: The iteration loop

```
Describe what you want → See what it builds → Notice what's off → Describe the change → Repeat
```

The faster you get comfortable with this loop, the more powerful you become.

---

## Session 2: Making It Real

**Duration:** 60–90 minutes
**Goal:** Students deploy what they built and give it a real, shareable URL.

### Why "real" matters

- A link you can send to someone feels completely different from a prototype that only you can see
- The psychological shift from "this is an experiment" to "this is a thing that exists"
- Why deploying early, even with rough edges, is better than waiting for perfection

### Deployment basics with Vercel

- What deployment is: moving code from your laptop (or the AI tool's sandbox) to the internet
- Vercel as the go-to free hosting platform for vibe-coded projects
- Step-by-step walkthrough:
  1. Export or download your project from Lovable/Bolt/V0
  2. Connect to Vercel
  3. Get a live URL in under 5 minutes

### Custom domains (brief intro)

- Why the default URL (e.g., `your-app.lovable.app`) looks obviously AI-generated
- Buying a domain through a registrar (Squarespace, Namecheap, Google Domains)
- Pointing it at Vercel — high level only

### Polish: the details that make something feel real

Three small moves that dramatically change how a project looks when shared:

- **Favicon:** The tiny icon in the browser tab — without it, the tab looks blank and generic
- **Open Graph image:** The image that appears when you share a link in iMessage, Slack, or social media — without it, you get an ugly blank preview
- **Professional URL:** Swapping `your-thing.lovable.app` for `yourthing.com`

Walk through asking the AI to add each of these things: "Add a favicon using a [description] icon" and "Add an Open Graph image with [description] so that when this link is shared it looks good."

### The "critical eye" habit

- How to look at your own project the way a user would
- The practice of asking AI: "Look at this app and tell me 5 things that would make it feel more polished"
- Using AI not just to build but to audit and improve

### Live exercise: Deploy what you built in Session 1

Students leave Session 2 with a live URL they can share with anyone.

---

## Session 3 (Optional): Going Further

**Duration:** 60–90 minutes
**Goal:** Students build on the foundation and begin thinking about more ambitious projects.

### Planning before building (product thinking)

- The power of using AI for upfront thinking, not just execution
- Brain-dumping your idea to AI: customer, problem, features, priorities
- Creating a simple spec (like a PRD): "Here's what I'm building and why" — so the AI knows what it's working toward and doesn't have to guess
- Asking AI: "Based on what I described, what are the 5 most important things this app needs to do?"

### When Lovable/Bolt is the right tool — and when it isn't

- For truly simple projects or fast prototypes: stay in these tools
- For anything you'll keep iterating on for weeks or months: the intermediate course tools (GitHub, Cursor) become worth learning
- The decision point: "Is this a prototype I'll throw away, or a product I'll actually maintain?"

### Know your limits (and AI's limits)

- The "context window" problem: why AI sometimes seems to "get dumber" as a conversation gets longer
- What to do when AI starts breaking things it already fixed
- When to start fresh vs. push through

### What to build next

- Personal project as the best learning vehicle: pick something you actually want to exist
- Ideas by audience:
  - For teams: internal tools, dashboards, simple form-based workflows
  - For personal use: habit trackers, idea journals, simple games
  - For side projects: landing pages, portfolio sites, small SaaS concepts
- The 80/20: most of what you'll want to build is well within what these tools can handle

### Looking ahead: the intermediate course

- Preview of what comes next: real developer workflow, GitHub, Cursor, AI agents
- When it makes sense to level up: when you're hitting walls, building something you care about long-term, or want to understand what's actually happening under the hood

---

## Tools Referenced (Intro Course)

- **Claude Artifacts** — interactive experiments directly in Claude chat
- **Lovable** — full web app generation; adds Lovable branding by default
- **V0** (Vercel) — UI and front-end component generation
- **Bolt** — fast full-stack prototyping
- **Base44** — simple apps and internal tools
- **Replit** — code + run in the browser
- **Vercel** — free deployment platform; the go-to for getting a live URL
- **Squarespace / Namecheap** — domain registrars for buying a custom URL
- **Dribbble** — design inspiration and visual reference material

---

---

# Course 2: Intermediate Vibe Coding

## Course Description

This course is for people who've already tasted what's possible with vibe coding and want to build more serious things — apps they'll actually maintain, tools they'll share with colleagues, and workflows that save them real time. Students will set up a professional-grade AI development environment using the same tools working developers use, adapted for non-technical builders.

The difference between intro and intermediate isn't how much code you write — it's the infrastructure around the code. This course teaches you to work like someone who's serious about building.

## Who This Is For

Professionals who have either completed the Intro course or have some experience with AI coding tools (Lovable, ChatGPT for code, etc.) and feel ready to understand the full picture. Also appropriate for anyone who's hit the limits of simpler tools and wants more control.

## Learning Outcomes

By the end of this course, students will be able to:

- Set up and use a real developer environment (VS Code or Cursor, GitHub)
- Understand the relationship between local files, GitHub, and deployment
- Use AI coding tools effectively inside a proper editor (Cursor, Claude Code, Codex)
- Keep AI from "forgetting" context using documentation habits
- Understand what an AI agent is and how to build simple automated workflows

---

## Session 1: Setting Up Your Real Dev Environment

**Duration:** 60–90 minutes
**Goal:** Students have a working local environment with GitHub connected by end of session.

### The mental model shift

- In intro tools (Lovable, Bolt), the code lives somewhere else — you never see it
- Intermediate workflow: code lives on your computer, backed up to GitHub, deployed via Vercel
- Why this matters: you own it, you can switch tools, nothing gets lost

### The building blocks of web development

Four components that make up nearly every web project:

1. **Code** — the files that make up your app (HTML, CSS, JavaScript, and libraries like Tailwind that make styling easier)
2. **Deployment/hosting** — where your app actually runs and how people access it (Vercel, Netlify)
3. **Domain** — the URL that points people to your app (Squarespace, Namecheap, Google Domains)
4. **Backend** (optional) — databases, user accounts, and server logic — most beginner/intermediate projects don't need this

Understanding these four layers is the "mental layout" that makes everything else click into place.

### GitHub: Google Drive for code

- What GitHub is: cloud storage for code, with version history
- The local clone: why you always have a copy on your computer and one in the cloud
- The workflow: work locally → push to GitHub → Vercel auto-deploys
- GitHub Desktop vs the command line: you don't need to use the terminal directly — AI and VS Code handle most of it
- The only things you need to understand:
  - A **repo** is a project folder with a history
  - **Committing** is saving a named checkpoint
  - **Pushing** sends that checkpoint to the cloud

### VS Code and Cursor

- **VS Code** is the industry-standard code editor — think of it as a very smart file viewer with a built-in terminal
- **Cursor** is a fork of VS Code with AI built directly in — conceptually identical, but you can chat with your code natively
- For most people: start with Cursor; everything you learn applies to VS Code too
- The five zones of the VS Code/Cursor interface:
  - Left sidebar (file explorer, extensions, source control)
  - Main editor area
  - Terminal (at the bottom — you'll use this occasionally, when AI tells you to)
  - AI chat panel (Cursor's built-in chat / Claude Code extension)
  - Preview pane (for seeing your app without a browser)

### Live exercise: Set up your environment

Step-by-step walkthrough:

1. Install VS Code or Cursor
2. Create a GitHub account (if needed)
3. Start a project in Lovable or V0 → export/download the code
4. Create one organized folder on your computer (e.g., `AI Projects`) — this is where everything lives
5. Drop the project into that folder
6. Open it in Cursor
7. Tell the AI: "Connect this project to a new GitHub repo and push it"
8. Verify it appears on github.com

---

## Session 2: Working with AI Coding Tools

**Duration:** 60–90 minutes
**Goal:** Students are fluent in the main AI coding tools inside their editor, and know how to see and test their work.

### The AI tools landscape (inside your editor)

Multiple AI tools can operate inside VS Code/Cursor — think of them as different assistants you can call on:

| Tool | What it is | Best use |
|------|-----------|---------|
| **Cursor (built-in)** | AI woven into the editor itself | Everyday coding, inline edits, chat about your code |
| **Claude Code** (extension) | Claude operating as an agent in your editor | Complex, multi-step tasks; works across multiple files |
| **Codex** (extension + Mac app) | OpenAI's coding model | Alternative to Claude; good second opinion |

The practical difference between these tools is small for most tasks. The key is learning how to communicate well with any of them — that skill transfers.

### Using the AI in practice

- **Inline chat vs agent mode:** inline is for quick edits ("change this button color"); agent mode is for larger tasks ("add a login page that connects to my existing navbar")
- How to give the AI good context: don't just say what to do, say what you're building and why
- Watching what the AI edits: keeping situational awareness by noticing which files change
- Using Cursor's visual features: clicking on a part of the page preview and saying "change this section" — the AI can see what you're pointing at

### Seeing and testing your app

- Starting a dev server: the app running locally so you can see changes in real time
  - You don't need to know the command — just tell the AI: "Spin up a dev server so I can see what you did"
- Preview in Cursor vs. your browser: Cursor's built-in preview is fine for quick checks; browser is better for accurate testing
- The loop: make a change → dev server refreshes → you see the result instantly

### When to use the terminal

- You should almost never need to use the terminal directly
- Two exceptions: (1) starting a dev server when the AI can't do it automatically, (2) when the AI explicitly tells you to run a specific command
- Letting AI handle Git (`git init`, commits, branches) from inside the editor rather than learning the command line deeply
- If you see something you don't understand in the terminal, just ask the AI: "What does this mean and what should I do?"

### Extensions worth installing

- Claude Code (for Cursor/VS Code)
- Codex (for a second AI option)
- GitHub extension (simplifies repo management)
- Prettier (auto-formats code — keeps things tidy)

### Live exercise: Iterate on your project with proper tools

Take the project from Session 1 and make 3 meaningful changes using the AI inside Cursor. Practice: (1) asking for a change in the chat, (2) watching which files change, (3) seeing the result in the preview, (4) committing to GitHub.

---

## Session 3: Building Good Habits

**Duration:** 60–90 minutes
**Goal:** Students understand how to keep AI useful across long projects by managing context and documentation.

### Why AI "gets dumber" over time — and what to do about it

- The context window: AI can only "see" a limited amount of conversation and code at once
- As a project grows, the AI has less room to hold everything in mind at once
- Signs of context exhaustion: breaking things it already fixed, reverting earlier decisions, giving generic answers
- The solution: **documentation as memory** — teaching the AI what it needs to know at the start of each session

### The documentation system

Three types of files that serve as your AI's external memory:

**Project-level context (`claude.md` or `README.md` in the root)**

This is the most important file. It tells any AI tool (or new collaborator) exactly what this project is. Ask the AI to create and maintain it:

> "Write a `claude.md` file for this project that explains what we're building, the key decisions we've made, the current state of the app, and what we're working on next."

Paste this file into the AI chat at the start of each session: "Here's the context for this project — read this first."

**Component-level readmes**

For larger projects: a brief markdown file in each major folder explaining what that part of the code does.

**Running notes / changelog**

A simple log of what was built, what was tried, and what didn't work. Prevents AI from re-suggesting approaches you've already ruled out.

### The habit: update docs as you go

After a productive session, ask the AI:

> "Update the project README with what we built today and add any open TODOs you're aware of."

This takes 30 seconds and saves enormous confusion later.

### Planning before prompting

- The biggest mistake: jumping straight into building without describing what you're building
- The PRD habit: before starting a new feature, brain-dump your intent to the AI:
  - What is this feature for?
  - Who uses it and how?
  - What are the 3 most important things it has to do?
  - What does success look like?
- Ask the AI to confirm back: "Based on what I described, explain your plan before you start coding"
- This surfaces misunderstandings before they become built mistakes

### Understanding your codebase (at a high level)

You don't need to read code — but you should know what files do what:

- `index.html` or similar: the main page
- CSS files / Tailwind classes: how the app looks
- JavaScript files: how the app behaves
- `package.json`: the list of tools and libraries your project uses
- The `.env` file (if present): private credentials — never share this file or commit it to GitHub

### Live exercise: Build the documentation habit

Take your existing project and ask the AI to:
1. Write a `claude.md` from scratch that captures everything about the project
2. List all the TODOs it's aware of
3. Explain the current file structure in plain English

Review the output and correct anything wrong. This is now your project's source of truth.

---

## Session 4: Agents and Automation

**Duration:** 60–90 minutes
**Goal:** Students understand what an AI agent is, can use agents for real tasks, and know how to think about automation workflows.

### What's the difference between "chat" and an "agent"?

- **Chat (one-shot):** you ask, AI responds, you copy the output and do something with it
- **Agent:** AI that can use tools, take actions, and work through a multi-step task on its own

Most "agents" in practice are just AI with access to a few extra tools (search, file reading, code execution). The UX is often identical to chat — the difference is what happens underneath.

Real examples of agents you may already be using without realizing it:
- "Search these 10 government sites, summarize what you find, and put it in a spreadsheet" → that's an agent task
- "Review this document against these criteria and give me detailed feedback" → agent task
- Claude Code running in your repo, editing multiple files to complete a feature → agent

### Agents you can build right now

**One-shot workflow agents (triggered manually):**

These are prompts you save and reuse. They're "agents" in the sense that you give them a task and they work through it step by step:

- **Document reviewer:** Share a repo or skill with teammates. They run it on their docs to get structured, consistent feedback — like a very picky editor who never gets tired.
- **Research to spreadsheet:** "Search [these sources], find all mentions of [X], and create a spreadsheet with [columns]"
- **Status update drafter:** "Here are my notes from this week and the prior week's status deck. Draft my Friday update in the same format."

These workflows are already enormously valuable and require zero additional tools.

**The Apple example (real workflow):**
> Every Friday, Claude reads the week's notes, pulls from Slack, and drafts a status slide in the existing format. What used to take 30 minutes of writing now takes 5 minutes of review and light editing.

### When you need more: triggered workflows

Some automation ideas require AI to wake up on a schedule or respond to events (a new email, a calendar entry, an incoming form submission). This is where you need workflow platforms:

- **n8n** and **Make** are the main tools — think of them as "Rube Goldberg machine builders" for software
- You connect triggers (email arrives, time of day, form submitted) to actions (run an AI prompt, update a spreadsheet, send a Slack message)
- Authentication is the hard part: these tools require access to your accounts, which involves OAuth connections and API keys

Honest assessment: triggered, autonomous workflows are genuinely more complex to set up than one-shot agents. Worth learning if you have a clear, recurring workflow in mind. Not worth starting with.

### The spectrum: where does your idea sit?

Ask this to evaluate any automation idea:

1. **Is this something I'd want to trigger manually each time?** → One-shot workflow; just save a good prompt.
2. **Is this something that happens on a schedule?** → Triggered workflow; consider n8n or Make.
3. **Is this something that reacts to events in real time?** → More complex; may require engineering help.

Most valuable business workflows live in category 1. Start there.

### Skills and slash commands

- A "skill" is a reusable prompt that gives AI a specific persona, task, and format — essentially a saved workflow in markdown
- Slash commands are shortcuts to run skills
- Think of them as specialized reviewers or assistants: a "sub-agent" that reviews documents, writes in a specific voice, or applies a specific framework
- These are simple enough to build yourself: describe the task, the format, and any constraints in a markdown file

### Tool landscape for agents and automation

| Tool | Role |
|------|------|
| **Claude Code** | Agent operating inside your repo / editor |
| **Codex** | Similar; OpenAI's equivalent |
| **Claude Cowork** | Desktop agent for file and task management (less code-focused) |
| **n8n** | Open-source workflow automation (self-hosted or cloud) |
| **Make** | SaaS workflow automation; more user-friendly than n8n |
| **Claude Skills / markdown prompts** | Lightweight reusable agents you build yourself |

### Live exercise: Build your first one-shot workflow

Students pick a real, recurring task they do (weekly update, document review, meeting notes cleanup) and:

1. Describe the task to Claude in detail
2. Provide an example input
3. Refine the output format until it's right
4. Save the prompt as a reusable "skill" or template they can run next week

---

## Tools Referenced (Intermediate Course)

**Code hosting & deployment:**
- GitHub (web + local clones)
- GitHub Desktop (mentioned; not required)
- Vercel (deployment, custom domains, favicon/OG images)
- Netlify (similar to Vercel)
- Squarespace / Namecheap (domain registrars)

**Code editors / IDEs:**
- VS Code (Visual Studio Code)
- Cursor (VS Code fork with built-in AI and preview)

**AI coding tools:**
- Cursor (built-in AI)
- Claude Code (VS Code/Cursor extension)
- Codex (VS Code extension + standalone Mac app)
- Claude Cowork (desktop agent mode)
- V0 (AI prototyping; good source for exporting into a real workflow)
- Lovable (similar; note: adds its own branding)
- ChatGPT (useful for planning and early-stage prototyping)

**Automation / agents / workflow tools:**
- n8n (workflow automation)
- Make (workflow automation; more accessible)
- Claude Skills / markdown skill files (lightweight reusable agents)
- MCP + browser control (for allowing AI to operate your browser)

**Supporting tools / context:**
- Slack (input to automated workflows)
- Dribbble (design inspiration and visual reference)

---

---

## Appendix: Frequently Asked Questions

These are real questions from students, useful for calibrating instruction and anticipating confusion.

**"Is the struggle worth it right now, or should I wait for tooling to mature?"**
Starting earlier means you'll be better at it when it matters. The tools are already good enough to build real things. The main skill being developed — communicating clearly with AI — only improves through practice, not through waiting.

**"Do I need to read all the code the AI writes?"**
No. You should know what files exist and roughly what they do. You don't need to understand the syntax. Your job is to review the *output* (what the app does) and direct the AI when something's wrong.

**"Why does the AI seem to get dumber as I keep fixing things?"**
Context limits. As the conversation grows, the AI has less room to remember everything. See Session 3 of the Intermediate course for the documentation habits that solve this.

**"What's the difference between Claude Code, Codex, and Cowork?"**
- **Claude Code**: An agent that runs inside your code editor, can read and edit your files, and executes multi-step coding tasks
- **Codex**: OpenAI's equivalent; similar function, different underlying model
- **Cowork**: A desktop-level agent for file and task management — less focused on code, more on general productivity
For coding work, Claude Code or Codex. For file organization, research, and document tasks, Cowork.

**"What's the difference between an agent and just telling it something in chat?"**
An agent can take *actions* — edit files, run code, search the web, call APIs. Regular chat produces text you then act on yourself. In practice, the line blurs constantly: many "chat" interfaces are actually running agents under the hood.

**"If I want something like a family calendar manager that runs by itself, is that actually possible?"**
Yes, but it requires a triggered workflow (n8n or Make) plus OAuth connections to your calendar. It's doable — but it's an intermediate-to-advanced project. Start with one-shot workflows first.

**"What's the real difference between Lovable and VS Code/Cursor?"**
Lovable is like building with pre-assembled furniture — fast, clean, limited. VS Code/Cursor is like having a workshop: more setup, but you can build anything. When your project is simple or temporary, Lovable is right. When you'll keep working on it or need more control, move to a real editor.

---

*End of master curriculum document. Reference this file when producing: website copy, course landing pages, session slide decks, email sequences, or social content.*
