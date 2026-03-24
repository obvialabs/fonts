// src/index.ts
import localFont from "next/font/local";
var obviaSans = localFont({
  src: "./fonts/obvia-sans/Obvia-Variable.woff2",
  variable: "--font-obvia-sans",
  weight: "100 900"
});
var obviaMono = localFont({
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
    "monospace"
  ],
  adjustFontFallback: false
});
var obviaPixelSquare = localFont({
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
    "monospace"
  ],
  adjustFontFallback: false
});
var obviaPixelGrid = localFont({
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
    "monospace"
  ],
  adjustFontFallback: false
});
var obviaPixelCircle = localFont({
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
    "monospace"
  ],
  adjustFontFallback: false
});
var obviaPixelTriangle = localFont({
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
    "monospace"
  ],
  adjustFontFallback: false
});
var obviaPixelLine = localFont({
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
    "monospace"
  ],
  adjustFontFallback: false
});
export {
  obviaMono,
  obviaPixelCircle,
  obviaPixelGrid,
  obviaPixelLine,
  obviaPixelSquare,
  obviaPixelTriangle,
  obviaSans
};
//# sourceMappingURL=index.mjs.map