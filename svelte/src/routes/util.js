import axios from "axios";

export const request = axios.create({
    xsrfCookieName: "xsrf_token",
});
