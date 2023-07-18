Powered by [`create-svelte`](https://github.com/sveltejs/kit/tree/master/packages/create-svelte).

## Using the project

Install Node.js using chocolatey:

```bash
choco install nodejs -y
```

Install the project dependencies:

```bash
npm install
```

Run the project locally with live edit enabled:

```bash
npm run dev -- --open
```

Build:

```bash
npm run build
```

Preview the build:

```bash
npm run preview
```

Now copy the contents of the `build` directory to the to the website via FTP.


## Updating the games page

To automatically add games from itch.io to the games page, run the following:

```bash
python scripts\itch_games_to_html.py
```

That will replace the GameEntry html in the `src/routes/Games/+page.svelte` file.