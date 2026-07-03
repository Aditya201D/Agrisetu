import { useState } from "react";

interface Props {
    onSend: (message: string) => void;
    loading?: boolean;
}

export default function ChatInput({ onSend, loading = false }: Props) {
    const [text, setText] = useState("");

    function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        if (!text.trim()) return;

        if (text === "__location__") {
            return;
        }

        onSend(text);

        setText("");
    }

    return (
        <form onSubmit={handleSubmit} className="flex gap-3 p-4 border-t">
            <input
                disabled={loading}
                className="flex-1 border rounded-lg px-4 py-3"
                placeholder="Type your message..."
                value={text}
                onChange={e => setText(e.target.value)}
            />

            <button disabled={loading} className="bg-green-700 text-white px-6 rounded-lg">
                {loading ? "Searching..." : "Send"}
            </button>
        </form>
    );
}
