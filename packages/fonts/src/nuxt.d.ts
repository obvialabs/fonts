import type { ObviaFonts } from "./vue"

declare module "#app" {
    interface NuxtApp {
        $fonts: ObviaFonts
    }
}

declare module "vue" {
    interface ComponentCustomProperties {
        $fonts: ObviaFonts
    }
}
