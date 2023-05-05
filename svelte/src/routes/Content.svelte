<script>
    import axios from "axios";
    import { onMount } from "svelte";
    import { contents, currentContentID } from "./store.js";

    onMount(() => {
        getContents();
    });

    async function getContents() {
        try {
            const res = await axios.get("/api/content/");
            $contents = res.data;
            console.log(res.data);
        } catch (err) {
            console.log(err);
        }
    }

    async function updateContent() {
        const index = getCurrentIndex();
        if (index === -1) return;

        try {
            const res = await axios.put("/api/content", {
                id: $contents[index].id,
                title: $contents[index].title,
                content: $contents[index].content,
            });
            $contents[index].modified = false;
            console.log(res.data);
        } catch (err) {
            console.log(err);
        }
    }

    function handleInput() {
        const index = getCurrentIndex();
        if (index === -1) return;
        $contents[index].modified = true;
    }

    function handleKeydown(event) {
        if (event.key === "s" && event.ctrlKey) {
            event.preventDefault();
            updateContent();
        }
    }

    function downloadFile() {
        const index = getCurrentIndex();
        if (index === -1) return;
        const blob = new Blob([$contents[index].content], {
            type: "text/plain",
        });
        const blobUrl = URL.createObjectURL(blob);
        const anchor = document.createElement("a");
        anchor.href = blobUrl;
        anchor.download = `${$contents[index].title}.txt`;
        anchor.click();
        URL.revokeObjectURL(blobUrl);
    }

    function getCurrentIndex() {
        return $contents.findIndex((obj) => obj.id === $currentContentID);
    }
</script>

<div class="container">
    <div class="control" class:control_visible={$currentContentID !== ""}>
        <button on:click={updateContent}>Save</button><button
            on:click={downloadFile}>Download</button
        >
    </div>

    {#each $contents as content}
        <div
            class="content"
            class:content_visible={$currentContentID === content.id}
        >
            <input
                bind:value={content.title}
                on:input={handleInput}
                class="title_field"
            />
            <textarea
                bind:value={content.content}
                on:input={handleInput}
                class="content_field"
                placeholder="テキストを入力..."
            />
        </div>
    {/each}
</div>

<svelte:window on:keydown={handleKeydown} />

<style>
    .container {
        display: grid;
        grid-template-rows: auto 1fr;
    }
    .content {
        display: none;
    }
    .content_visible {
        display: grid;
        grid-template-rows: auto 1fr;
    }
    input,
    textarea {
        font-size: 16px;
        font-family: inherit;
        border: none;
        width: 100%;
        color: var(--text-color-primary);
        background-color: var(--bg-color-primary);
    }
    input:focus,
    textarea:focus {
        outline: none;
    }
    .title_field {
        padding: 32px 0;
        font-size: 32px;
    }
    .content_field {
        padding-top: 0;
        padding-bottom: 256px;
        padding-left: 0;
    }
    .control {
        display: none;
    }
    .control_visible {
        display: flex;
        gap: 16px;
        padding-top: 16px;
    }
    button {
        border: none;
        border-radius: 4px;
        padding: 4px 8px;
        color: var(--text-color-secondary);
        background-color: var(--bg-color-secondary);
    }
    button:hover {
        cursor: pointer;
        color: var(--text-color-primary);
    }
</style>
