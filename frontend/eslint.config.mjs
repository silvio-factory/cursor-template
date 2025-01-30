// Location: frontend/eslint.config.mjs
// Purpose: ESLint configuration file that defines code style and quality rules
// This file sets up linting rules and plugins for maintaining consistent code quality

import { FlatCompat, FlatCompat } from "@eslint/eslintrc";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [
  ...compat.extends("next/core-web-vitals", "next/typescript"),
];

export default eslintConfig;
