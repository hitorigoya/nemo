<script>
    import Header from "./Header.svelte";
    import Content from "./Content.svelte";
    import ContentsList from "./ContentsList.svelte";
    import Sidebar from "./Sidebar.svelte";
</script>

<svelte:head>
    <title>Nemo | オンラインメモ帳アプリ</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP&family=Noto+Serif+Display&display=swap"
        rel="stylesheet"
    /></svelte:head
>
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
