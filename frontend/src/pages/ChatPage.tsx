import { useState } from "react";

import ChatWindow from "../components/ChatWindow";
import ConversationSidebar from "../components/ConversationSidebar";
import Header from "../components/Header";

export default function ChatPage() {
    const [selectedConversationId, setSelectedConversationId] = useState<number | null>(null);
    const [newChatTrigger, setNewChatTrigger] = useState(0);
    const [sidebarRefresh, setSidebarRefresh] = useState(0);

    function handleConversationSelect(conversationId: number) {
        setSelectedConversationId(conversationId);
    }

    function handleNewChat() {
        setSelectedConversationId(null);
        setNewChatTrigger(prev => prev + 1);
        setSidebarRefresh(prev => prev + 1);
    }

    return (
        <div className="flex h-screen">
            <ConversationSidebar
                activeConversationId={selectedConversationId}
                onSelect={handleConversationSelect}
                onNewChat={handleNewChat}
                refreshTrigger={sidebarRefresh}
            />

            <div className="flex flex-col flex-1">
                <Header />

                <ChatWindow selectedConversationId={selectedConversationId} newChatTrigger={newChatTrigger} />
            </div>
        </div>
    );
}
