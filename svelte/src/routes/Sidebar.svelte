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

    async function deleteContent() {
        const index = $contents.findIndex(
            (obj) => obj.id === $currentContentID
        );
        if (index === -1) return;

        try {
            const res = await axios.delete(
                `/api/content/${$contents[index].id}`
            );
            console.log(res.data);
            $currentContentID = "";
            getContents();
        } catch (err) {
            console.log(err);
        }
    }
</script>

<ul>
    {#each $contents as content}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <li
            on:click={() => ($currentContentID = content.id)}
            class:current_content={$currentContentID === content.id}
            class:modified={content.modified}
        >
            {content.title}<span
                on:click={deleteContent}
                class="delete_btn"
                class:visible={$currentContentID === content.id}>×</span
            >
        </li>
    {/each}
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <li on:click={createContent}>+ テキストを追加</li>
</ul>

<style>
    ul {
        display: none;
    }
    @media (min-width: 768px) {
        ul {
            display: block;
            list-style: none;
            position: sticky;
            top: 64px;
            height: calc(100vh - 64px);
            margin: 0;
            padding: 0;
            overflow-y: auto;
        }
        ul li {
            font-size: 14px;
            padding: 4px 16px;
            white-space: nowrap;
            position: relative;
            color: var(--text-color-secondary);
        }
        ul li:hover {
            cursor: pointer;
            background-color: #313131;
        }
        ul li:last-of-type {
            font-size: 12px;
        }
        .current_content {
            color: var(--text-color-primary) !important;
            background-color: #313131;
        }
        .modified::before {
            content: "* ";
        }
        .delete_btn {
            display: none;
            position: absolute;
            top: 10%;
            bottom: 10%;
            right: 0;
            padding: 0 4px;
            border: 1px solid var(--text-color-secondary);
            border-radius: 4px;
            color: var(--text-color-secondary);
            background-color: var(--bg-color-secondary);
        }
        .delete_btn:hover {
            color: var(--text-color-primary);
            border-color: var(--text-color-primary);
        }
        .visible {
            display: block;
        }
    }
</style>
