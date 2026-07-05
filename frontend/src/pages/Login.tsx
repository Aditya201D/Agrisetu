import { useState } from "react";
import { Link, Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

import { useNavigate } from "react-router-dom";

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
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
            <form onSubmit={handleSubmit} className="bg-white shadow rounded-xl p-8 w-96">
                <h1 className="text-2xl font-bold mb-6 text-center">Login</h1>

                <input
                    className="border rounded w-full p-2 mb-4"
                    placeholder="Username or Email"
                    value={identifier}
                    onChange={e => setIdentifier(e.target.value)}
                />

                <input
                    className="border rounded w-full p-2 mb-4"
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                />

                {error && <p className="text-red-500 mb-4">{error}</p>}

                <button className="w-full bg-green-600 text-white rounded p-2">Login</button>

                <p className="mt-4 text-center">
                    Don't have an account?{" "}
                    <Link to="/register" className="text-green-700">
                        Register
                    </Link>
                </p>
            </form>
        </div>
    );
}
