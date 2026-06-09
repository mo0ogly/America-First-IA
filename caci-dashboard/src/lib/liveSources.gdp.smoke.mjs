// Manual smoke check (needs open network). Not part of CI.
// Mirrors the production wbFetchAll URL form (country/all, mrnev, per_page=400).
const WB = 'https://api.worldbank.org/v2';
const res = await fetch(`${WB}/country/all/indicator/NY.GDP.MKTP.CD?format=json&mrnev=1&per_page=400`);
const d = await res.json();
const usa = d[1].find((r) => r.countryiso3code === 'USA');
if (!usa) throw new Error('USA row not found');
const v = usa.value / 1e12;
console.log('USA GDP (trillions):', v.toFixed(2), 'year', usa.date, '| rows:', d[1].length);
if (!(v > 20 && v < 40)) throw new Error('USA GDP out of expected range');
console.log('OK');
