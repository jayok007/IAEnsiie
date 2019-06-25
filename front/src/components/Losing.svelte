<script>
  export let text = ''
  export let name = ''
  export let isLosing = false
</script>

<div class={`modal ${isLosing ? 'is-active' : ''}`}>
  <div class="modal-background"></div>
  <div class="modal-content">
    <article class="message is-danger">
      <div class="message-header">
        <p>Dommage, C'etait {name}.</p>
        <button on:click={() => isLosing = false} class="delete" aria-label="delete"></button>
      </div>
      <div class="message-body">
        {text}
      </div>
    </article>
  </div>
</div>
