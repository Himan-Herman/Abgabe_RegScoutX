/// <reference types="vitest/config" />
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Entwicklungsserver leitet /api an die lokale Anwendungs-API weiter (regscoutx.web_server).
export default defineConfig({
  plugins: [react()],
  base: "./",
  server: {
    host: "127.0.0.1",
    port: 5173,
    proxy: { "/api": { target: "http://127.0.0.1:8787", changeOrigin: true } },
  },
  build: {
    outDir: "dist",
    emptyOutDir: true,
    license: true,
    sourcemap: false,
    target: "es2022",
    // Bibliotheken getrennt vom Anwendungscode ausliefern (stabile Caches, keine Übergröße je Datei).
    rolldownOptions: {
      output: {
        codeSplitting: {
          groups: [
            { name: "react", test: /node_modules[\\/](react|react-dom|scheduler)[\\/]/ },
            { name: "react-aria", test: /node_modules[\\/](@react-aria|@react-stately|@react-types|react-aria|react-aria-components|react-stately|@internationalized|@swc|client-only|clsx)[\\/]?/ },
          ],
        },
      },
    },
  },
  test: {
    environment: "jsdom",
    include: ["src/**/*.test.{ts,tsx}"],
    setupFiles: ["src/test/setup.ts"],
  },
});
