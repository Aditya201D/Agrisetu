import type { Message as MessageType } from "../types/chat";

interface Props {
    message: MessageType;
}

export default function Message({ message }: Props) {
    const isUser = message.sender === "user";

    return (
        <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
            <div
                className={`max-w-[70%] rounded-xl px-4 py-3 whitespace-pre-wrap
                ${isUser ? "bg-green-700 text-white" : "bg-gray-200"}`}
            >
                {message.text}
            </div>
        </div>
    );
}
