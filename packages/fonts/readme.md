# Obvia Font Family

Obvia is a contemporary type system envisioned by [Selçuk Çukur](https://selcukcukur.me) in 
collaboration with [Obvia](https://obvia.studio). It is built on clarity, rhythm, and versatility
— designed to serve both functional and expressive needs across digital and print environments.

- **Obvia Sans** - A geometric sans-serif crafted for precision and readability. Rooted in Swiss modernist principles, 
it balances simplicity with strength, making it suitable for body text, headlines, branding, and 
large-scale display use.

- **Obvia Mono** - A monospaced companion to Obvia Sans. Designed for technical contexts — code editors, diagrams, 
and terminal interfaces — it brings consistency and clarity to environments where structure matters 
most.

- **Obvia Pixel** - A playful display family of five pixel-inspired styles. Each variant explores a different facet of 
digital aesthetics, offering bold, decorative forms for logos, posters, and expressive headlines.

## Installation

Obvia ships as a single package — installing @obvia/fonts gives you access to Sans, Mono, and Pixel families all at once.

```sh
npm install @obvia/fonts
```

After installation, you can import any style directly :
```ts
// Sans
import { obviaSans } from "@obvia/fonts"

// Mono
import { obviaMono } from "@obvia/fonts"

// Pixel
import { obviaPixel } from "@obvia/fonts"
```

This unified distribution ensures consistency across projects: one install, three families, infinite possibilities.

## Quickstart

### Using with Next.js

In `next.config.ts` add transpilePackages so that the @obvia/fonts package is properly transpiled by Next.js.

```ts
import type { NextConfig } from "next"

const nextConfig: NextConfig = {
    reactStrictMode: true, 
    transpilePackages: ["@obvia/fonts"]
}

export default nextConfig
```

In `layout.tsx` import the Sans font from @obvia/fonts and apply it to the root layout.

```tsx
// Sans
import { obviaSans } from "@obvia/fonts"

// Define the root layout component for the application
export default function RootLayout({ children }) {
    return (
        <html lang="en" className={obviaSans.variable}>
        <body>{children}</body>
        </html>
    )
}
```

In `layout.tsx` import the Mono font from @obvia/fonts and apply it to the root layout.

```tsx
// Mono
import { obviaMono } from "@obvia/fonts"

// Define the root layout component for the application
export default function RootLayout({ children }) {
    return (
        <html lang="en" className={obviaMono.variable}>
        <body>{children}</body>
        </html>
    )
}
```

In `layout.tsx` import the Pixel font from @obvia/fonts and apply it to the root layout.

```tsx
// Pixel
import {
    obviaPixelSquare,
    obviaPixelGrid,
    obviaPixelCircle,
    obviaPixelTriangle,
    obviaPixelLine
} from "@obvia/fonts"

// Define the root layout component for the application
export default function RootLayout({ children }) {
    return (
        // Set the HTML language attribute and apply the Obvia Pixel Square font as a CSS variable
        <html lang="en" className={`${obviaPixelSquare.variable}`}>
        {/* Render the application content inside the body */}
        <body>{children}</body>
        </html>
    )
}
```

### Using with Tailwind CSS

In `globals.css` (or your global CSS theme file) extend the theme by mapping the Obvia font tokens to Tailwind’s 
font variables. This ensures that the `@obvia/fonts` package integrates properly with Tailwind.

```css
@theme {
    /* Obvia (Sans) */
    --font-sans: var(--font-obvia-sans);
    /* Obvia (Mono) */
    --font-mono: var(--font-obvia-mono);
    /* Obvia (Pixel) */
    --font-pixel-square: var(--font-obvia-pixel-square);
    --font-pixel-grid: var(--font-obvia-pixel-grid);
    --font-pixel-circle: var(--font-obvia-pixel-circle);
    --font-pixel-triangle: var(--font-obvia-pixel-triangle);
    --font-pixel-line: var(--font-obvia-pixel-line);
}
```

## License

The Obvia font family is free and open sourced under the [SIL Open Font License](../../LICENSE.txt).

## Inspiration

Obvia draws its spirit from a lineage of remarkable typefaces. Each of these designs has shaped 
our perspective on clarity, rhythm, and modernity :

- [Geist](https://vercel.com/geist/geist)
- [Inter](https://rsms.me/inter)
- [Univers](https://www.linotype.com/1567/univers-family.html)
- [SF Mono](https://developer.apple.com/fonts/)
- [SF Pro](https://developer.apple.com/fonts/)
- [Suisse International](https://www.swisstypefaces.com/fonts/suisse/)
- [ABC Diatype Mono](https://abcdinamo.com/typefaces/diatype)
- [ABC Diatype](https://abcdinamo.com/typefaces/diatype)

We acknowledge and thank the creators of these typefaces for their craft and vision. Their work 
continues to inspire and guide our own.
