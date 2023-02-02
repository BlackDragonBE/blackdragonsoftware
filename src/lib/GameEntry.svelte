<script lang="ts">
	export let name: string;
	export let url: string = "#";
	export let imageSrc: string;
	export let releaseDate: string;
	export let description: string;

	export let web: boolean = false;
	export let windows: boolean = false;
	export let macos: boolean = false;
	export let linux: boolean = false;
	export let android: boolean = false;
</script>

<div class="column is-one-third is-3-desktop is-2-widescreen">
	<a href="{url}">
		<div class="card scalehover has-background-dark">
			<figure class="image image is-16by9 is-fullwidth">
				<img src={imageSrc} alt={name} style="object-fit: contain;background-color: black;" />
			</figure>
			<div class="media-content p-2">
				<div>
					{#if web}
						<i title="Play in your browser!" class="fab fa-chrome fa-fw" />
					{/if}
					{#if windows}
						<i title="Windows" class="fab fa-windows fa-fw" />
					{/if}
					{#if macos}
						<i title="macOS" class="fab fa-apple fa-fw" />
					{/if}
					{#if linux}
						<i title="Linux" class="fab fa-linux fa-fw" />
					{/if}
					{#if android}
						<i title="Android" class="fab fa-android fa-fw" />
					{/if}
				</div>
				<p class="is-size-5 has-text-warning">{name}</p>
				<h2 class="subtitle is-size-6">Released on {releaseDate}</h2>
				<p>{description}</p>
			</div>
		</div>
	</a>
</div>
