import type { Message as MessageType } from "../types/chat";

interface Props {
    message: MessageType;
}

export default function Message({ message }: Props) {
    const isUser = message.sender === "user";

    return (
        <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
            <div
                className={`max-w-[78%] rounded-2xl px-5 py-4 shadow-sm whitespace-pre-wrap

                ${
                    isUser
                        ? "bg-green-700 text-white rounded-br-md"
                        : "bg-white border border-gray-200 text-gray-800 rounded-bl-md"
                }`}
            >
                <div
                    className={`mb-2 text-xs font-semibold uppercase tracking-wide

                    ${isUser ? "text-green-100" : "text-green-700"}`}
                >
                    {isUser ? "You" : "AgriSetu"}
                </div>

                <div className="leading-7">{message.text}</div>
            </div>
        </div>
    );
}
