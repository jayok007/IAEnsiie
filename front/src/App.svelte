<script>
  import { onMount } from 'svelte'
  import Header from './components/Header.svelte'
  import Question from './components/Question.svelte'
  import Loader from './components/Loader.svelte'
  import Winning from './components/Winning.svelte'
  import Losing from './components/Losing.svelte'

  let response = ''
  let people = null
  let questions = []
  let displayedQuestions = []
  let isWinning = false
  let isLosing = false
  let loading = true

  function fetchRandomPeople() {
    response = ''
    people = null
    questions = []
    displayedQuestions = []
    isWinning = false
    isLosing = false
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
    if (people.birth_date) {
      questions = [...questions, `Je suis né le ${people.birth_date}`]
    }
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
    isLosing = true
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
    {#if people}
      <Winning text={people.text} name={people.name} {isWinning}></Winning>
      <Losing text={people.text} name={people.name} {isLosing}></Losing>
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
      disabled={isWinning || isLosing}
      on:click={displayQuestion}
    >
      Nouvelle question
    </button>
    <button
      class="button is-info"
      disabled={isWinning || isLosing}
      on:click={giveUp}
    >
      Je donne ma langue au chat
    </button>
    <button
      class="button is-info"
      disabled={!isWinning && !isLosing}
      on:click={fetchRandomPeople}
    >
      Recommencer
    </button>

    {#each displayedQuestions as question}
      <Question question={question} color="is-warning"></Question>
    {/each}
  </div>
</main>
