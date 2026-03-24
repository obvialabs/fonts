import { defineConfig } from "tsup"

export default defineConfig({
    // Entry point(s) for the build
    entry: ["src/index.ts"],

    // Output directory for compiled files
    outDir: "dist",

    // Build formats: ESM (.mjs) and CommonJS (.js)
    format: ["esm", "cjs"],

    // Generate TypeScript declaration files (.d.ts / .mts)
    dts: {
        entry: "src/index.ts",
    },

    // Generate source maps for debugging
    sourcemap: true,

    // Clean the output directory before each build
    clean: true,

    // Minify the output for production
    minify: false,

    // Target modern JavaScript (ESNext)
    target: "esnext",

    // Enable code splitting (useful for multiple entry points)
    splitting: true,

    // Bundle everything into distributable files
    bundle: true,

    // Do not bundle node_modules dependencies
    skipNodeModulesBundle: true
})
