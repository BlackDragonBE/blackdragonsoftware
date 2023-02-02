<script>
	import NavBar from "$lib/NavBar.svelte";
	import "../../node_modules/bulma/css/bulma.css"
	import "../bulmatheme.css"
	import "../global.css"
</script>

<NavBar />

<slot />

<style>
	@import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css';
</style>
