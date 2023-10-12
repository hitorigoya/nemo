<script>
    import { onMount } from "svelte";
    import axios from "axios";
    import validator from "validator";

    let email = "";
    let password = "";
    let emailWarn = false;
    let passwordWarn = false;
    let displayLoginErrorMsg = false;
    let inputElement;

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
                await axios.post("/api/signup/", {
                    email: email,
                    password: password,
                });
                window.location.replace("/");
            } catch (err) {
                if (err.response.status === 404) {
                    displayLoginErrorMsg = true;
                }
            }
        }
    }

    onMount(() => {
        inputElement.focus();
    });
</script>

<svelte:head>
    <title>サインアップ | Nemo</title>
</svelte:head>

<div class="container">
    <div class="form_container">
        <div class="app_title">オンラインメモ帳アプリ - Nemo -</div>
        <div class="form_title">サインアップ</div>
        <div class="signup">登録済みの場合は<a href="/login/">ログイン</a></div>
        <form on:submit|preventDefault={handleSubmit}>
            <label
                ><span class="label_text"
                    >メールアドレス<span class="required_mail">*</span></span
                >
                <input
                    bind:this={inputElement}
                    bind:value={email}
                    on:input={validateEmail}
                    class:validator_warn={emailWarn}
                />
            </label>
            <label
                ><span class="label_text"
                    >パスワード（半角英数字8文字以上）<span class="required"
                        >*</span
                    ></span
                >
                <input
                    bind:value={password}
                    on:input={validatePassword}
                    type="password"
                    class:validator_warn={passwordWarn}
                />
            </label>
            <button>サインアップ</button>
            <div class="login_error_msg" class:visible={displayLoginErrorMsg}>
                このメールアドレスはすでに登録されています
            </div>
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
        background-image: url("/sunset-3563482_1920.jpg");
        display: grid;
        justify-content: center;
        align-content: center;
        gap: 32px;
    }
    .form_container {
        padding: 16px;
        background-color: var(--bg-color-primary);
        opacity: 0.94;
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
    .signup {
        text-align: center;
        font-size: 14px;
        margin-bottom: 24px;
        color: var(--text-color-secondary);
    }
    .required_mail {
        color: tomato;
        padding-left: 4px;
    }
    .required {
        color: tomato;
    }
    .label_text {
        display: inline-block;
        font-size: 13px;
        font-weight: bold;
        margin-bottom: 4px;
        color: #bfbfbf;
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
    .login_error_msg {
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
