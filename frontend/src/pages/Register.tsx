import { useState } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const navigate = useNavigate();

export default function Register() {
    const { register, user } = useAuth();

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [message, setMessage] = useState("");

    if (user) {
        return <Navigate to="/" replace />;
    }

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        const success = await register(username, email, password);

        if (success) {
            navigate("/login");
        } else {
            setMessage("Registration failed.");
        }
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
            <form onSubmit={handleSubmit} className="bg-white shadow rounded-xl p-8 w-96">
                <h1 className="text-2xl font-bold mb-6 text-center">Register</h1>

                <input
                    className="border rounded w-full p-2 mb-4"
                    placeholder="Username"
                    value={username}
                    onChange={e => setUsername(e.target.value)}
                />

                <input
                    className="border rounded w-full p-2 mb-4"
                    placeholder="Email"
                    value={email}
                    onChange={e => setEmail(e.target.value)}
                />

                <input
                    className="border rounded w-full p-2 mb-4"
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                />

                {message && <p className="mb-4">{message}</p>}

                <button className="w-full bg-green-600 text-white rounded p-2">Register</button>

                <p className="mt-4 text-center">
                    Already have an account?{" "}
                    <Link to="/login" className="text-green-700">
                        Login
                    </Link>
                </p>
            </form>
        </div>
    );
}
