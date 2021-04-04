<script>
  import { Types, Tenses } from "./constants";
  import { fade, slide } from "svelte/transition";

  const DEV_URL = "http://localhost:3001/api";
  const MessageTypes = {
    Error: "error",
    Success: "success"
  };

  let selected = Types.Vocabulary;
  let verbTense = "";
  let word = "";
  let flash = null;
  let loading = false;

  $: buttonDisabled = !word || (selected === Types.Verb && verbTense === "");

  function selectWordType(type) {
    selected = type;
  }

  function selectVerbTense(tense) {
    verbTense = Tenses[tense];
  }

  async function save() {
    try {
      loading = true;
      const response = await fetch(`/api/${selected}`, {
        method: "POST",
        body: JSON.stringify({
          word,
          tense: verbTense
        }),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json"
        }
      });
      const json = await response.json();

      if (response.status !== 200) throw new Error(json.error);

      // word successfully saved
      flash = {
        type: MessageTypes.Success,
        message: `Added ${json.front} to ${json.deck}`,
        preview: json.back
      };
    } catch (err) {
      flash = {
        type: MessageTypes.Error,
        message: err.message
      };
    } finally {
      loading = false;
    }
  }
</script>

{#if flash}
  <div
    transition:fade
    class={`w-full absolute top-0 rounded-sm w-48 m-auto p-3 text-white
    font-medium ${flash.type === MessageTypes.Error ? 'bg-red-400' : 'bg-green-300'}`}>
    {flash.message}
    <span
      class="absolute top-3 right-5 font-semibold cursor-pointer"
      on:click={() => (flash = null)}>
      X
    </span>

    {#if flash.type === MessageTypes.Success}
      {@html flash.preview}
    {/if}
  </div>
{/if}
<form
  transition:fade
  class="flex-initial p-7 shadow-sm rounded-2xl h-auto bg-white"
  on:submit|preventDefault>
  <header class="flex flex-auto my-6 justify-between">
    <h1 class="text-xl font-semibold mr-5">🌐 Linguistics Framework</h1>
    <div class="text-xl font-semibold text-gray-500">Español 🇪🇸 🇲🇽 🇻🇪</div>
  </header>
  <textarea
    class="focus:border-light-purple-500 focus:ring-1
    focus:ring-light-purple-500 focus:outline-none w-full text-sm text-black
    placeholder-gray-500 border border-gray-200 rounded-md py-2 pl-2 my-4"
    type="text"
    aria-label="Enter Word or Verb"
    placeholder="Enter Word or Verb"
    on:input={() => {
      flash = null;
    }}
    bind:value={word} />
  <div class="space-x-2 flex w-full my-5">
    {#each Object.values(Types) as wordType}
      <button
        on:click={() => selectWordType(wordType)}
        class={`transition duration-500 bg-purple-300 hover:bg-purple-500 text-white font-medium font-sm py-2 px-4 rounded-md capitalize ${selected === wordType ? 'bg-purple-500' : ''}`}>
        {wordType}
      </button>
    {/each}
  </div>
  {#if selected === Types.Verb}
    <div
      class="flex flex-col md:space-x-2 lg:space-x-2 md:flex-row lg:flex-row
      w-full my-3"
      transition:slide>
      {#each Object.keys(Tenses) as tense}
        <button
          on:click={() => selectVerbTense(tense)}
          class={`transition duration-500 hover:bg-purple-400 text-grey
          font-medium font-sm py-2 px-4 rounded-full text-xs mt-5 md:mt-0
          lg:mt-0 ${verbTense === Tenses[tense] ? 'bg-purple-400 text-white' : ''}`}>
          {tense}
        </button>
      {/each}
    </div>
  {/if}
  <button
    on:click={save}
    disabled={!!buttonDisabled}
    class="transition duration-500 py-2 px-4 w-full font-semibold rounded-full
    shadow-sm text-white bg-purple-500 hover:bg-purple-700 mt-5 h-12
    disabled:opacity-50">
    {loading ? 'Saving...' : 'Save'}
  </button>
</form>
