const fs = require('fs');
const xlsx = require('xlsx');

// Giriş ve çıkış dosya adları
const input_file = 'input.xlsx';
const output_file = 'output_list.txt';

// Giriş Excel dosyasını aç
const input_workbook = xlsx.readFile(input_file);
const input_sheet = input_workbook.Sheets[input_workbook.SheetNames[0]];

// Çıktı verilerini tutacak dizi
const output_data = []; // Using an array to store the keys

// Tüm hücreleri gez ve verileri JSON olarak yükle
for (const cellAddress in input_sheet) {
    if (!input_sheet.hasOwnProperty(cellAddress)) continue;

    const cell = input_sheet[cellAddress];
    const value = cell.v;

    if (value && typeof value === 'string') {
        const regex = /"([^"]+)":/g; // Match key names between quotes
        let match;
        while ((match = regex.exec(value)) !== null) {
            output_data.push(`'"${match[1]}"'`); // Add key with double quotes
        }
    }
}

// Oluşturulan verileri Python list formatına dönüştür
const python_list = '[' + output_data.join(', ') + ']';

// Python list formatını dosyaya yaz
fs.writeFileSync(output_file, python_list);

console.log('İşlem tamamlandı.');
