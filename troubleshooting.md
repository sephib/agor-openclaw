# Troubleshooting Guide: NotebookLM + Gemini Websites

Quick solutions to common issues when building websites with NotebookLM and Gemini Canvas.

---

## Table of Contents

- [NotebookLM Issues](#notebooklm-issues)
- [Gemini Generation Issues](#gemini-generation-issues)
- [Code Display & Rendering Issues](#code-display--rendering-issues)
- [Responsive Design Problems](#responsive-design-problems)
- [Browser Compatibility Issues](#browser-compatibility-issues)
- [Deployment Problems](#deployment-problems)
- [Content & Styling Issues](#content--styling-issues)

---

## NotebookLM Issues

### Issue: NotebookLM brief is incomplete or missing content

**Symptoms:**
- Generated brief doesn't include all your sources
- Missing important details
- Sections are too vague

**Solution:**
```
Prompt: "Review all sources again and create a comprehensive brief that includes:
1. Every project/item I mentioned
2. All contact information from my sources
3. Complete skill lists
4. Specific design preferences I noted

Don't summarize - include the actual content."
```

**Prevention:**
- Structure sources clearly with headings
- Use bullet points for lists
- Review the brief before sending to Gemini

---

### Issue: NotebookLM brief is too long for Gemini

**Symptoms:**
- Brief exceeds Gemini's input limits
- Can't paste the entire thing

**Solution:**
1. Ask NotebookLM to create a condensed version:
   ```
   "Create a shorter version of this brief (under 2000 words) that includes only the essential information needed to generate the website code."
   ```

2. Or split into multiple prompts:
   - First: Structure and design
   - Second: Content details
   - Third: Special features

**Prevention:**
- Keep sources focused and organized
- Don't include unnecessary background information

---

### Issue: Can't upload sources to NotebookLM

**Symptoms:**
- File upload fails
- URL sources won't load

**Quick Fixes:**
- **PDFs:** Ensure file size is under 50MB
- **URLs:** Check if the website allows scraping
- **Google Docs:** Make sure sharing is set to "Anyone with the link"

**Workaround:**
- Copy and paste content directly as a note instead of uploading
- Convert PDFs to text files
- Screenshot and describe inaccessible content

---

## Gemini Generation Issues

### Issue: Gemini's response cuts off mid-code

**Symptoms:**
- HTML file is incomplete
- Missing closing tags
- Code stops abruptly

**Solution:**
```
Simply say: "Continue from where you left off"
```

Gemini will resume and complete the code.

**Alternative:**
```
"Finish generating the complete HTML file, starting from the [last section visible]"
```

**Prevention:**
- Request code in sections if it's complex
- Ask for "complete but minimal" initial version
- Add complexity in iterations

---

### Issue: Gemini generates separate CSS file instead of inline

**Symptoms:**
- Receives CSS code separately
- HTML has `<link>` to external stylesheet

**Solution:**
```
"Please regenerate this with all CSS inline in a <style> tag within the HTML file. I need a single HTML file with no external dependencies."
```

**Prevention:**
- Always specify "single HTML file with inline CSS" in initial prompt
- Mention "no external dependencies"

---

### Issue: Gemini refuses to generate code or gives generic advice

**Symptoms:**
- Provides tips instead of code
- Says "you should" instead of showing code

**Solution:**
```
"I need you to generate the actual HTML code, not instructions. Please create a complete, working HTML file based on my requirements."
```

Or switch to Canvas mode:
```
"Switch to Canvas mode and generate the HTML code"
```

**Prevention:**
- Be very explicit: "Generate the code now"
- Use phrases like "create the complete HTML file"

---

### Issue: Generated code doesn't match the brief

**Symptoms:**
- Missing sections
- Wrong colors
- Different layout than requested

**Solution:**
```
"The generated code is missing [specific elements]. Please regenerate including:
1. [Missing element 1]
2. [Missing element 2]
...

Also ensure:
- Colors match [specific colors]
- Layout is [specific layout]"
```

**Prevention:**
- Be extremely specific in the initial prompt
- Use bullet points for requirements
- Include examples or references

---

## Code Display & Rendering Issues

### Issue: HTML file shows code instead of rendering

**Symptoms:**
- Browser displays HTML code as text
- Tags are visible on the page

**Cause:** File wasn't saved with `.html` extension

**Solution:**
1. Rename file to ensure it ends in `.html`
   - Right-click file → Rename
   - Change `website.txt` to `website.html`

2. If on Windows, enable file extensions:
   - File Explorer → View → Show file extensions

3. Re-open in browser

**Quick Test:**
- File should have a browser icon
- Double-clicking should open in browser, not text editor

---

### Issue: Blank page when opening HTML

**Symptoms:**
- Page loads but shows nothing
- Completely white screen

**Debugging Steps:**

1. **Check browser console:**
   - Right-click → Inspect → Console tab
   - Look for red error messages

2. **Common causes:**
   - Missing opening `<html>` tag
   - Broken CSS syntax
   - Missing closing tags

3. **Quick fix:**
   ```
   Tell Gemini: "The HTML file shows a blank page. Please check for syntax errors and regenerate valid HTML."
   ```

---

### Issue: Images don't show

**Symptoms:**
- Broken image icons
- Alt text displays instead of images

**Cause:** Using placeholder URLs that don't exist

**Solutions:**

1. **Use free stock images:**
   - Unsplash: `https://source.unsplash.com/800x600/?[keyword]`
   - Picsum: `https://picsum.photos/800/600`

2. **Upload your images:**
   - Use Imgur, Cloudinary, or similar
   - Replace placeholder URLs with actual URLs

3. **Example fix:**
   ```html
   <!-- Before -->
   <img src="placeholder-image.jpg" alt="Project">

   <!-- After -->
   <img src="https://source.unsplash.com/800x600/?portfolio" alt="Project">
   ```

---

### Issue: Styles not applying

**Symptoms:**
- Page has content but no styling
- Everything looks like plain HTML

**Debugging:**

1. **Check if CSS is in the file:**
   - Open file in text editor
   - Look for `<style>` tag in `<head>`

2. **If CSS is missing:**
   ```
   Tell Gemini: "The HTML file has no styling. Add a complete <style> tag with all the CSS inline."
   ```

3. **If CSS exists but doesn't work:**
   - Check browser console for syntax errors
   - Verify closing `</style>` tag exists
   - Look for typos in CSS

---

## Responsive Design Problems

### Issue: Site looks broken on mobile

**Symptoms:**
- Text is tiny
- Elements overflow the screen
- Horizontal scrolling required

**Quick Fix:**
```
Tell Gemini: "The website doesn't work on mobile devices. Add this viewport meta tag and make all sections responsive:

<meta name="viewport" content="width=device-width, initial-scale=1.0">

Then update all fixed widths to be responsive using max-width and percentages. Make multi-column layouts stack vertically below 768px."
```

**Test Mobile:**
1. Desktop browser: Right-click → Inspect → Toggle device toolbar
2. Or resize browser window to phone size
3. Test on actual phone for real results

---

### Issue: Navigation menu breaks on mobile

**Symptoms:**
- Menu items overlap
- Can't tap menu items
- Text too small on phone

**Solution:**
```
Tell Gemini: "Convert the navigation to a mobile-friendly design:
- On screens below 768px, show a hamburger menu icon
- Menu items stack vertically
- Increase touch targets to minimum 44px height
- Add padding for easier tapping"
```

**Quick Alternative:**
```
"Simplify the mobile navigation to just a centered, stacked list of links with large touch targets on screens below 768px"
```

---

### Issue: Images too large on mobile

**Symptoms:**
- Images cause horizontal scroll
- Slow loading on mobile
- Layout breaks with images

**Solution:**
```css
Add this CSS to all img tags:

img {
    max-width: 100%;
    height: auto;
}
```

Or tell Gemini:
```
"Make all images responsive by adding max-width: 100% and height: auto to the img CSS"
```

---

### Issue: Text too small/large on mobile

**Solution:**
```
Tell Gemini: "Adjust typography for mobile devices:
- Base font size: 16px on mobile (currently too small)
- Headings: Reduce by 20% on screens below 768px
- Line height: Increase to 1.6 for readability
- Paragraph width: Maximum 65 characters for easy reading"
```

---

## Browser Compatibility Issues

### Issue: Site looks different in Safari vs Chrome

**Common Problems:**
- Flexbox or Grid layout differences
- Font rendering variations
- Smooth scroll doesn't work in older browsers

**Solution:**
```
Tell Gemini: "Add browser compatibility fixes:
- Include vendor prefixes for flexbox (-webkit-flex)
- Add fallback fonts
- Use widely supported CSS properties
- Avoid experimental features"
```

**Test in Multiple Browsers:**
- Chrome
- Firefox
- Safari (important for iOS users)
- Edge

---

### Issue: Site doesn't work in older browsers

**Symptoms:**
- Works in modern browsers, broken in IE11 or older

**Realistic Solution:**
Most modern sites don't support very old browsers. Include a notice:

```html
<!--[if lt IE 11]>
<p style="text-align: center; padding: 20px; background: #ff0000; color: #fff;">
  Please upgrade to a modern browser for the best experience.
</p>
<![endif]-->
```

Or tell Gemini:
```
"Add a browser upgrade notice for users on Internet Explorer"
```

---

## Deployment Problems

### Issue: Netlify Drop says "Invalid HTML"

**Causes:**
- HTML syntax errors
- Missing required tags
- Broken structure

**Fix:**
1. Validate HTML: https://validator.w3.org/
2. Paste HTML code, check for errors
3. Tell Gemini to fix specific errors found

```
"The HTML validator found these errors: [paste errors]
Please fix them and regenerate valid HTML."
```

---

### Issue: GitHub Pages shows 404

**Common causes:**
- File not named `index.html`
- Pages not enabled in settings
- Wrong branch selected

**Solutions:**

1. **Rename file to `index.html`** (case-sensitive!)

2. **Enable GitHub Pages:**
   - Repository → Settings → Pages
   - Source: Select your branch (usually `main`)
   - Save

3. **Wait 2-3 minutes** for deployment

4. **Check URL format:**
   - Should be: `https://username.github.io/repository-name/`
   - Not: `https://github.com/username/repository-name/`

---

### Issue: Deployed site missing images

**Cause:** Images referenced with relative paths that don't exist

**Solution:**

1. **Use absolute URLs:**
   ```html
   <!-- Wrong -->
   <img src="images/photo.jpg">

   <!-- Right -->
   <img src="https://yourdomain.com/images/photo.jpg">
   ```

2. **Or upload images to the same repository:**
   - Create `images/` folder
   - Upload images
   - Reference as `./images/photo.jpg`

---

### Issue: Custom domain doesn't work

**Symptoms:**
- Domain shows error
- DNS not propagating

**Steps:**

1. **Check DNS settings at domain registrar:**
   ```
   Type: A
   Name: @ (or your domain)
   Value: [Your hosting provider's IP]
   ```

2. **Wait 24-48 hours** for DNS propagation

3. **Verify in hosting platform:**
   - Netlify: Settings → Domain management
   - Vercel: Project → Settings → Domains
   - GitHub Pages: Settings → Pages → Custom domain

4. **Check SSL certificate** is issued (can take 24 hours)

---

## Content & Styling Issues

### Issue: Colors don't match brand

**Solution:**
```
Tell Gemini: "Update all colors to match my brand palette:
- Primary: #[hex]
- Secondary: #[hex]
- Text: #[hex]
- Background: #[hex]
- Accent: #[hex]

Apply consistently throughout the entire website."
```

---

### Issue: Too much/too little spacing

**Solution:**
```
Tell Gemini: "Adjust spacing:
- Increase padding between sections to 5rem
- Reduce margin around headings to 1rem
- Add 2rem gap between cards in grid
- Increase line-height to 1.6 for paragraphs"
```

---

### Issue: Fonts look wrong or don't load

**Cause:** External font links missing or incorrect

**Solution:**

1. **Use system fonts (reliable):**
   ```css
   font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
   ```

2. **Or add Google Fonts:**
   ```html
   <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
   ```

Tell Gemini:
```
"Add Google Fonts for [font name] and update the font-family throughout"
```

---

### Issue: Text content overflows containers

**Symptoms:**
- Text breaks layout
- Horizontal scroll appears
- Text overlaps other elements

**Solution:**
```css
Add to affected elements:

word-wrap: break-word;
overflow-wrap: break-word;
max-width: 100%;
```

Or tell Gemini:
```
"Fix text overflow in [section] by adding word wrapping and ensuring max-width is set"
```

---

### Issue: Buttons/links not working

**Causes:**
- Empty `href="#"`
- JavaScript required but not included
- Overlapping elements blocking clicks

**Debugging:**

1. **Check href values:**
   ```html
   <!-- Doesn't go anywhere -->
   <a href="#">Click me</a>

   <!-- Actually works -->
   <a href="#contact">Click me</a>
   ```

2. **Test click targets:**
   - Right-click → Inspect
   - Check if another element is on top

3. **Fix:**
   ```
   Tell Gemini: "Update all navigation links to point to the correct section IDs"
   ```

---

## Diagnostic Flowchart

### Page doesn't load?
1. ✓ File extension is `.html`?
2. ✓ Opening in web browser (not text editor)?
3. ✓ Check browser console for errors

### Page loads but looks wrong?
1. ✓ Check if CSS is present in `<style>` tag
2. ✓ Verify viewport meta tag exists
3. ✓ Test in different browser
4. ✓ Check browser console

### Works on desktop, broken on mobile?
1. ✓ Viewport meta tag present?
2. ✓ Media queries at 768px breakpoint?
3. ✓ Fixed widths changed to max-width?
4. ✓ Multi-column layouts have mobile stacking?

### Images don't show?
1. ✓ URLs are absolute (https://...)?
2. ✓ URLs actually work (paste in browser)?
3. ✓ img tags have src attribute?
4. ✓ No typos in URLs?

---

## Emergency Reset

If everything is broken and you want to start over:

```
Tell Gemini: "Regenerate the entire website from scratch based on the original brief.
Create a clean, working version with:
- Valid HTML structure
- All CSS inline
- No external dependencies
- Mobile responsive
- Tested basic functionality

Start fresh and keep it simple."
```

---

## Getting Help

### Before Asking for Help:

1. **Check browser console** - Most issues show error messages there
2. **Test in another browser** - Might be browser-specific
3. **Validate HTML** - Use https://validator.w3.org/
4. **Try the emergency reset** - Sometimes easiest to start fresh

### When Asking Gemini for Help:

Be specific:
```
❌ "The website is broken"
✅ "The navigation menu overlaps the hero section on mobile devices (screens below 768px)"

❌ "Fix the colors"
✅ "Change the button color from #ff0000 to #4f46e5 throughout the entire site"

❌ "It doesn't work on my phone"
✅ "On iPhone screens (390px width), the text in the pricing section is too small to read comfortably"
```

### Community Resources:

- **Web.dev** - Learn web development best practices
- **MDN Web Docs** - HTML/CSS reference
- **Can I Use** - Check browser compatibility
- **Stack Overflow** - Specific technical questions

---

## Prevention Checklist

Avoid issues by following these practices:

### Before Generating:
- [ ] NotebookLM brief is complete and accurate
- [ ] Specific colors chosen (hex codes ready)
- [ ] Content is organized by section
- [ ] Design references gathered
- [ ] Viewport/responsive requirements noted

### When Prompting Gemini:
- [ ] Specify "single HTML file with inline CSS"
- [ ] Include "mobile responsive" requirement
- [ ] Mention specific colors with hex codes
- [ ] List all required sections
- [ ] Request "production-ready code"

### After Generating:
- [ ] Save as `.html` file
- [ ] Test in browser immediately
- [ ] Test mobile responsiveness
- [ ] Check all links work
- [ ] Validate HTML if deploying
- [ ] Test in multiple browsers

### Before Deploying:
- [ ] All content is finalized
- [ ] Images use working URLs
- [ ] Links point to correct destinations
- [ ] Contact info is accurate
- [ ] Tested on real mobile device
- [ ] Spell-checked all content

---

## Quick Fixes Reference

| Problem | Quick Solution |
|---------|---------------|
| Code cuts off | "Continue from where you left off" |
| Blank page | Check `<html>`, `<head>`, `<body>` tags exist |
| No styling | Verify `<style>` tag in `<head>` |
| Images missing | Use absolute URLs (https://...) |
| Mobile broken | Add viewport meta tag, responsive CSS |
| Navigation doesn't work | Check href="#section-id" matches IDs |
| Wrong colors | "Change all [color] to [hex code]" |
| Too cramped | "Increase padding/margin to [amount]" |
| Text overflow | Add "word-wrap: break-word" |
| Deploy fails | Validate HTML at validator.w3.org |

---

**Remember:** Most issues have simple solutions. Check the basics first (file extension, browser console, mobile testing) before assuming complex problems.

**When in doubt:** Ask Gemini to regenerate with specific requirements. It's often faster than debugging.
