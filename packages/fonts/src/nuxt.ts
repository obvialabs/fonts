import { defineNuxtPlugin } from "nuxt/app"
import { fonts } from "./vue"
import "./fonts.css"

export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.provide("fonts", fonts)
})