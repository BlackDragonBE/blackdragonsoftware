<script lang="ts">
	export let sketchfabUrl: string;
	export let description: string;
</script>

<div class="column is-one-third">
	<div class="card">
		<div class="sketchfab-embed-wrapper">
			<iframe class="sketchfab" src="{sketchfabUrl}/embed?autospin=0&ui_theme=dark" />
			<p class="px-2"><a href={sketchfabUrl}>{description}</a></p>
		</div>
	</div>
</div>
