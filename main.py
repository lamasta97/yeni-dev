const fs = require('fs');
const xlsx = require('xlsx');

// Giriş ve çıkış dosya adları
const input_file = 'input.xlsx';
const output_file = 'output.xlsx';

// Giriş Excel dosyasını aç
const input_workbook = xlsx.readFile(input_file);
const input_sheet = input_workbook.Sheets[input_workbook.SheetNames[0]];

// Çıktı verilerini tutacak dizi
const output_data = new Set(); // Using a Set to avoid duplicate keys

// Tüm hücreleri gez ve verileri JSON olarak yükle
for (const cellAddress in input_sheet) {
    if (!input_sheet.hasOwnProperty(cellAddress)) continue;

    const cell = input_sheet[cellAddress];
    const value = cell.v;

    if (value && typeof value === 'string') {
        const regex = /"([^"]+)":/g; // Match key names between quotes
        let match;
        while ((match = regex.exec(value)) !== null) {
            output_data.add(match[1]);
        }
    }
}

// Yeni bir Excel dosyası oluştur ve verileri yaz
const output_workbook = xlsx.utils.book_new();
const output_sheet_data = Array.from(output_data).map(data => [data]);
const output_sheet = xlsx.utils.aoa_to_sheet(output_sheet_data);
xlsx.utils.book_append_sheet(output_workbook, output_sheet, 'Sheet1');

// Çıkış Excel dosyasını kaydet
xlsx.writeFile(output_workbook, output_file);

console.log('İşlem tamamlandı.');
