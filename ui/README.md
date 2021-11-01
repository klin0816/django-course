# Svelte + Vite + Pug + Sass

## Getting Start

use yarn to create a Vite project.

```bash
$ yarn create vite
yarn create v1.22.5
[1/4] 🔍  Resolving packages...
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
[4/4] 🔨  Building fresh packages...
success Installed "create-vite@2.6.6" with binaries:
      - create-vite
      - cva
✔ Project name: [project_name]
✔ Select a framework: › svelte
✔ Select a variant: › svelte
```

Your Svelte project is ready!

## Svelte-preprocess

Svelte use HTML and CSS as default. If we want to change to Pug + Sass we need to add preprocessor into project

```bash
$ yarn add -D svelte-preprocess

# svelte-preprocess not include pug and sass, so need to install manually
$ yarn add -D pug sass
```

Then add preprocess into `vite.config.js`
```javascript
# vite.congfig.js
...
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import sveltePreprocess from 'svelte-preprocess'

export default defineConfig({
plugins: [
  svelte({
    preprocess: sveltePreprocess()
  })]
})
```

Feel free to use pug and sass in `*.svelte`!
