import "./fonts.css";
export const fonts = {
    obviaSans: "font-obvia-sans",
    obviaMono: "font-obvia-mono",
    obviaPixelSquare: "font-obvia-pixel-square",
    obviaPixelGrid: "font-obvia-pixel-grid",
    obviaPixelCircle: "font-obvia-pixel-circle",
    obviaPixelTriangle: "font-obvia-pixel-triangle",
    obviaPixelLine: "font-obvia-pixel-line"
};
export default {
    install(app) {
        app.config.globalProperties.$fonts = fonts;
    }
};
