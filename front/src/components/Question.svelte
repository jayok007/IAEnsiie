<script>
  export let question
  export let color
</script>

<style>
  .question {
    margin: 10px 0 10px 0;
  }
</style>

<div class="question">
  <article class="tile is-child notification {color}">
    <p class="subtitle">{question}</p>
  </article>
</div>
