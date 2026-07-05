import axios from "axios";
import type { ChatResponse } from "../types/chat";

const api = axios.create({
    baseURL: "http://localhost:8000",
});

// Automatically attach JWT to every request
api.interceptors.request.use(config => {
    const token = localStorage.getItem("access_token");

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

export async function sendMessage(message: string): Promise<ChatResponse> {
    const response = await api.post("/chat", {
        message,
    });

    return response.data;
}
