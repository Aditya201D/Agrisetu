import { useEffect, useState } from "react";

import { getConversations } from "../api/history";

import type { Conversation } from "../types/chat";

interface Props {
    activeConversationId: number | null;
    onSelect: (conversationId: number) => void;
    onNewChat: () => void;
    refreshTrigger: number;
}

export default function ConversationSidebar({ activeConversationId, onSelect, onNewChat, refreshTrigger }: Props) {
    const [conversations, setConversations] = useState<Conversation[]>([]);

    async function loadConversations() {
        try {
            const data = await getConversations();

            setConversations(data);
        } catch (err) {
            console.error(err);
        }
    }

    useEffect(() => {
        loadConversations();
    }, [refreshTrigger]);

    return (
        <aside className="w-80 bg-white border-r shadow-sm flex flex-col">
            <div className="border-b p-5">
                <button
                    onClick={onNewChat}
                    className="w-full rounded-xl bg-green-700 py-3 font-semibold text-white
                    shadow hover:bg-green-800 transition"
                >
                    ＋ New Conversation
                </button>
            </div>

            <div className="px-5 pt-4">
                <h2 className="text-sm font-semibold uppercase tracking-wider text-gray-500">Conversation History</h2>
            </div>

            <div className="flex-1 overflow-y-auto p-4 space-y-3">
                {conversations.length === 0 && (
                    <div className="text-center text-sm text-gray-500 mt-8">No conversations yet.</div>
                )}

                {conversations.map(conversation => (
                    <button
                        key={conversation.id}
                        onClick={() => onSelect(conversation.id)}
                        className={`
                        w-full
                        rounded-xl
                        border
                        p-4
                        text-left
                        transition
                        hover:border-green-500
                        hover:shadow-md
                        ${
                            activeConversationId === conversation.id
                                ? "border-green-600 bg-green-50 shadow"
                                : "border-gray-200 bg-white"
                        }

                        `}
                    >
                        <div className="font-semibold text-gray-800 truncate">{conversation.title}</div>

                        <div className="mt-2 text-xs text-gray-500">
                            {new Date(conversation.updated_at).toLocaleString()}
                        </div>
                    </button>
                ))}
            </div>
        </aside>
    );
}
