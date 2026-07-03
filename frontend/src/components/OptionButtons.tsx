interface Props {
    options: string[];
    onSelect: (value: string) => void;
}

export default function OptionButtons({ options, onSelect }: Props) {
    if (!options.length) return null;

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
        </div>
    );
}
