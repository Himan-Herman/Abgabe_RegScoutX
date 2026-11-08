import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./experience/regscoutx/tokens.css";
import "./core/styles/base.css";
import "./core/primitives/primitives.css";
import "./domain/shell/shell.css";
import "./domain/views.css";
import { App } from "./App";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
