import { useEffect, useState } from "react";

import ChatContainer from "./components/ChatContainer";
import ChatInput from "./components/ChatInput";
import Header from "./components/Header";
import OptionButtons from "./components/OptionButtons";
import SessionDebug from "./components/SessionDebug";

import { sendMessage } from "./api/chat";

import type { Message, Session } from "./types/chat";

import { getCurrentLocation } from "./services/geolocation";

export default function App() {
    const USER_ID = "user1";

    const [messages, setMessages] = useState<Message[]>([]);
    const [session, setSession] = useState<Session | null>(null);
    const [loading, setLoading] = useState(false);
    const [options, setOptions] = useState<string[]>([]);

    async function handleSend(text: string) {
        setOptions([]);
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
            setOptions(response.options);
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
            <OptionButtons options={options} onSelect={handleSend} />
            <ChatInput onSend={handleSend} disabled={loading} />
            <SessionDebug session={session} />
        </div>
    );
}
