export interface Retailer {
    retailer_id: number;
    agency_name: string;
    product_name: string;
    quantity: number;
    latitude: number;
    longitude: number;
}

export interface Session {
    state: string;
    search_mode: string | null;
    district_name: string | null;
    latitude: number | null;
    longitude: number | null;
    radius_km: number | null;
    product_group: string | null;
    last_results: Retailer[] | null;
}

export interface ChatResponse {
    reply: string;
    session: Session;
}

export interface Message {
    sender: "user" | "bot";
    text: string;
}
