import { useEffect, useRef } from "react";
import type { Message as MessageType } from "../types/chat";
import Message from "./Message";

interface Props {
    messages: MessageType[];
}

export default function ChatContainer({ messages }: Props) {
    const bottomRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages]);

    return (
        <div className="flex-1 overflow-y-auto p-5 space-y-4">
            {messages.map((msg, index) => (
                <Message key={index} message={msg} />
            ))}

            <div ref={bottomRef} />
        </div>
    );
}
