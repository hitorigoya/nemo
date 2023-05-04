<script>
    import { onMount } from "svelte";
    import { request } from "./util.js";

    let email = "";
    onMount(async () => {
        try {
            const res = await request.get("/api/user/");
            email = res.data.email;
        } catch (err) {
            console.log(err);
        }
    });
</script>

<header>
    <div>{email}</div>
    <div>
        <a href="/login/">ログイン</a>
        <a href="/signup/">サインアップ</a>
    </div>
</header>

<style>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px;
        height: 64px;
        position: sticky;
        top: 0;
        font-size: 14px;
        background-color: var(--bg-color-secondary);
    }
</style>
