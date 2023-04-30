<script>
    import { onMount } from "svelte";
    import axios from "axios";

    let email = "";
    onMount(async () => {
        try {
            const res = await axios.get("/api/user/");
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
        background-color: var(--bg-color-secondary);
        font-size: 14px;
    }
</style>
