<script>
    import { onMount } from "svelte";
    import axios from "axios";
    import validator from "validator";

    export let authType;

    const LOGIN = "login";
    const SIGNUP = "signup";

    let email = "";
    let password = "";
    let emailWarn = false;
    let passwordWarn = false;
    let displayAuthErrorMsg = false;
    let inputEmailElement;

    function validateEmail() {
        if (validator.isEmail(email)) {
            emailWarn = false;
        } else {
            emailWarn = true;
        }
    }
    function validatePassword() {
        if (
            validator.isLength(password, { min: 8, max: undefined }) &&
            validator.isAlphanumeric(password)
        ) {
            passwordWarn = false;
        } else {
            passwordWarn = true;
        }
    }
    async function handleSubmit() {
        if (
            validator.isEmail(email) &&
            validator.isLength(password, { min: 8, max: undefined }) &&
            validator.isAlphanumeric(password)
        ) {
            try {
                let path = "";
                if (authType === LOGIN) {
                    path = LOGIN;
                } else if (authType === SIGNUP) {
                    path = SIGNUP;
                } else {
                    return;
                }
                await axios.post(`/api/${path}/`, {
                    email: email,
                    password: password,
                });
                window.location.replace("/");
            } catch (err) {
                displayAuthErrorMsg = true;
            }
        }
    }

    onMount(() => {
        inputEmailElement.focus();
    });
</script>

<svelte:head>
    {#if authType === LOGIN}
        <title>ログイン | Nemo</title>
    {:else if authType === SIGNUP}
        <title>サインアップ | Nemo</title>
    {/if}
</svelte:head>

<div class="container">
    <div class="form_container">
        <div class="app_title">オンラインメモ帳アプリ - Nemo -</div>
        {#if authType === LOGIN}
            <div class="form_title">ログイン</div>
            <div class="form_nav">
                未登録の場合は<a href="/signup/">サインアップ</a>
            </div>
        {:else if authType === SIGNUP}
            <div class="form_title">サインアップ</div>
            <div class="form_nav">
                登録済みの場合は<a href="/login/">ログイン</a>
            </div>
        {/if}
        <form on:submit|preventDefault={handleSubmit}>
            <label
                ><span class="label_text"
                    >メールアドレス<span class="required_mail">*</span></span
                >
                <input
                    bind:this={inputEmailElement}
                    bind:value={email}
                    on:input={validateEmail}
                    class:validator_warn={emailWarn}
                />
            </label>
            <label
                ><span class="label_text"
                    >パスワード（半角英数字8文字以上）<span
                        class="required_password">*</span
                    ></span
                >
                <input
                    bind:value={password}
                    on:input={validatePassword}
                    type="password"
                    class:validator_warn={passwordWarn}
                />
            </label>
            {#if authType === LOGIN}
                <button>ログイン</button>
                <div class="auth_error_msg" class:visible={displayAuthErrorMsg}>
                    メールアドレスもしくはパスワードが違います
                </div>
            {:else if authType === SIGNUP}
                <button>サインアップ</button>
                <div class="auth_error_msg" class:visible={displayAuthErrorMsg}>
                    このメールアドレスはすでに登録されています
                </div>
            {/if}
        </form>
    </div>

    <div class="help">
        <ul>
            <li>このアプリはデモアプリです。個人情報を入力しないで下さい</li>
            <li>
                サインアップの際に実在するメールアドレスを入力する必要はありません。メールアドレスの認証は行っておりません
            </li>
            <li>24時間で自動的にログアウトされます</li>
        </ul>
    </div>
</div>

<style>
    .container {
        min-height: 100vh;
        background-image: url("/camp-4363073_1920.png");
        display: grid;
        justify-content: center;
        gap: 32px;
    }
    .form_container {
        padding: 16px;
        background-color: var(--bg-color-primary);
    }
    .app_title {
        text-align: center;
        font-weight: bold;
        padding-top: 16px;
    }
    .form_title {
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 32px;
        margin-bottom: 8px;
        color: var(--text-content-title);
    }
    .form_nav {
        text-align: center;
        font-size: 14px;
        margin-bottom: 24px;
        color: var(--text-color-secondary);
    }
    .label_text {
        display: inline-block;
        font-size: 13px;
        font-weight: bold;
        margin-bottom: 4px;
        color: #bfbfbf;
    }
    .required_mail {
        color: tomato;
        padding-left: 4px;
    }
    .required_password {
        color: tomato;
    }
    input {
        font-size: 16px;
        display: block;
        width: 100%;
        padding: 12px 16px;
        border: 1px solid transparent;
        border-radius: 4px;
        margin-bottom: 16px;
        color: var(--text-color-primary);
        background-color: var(--bg-color-secondary);
    }
    input:focus {
        outline: none;
    }
    button {
        font-size: 16px;
        text-align: center;
        width: 100%;
        padding: 12px 16px;
        margin-top: 16px;
        border: none;
        border-radius: 4px;
        color: #fff;
        background-color: #1473e6;
    }
    button:hover {
        cursor: pointer;
    }
    .validator_warn {
        border-color: tomato;
    }
    .auth_error_msg {
        display: none;
        text-align: center;
        font-size: 14px;
        margin-top: 16px;
        color: tomato;
    }
    .visible {
        display: block;
    }
    .help {
        border: 1px solid var(--text-color-primary);
        border-radius: 4px;
        padding: 8px 16px;
        font-size: 14px;
        color: #fff;
        background-color: #000;
    }
    @media (min-width: 768px) {
        .container {
            align-content: center;
        }
        .form_container {
            max-width: 520px;
            border-radius: 8px;
            padding: 32px;
            background-color: var(--bg-color-primary);
        }
        .app_title {
            font-size: 18px;
        }
        .form_title {
            font-size: 20px;
        }
        .help {
            max-width: 520px;
        }
    }
</style>
