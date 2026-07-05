interface Props {
    options: string[];
    onSelect: (value: string) => void;
    showLocationButton?: boolean;
    onCurrentLocation?: () => void;
}

export default function OptionButtons({ options, onSelect, showLocationButton = false, onCurrentLocation }: Props) {
    if (!options.length && !showLocationButton) return null;

    return (
        <div className="flex flex-wrap gap-2 mt-2">
            {options.map(option => (
                <button
                    key={option}
                    onClick={() => onSelect(option)}
                    className="px-4 py-2 rounded-full bg-green-600 text-white hover:bg-green-700"
                >
                    {option}
                </button>
            ))}

            {showLocationButton && (
                <button
                    onClick={onCurrentLocation}
                    className="px-4 py-2 rounded-full bg-blue-600 text-white hover:bg-blue-700"
                >
                    📍 Use Current Location
                </button>
            )}
        </div>
    );
}
