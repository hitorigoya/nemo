<script>
    import Content from "./Content.svelte";
    import ContentsList from "./ContentsList.svelte";
    import ContentsListDesktop from "./ContentsListDesktop.svelte";
    import axios from "axios";
    import { onMount } from "svelte";
    import { contents } from "./store.js";

    async function getContents() {
        try {
            const res = await axios.get("/api/content/");
            $contents = res.data;
            console.log(res.data);
        } catch (err) {
            console.log(err);
            window.location.replace("/login/");
        }
    }

    onMount(() => {
        getContents();
    });
</script>

<main>
    <div class="mobile">
        <ContentsList />
        <Content />
    </div>
    <div class="desktop">
        <ContentsListDesktop />
        <Content />
    </div>
</main>

<style>
    main {
        height: calc(100vh - 64px);
    }
    .desktop {
        display: none;
    }
    @media (min-width: 768px) {
        .mobile {
            display: none;
        }
        .desktop {
            display: grid;
            grid-template-columns: 256px 1fr;
            gap: 32px;
        }
    }
</style>
