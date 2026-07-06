import { useState } from "react";

interface Props {
    onSend: (message: string) => void;

    loading?: boolean;
}

export default function ChatInput({
    onSend,

    loading = false,
}: Props) {
    const [text, setText] = useState("");

    function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        if (!text.trim()) return;

        onSend(text);

        setText("");
    }

    return (
        <form onSubmit={handleSubmit} className="mt-5 flex gap-3">
            <input
                disabled={loading}
                className="flex-1 rounded-xl border border-gray-300 bg-white
                px-5 py-4 shadow-sm transition
                focus:border-green-600
                focus:ring-2
                focus:ring-green-200
                focus:outline-none"
                placeholder="Ask about fertilizer retailers..."
                value={text}
                onChange={e => setText(e.target.value)}
            />

            <button
                disabled={loading}
                className="rounded-xl bg-green-700 px-8
                font-semibold text-white
                transition
                hover:bg-green-800
                disabled:bg-green-400"
            >
                {loading ? "..." : "Send"}
            </button>
        </form>
    );
}
