export interface Session {
    state: string;
    search_mode: string | null;
    district_name: string | null;
    latitude: number | null;
    longitude: number | null;
    radius_km: number | null;
    product_group: string | null;
}

export interface ChatResponse {
    reply: string;
    session: Session;
}

export interface Message {
    sender: "user" | "bot";
    text: string;
}
