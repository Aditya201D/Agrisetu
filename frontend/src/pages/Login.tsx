import { useState } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Login() {
    const navigate = useNavigate();
    const { login, user } = useAuth();

    const [identifier, setIdentifier] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    if (user) {
        return <Navigate to="/" replace />;
    }

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        setError("");

        const success = await login(identifier, password);

        if (success) {
            navigate("/");
        } else {
            setError("Invalid username/email or password.");
        }
    }

    return (
        <div className="min-h-screen bg-linear-to-br from-green-50 via-white to-gray-100 flex items-center justify-center px-6">
            <div className="w-full max-w-110">
                <div className="text-center mb-8">
                    <div className="text-5xl mb-3">🌱</div>

                    <h1 className="text-4xl font-bold text-green-800">AgriSetu</h1>

                    <p className="mt-2 text-gray-600">Fertilizer Availability Assistant</p>

                    <p className="text-sm text-gray-500 mt-1">Government Fertilizer Retailer Search Portal</p>
                </div>

                <form onSubmit={handleSubmit} className="bg-white border border-gray-200 rounded-2xl shadow-xl p-8">
                    <h2 className="text-2xl font-semibold text-center text-gray-800 mb-6">Login</h2>

                    <div className="space-y-5">
                        <input
                            className="w-full rounded-xl border border-gray-300 px-4 py-3
                            focus:outline-none focus:ring-2 focus:ring-green-600
                            focus:border-green-600 transition"
                            placeholder="Username or Email"
                            value={identifier}
                            onChange={e => setIdentifier(e.target.value)}
                        />

                        <input
                            className="w-full rounded-xl border border-gray-300 px-4 py-3
                            focus:outline-none focus:ring-2 focus:ring-green-600
                            focus:border-green-600 transition"
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={e => setPassword(e.target.value)}
                        />
                    </div>

                    {error && (
                        <div className="mt-5 rounded-lg bg-red-50 border border-red-200 px-4 py-3 text-sm text-red-700">
                            {error}
                        </div>
                    )}

                    <button
                        className="mt-6 w-full rounded-xl bg-green-700 py-3 text-white
                        font-semibold hover:bg-green-800 transition shadow-sm"
                    >
                        Login
                    </button>

                    <p className="mt-6 text-center text-gray-600">
                        Don't have an account?{" "}
                        <Link to="/register" className="font-medium text-green-700 hover:underline">
                            Register
                        </Link>
                    </p>
                </form>

                <p className="text-center text-xs text-gray-500 mt-6">© Government Fertilizer Availability Platform</p>
            </div>
        </div>
    );
}
