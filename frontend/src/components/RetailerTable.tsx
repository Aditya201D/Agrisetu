import type { Retailer } from "../types/chat";

interface Props {
    retailers: Retailer[];

    visible: boolean;
}

export default function RetailerTable({
    retailers,

    visible,
}: Props) {
    if (!visible || retailers.length === 0) return null;

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
        <div className="overflow-hidden rounded-2xl border bg-white shadow-lg">
            <div className="flex items-center justify-between bg-green-700 px-6 py-4">
                <div>
                    <h2 className="text-lg font-semibold text-white">Retailers Found</h2>

                    <p className="text-sm text-green-100">{groupedRetailers.length} retailer(s)</p>
                </div>
            </div>

            <table className="w-full">
                <thead className="bg-green-50">
                    <tr className="text-sm uppercase tracking-wide text-gray-600">
                        <th className="px-5 py-4 text-left">Retailer</th>

                        <th className="px-5 py-4 text-left">Products</th>

                        <th className="px-5 py-4 text-center">Distance</th>

                        <th className="px-5 py-4 text-center">Maps</th>
                    </tr>
                </thead>

                <tbody>
                    {groupedRetailers.map(retailer => (
                        <tr key={retailer.retailer_id} className="border-t hover:bg-green-50 transition">
                            <td className="px-5 py-5 align-top">
                                <div className="font-semibold text-gray-800">{retailer.agency_name}</div>
                            </td>

                            <td className="px-5 py-5">
                                <div className="flex flex-wrap gap-2">
                                    {retailer.products.map((product: any) => (
                                        <span
                                            key={product.product_name}
                                            className="rounded-full bg-green-100
                                            px-3 py-1 text-sm text-green-800"
                                        >
                                            {product.product_name} ({product.quantity})
                                        </span>
                                    ))}
                                </div>
                            </td>

                            <td className="px-5 py-5 text-center">
                                {retailer.distance != null ? (
                                    <span className="rounded-full bg-blue-100 px-3 py-1 text-blue-700">
                                        {retailer.distance.toFixed(2)} km
                                    </span>
                                ) : (
                                    "-"
                                )}
                            </td>

                            <td className="px-5 py-5 text-center">
                                <a
                                    href={`https://www.google.com/maps?q=${retailer.latitude},${retailer.longitude}`}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="rounded-lg bg-green-700 px-4 py-2
                                    text-white transition
                                    hover:bg-green-800"
                                >
                                    View Map
                                </a>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
