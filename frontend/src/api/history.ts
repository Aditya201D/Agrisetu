import axios from "axios";
import type { Message } from "../types/chat";

const api = axios.create({
    baseURL: "http://localhost:8000",
});

api.interceptors.request.use(config => {
    const token = localStorage.getItem("access_token");

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

export async function getHistory(): Promise<Message[]> {
    const response = await api.get("/chat/history");

    return response.data.map((item: { sender: string; message: string }) => ({
        sender: item.sender,
        text: item.message,
    }));
}
