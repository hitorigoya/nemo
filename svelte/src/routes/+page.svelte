<script>
    import Header from "./Header.svelte";
    import { onMount } from "svelte";
    import { tick } from "svelte";
    import axios from "axios";

    let contents = [];
    let currentContentID = "";

    onMount(async () => {
        getContents();
    });

    async function getContents() {
        try {
            const res = await axios.get("/api/content/");
            contents = res.data;
            console.log(contents);
        } catch (err) {
            console.log(err);
        }
    }

    async function updateContent() {
        const index = contents.findIndex((obj) => obj.id === currentContentID);
        if (index === -1) return;

        try {
            const res = await axios.put("/api/content", {
                id: contents[index].id,
                title: contents[index].title,
                content: contents[index].content,
            });
            contents[index].modified = false;
            console.log(res);
        } catch (err) {
            console.log(err);
        }
    }

    async function createContent() {
        try {
            const res = await axios.post("/api/content");
            console.log(res);
            getContents();
        } catch (err) {
            console.log(err);
        }
    }

    function handleInput(content) {
        const index = contents.findIndex((obj) => obj.id === content.id);
        if (index === -1) return;
        contents[index].modified = true;
    }

    function handleKeydown(event) {
        if (event.key === "s" && event.ctrlKey) {
            event.preventDefault();
            updateContent();
        }
    }
</script>

<Header />

<main>
    <ul class="side_bar">
        {#each contents as content}
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <li
                on:click={() => (currentContentID = content.id)}
                class:current_content={currentContentID === content.id}
                class:modified={content.modified}
            >
                {content.title}
            </li>
        {/each}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <li on:click={createContent}>+ ページを追加</li>
    </ul>

    <div>
        {#each contents as content}
            <div
                class="content"
                class:visible={currentContentID === content.id}
            >
                <input
                    bind:value={content.title}
                    on:input={handleInput(content)}
                    class="title_field"
                />
                <textarea
                    bind:value={content.content}
                    on:input={handleInput(content)}
                    class="content_field"
                />
            </div>
        {/each}
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
        <div>
            Use jobs..needs to identify any jobs that must complete successfully
            before this job will run. <br />
            It can be a string or array of strings. <br />
            If a job fails or is skipped, all jobs that need it are skipped unless
            the jobs use a conditional expression that causes the job to continue.
            <br />
            If a run contains a series of jobs that need each other, <br />
            a failure or skip applies to all jobs in the dependency chain from the
            point of failure or skip onwards.
        </div>
    </div>
</main>

<svelte:window on:keydown={handleKeydown} />

<style>
    main {
        display: flex;
    }

    /* sidebar */
    .side_bar {
        list-style: none;
        position: sticky;
        top: 64px;
        height: 100%;
        width: 240px;
        margin: 0;
        padding: 0;
        overflow: hidden;
        /* border-right: 1px solid #404040; */
    }
    .side_bar li {
        font-size: 14px;
        color: var(--text-color-secondary);
        padding: 4px 16px;
        white-space: nowrap;
    }
    .side_bar li:hover {
        cursor: pointer;
        background-color: #313131;
    }

    .side_bar li:last-of-type {
        font-size: 12px;
    }

    /* content */
    .content {
        display: none;
    }
    input,
    textarea {
        font-size: 16px;
        font-family: inherit;
        border: none;
        width: 100%;
        background-color: var(--bg-color-primary);
        color: var(--text-color-primary);
    }
    input:focus,
    textarea:focus {
        outline: none;
    }
    .title_field {
        padding: 32px 62px;
        padding-bottom: 0;
        font-size: 32px;
    }
    .content_field {
        padding: 32px 62px;
    }
    .current_content {
        color: var(--text-color-primary) !important;
        background-color: #313131;
    }

    /* state */
    .visible {
        display: block;
    }
    .modified::before {
        content: "* ";
    }
</style>
