import { useEffect, useRef } from "react";

import type { Message as MessageType, Retailer } from "../types/chat";

import Message from "./Message";
import RetailerTable from "./RetailerTable";

interface Props {
    messages: MessageType[];
    retailers: Retailer[];
    showRetailers: boolean;
}

export default function ChatContainer({ messages, retailers, showRetailers }: Props) {
    const bottomRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages, retailers]);

    return (
        <div className="flex-1 overflow-y-auto p-5 space-y-4">
            {messages.map((msg, index) => (
                <Message key={index} message={msg} />
            ))}

            <RetailerTable retailers={retailers} visible={showRetailers} />

            <div ref={bottomRef} />
        </div>
    );
}
