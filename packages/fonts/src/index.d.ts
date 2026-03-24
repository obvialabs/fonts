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
     */
    export const obviaMono: NextFontWithVariable

    /**
     * **Obvia Pixel Square** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     */
    export const obviaPixelSquare: NextFontWithVariable

    /**
     * **Obvia Pixel Grid** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     */
    export const obviaPixelGrid: NextFontWithVariable

    /**
     * **Obvia Pixel Circle** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     */
    export const obviaPixelCircle: NextFontWithVariable

    /**
     * **Obvia Pixel Triangle** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     */
    export const obviaPixelTriangle: NextFontWithVariable

    /**
     * **Obvia Pixel Line** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
     *
     * **Weights**
     * - `500` - Medium
     */
    export const obviaPixelLine: NextFontWithVariable
}