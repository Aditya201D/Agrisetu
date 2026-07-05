import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Header() {
    const { user, logout } = useAuth();
    const navigate = useNavigate();

    return (
        <header className="bg-green-700 text-white px-6 py-4 shadow flex justify-between items-center">
            <div>
                <h1 className="text-2xl font-bold">AgriSetu</h1>

                <p className="text-sm opacity-90">Fertilizer Availability Assistant</p>
            </div>

            <div className="flex items-center gap-4">
                <span className="text-sm">{user?.username}</span>

                <button
                    onClick={() => {
                        logout();
                        navigate("/login");
                    }}
                    className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded"
                >
                    Logout
                </button>
            </div>
        </header>
    );
}
