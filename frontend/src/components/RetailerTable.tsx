import type { Retailer } from "../types/chat";

interface Props {
    retailers: Retailer[];
    visible: boolean;
}

export default function RetailerTable({ retailers, visible }: Props) {
    if (!visible || retailers.length === 0) {
        return null;
    }

    const groupedRetailers = Array.from(
        retailers
            .reduce((map, retailer) => {
                if (!map.has(retailer.retailer_id)) {
                    map.set(retailer.retailer_id, {
                        retailer_id: retailer.retailer_id,
                        agency_name: retailer.agency_name,
                        latitude: retailer.latitude,
                        longitude: retailer.longitude,
                        distance: retailer.distance,
                        products: [],
                    });
                }

                map.get(retailer.retailer_id).products.push({
                    product_name: retailer.product_name,
                    quantity: retailer.quantity,
                });

                return map;
            }, new Map<number, any>())
            .values(),
    );

    return (
        <div className="mx-4 mb-4 overflow-hidden rounded-lg border bg-white shadow">
            <div className="bg-green-700 px-4 py-3 font-semibold text-white">Retailers Found ({retailers.length})</div>

            <table className="w-full text-sm">
                <thead className="bg-gray-100">
                    <tr>
                        <th className="text-left p-3">Agency</th>
                        <th className="text-left p-3">Available Products</th>
                        <th className="p-3 text-center">Distance</th>
                        <th className="text-center p-3">Map</th>
                    </tr>
                </thead>

                <tbody>
                    {groupedRetailers.map(retailer => (
                        <tr key={retailer.retailer_id} className="border-t align-top">
                            <td className="p-3 font-medium">{retailer.agency_name}</td>

                            <td className="p-3">
                                {retailer.products.map((p: any) => (
                                    <div key={p.product_name}>
                                        {p.product_name} ({p.quantity})
                                    </div>
                                ))}
                            </td>

                            <td className="text-center p-3">
                                {retailer.distance != null ? `${retailer.distance.toFixed(2)} km` : "-"}
                            </td>

                            <td className="p-3 text-center">
                                <a
                                    href={`https://www.google.com/maps?q=${retailer.latitude},${retailer.longitude}`}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="text-green-700 hover:underline"
                                >
                                    View
                                </a>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
