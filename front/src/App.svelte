<script>
  import { onMount } from 'svelte';
  import Question from './components/Question.svelte';

  let response = '';

  onMount(() => {
    console.log('coucou')
    fetch('/api/peoples')
      .then(console.log)
      .catch(console.error)
  })
</script>

<style>
  .input {
    margin-top: 10px;
  }
</style>

<svelte:head>
	<title>Qui est-ce ?</title>
</svelte:head>

<header>
  <section class="hero is-primary">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">
          Qui est-ce ?
        </h1>
        <h2 class="subtitle">
          Devinez qui est la célébrité !
        </h2>
      </div>
    </div>
  </section>
</header>

<main>
  <div class="container">
    <input class="input is-large" type="text" placeholder="Qui est-ce ?" bind:value={response}>
    {response}
    <Question question="he ?" color="is-info"></Question>
    <Question question="ha ?" color="is-warning"></Question>
  </div>
</main>
