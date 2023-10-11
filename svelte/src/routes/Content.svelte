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

<div class="container" class:hide_container={$currentContentID === ""}>
    {#each $contents as content}
        <div
            class="control"
            class:hide_control={$currentContentID !== content.id}
        >
            <button
                class="return_to_contents_list"
                on:click={() => ($currentContentID = "")}
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    height="24"
                    viewBox="0 -960 960 960"
                    width="24"
                    ><path
                        d="M640-80 240-480l400-400 71 71-329 329 329 329-71 71Z"
                        fill="currentColor"
                    /></svg
                >
            </button>
            <div class="control_btn_container">
                <button
                    class:modified={content.modified}
                    on:click={updateContent}>Save</button
                >
                <button on:click={downloadFile}>Download</button>
                <button on:click={deleteContent}>Delete</button>
            </div>
        </div>
        <div
            class="content"
            class:content_visible={$currentContentID === content.id}
        >
            <input
                bind:value={content.title}
                on:input={handleInput}
                class="title_field"
                placeholder="タイトルを入力..."
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
        height: calc(100vh - 64px);
        display: grid;
        grid-template-rows: auto 1fr;
    }
    .hide_container {
        display: none;
    }
    .control {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        padding: 16px;
    }
    .control_btn_container {
        display: flex;
        gap: 16px;
    }
    .control_btn_container button {
        font-size: 15px;
    }
    .hide_control {
        display: none;
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
    .return_to_contents_list {
        display: flex;
    }
    .modified {
        color: #2dc770;
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
        padding: 24px 16px;
        font-size: 24px;
        color: var(--text-content-title);
    }
    .content_field {
        padding: 16px;
        padding-bottom: 256px;
    }
    @media (min-width: 768px) {
        .return_to_contents_list {
            display: none;
        }
    }
</style>
