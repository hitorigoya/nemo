<script>
    import Header from "./Header.svelte";
    import Sidebar from "./Sidebar.svelte";
    import Content from "./Content.svelte";
</script>

<Header />

<main>
    <Sidebar />
    <Content />
</main>

<style>
    main {
        display: grid;
        grid-template-columns: 256px 1fr;
        gap: 64px;
    }
</style>
