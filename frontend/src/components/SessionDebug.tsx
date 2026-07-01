import type { Session } from "../types/chat";

interface Props {
    session: Session | null;
}

export default function SessionDebug({ session }: Props) {
    if (!session) return null;

    return <pre className="bg-gray-100 text-xs p-4 overflow-auto border-t">{JSON.stringify(session, null, 2)}</pre>;
}
