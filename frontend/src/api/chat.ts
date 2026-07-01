import axios from "axios";
import type { ChatResponse } from "../types/chat";

const api = axios.create({
    baseURL: "http://localhost:8000",
});

export async function sendMessage(userId: string, message: string): Promise<ChatResponse> {
    const response = await api.post("/chat", {
        user_id: userId,
        message,
    });

    return response.data;
}
