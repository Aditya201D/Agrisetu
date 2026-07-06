import axios from "axios";
import type { ChatResponse, Message } from "../types/chat";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
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

export interface Conversation {
    id: number;
    title: string;
    created_at: string;
    updated_at: string;
}

export async function getConversations(): Promise<Conversation[]> {
    const response = await api.get("/history/conversations");
    return response.data;
}

export async function getConversation(conversationId: number): Promise<Message[]> {
    const response = await api.get(`/history/${conversationId}`);

    return response.data.map((msg: any) => ({
        sender: msg.sender,
        text: msg.message,
    }));
}

export async function newConversation() {
    const response = await api.post("/history/new");

    return response.data;
}
