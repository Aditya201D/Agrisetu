import ChatWindow from "../components/ChatWindow";
import Header from "../components/Header";

export default function ChatPage() {
    return (
        <div className="h-screen flex flex-col">
            <Header />
            <ChatWindow />
        </div>
    );
}
