import { useState } from "react";

interface Props {
    onSend: (message: string) => void;
    disabled?: boolean;
}

export default function ChatInput({ onSend, disabled = false }: Props) {
    const [text, setText] = useState("");

    function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        if (!text.trim()) return;

        onSend(text);

        setText("");
    }

    return (
        <form onSubmit={handleSubmit} className="flex gap-3 p-4 border-t">
            <input
                disabled={disabled}
                className="flex-1 border rounded-lg px-4 py-3"
                placeholder="Type your message..."
                value={text}
                onChange={e => setText(e.target.value)}
            />

            <button disabled={disabled} className="bg-green-700 text-white px-6 rounded-lg">
                {disabled ? "..." : "Send"}
            </button>
        </form>
    );
}
