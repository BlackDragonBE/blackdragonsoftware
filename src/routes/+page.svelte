<script lang="ts">
	import gh from '$lib/images/github.jpg';
	import itch from '$lib/images/itch.jpg';
	import rw from '$lib/images/rw.jpg';
	import logo_full from '$lib/images/logo-full.png';
</script>

<div class="columns mt-4">
	<div class="column is-half is-offset-one-quarter has-text-centered">
		<img src={logo_full} />
		<p class="subtitle">Digital creations by Eric Van de Kerckhove</p>
	</div>
</div>

<div class="columns p-4">
	<div class="column is-offset-1">
		<div class="card scalehover" style="height: 100%">
			<div class="card-image">
				<figure class="image is-4by3">
					<a href="https://blackdragonbe.itch.io/"><img src={itch} alt="itch.io" /></a>
				</figure>
			</div>
			<div class="card-content">
				<div class="media">
					<div class="media-left">
						<figure class="image is-48x48">
							<i class="fab fa-itch-io fa-3x" />
						</figure>
					</div>
					<div class="media-content">
						<p class="title is-4"><a href="https://blackdragonbe.itch.io/">itch.io</a></p>
						<p class="subtitle is-6">Game developer</p>
					</div>
				</div>

				<div class="content">
					I host most of my recent Unity games and old prototypes on itch.io. I'm a fan of game jams as well!
					<br />
				</div>
			</div>
		</div>
	</div>
	<div class="column">
		<div class="card scalehover" style="height: 100%">
			<div class="card-image">
				<figure class="image is-4by3">
					<a href="https://www.raywenderlich.com/gametech"><img src={rw} alt="Kodeco" /></a>
				</figure>
			</div>
			<div class="card-content">
				<div class="media">
					<div class="media-left">
						<figure class="image is-48x48">
							<i class="fas fa-book fa-3x" />
						</figure>
					</div>
					<div class="media-content">
						<p class="title is-4">
							<a href="https://www.kodeco.com/gametech">Kodeco</a>
						</p>
						<p class="subtitle is-6">Team lead</p>
					</div>
				</div>

				<div class="content">
					I'm the lead of an amazing group of people that teach people how to make games and experiences.
					<br />
				</div>
			</div>
		</div>
	</div>
	<div class="column">
		<div class="card scalehover" style="height: 100%">
			<div class="card-image">
				<figure class="image is-4by3">
					<a href="https://github.com/BlackDragonBE"><img src={gh} alt="Github" /></a>
				</figure>
			</div>
			<div class="card-content">
				<div class="media">
					<div class="media-left">
						<figure class="image is-48x48">
							<i class="fab fa-github fa-3x" />
						</figure>
					</div>
					<div class="media-content">
						<p class="title is-4"><a href="https://github.com/BlackDragonBE">Github</a></p>
						<p class="subtitle is-6">Coder</p>
					</div>
				</div>
				<div class="content">
					There's a bunch of scripts and useful little applications I made over on my Github.
					<br />
				</div>
			</div>
		</div>
	</div>
	<div class="column is-1" />
</div>
