import fs from 'fs';

// Using the 2024 values we researched earlier directly to create a clean API.
// We verified that the Datahub CSV only goes up to 2020. 
// Thus, using our explicit 2024 WEO numbers to ensure transparency.
const gdp2024Data = {
    USA: 29.3,
    China: 18.7,
    EU: 18.9, // Estimated aggregate
    UK: 3.6,
    "Asia (Ex-China)": 13.5, // Estimated aggregate
    India: 3.9,
    France: 3.16,
    Germany: 4.68,
    "South America": 4.2, // Estimated aggregate
    Africa: 3.1, // Estimated aggregate
};

const csvContent = "Country,GDP_Trillions_USD\n" +
    Object.entries(gdp2024Data).map(([c, v]) => `${c.includes(',') || c.includes('(') ? '"' + c + '"' : c},${v}`).join("\n");

fs.writeFileSync('./public/data/gdp_data.csv', csvContent);
console.log("Created public/data/gdp_data.csv");
