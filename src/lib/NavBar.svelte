<script lang="ts">
	import { page } from '$app/stores';
	import logo from '$lib/images/logo.svg';
	import NavBarItem from './NavBarItem.svelte';

	let navbarActive: boolean = false;
	let navbarClass: string;
	let path: string;

	$: navbarClass = navbarActive ? 'is-active' : '';
	$: path = $page.url.pathname;

</script>

<nav class="navbar" aria-label="main navigation">
	<div class="navbar-brand">
		<a class="navbar-item" href="/">
			<img src={logo} width="40" height="28" />
			Black Dragon Software
		</a>

		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<!-- svelte-ignore a11y-missing-attribute -->
		<a
			role="button"
			class="navbar-burger {navbarClass}"
			aria-label="menu"
			aria-expanded="false"
			data-target="navbarBasicExample"
			on:click={() => (navbarActive = !navbarActive)}
		>
			<span aria-hidden="true" />
			<span aria-hidden="true" />
			<span aria-hidden="true" />
		</a>
	</div>

	<div id="navbarBasicExample" class="navbar-menu {navbarClass}">
		<div class="navbar-start">
			<NavBarItem path={path} link='/' linkName='Home' faIcon='fas fa-home'/>
			<NavBarItem path={path} link='/Games' linkName='Games' faIcon='fas fa-gamepad'/>
			<NavBarItem path={path} link='/3D' linkName='3D' faIcon='fas fa-cube'/>
			<!-- <NavBarItem path={path} link='/unity' linkName='Unity' faIcon='fab fa-unity'/>
			<NavBarItem path={path} link='/godot' linkName='Godot' faIcon='fas fa-home'/> -->
			<!-- <a class="navbar-item"> Documentation </a>
			<div class="navbar-item has-dropdown is-hoverable">
				<a class="navbar-link"> More </a>

				<div class="navbar-dropdown">
					<a class="navbar-item"> About </a>
					<a class="navbar-item"> Jobs </a>
					<a class="navbar-item"> Contact </a>
					<hr class="navbar-divider" />
					<a class="navbar-item"> Report an issue </a>
				</div>
			</div> -->
		</div>
	</div>
</nav>
