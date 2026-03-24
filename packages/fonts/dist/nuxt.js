import { defineNuxtPlugin } from "nuxt/app";
import { fonts } from "./vue";
import "../fonts/fonts.css";
export default defineNuxtPlugin((nuxtApp) => {
    // Provide fonts via Nuxt injection system
    // Accessible with: const nuxtApp = useNuxtApp(); nuxtApp.$fonts
    nuxtApp.provide("fonts", fonts);
    // Add fonts to Vue global properties
    // Accessible directly in templates with: $fonts
    nuxtApp.vueApp.config.globalProperties.$fonts = fonts;
});
