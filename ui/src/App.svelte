<script>
  import { Types } from "./constants";
  import Flag from "./SpainFlag.svelte";

  export let name;
</script>

<style global lang="postcss">
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
</style>

<main
  class="flex justify-center items-center h-full bg-gradient-to-r
  from-purple-300">
  <div class="flex p-10 shadow-sm rounded-lg h-90 bg-white">
    <form class="flex-auto">
      <div class="flex flex-wrap">
        <h1 class="flex-auto text-xl font-semibold">Linguistics Framework</h1>
        <div class="text-xl font-semibold text-gray-500">Spanish</div>
        <input
          class="focus:border-light-blue-500 focus:ring-1
          focus:ring-light-blue-500 focus:outline-none w-full text-sm text-black
          placeholder-gray-500 border border-gray-200 rounded-md py-2 pl-10"
          type="text"
          aria-label="Enter Word or Phrase"
          placeholder="Enter Word or Phrase..." />
      </div>
      <div class="flex items-baseline mt-4 mb-6">
        <div class="space-x-2 flex">
          {#each Object.keys(Types) as wordType}
            <button
              class="flex-none flex items-center justify-center h-9
              rounded-md text-gray-400 border border-gray-300"
              type="button"
              aria-label="like">
              {wordType}
            </button>
          {/each}
        </div>
      </div>
      <div class="flex space-x-3 mb-4 text-sm font-medium">
        <button
          class="flex-none flex items-center justify-center w-9 h-9 rounded-md
          text-gray-400 border border-gray-300"
          type="button"
          aria-label="like">
          Save
        </button>
      </div>
    </form>
  </div>

</main>
