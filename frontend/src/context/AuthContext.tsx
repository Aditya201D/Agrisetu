import { createContext, useContext, useEffect, useState, type ReactNode } from "react";

import { login as apiLogin, register as apiRegister, verifyToken } from "../api/auth";

interface User {
    id: number;
    username: string;
    email: string;
}

interface AuthContextType {
    user: User | null;
    loading: boolean;
    login: (identifier: string, password: string) => Promise<boolean>;
    register: (username: string, email: string, password: string) => Promise<boolean>;
    logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        restoreSession();
    }, []);

    async function restoreSession() {
        const token = localStorage.getItem("access_token");

        if (!token) {
            setLoading(false);
            return;
        }

        try {
            const result = await verifyToken(token);

            if (result.valid) {
                setUser(result.user);
            } else {
                localStorage.removeItem("access_token");
            }
        } catch {
            localStorage.removeItem("access_token");
        }

        setLoading(false);
    }

    async function login(identifier: string, password: string) {
        try {
            const result = await apiLogin(identifier, password);

            if (!result.success) {
                return false;
            }

            localStorage.setItem("access_token", result.access_token);

            setUser(result.user);

            return true;
        } catch {
            return false;
        }
    }

    async function register(username: string, email: string, password: string) {
        try {
            const result = await apiRegister(username, email, password);

            return result.success;
        } catch {
            return false;
        }
    }

    function logout() {
        localStorage.removeItem("access_token");
        setUser(null);
    }

    return (
        <AuthContext.Provider
            value={{
                user,
                loading,
                login,
                register,
                logout,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);

    if (!context) {
        throw new Error("useAuth must be used inside AuthProvider");
    }

    return context;
}
