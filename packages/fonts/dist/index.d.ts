import { NextFontWithVariable } from "next/dist/compiled/@next/font"

declare module "@obvia/fonts" {
    /**
     * **Obvia Sans** font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `100` - Thin
     * - `200` - Ultra Light
     * - `300` - Light
     * - `400` - Regular
     * - `500` - Medium
     * - `600` - Semibold
     * - `700` - Bold
     * - `800` - Black
     * - `900` - Ultra Black
     *
     * **Usage**
     * ```tsx
     * import { obviaSans } from "@obvia/fonts"
     *
     * export default function RootLayout({ children }: { children: React.ReactNode }) {
     *   return (
     *     <html lang="en">
     *     <body className={`${obviaSans.variable}`}>
     *     {children}
     *     </body>
     *     </html>
     *   );
     * }
     * ```
     */
    export const obviaSans: NextFontWithVariable

    /**
     * **Obvia Mono** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `100` - Thin
     * - `200` - Ultra Light
     * - `300` - Light
     * - `400` - Regular
     * - `500` - Medium
     * - `600` - Semibold
     * - `700` - Bold
     * - `800` - Black
     * - `900` - Ultra Black
     *
     * **Usage**
     * ```tsx
     * import { obviaMono } from "@obvia/fonts"
     *
     * export default function RootLayout({ children }: { children: React.ReactNode }) {
     *   return (
     *     <html lang="en">
     *     <body className={`${obviaMono.variable}`}>
     *     {children}
     *     </body>
     *     </html>
     *   );
     * }
     * ```
     */
    export const obviaMono: NextFontWithVariable

    /**
     * **Obvia Pixel Square** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```tsx
     * import { obviaPixelSquare } from "@obvia/fonts"
     *
     * export default function RootLayout({ children }: { children: React.ReactNode }) {
     *   return (
     *     <html lang="en">
     *     <body className={`${obviaPixelSquare.variable}`}>
     *     {children}
     *     </body>
     *     </html>
     *   );
     * }
     * ```
     */
    export const obviaPixelSquare: NextFontWithVariable

    /**
     * **Obvia Pixel Grid** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```tsx
     * import { obviaPixelGrid } from "@obvia/fonts"
     *
     * export default function RootLayout({ children }: { children: React.ReactNode }) {
     *   return (
     *     <html lang="en">
     *     <body className={`${obviaPixelGrid.variable}`}>
     *     {children}
     *     </body>
     *     </html>
     *   );
     * }
     * ```
     */
    export const obviaPixelGrid: NextFontWithVariable

    /**
     * **Obvia Pixel Circle** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```tsx
     * import { obviaPixelCircle } from "@obvia/fonts"
     *
     * export default function RootLayout({ children }: { children: React.ReactNode }) {
     *   return (
     *     <html lang="en">
     *     <body className={`${obviaPixelCircle.variable}`}>
     *     {children}
     *     </body>
     *     </html>
     *   );
     * }
     * ```
     */
    export const obviaPixelCircle: NextFontWithVariable

    /**
     * **Obvia Pixel Triangle** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```tsx
     * import { obviaPixelTriangle } from "@obvia/fonts"
     *
     * export default function RootLayout({ children }: { children: React.ReactNode }) {
     *   return (
     *     <html lang="en">
     *     <body className={`${obviaPixelTriangle.variable}`}>
     *     {children}
     *     </body>
     *     </html>
     *   );
     * }
     * ```
     */
    export const obviaPixelTriangle: NextFontWithVariable

    /**
     * **Obvia Pixel Line** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```tsx
     * import { obviaPixelLine } from "@obvia/fonts"
     *
     * export default function RootLayout({ children }: { children: React.ReactNode }) {
     *   return (
     *     <html lang="en">
     *     <body className={`${obviaPixelLine.variable}`}>
     *     {children}
     *     </body>
     *     </html>
     *   )
     * }
     * ```
     */
    export const obviaPixelLine: NextFontWithVariable
}