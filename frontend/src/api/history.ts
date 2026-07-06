import axios from "axios";

import type { Conversation, Message } from "../types/chat";

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

function convertMessages(data: any[]): Message[] {
    return data.map(item => ({
        sender: item.sender,
        text: item.message,
    }));
}

export async function getHistory(): Promise<Message[]> {
    const response = await api.get("/history/current");

    return convertMessages(response.data);
}

export async function getConversationHistory(conversationId: number): Promise<Message[]> {
    const response = await api.get(`/history/${conversationId}`);

    return convertMessages(response.data);
}

export async function getConversations(): Promise<Conversation[]> {
    const response = await api.get("/history/conversations");

    return response.data;
}

export async function newConversation() {
    const response = await api.post("/history/new");

    return response.data;
}
