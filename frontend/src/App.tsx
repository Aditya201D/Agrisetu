import { useEffect, useState } from "react";

import ChatContainer from "./components/ChatContainer";
import ChatInput from "./components/ChatInput";
import Header from "./components/Header";
import SessionDebug from "./components/SessionDebug";

import { sendMessage } from "./api/chat";

import type { Message, Session } from "./types/chat";

import { getCurrentLocation } from "./services/geolocation";

export default function App() {
    const USER_ID = "user1";

    const [messages, setMessages] = useState<Message[]>([]);
    const [session, setSession] = useState<Session | null>(null);
    const [loading, setLoading] = useState(false);

    async function handleSend(text: string) {
        if (loading) return;

        setMessages(prev => [
            ...prev,
            {
                sender: "user",
                text,
            },
        ]);

        setLoading(true);

        try {
            const response = await sendMessage(USER_ID, text);

            if (response.reply.trim()) {
                setMessages(prev => [
                    ...prev,
                    {
                        sender: "bot",
                        text: response.reply,
                    },
                ]);
            }

            setSession(response.session);
        } catch (error) {
            console.error(error);

            setMessages(prev => [
                ...prev,
                {
                    sender: "bot",
                    text: "Unable to contact AgriSetu server.\nPlease try again.",
                },
            ]);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        handleSend("");
    }, []);

    useEffect(() => {
        async function sendLocation() {
            if (session?.state !== "ASK_LOCATION") return;

            const location = await getCurrentLocation();

            handleSend(location);
        }

        sendLocation();
    }, [session]);

    return (
        <div className="h-screen flex flex-col">
            <Header />
            <ChatContainer
                messages={messages}
                retailers={session?.last_results ?? []}
                showRetailers={session?.state === "POST_RESULTS"}
            />
            <ChatInput onSend={handleSend} disabled={loading} />
            <SessionDebug session={session} />
        </div>
    );
}
