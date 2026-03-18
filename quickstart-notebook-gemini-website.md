# Quick Start: Build a Website with NotebookLM + Gemini Canvas

**Time to complete:** 30-60 minutes
**Skill level:** Beginner-friendly
**What you'll build:** A professional website ready to deploy

---

## Overview

This guide shows you how to create production-ready websites using Google's NotebookLM for content organization and Gemini Canvas for code generation. The workflow is perfect for portfolios, landing pages, documentation sites, and more.

### What You'll Need

- Google account (for NotebookLM and Gemini)
- Basic understanding of what websites are (no coding required!)
- Content for your website (text, links to images, etc.)

### Why This Workflow Works

- **No coding required** - Gemini generates all the HTML/CSS
- **Professional results** - Modern, responsive designs
- **Fast iteration** - Make changes instantly with natural language
- **Production-ready** - Code that works across all browsers and devices

---

## The 5-Step Process

### Step 1: Organize Your Content in NotebookLM (10 minutes)

NotebookLM helps you gather and structure all your website content before generating code.

#### What to Do:

1. **Go to [NotebookLM](https://notebooklm.google.com)**
2. **Create a new notebook** - Name it after your website project (e.g., "My Portfolio Site")
3. **Add your content as sources:**
   - Upload documents (resume, about me, project descriptions)
   - Paste URLs (LinkedIn, GitHub, Dribbble profiles)
   - Add notes with raw content you want on the site

#### Example Content Structure:

```
Source 1: About Me
- Bio paragraph
- Skills list
- Professional photo URL

Source 2: Projects
- Project 1: Title, description, technologies, link
- Project 2: Title, description, technologies, link
- Project 3: Title, description, technologies, link

Source 3: Contact Information
- Email
- LinkedIn
- GitHub
- Portfolio links
```

#### Pro Tips:

✅ **DO:**
- Organize content by page sections
- Include all text exactly as you want it to appear
- Note image URLs or descriptions
- Specify color preferences or brand guidelines

❌ **DON'T:**
- Worry about formatting yet - just gather content
- Include things you don't want public
- Skip important details (better to have too much than too little)

---

### Step 2: Ask NotebookLM for a Website Brief (5 minutes)

Let NotebookLM analyze your content and create a structured brief for Gemini.

#### The Prompt:

```
Based on all my sources, create a comprehensive website brief that includes:

1. Site type and purpose
2. Target audience
3. All content organized by section
4. Design preferences (colors, style, mood)
5. Required features and functionality
6. Navigation structure

Format this so it's ready to give to an AI code generator.
```

#### What You'll Get:

NotebookLM will synthesize your content into a clear, structured brief like:

```
Website Brief: Professional Portfolio

Purpose: Showcase design work and attract client inquiries
Audience: Potential clients and employers in tech/design

Sections:
- Hero: "Jane Doe - Product Designer crafting delightful experiences"
- Projects: 3 case studies with images and descriptions
- About: Background, skills, process
- Contact: Email, LinkedIn, Dribbble

Style: Modern, clean, professional with purple accent color (#764ba2)
Features: Responsive design, smooth scrolling, project filtering
```

#### Pro Tips:

- Copy this brief to a text file - you'll paste it into Gemini
- Review and edit any details NotebookLM got wrong
- Add any missing requirements you thought of

---

### Step 3: Generate Your Website with Gemini Canvas (10 minutes)

Now take your brief to Gemini and generate the actual website code.

#### What to Do:

1. **Go to [Gemini](https://gemini.google.com)**
2. **Paste this prompt + your brief:**

```
Create a complete, single-page HTML website with inline CSS based on this brief:

[PASTE YOUR NOTEBOOKLM BRIEF HERE]

Requirements:
- Single HTML file with all styles inline
- Modern, professional design
- Fully responsive (mobile, tablet, desktop)
- Smooth scrolling navigation
- Production-ready code
- Include placeholder comments for images

Generate the complete HTML code.
```

#### What Happens:

Gemini will:
1. Analyze your brief
2. Design the layout and structure
3. Generate complete HTML with CSS
4. Create a file you can immediately test

#### Pro Tips:

- Gemini might ask clarifying questions - answer them!
- If the code is too long, ask: "Continue from where you left off"
- Request the code in Canvas mode for easier editing

---

### Step 4: Test and Iterate (15-30 minutes)

Now refine your website through conversation with Gemini.

#### How to Test:

1. **Copy the HTML code** from Gemini
2. **Save as `.html` file** (e.g., `index.html`)
3. **Open in your browser** - just double-click the file
4. **View on mobile** - resize your browser window

#### Common Refinements:

**Change colors:**
```
Change the purple accent color to teal (#14b8a6) throughout the site
```

**Adjust layout:**
```
Make the hero section taller and center the text vertically
```

**Add features:**
```
Add a sticky navigation bar that appears when scrolling down
```

**Modify content:**
```
Change the about section to a two-column layout with image on the left
```

**Fix mobile issues:**
```
The navigation menu is too cramped on mobile - make it a hamburger menu
```

#### Iteration Workflow:

1. Describe what you want to change
2. Gemini updates the code
3. Copy, save, and refresh your browser
4. Repeat until perfect

#### Pro Tips:

✅ **Effective iteration prompts:**
- "Make the font size larger for headings"
- "Add more spacing between sections"
- "Change the project cards to show 2 columns instead of 3"
- "Add hover effects to the buttons"

❌ **Avoid vague requests:**
- "Make it better" (too vague)
- "Fix the design" (what needs fixing?)
- "It doesn't look right" (be specific!)

---

### Step 5: Deploy Your Website (10-15 minutes)

Get your website live on the internet for free.

#### Option A: Netlify Drop (Easiest)

1. Go to [drop.netlify.com](https://drop.netlify.com)
2. Drag your HTML file onto the page
3. Get instant URL: `https://random-name-123.netlify.app`
4. **Free custom domain** available in settings

#### Option B: GitHub Pages (Best for portfolios)

1. Create a GitHub account if you don't have one
2. Create a new repository named `username.github.io`
3. Upload your HTML file (rename to `index.html`)
4. Enable GitHub Pages in Settings → Pages
5. Your site will be live at `https://username.github.io`

#### Option C: Vercel (Professional)

1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click "Add New" → "Project"
4. Upload your HTML file
5. Get instant deployment with custom domain support

#### Pro Tips:

- **Images:** Host on Imgur, Cloudinary, or in the same repo
- **Custom domain:** Most platforms support custom domains (yourname.com)
- **Updates:** Just re-upload the HTML file to deploy changes
- **Free tier:** All these options are free for personal projects

---

## Real-World Example: Portfolio Website

Let's walk through a complete example.

### NotebookLM Setup:

**Source 1 - About:**
```
I'm Alex Chen, a full-stack developer specializing in React and Node.js.
I build scalable web applications and love clean code.
Skills: React, TypeScript, Node.js, PostgreSQL, AWS
```

**Source 2 - Projects:**
```
1. TaskMaster Pro - Team collaboration app with real-time updates
   Tech: React, Socket.io, MongoDB
   Link: github.com/alex/taskmaster

2. DevBlog Engine - Markdown-based blog platform
   Tech: Next.js, MDX, Tailwind CSS
   Link: github.com/alex/devblog

3. API Analytics Dashboard - Monitor API performance
   Tech: React, D3.js, Express
   Link: github.com/alex/api-dash
```

**Source 3 - Contact:**
```
Email: alex@example.com
GitHub: github.com/alexchen
LinkedIn: linkedin.com/in/alexchen
Twitter: @alexcodes
```

### NotebookLM Brief Prompt:

```
Create a website brief for my portfolio based on my sources.
Include all project details, skills, and contact info.
Style should be modern and developer-focused with a dark theme option.
```

### Gemini Prompt:

```
Create a single-page portfolio website for a developer with these details:

[Paste NotebookLM's generated brief]

Include:
- Hero section with name and tagline
- Skills section with tech badges
- Project showcase with cards
- Contact section with social links
- Dark color scheme with blue accents
- Smooth animations on scroll
- Mobile responsive
```

### Result:

Gemini generates a complete portfolio website in ~30 seconds.

### Iterations:

```
Prompt: "Add a light/dark mode toggle in the header"
Result: Toggle button added with theme switching

Prompt: "Make project cards larger with more prominent images"
Result: Cards redesigned with featured images

Prompt: "Add a skills filter to show only frontend or backend skills"
Result: Filter buttons added above skills section
```

### Deploy:

Upload to GitHub Pages → Live at `alexchen.github.io`

**Total time:** 45 minutes from start to deployed website

---

## What Website Types Work Best

### ✅ Perfect For:

- **Portfolio websites** - Showcase your work
- **Landing pages** - Single-purpose marketing sites
- **Documentation sites** - Product docs, guides
- **Personal websites** - About me, resume sites
- **Small business sites** - Local business presence
- **Event pages** - Conference, wedding, meetup sites
- **Product showcases** - App or product marketing

### ⚠️ Limitations:

- **Complex web apps** - Use proper frameworks for dynamic apps
- **E-commerce** - Use Shopify, WooCommerce for stores
- **Multi-page sites** - Gemini works best with single-page sites
- **Backend functionality** - No server-side code (use APIs separately)

---

## Common Pitfalls & Solutions

### Pitfall 1: Content Too Scattered

**Problem:** NotebookLM brief is disorganized
**Solution:** Manually structure your sources into clear sections before asking for a brief

### Pitfall 2: Gemini Code Is Too Long

**Problem:** Response cuts off mid-code
**Solution:** Say "Continue generating the code from where you stopped"

### Pitfall 3: Website Doesn't Look Right on Mobile

**Problem:** Layout breaks on small screens
**Solution:** Tell Gemini specifically: "The [element] doesn't work on mobile. Make it responsive with a vertical layout below 768px"

### Pitfall 4: Colors Don't Match Brand

**Problem:** Gemini chose random colors
**Solution:** Always specify exact hex codes in your initial prompt: "Use #764ba2 as primary color"

### Pitfall 5: Images Don't Show

**Problem:** Placeholder image URLs don't work
**Solution:** Replace with actual URLs from Imgur, Unsplash, or your own hosting

### Pitfall 6: Too Much Back-and-Forth

**Problem:** Making 20+ small changes individually
**Solution:** List all changes in one prompt: "Make these 5 changes: 1) ..., 2) ..., 3) ..."

---

## Next Steps

### Enhance Your Site:

- Add contact forms using Formspree or Google Forms
- Integrate analytics with Google Analytics or Plausible
- Add animations with libraries like AOS (Animate On Scroll)
- Connect to a CMS like Airtable for dynamic content

### Learn More:

- See `gemini-prompts.md` for a library of effective prompts
- Check `examples/` folder for complete template files
- Read `troubleshooting.md` if you encounter issues

### Share Your Creation:

Built something cool? The community would love to see it!

---

## Quick Reference

### NotebookLM → Brief

```
"Create a website brief from my sources including sections, content, design preferences, and technical requirements"
```

### Gemini → Generate

```
"Create a single-page HTML website with inline CSS based on this brief: [brief]. Make it responsive and production-ready."
```

### Gemini → Iterate

```
"Change [specific element] to [desired outcome]"
"Add [feature] with [specific behavior]"
"Fix [issue] on mobile devices"
```

### Deploy

- Drag & drop: drop.netlify.com
- GitHub Pages: Upload to `username.github.io` repo
- Vercel: Import project from GitHub

---

**Time saved:** What used to take days of coding now takes under an hour.
**Cost:** $0 (all tools are free)
**Results:** Professional websites ready to impress

Ready to build? Start with NotebookLM and gather your content!
