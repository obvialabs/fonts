"use strict";Object.defineProperty(exports, "__esModule", {value: true}); function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }// src/index.ts
var _local = require('next/font/local'); var _local2 = _interopRequireDefault(_local);
var obviaSans = _local2.default.call(void 0, {
  src: "./fonts/obvia-sans/Obvia-Variable.woff2",
  variable: "--font-obvia-sans",
  weight: "100 900"
});
var obviaMono = _local2.default.call(void 0, {
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
var obviaPixelSquare = _local2.default.call(void 0, {
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
var obviaPixelGrid = _local2.default.call(void 0, {
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
var obviaPixelCircle = _local2.default.call(void 0, {
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
var obviaPixelTriangle = _local2.default.call(void 0, {
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
var obviaPixelLine = _local2.default.call(void 0, {
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








exports.obviaMono = obviaMono; exports.obviaPixelCircle = obviaPixelCircle; exports.obviaPixelGrid = obviaPixelGrid; exports.obviaPixelLine = obviaPixelLine; exports.obviaPixelSquare = obviaPixelSquare; exports.obviaPixelTriangle = obviaPixelTriangle; exports.obviaSans = obviaSans;
//# sourceMappingURL=index.js.map