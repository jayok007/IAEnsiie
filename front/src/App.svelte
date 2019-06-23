<script>
  import { onMount } from 'svelte'
  import Header from './components/Header.svelte'
  import Question from './components/Question.svelte'
  import Loader from './components/Loader.svelte'

  let response = ''
  let people = null
  let questions = []
  let displayedQuestions = []
  let isWinning = false
  let loading = true

  function fetchRandomPeople() {
    response = ''
    people = null
    questions = []
    displayedQuestions = []
    isWinning = false
    loading = true

    fetch('/api/random-people')
      .then(res => res.json())
      .then(p => (people = p))
      .then(generateQuestions)
      .then(displayQuestion)
      .catch(console.error)
      .finally(() => (loading = false))
  }

  function generateQuestions() {
    let isMan = people.sexe === 'M'
    questions = [...questions, `Je suis né le ${people.birth_date}`]
    questions = [...questions, `Je suis un${isMan ? '' : 'e'} ${isMan ? 'homme' : 'femme'}`]
    people.jobs.forEach(job => {
      questions = [...questions, `Je suis ${job}`]
    })
    if (people.death_date) {
      questions = [...questions, `Je suis mort le ${people.death_date}`]
    }
  }

  function displayQuestion() {
    if (questions.length < 1) return
    displayedQuestions = [...displayedQuestions, questions.shift()]
  }

  function giveUp() {
    isWinning = true
  }

  function validate() {
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
    {#if loading}
    <Loader></Loader>
    {/if}
    {#if isWinning}
    {people.name}
    {/if}
    <input
      class="input is-info is-large"
      type="text" placeholder="Qui est-ce ?"
      disabled={isWinning}
      bind:value={response}
      on:keyup={validate}
    >

    <button
      class="button is-info"
      disabled={isWinning}
      on:click={displayQuestion}
    >
      Nouvelle question
    </button>
    <button
      class="button is-info"
      disabled={isWinning}
      on:click={giveUp}
    >
      Je donne ma langue au chat
    </button>
    <button
      class="button is-info"
      disabled={!isWinning}
      on:click={fetchRandomPeople}
    >
      Recommencer
    </button>

    {#each displayedQuestions as question}
      <Question question={question} color="is-warning"></Question>
    {/each}
  </div>
</main>
