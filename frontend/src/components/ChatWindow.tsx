import { useEffect, useState } from "react";

import { sendMessage } from "../api/chat";
import { getConversationHistory, getHistory, newConversation } from "../api/history";
import { getCurrentLocation } from "../services/geolocation";

import ChatContainer from "./ChatContainer";
import ChatInput from "./ChatInput";
import OptionButtons from "./OptionButtons";
import SessionDebug from "./SessionDebug";

import type { Message, Session } from "../types/chat";

interface Props {
    selectedConversationId: number | null;
    newChatTrigger: number;
}

export default function ChatWindow({ selectedConversationId, newChatTrigger }: Props) {
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

    async function initializeCurrentConversation() {
        try {
            const history = await getHistory();

            if (history.length > 0) {
                setMessages(history);

                const response = await sendMessage("");

                setSession(response.session);
                setOptions(response.options);
            } else {
                await handleSend("");
            }
        } catch (error) {
            console.error(error);
            await handleSend("");
        }
    }

    useEffect(() => {
        initializeCurrentConversation();
    }, []);

    // We'll activate this in the next step.
    useEffect(() => {
        async function loadConversation() {
            if (selectedConversationId === null) return;

            try {
                const history = await getConversationHistory(selectedConversationId);

                setMessages(history);

                const response = await sendMessage("");

                setSession(response.session);
                setOptions(response.options);
            } catch (err) {
                console.error(err);
            }
        }

        loadConversation();
    }, [selectedConversationId]);

    // We'll activate this in the next step.
    useEffect(() => {
        async function startNewChat() {
            if (newChatTrigger === 0) return;

            try {
                await newConversation();

                setMessages([]);
                setOptions([]);
                setSession(null);

                await handleSend("");
            } catch (err) {
                console.error(err);
            }
        }

        startNewChat();
    }, [newChatTrigger]);

    return (
        <main className="flex-1 overflow-y-auto p-6">
            <div className="max-w-4xl mx-auto">
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
        </main>
    );
}
