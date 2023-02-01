<script lang="ts">
	export let path : string;
	export let link : string = "";
	export let linkName : string = "Home";
	export let faIcon : string = "fas fa-home";
</script>

<a class="navbar-item {path === link ? 'active' : ''}" href={link}>{linkName}</a>
