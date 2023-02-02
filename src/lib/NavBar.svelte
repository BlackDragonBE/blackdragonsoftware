<script lang="ts">
	import { page } from '$app/stores';
	import logo from '$lib/images/logo.svg';
	import NavBarItem from './NavBarItem.svelte';
	import logo_full from '$lib/images/logo-full.png';

	let navbarActive: boolean = false;
	let navbarClass: string;
	let path: string;

	$: navbarClass = navbarActive ? 'is-active' : '';
	$: path = $page.url.pathname;
</script>

<nav class="navbar is-primary" aria-label="main navigation">
	<div class="navbar-brand">
		<a class="navbar-item" href="/">
			<img src={logo} width="40" height="28" />
			Black Dragon Software
		</a>

		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<!-- svelte-ignore a11y-missing-attribute -->
		<a role="button" class="navbar-burger {navbarClass}" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" on:click={() => (navbarActive = !navbarActive)}>
			<span aria-hidden="true" />
			<span aria-hidden="true" />
			<span aria-hidden="true" />
		</a>
	</div>

	<div id="navbarBasicExample" class="navbar-menu {navbarClass}">
		<div class="navbar-start">
			<NavBarItem {path} link="/" linkName="Home" faIcon="fas fa-home" />
			<NavBarItem {path} link="/Games" linkName="Games" faIcon="fas fa-gamepad" />
			<NavBarItem {path} link="/3D" linkName="3D Art" faIcon="fas fa-cube" />
			<NavBarItem {path} link="/About" linkName="About" faIcon="fas fa-cube" />

			<!-- <div class="navbar-item has-dropdown is-hoverable">
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

		<div class="navbar-end">
			<div class="navbar-item">
				<div class="field is-grouped">
					<p class="control">
						<a class="button is-primary" href="https://twitter.com/BlackDragonBE">
							<span class="icon">
								<i class="fab fa-twitter" aria-hidden="true" />
							</span>
							<span>@BlackDragonBE</span>
						</a>
					</p>
				</div>
			</div>
		</div>
	</div>
</nav>
