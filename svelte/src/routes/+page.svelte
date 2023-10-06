<script>
    import Header from "./Header.svelte";
    import Content from "./Content.svelte";
    import ContentsList from "./ContentsList.svelte";
    import Sidebar from "./Sidebar.svelte";
</script>

<Header />

<main>
    <Sidebar />
    <Content />
    <ContentsList />
</main>

<style>
    main {
        height: calc(100vh - 64px);
        display: grid;
        grid-template-rows: 1fr;
    }
    @media (min-width: 768px) {
        main {
            display: grid;
            grid-template-columns: 256px 1fr;
            gap: 64px;
        }
    }
</style>
