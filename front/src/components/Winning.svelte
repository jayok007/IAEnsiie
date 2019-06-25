<script>
  export let text = ''
  export let name = ''
  export let isWinning = false
</script>

<div class={`modal ${isWinning ? 'is-active' : ''}`}>
  <div class="modal-background"></div>
  <div class="modal-content">
    <article class="message is-success">
      <div class="message-header">
        <p>C'est bien {name}, vous avez gagné !!!</p>
        <button on:click={() => isWinning = false} class="delete" aria-label="delete"></button>
      </div>
      <div class="message-body">
        {text}
      </div>
    </article>
  </div>
</div>
