interface Props {
    options: string[];
    onSelect: (option: string) => void;
    showLocationButton?: boolean;
    onCurrentLocation?: () => void;
}

export default function OptionButtons({ options, onSelect, showLocationButton = false, onCurrentLocation }: Props) {
    if (options.length === 0 && !showLocationButton) {
        return null;
    }

    return (
        <div className="mt-5">
            <div className="mb-3 text-sm font-semibold uppercase tracking-wide text-gray-500">Quick Actions</div>

            <div className="flex flex-wrap gap-3">
                {options.map(option => (
                    <button
                        key={option}
                        onClick={() => onSelect(option)}
                        className="rounded-xl border border-green-200 bg-white px-5 py-3
                        text-green-800 font-medium shadow-sm
                        transition-all
                        hover:bg-green-700
                        hover:text-white
                        hover:shadow-md"
                    >
                        {option}
                    </button>
                ))}

                {showLocationButton && (
                    <button
                        onClick={onCurrentLocation}
                        className="rounded-xl bg-blue-600 px-5 py-3 font-medium
                        text-white shadow-sm transition
                        hover:bg-blue-700"
                    >
                        📍 Use Current Location
                    </button>
                )}
            </div>
        </div>
    );
}
