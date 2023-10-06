<script>
    import axios from "axios";
    import { onMount } from "svelte";

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
    <button popovertarget="help" class="help_btn">?</button>
    <div id="help" popover>
        <div class="help_title">オンラインメモ帳アプリ- Nemo</div>
        <ul>
            <li>このアプリはデモアプリです。個人情報を入力しないで下さい</li>
            <li>
                サインアップの際に実在するメールアドレスを入力する必要はありません。メールアドレスの認証は行っておりません
            </li>
            <li>24時間で自動的にログアウトされます</li>
        </ul>
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
        color: var(--text-color-secondary);
        background-color: var(--bg-color-secondary);
    }
    #help {
        border: 1px solid var(--text-color-primary);
        border-radius: 4px;
        padding: 8px 16px;
    }
    .help_title {
        text-align: center;
    }
    .help_btn {
        border: none;
        padding: 8px 12px;
        border-radius: 50%;
        color: var(--text-color-primary);
        background-color: var(--bg-color-primary);
    }
    .help_btn:hover {
        cursor: pointer;
    }
</style>
