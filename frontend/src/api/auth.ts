import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
});

export interface LoginResponse {
    success: boolean;
    message: string;
    access_token: string;
    token_type: string;

    user: {
        id: number;
        username: string;
        email: string;
    };
}

export async function login(identifier: string, password: string) {
    const response = await api.post<LoginResponse>("/auth/login", {
        identifier,
        password,
    });

    return response.data;
}

export async function register(username: string, email: string, password: string) {
    const response = await api.post("/auth/register", {
        username,
        email,
        password,
    });

    return response.data;
}

export async function verifyToken(token: string) {
    const response = await api.get("/auth/verify", {
        params: {
            token,
        },
    });

    return response.data;
}
