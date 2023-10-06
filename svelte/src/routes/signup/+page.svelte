<script>
    import axios from "axios";
    import validator from "validator";

    let email = "";
    let password = "";
    let emailWarn = false;
    let passwordWarn = false;
    let displayLoginErrorMsg = false;

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
</script>

<svelte:head>
    <title>サインアップ | Nemo</title>
</svelte:head>

<div class="form_container">
    <h2>サインアップ</h2>
    <div class="signup">登録済みの場合は<a href="/login/">ログイン</a></div>
    <form on:submit|preventDefault={handleSubmit}>
        <label
            ><span class="label_text">メールアドレス</span>
            <input
                bind:value={email}
                on:input={validateEmail}
                class:validator_warn={emailWarn}
            />
        </label>
        <label
            ><span class="label_text">パスワード（半角英数字8文字以上）</span>
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
    <div class="help_title">オンラインメモ帳アプリ - Nemo</div>
    <ul>
        <li>このアプリはデモアプリです。個人情報を入力しないで下さい</li>
        <li>
            サインアップの際に実在するメールアドレスを入力する必要はありません。メールアドレスの認証は行っておりません
        </li>
        <li>24時間で自動的にログアウトされます</li>
    </ul>
</div>

<style>
    .form_container {
        padding: 16px;
    }
    h2 {
        text-align: center;
        margin-bottom: 4px;
    }
    .signup {
        text-align: center;
        font-size: 14px;
        margin-bottom: 24px;
    }
    .signup a {
        font-weight: bold;
    }
    .label_text {
        display: inline-block;
        font-size: 14px;
        margin-bottom: 4px;
        color: #bfbfbf;
    }
    input {
        font-size: 16px;
        display: block;
        width: 100%;
        padding: 12px 16px;
        border: 1px solid #bfbfbf;
        border-radius: 4px;
        margin-bottom: 16px;
        color: var(--text-color-primary);
        background-color: var(--bg-color-secondary);
    }
    input:focus {
        outline: none;
    }
    button {
        font-size: 14px;
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
        margin-top: 64px;
        font-size: 14px;
        color: #fff;
        background-color: #000;
    }
    .help_title {
        text-align: center;
    }
    @media (min-width: 768px) {
        .form_container {
            max-width: 520px;
            margin: 32px auto;
            border-radius: 8px;
            padding: 32px;
            background-color: var(--bg-color-secondary);
        }
        .help {
            max-width: 520px;
            margin: 64px auto;
        }
    }
</style>
