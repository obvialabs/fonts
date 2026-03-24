import type { ObviaFonts } from "./vue"

declare module "nuxt/app" {
    interface NuxtApp {
        $fonts: ObviaFonts
    }
}

declare module "vue" {
    interface ComponentCustomProperties {
        $fonts: ObviaFonts
    }
}
