import { App } from "vue"
import "./fonts/fonts.css"

export type ObviaFonts = {
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
     * ```vue
     * <template>
     *   <div :class="$fonts.obviaSans">Hello Obvia Sans</div>
     * </template>
     * ```
     */
    obviaSans: string

    /**
     * **Obvia Mono** font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
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
     * ```vue
     * <template>
     *   <div :class="$fonts.obviaMono">Hello Obvia Mono</div>
     * </template>
     * ```
     */
    obviaMono: string

    /**
     * **Obvia Pixel Square** variable font, with `className` and `variable` properties,
     * meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```vue
     * <template>
     *   <div :class="$fonts.obviaPixelSquare">Hello Obvia Pixel Grid</div>
     * </template>
     * ```
     */
    obviaPixelSquare: string

    /**
     * **Obvia Pixel Grid** variable font, with `className` and `variable` properties,
     * meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```vue
     * <template>
     *   <div :class="$fonts.obviaPixelGrid">Hello Obvia Pixel Grid</div>
     * </template>
     * ```
     */
    obviaPixelGrid: string

    /**
     * **Obvia Pixel Circle** variable font, with `className` and `variable` properties,
     * meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```vue
     * <template>
     *   <div :class="$fonts.obviaPixelCircle">Hello Obvia Pixel Circle</div>
     * </template>
     * ```
     */
    obviaPixelCircle: string

    /**
     * **Obvia Pixel Triangle** variable font, with `className` and `variable` properties,
     * meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```vue
     * <template>
     *   <div :class="$fonts.obviaPixelTriangle">Hello Obvia Pixel Triangle</div>
     * </template>
     * ```
     */
    obviaPixelTriangle: string

    /**
     * **Obvia Pixel Line** variable font, with `className` and `variable` properties,
     * meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     *
     * **Usage**
     * ```vue
     * <template>
     *   <div :class="$fonts.obviaPixelLine">Hello Obvia Pixel Line</div>
     * </template>
     * ```
     */
    obviaPixelLine: string
}

export const fonts: ObviaFonts = {
    obviaSans: "font-obvia-sans",
    obviaMono: "font-obvia-mono",
    obviaPixelSquare: "font-obvia-pixel-square",
    obviaPixelGrid: "font-obvia-pixel-grid",
    obviaPixelCircle: "font-obvia-pixel-circle",
    obviaPixelTriangle: "font-obvia-pixel-triangle",
    obviaPixelLine: "font-obvia-pixel-line"
}

export default {
    install(app: App) {
        app.config.globalProperties.$fonts = fonts
    }
}