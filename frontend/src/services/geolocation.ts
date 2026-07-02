export function getCurrentLocation(): Promise<string> {
    return new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(position => {
            resolve(`${position.coords.latitude},${position.coords.longitude}`);
        }, reject);
    });
}
