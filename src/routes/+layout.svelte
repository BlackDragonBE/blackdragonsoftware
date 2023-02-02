<script>
	import NavBar from "$lib/NavBar.svelte";
	import Copyright from 'svelte-copyright';
	import "../../node_modules/bulma/css/bulma.css"
	import "../bulmatheme.css"
	import "../global.css"
</script>

<NavBar />

<slot />

<footer class="footer">
	<div class="content has-text-centered">
	  <p>
		© 2023 - <script>document.write(new Date().getFullYear())</script> Eric Van de Kerckhove - All Rights Reserved.
	  </p>
	</div>
  </footer>

<style>
	@import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css';
</style>
