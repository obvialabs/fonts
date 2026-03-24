import { fonts } from "./vue"

declare module "@vue/runtime-core" {
    interface ComponentCustomProperties {
        /**
         * **Obvia Font Family** variable font, with `className` and `variable` properties, meant to be attached to DOM elements via `className`
         *
         * **Family**
         * - `Obvia Sans` - A geometric sans-serif crafted for precision and readability. Rooted in Swiss modernist principles,
         * it balances simplicity with strength, making it suitable for body text, headlines, branding, and
         * large-scale display use
         * - `Obvia Mono` - A monospaced companion to Obvia Sans. Designed for technical contexts — code editors, diagrams,
         * and terminal interfaces — it brings consistency and clarity to environments where structure matters
         * most
         * - `Obvia Pixel` - A playful display family of five pixel-inspired styles. Each variant explores a different facet of
         * digital aesthetics, offering bold, decorative forms for logos, posters, and expressive headlines
         *
         * **Usage**
         * ```vue
         * <template>
         *   <div :class="$fonts.obviaSans">Obvia Sans Style</div>
         *   <div :class="$fonts.obviaMono">Pixel Mono Style</div>
         *   <div :class="$fonts.obviaPixelSquare">Pixel Square Style</div>
         *   <div :class="$fonts.obviaPixelGrid">Pixel Grid Style</div>
         *   <div :class="$fonts.obviaPixelCircle">Pixel Circle Style</div>
         *   <div :class="$fonts.obviaPixelTriangle">Pixel Triangle Style</div>
         *   <div :class="$fonts.obviaPixelLine">Pixel Line Style</div>
         * </template>
         * ```
         */
        $fonts: typeof fonts
    }
}
