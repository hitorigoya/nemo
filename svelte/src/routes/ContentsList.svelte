<script>
    import axios from "axios";
    import { contents, currentContentID } from "./store.js";

    async function getContents() {
        try {
            const res = await axios.get("/api/content/");
            $contents = res.data;
            console.log(res.data);
        } catch (err) {
            console.log(err);
        }
    }

    async function createContent() {
        try {
            const res = await axios.post("/api/content");
            console.log(res.data);
            getContents();
        } catch (err) {
            console.log(err);
        }
    }
</script>

<ul class:hide_contents_list={$currentContentID !== ""}>
    {#each $contents as content}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <li
            on:click={() => ($currentContentID = content.id)}
            class:modified={content.modified}
        >
            {content.title}
        </li>
    {/each}
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <li on:click={createContent}>+ テキストを追加</li>
</ul>

<style>
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }
    ul li {
        font-size: 14px;
        padding: 8px 16px;
        white-space: nowrap;
        color: var(--text-color-secondary);
    }
    .modified::before {
        content: "* ";
    }
    .hide_contents_list {
        display: none;
    }
</style>
