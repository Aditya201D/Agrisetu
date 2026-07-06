import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Header() {
    const { user, logout } = useAuth();
    const navigate = useNavigate();

    return (
        <header className="bg-white border-b shadow-sm">
            <div className="flex items-center justify-between px-8 py-4">
                <div className="flex items-center gap-4">
                    <div className="flex h-14 w-14 items-center justify-center rounded-full bg-green-100 text-3xl">
                        🌾
                    </div>

                    <div>
                        <h1 className="text-2xl font-bold text-green-800">AgriSetu</h1>

                        <p className="text-sm text-gray-600">Fertilizer Availability Assistant</p>
                    </div>
                </div>

                <div className="flex items-center gap-6">
                    <div className="text-right">
                        <p className="text-xs uppercase tracking-wide text-gray-500">Logged in as</p>

                        <p className="font-semibold text-gray-800">{user?.username}</p>
                    </div>

                    <button
                        onClick={() => {
                            logout();
                            navigate("/login");
                        }}
                        className="rounded-lg bg-red-600 px-5 py-2.5 text-white
                        transition hover:bg-red-700"
                    >
                        Logout
                    </button>
                </div>
            </div>
        </header>
    );
}
