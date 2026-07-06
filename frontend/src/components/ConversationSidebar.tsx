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
        <aside className="w-72 border-r bg-gray-50 flex flex-col">
            <div className="p-4 border-b">
                <button
                    onClick={onNewChat}
                    className="w-full rounded bg-green-600 px-4 py-2 text-white hover:bg-green-700"
                >
                    + New Chat
                </button>
            </div>

            <div className="flex-1 overflow-y-auto">
                {conversations.map(conversation => (
                    <button
                        key={conversation.id}
                        onClick={() => onSelect(conversation.id)}
                        className={`w-full text-left px-4 py-3 border-b hover:bg-gray-100 ${
                            activeConversationId === conversation.id ? "bg-green-100" : ""
                        }`}
                    >
                        <div className="font-medium">{conversation.title}</div>

                        <div className="text-xs text-gray-500">
                            {new Date(conversation.updated_at).toLocaleString()}
                        </div>
                    </button>
                ))}
            </div>
        </aside>
    );
}
