<script>
  import { onMount } from 'svelte'
  import Header from './components/Header.svelte'
  import Question from './components/Question.svelte'

  let response = ''
  let people = null
  let questions = []
  let isWinning = false

  function fetchRandomPeople() {
    fetch('/api/random-people')
      .then(res => res.json())
      .then(p => people = p)
      .catch(console.error)
  }

  function validate(event) {
    isWinning = response.toLowerCase() === people.name.toLowerCase()
  }

  onMount(fetchRandomPeople)
</script>

<style>
  .input, .button {
    margin-top: 10px;
  }
</style>

<Header></Header>
<main>
  <div class="container">
    <input
      class="input is-info is-large"
      type="text" placeholder="Qui est-ce ?"
      disabled={isWinning}
      bind:value={response}
      on:keyup={validate}
    >

    <button
      class="button is-info"
      on:click={validate}
      disabled={isWinning}
    >
      Valider
    </button>
    <button
      class="button is-info"
      disabled={isWinning}
    >
      Nouvelle question
    </button>
    <button
      class="button is-info"
      disabled={isWinning}
    >
      Je donne ma langue au chat
    </button>
    <button class="button is-info" disabled={!isWinning}>Recommencer</button>

    <Question question="he ?" color="is-warning"></Question>
  </div>
</main>
