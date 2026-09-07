# Modern Web Guidance Activated

[Read URL](https://raw.githubusercontent.com/GoogleChrome/modern-web-guidance/main/skills/modern-web-guidance/guides/performance/optimize-image-priority.md)

The **Modern Web Guidance** skill is loaded and ready. This skill injects modern, high-performance, accessible, and standards-compliant web platform APIs (supported by Google Chrome and Microsoft Edge) to avoid legacy JavaScript polyfills and outdated patterns.

---

### Available Core Domains & Guides (124+ Use Cases)

| Category                                | Key Modern Capabilities & Patterns                                                                                                                                                                                     |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Native UI & Overlays**          | Native`<dialog>` (modal & light dismiss), CSS Anchor Positioning (`anchor-name`, `position-anchor`), Popover API, Invoker commands (`commandfor`, `interestfor`), `@starting-style` entry/exit transitions |
| **Motion & Scroll**               | View Transitions API (same-document SPA & cross-document), Scroll-Driven Animations (`animation-timeline: scroll() / view()`), scroll-snap synchronization, parallax effects                                         |
| **Modern Layout & CSS**           | Container queries (size & style queries), subgrid, modern color spaces (`oklch()`, `color-mix()`, `light-dark()`), text wrapping (`text-wrap: balance / pretty`), `text-box` trim                            |
| **Forms & Validation**            | `:user-valid` / `:user-invalid` pseudo-classes (interaction-aware feedback), `field-sizing: content` (auto-expanding inputs/textareas), brand-consistent controls (`accent-color`)                             |
| **Performance & Core Web Vitals** | Speculation Rules API (prerendering/prefetching), Fetch Priority (`fetchpriority="high"` for LCP), `content-visibility: auto`, `scheduler.yield()` (breaking up long tasks for INP)                              |
| **Built-in On-Device AI**         | Chrome Prompt API (`LanguageModel`), Summarizer API, Translator API, Language Detection API                                                                                                                          |
| **Identity & Passkeys**           | WebAuthn passkey authentication, conditional UI (autofill passkeys), seamless registration                                                                                                                             |
| **WebMCP**                        | Declarative HTML form tools & imperative JavaScript tools for AI agents                                                                                                                                                |

---


# Optimize image priority

Browsers use heuristics to assign loading priorities to images, but these defaults may not always align with your page's Largest Contentful Paint (LCP).

Using `fetchpriority` on an `<img>` element allows you to explicitly signal an image's importance to the browser, ensuring critical images load faster while non-essential ones don't compete for bandwidth.

The `loading=lazy` attribute prevents images from being downloaded at all when sufficiently off-screen which can further help prioritize images.

## How to implement

1. **Identify the LCP image**: Determine which image is the most likely candidate for the Largest Contentful Paint (usually the hero image at the top of the page).
2. **Elevate LCP priority**: Add `fetchpriority="high"` to the `<img>` element for the LCP candidate.
3. **Deprioritize non-critical images**: For images that are part of a secondary UI or are only revealed after user interaction (like mega menus, modals, or off-screen carousel slides), add `fetchpriority="low"`.
4. **Optimize lazy loading**: Never use `loading="lazy"` on the LCP image. For standard below-the-fold images, `loading="lazy"` is sufficient to defer the request until the user scrolls near them. Avoid adding `fetchpriority="low"` to these images, as you want them to load at normal priority once the user scrolls to them. Reserve `fetchpriority="low"` for images that are technically "above the fold" but not initially visible (e.g., hidden carousel slides or mega menus). For these hidden images, it is acceptable to use `loading="lazy"` as well; the browser will handle the request timing while respecting the low priority.
5. **Prefer default priorities**: If an image should have normal loading priority, omit the `fetchpriority` attribute ent
