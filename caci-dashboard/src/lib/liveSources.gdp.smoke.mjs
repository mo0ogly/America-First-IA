// Manual smoke check (needs network). Not part of CI.
const WB = 'https://api.worldbank.org/v2';
const res = await fetch(`${WB}/country/USA/indicator/NY.GDP.MKTP.CD?format=json&mrnev=1&per_page=2`);
const d = await res.json();
const v = d[1][0].value / 1e12;
console.log('USA GDP (trillions):', v.toFixed(2), 'year', d[1][0].date);
if (!(v > 20 && v < 40)) throw new Error('USA GDP out of expected range');
console.log('OK');
