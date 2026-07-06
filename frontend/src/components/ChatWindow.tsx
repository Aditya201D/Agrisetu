import { useEffect, useState } from "react";

import { sendMessage } from "../api/chat";
import { getHistory } from "../api/history";
import { getCurrentLocation } from "../services/geolocation";

import ChatContainer from "./ChatContainer";
import ChatInput from "./ChatInput";
import OptionButtons from "./OptionButtons";
import SessionDebug from "./SessionDebug";

import type { Message, Session } from "../types/chat";

export default function ChatWindow() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [session, setSession] = useState<Session | null>(null);
    const [loading, setLoading] = useState(false);
    const [options, setOptions] = useState<string[]>([]);

    async function handleSend(text: string) {
        setOptions([]);
        if (loading) return;

        if (text.trim()) {
            setMessages(prev => [
                ...prev,
                {
                    sender: "user",
                    text,
                },
            ]);
        }

        setLoading(true);

        try {
            const response = await sendMessage(text);

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
        async function initialize() {
            try {
                const history = await getHistory();

                if (history.length > 0) {
                    setMessages(history);

                    // Fetch the current session state without adding a visible message.
                    const response = await sendMessage("");

                    setSession(response.session);
                    setOptions(response.options);
                } else {
                    await handleSend("");
                }
            } catch (error) {
                console.error(error);

                // Fall back to normal initialization.
                await handleSend("");
            }
        }

        initialize();
    }, []);

    return (
        <main className="flex-1 overflow-y-auto p-6">
            <div className="max-w-4xl mx-auto">
                <>
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
                </>
            </div>
        </main>
    );
}
