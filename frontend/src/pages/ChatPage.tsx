import ChatWindow from "../components/ChatWindow.tsx";
import Header from "../components/Header.tsx";

export default function ChatPage() {
    return (
        <div className="h-screen flex flex-col bg-gray-100">
            <Header />
            <ChatWindow />
        </div>
    );
}
