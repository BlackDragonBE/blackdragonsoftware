<script>
	import NavBar from "$lib/NavBar.svelte";
	import "../../node_modules/bulma/css/bulma.css"
	import "../bulmatheme.css"
	import "../global.css"
</script>

<NavBar />

<slot />

<footer class="footer mt-auto">
	<div class="content has-text-centered">
	  <p>
		© 2023 Black Dragon Software - All Rights Reserved.
	  </p>
	  <a href="/privacypolicy">Privacy policy</a> 
	</div>
  </footer>

<style>
	@import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css';
</style>
