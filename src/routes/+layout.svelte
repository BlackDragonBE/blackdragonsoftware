<script>
	import NavBar from "$lib/NavBar.svelte";
</script>

<NavBar />

<slot />

<style>
	@import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css';
	@import 'bulma/css/bulma.css';
	@import '../bulmatheme.css';
	@import '../global.css';
	/* @import 'https://unpkg.com/bulmaswatch/darkly/bulmaswatch.min.css'; */
</style>
