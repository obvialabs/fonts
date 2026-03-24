import { fonts } from "./vue"

declare module "#app" {
    interface NuxtApp {
        $fonts: typeof fonts
    }
}

declare module "vue" {
    interface ComponentCustomProperties {
        $fonts: typeof fonts
    }
}
