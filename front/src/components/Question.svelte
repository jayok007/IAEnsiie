<script>
  export let question;
  export let color;
</script>

<style>
  .question {
    margin: 10px;
  }
</style>

<div class="question">
  <article class="tile is-child notification {color}">
    <p class="subtitle">{question}</p>
  </article>
</div>
