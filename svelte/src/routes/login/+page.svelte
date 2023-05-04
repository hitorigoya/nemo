<script>
    import axios from "axios";
    import validator from "validator";

    let email = "";
    let password = "";
    let emailFormWarn = false;
    let passwordFormWarn = false;
    let displayLoginErrorMsg = false;

    function validateEmail() {
        if (validator.isEmail(email)) {
            emailFormWarn = false;
        } else {
            emailFormWarn = true;
        }
    }
    function validatePassword() {
        if (
            validator.isLength(password, { min: 8, max: undefined }) &&
            validator.isAlphanumeric(password)
        ) {
            passwordFormWarn = false;
        } else {
            passwordFormWarn = true;
        }
    }
    async function handleSubmit() {
        console.log(email);
        console.log(password);

        if (
            validator.isEmail(email) &&
            validator.isLength(password, { min: 8, max: undefined }) &&
            validator.isAlphanumeric(password)
        ) {
            try {
                const res = await axios.post("/api/login/", {
                    email: email,
                    password: password,
                });
                console.log(res);
                if (res.status === 200) {
                    window.location.replace("/");
                }
            } catch (err) {
                displayLoginErrorMsg = true;
            }
        } else {
            return;
        }
    }
</script>

<div class="form_container">
    <h2>ログイン</h2>
    <div class="signup">未登録の場合は<a href="/signup/">サインアップ</a></div>
    <form on:submit|preventDefault={handleSubmit}>
        <label
            ><span class="title">メールアドレス</span>
            <input
                bind:value={email}
                on:input={validateEmail}
                class:validator_warn={emailFormWarn === true}
            />
        </label>
        <label
            ><span class="title">パスワード（半角英数字8文字以上）</span>
            <input
                bind:value={password}
                on:input={validatePassword}
                type="password"
                class:validator_warn={passwordFormWarn === true}
            />
        </label>
        <button>ログイン</button>
        <div
            class="login_error_msg"
            class:visible={displayLoginErrorMsg === true}
        >
            メールアドレスもしくはパスワードが違います
        </div>
    </form>
</div>

<style>
    .form_container {
        max-width: 520px;
        margin: 32px auto;
        border-radius: 8px;
        padding: 32px;
        background-color: var(--bg-color-secondary);
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
    .title {
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
</style>
