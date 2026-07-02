import type { Retailer } from "../types/chat";

interface Props {
    retailers: Retailer[];
    visible: boolean;
}

export default function RetailerTable({ retailers, visible }: Props) {
    if (!visible || retailers.length === 0) {
        return null;
    }

    return (
        <div className="mx-4 mb-4 overflow-hidden rounded-lg border bg-white shadow">
            <div className="bg-green-700 px-4 py-3 font-semibold text-white">Retailers Found ({retailers.length})</div>

            <table className="w-full text-sm">
                <thead className="bg-gray-100">
                    <tr>
                        <th className="p-3 text-left">Agency</th>
                        <th className="p-3 text-left">Product</th>
                        <th className="p-3 text-center">Quantity</th>
                    </tr>
                </thead>

                <tbody>
                    {retailers.map(retailer => (
                        <tr key={retailer.retailer_id} className="border-t">
                            <td className="p-3">{retailer.agency_name}</td>

                            <td className="p-3">{retailer.product_name}</td>

                            <td className="p-3 text-center">{retailer.quantity}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
