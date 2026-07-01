import { useEffect, useState } from "react";

import ChatContainer from "./components/ChatContainer";
import ChatInput from "./components/ChatInput";
import Header from "./components/Header";
import SessionDebug from "./components/SessionDebug";

import { sendMessage } from "./api/chat";

import type { Message, Session } from "./types/chat";

export default function App() {
    const USER_ID = "user1";

    const [messages, setMessages] = useState<Message[]>([]);
    const [session, setSession] = useState<Session | null>(null);

    async function handleSend(text: string) {
        if (text.trim() !== "") {
            setMessages(prev => [
                ...prev,
                {
                    sender: "user",
                    text,
                },
            ]);
        }

        console.log("Sending:", text);
        const response = await sendMessage(USER_ID, text);
        console.log("Received:", response);

        if (response.reply.trim() !== "") {
            setMessages(prev => [
                ...prev,
                {
                    sender: "bot",
                    text: response.reply,
                },
            ]);
        }

        setSession(response.session);
    }

    useEffect(() => {
        console.log("App mounted");
        handleSend("");
    }, []);

    return (
        <div className="h-screen flex flex-col">
            <Header />

            <ChatContainer messages={messages} />

            <ChatInput onSend={handleSend} />

            <SessionDebug session={session} />
        </div>
    );
}
