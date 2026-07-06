import { useEffect, useRef } from "react";

import type { Message as MessageType, Retailer } from "../types/chat";

import Message from "./Message";
import RetailerTable from "./RetailerTable";

interface Props {
    messages: MessageType[];

    retailers: Retailer[];

    showRetailers: boolean;
}

export default function ChatContainer({
    messages,

    retailers,

    showRetailers,
}: Props) {
    const bottomRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages, retailers]);

    return (
        <div
            className="rounded-2xl border bg-linear-to-b from-gray-50 to-white
shadow-inner p-6 h-[68vh] overflow-y-auto space-y-5"
        >
            {messages.length === 0 && (
                <div className="flex h-full flex-col items-center justify-center text-center py-20">
                    <div className="mb-6 text-6xl">🌾</div>

                    <h2 className="text-2xl font-bold text-green-800">Welcome to AgriSetu</h2>

                    <p className="mt-3 max-w-lg text-gray-600 leading-7">
                        Search fertilizer retailers by district or nearby location. Start by selecting one of the quick
                        actions below or type your request.
                    </p>
                </div>
            )}
            {messages.map((msg, index) => (
                <Message key={index} message={msg} />
            ))}

            <RetailerTable retailers={retailers} visible={showRetailers} />

            <div ref={bottomRef} />
        </div>
    );
}
