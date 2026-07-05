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

    async function handleCurrentLocation() {
        try {
            setLoading(true);

            const location = await getCurrentLocation();

            await handleSend(location);
        } catch {
            setMessages(prev => [
                ...prev,
                {
                    sender: "bot",
                    text: "Unable to read your location. You can also enter coordinates manually.",
                },
            ]);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        handleSend("");
    }, []);

    return (
        <div className="h-screen flex flex-col">
            <Header />
            <ChatContainer
                messages={messages}
                retailers={session?.last_results ?? []}
                showRetailers={session?.state === "POST_RESULTS"}
            />
            <OptionButtons
                options={options}
                onSelect={handleSend}
                showLocationButton={session?.state === "ASK_LOCATION"}
                onCurrentLocation={handleCurrentLocation}
            />
            <ChatInput onSend={handleSend} loading={loading} />
            <SessionDebug session={session} />
        </div>
    );
}
