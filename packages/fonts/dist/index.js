import localFont from "next/font/local";
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
 */
export const obviaSans = localFont({
    src: "./fonts/obvia-sans/Obvia-Variable.woff2",
    variable: "--font-obvia-sans",
    weight: "100 900"
});
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
 */
export const obviaMono = localFont({
    src: "./fonts/obvia-mono/ObviaMono-Variable.woff2",
    variable: "--font-obvia-mono",
    weight: "100 900",
    fallback: [
        "ui-monospace",
        "SFMono-Regular",
        "Roboto Mono",
        "Menlo",
        "Monaco",
        "Liberation Mono",
        "DejaVu Sans Mono",
        "Courier New",
        "monospace",
    ],
    adjustFontFallback: false
});
/**
 * **Obvia Pixel Square** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
 *
 * **Weights**
 * - `500` - Medium
 */
export const obviaPixelSquare = localFont({
    src: "./fonts/obvia-pixel/ObviaPixel-Square.woff2",
    variable: "--font-obvia-pixel-square",
    weight: "500",
    fallback: [
        "Obvia Mono",
        "ui-monospace",
        "SFMono-Regular",
        "Roboto Mono",
        "Menlo",
        "Monaco",
        "Liberation Mono",
        "DejaVu Sans Mono",
        "Courier New",
        "monospace",
    ],
    adjustFontFallback: false
});
/**
 * **Obvia Pixel Grid** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
 *
 * **Weights**
 * - `500` - Medium
 */
export const obviaPixelGrid = localFont({
    src: "./fonts/obvia-pixel/ObviaPixel-Grid.woff2",
    variable: "--font-obvia-pixel-grid",
    weight: "500",
    fallback: [
        "Obvia Mono",
        "ui-monospace",
        "SFMono-Regular",
        "Roboto Mono",
        "Menlo",
        "Monaco",
        "Liberation Mono",
        "DejaVu Sans Mono",
        "Courier New",
        "monospace",
    ],
    adjustFontFallback: false
});
/**
 * **Obvia Pixel Circle** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
 *
 * **Weights**
 * - `500` - Medium
 */
export const obviaPixelCircle = localFont({
    src: "./fonts/obvia-pixel/ObviaPixel-Circle.woff2",
    variable: "--font-obvia-pixel-circle",
    weight: "500",
    fallback: [
        "Obvia Mono",
        "ui-monospace",
        "SFMono-Regular",
        "Roboto Mono",
        "Menlo",
        "Monaco",
        "Liberation Mono",
        "DejaVu Sans Mono",
        "Courier New",
        "monospace",
    ],
    adjustFontFallback: false
});
/**
 * **Obvia Pixel Triangle** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
 *
 * **Weights**
 * - `500` - Medium
 */
export const obviaPixelTriangle = localFont({
    src: "./fonts/obvia-pixel/ObviaPixel-Triangle.woff2",
    variable: "--font-obvia-pixel-triangle",
    weight: "500",
    fallback: [
        "Obvia Mono",
        "ui-monospace",
        "SFMono-Regular",
        "Roboto Mono",
        "Menlo",
        "Monaco",
        "Liberation Mono",
        "DejaVu Sans Mono",
        "Courier New",
        "monospace",
    ],
    adjustFontFallback: false
});
/**
 * **Obvia Pixel Line** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
 *
 * **Weights**
 * - `500` - Medium
 */
export const obviaPixelLine = localFont({
    src: "./fonts/obvia-pixel/ObviaPixel-Line.woff2",
    variable: "--font-obvia-pixel-line",
    weight: "500",
    fallback: [
        "Obvia Mono",
        "ui-monospace",
        "SFMono-Regular",
        "Roboto Mono",
        "Menlo",
        "Monaco",
        "Liberation Mono",
        "DejaVu Sans Mono",
        "Courier New",
        "monospace",
    ],
    adjustFontFallback: false
});
