import type { Session } from "../types/chat";

interface Props {
    session: Session | null;
}

export default function SessionDebug({ session }: Props) {
    if (!session) return null;

    return (
        <div className="fixed bottom-24 right-4 w-80 max-h-96 overflow-auto rounded-lg border bg-white shadow-xl text-xs p-3">
            <h3 className="font-semibold mb-2">Session Debug</h3>

            <pre className="whitespace-pre-wrap">{JSON.stringify(session, null, 2)}</pre>
        </div>
    );
}
