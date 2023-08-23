const fs = require('fs');
const xlsx = require('xlsx');

// Giriş ve çıkış dosya adları
const input_file = 'input.xlsx';
const output_file = 'output.xlsx';

// Giriş Excel dosyasını aç
const input_workbook = xlsx.readFile(input_file);
const input_sheet = input_workbook.Sheets[input_workbook.SheetNames[0]];

// Çıktı verilerini tutacak dizi
const output_data = [];

// Tüm hücreleri gez ve verileri JSON olarak yükle
for (const cellAddress in input_sheet) {
    if (!input_sheet.hasOwnProperty(cellAddress)) continue;
    
    const cell = input_sheet[cellAddress];
    const value = cell.v;
    
    if (value) {
        try {
            const data = JSON.parse('{' + value + '}'); // JSON olarak yükle
            if (typeof data === 'object' && data !== null) {
                for (const key in data) {
                    output_data.push([key.trim()]); // Sadece sol tarafları al
                }
            }
        } catch (error) {
            // Hatalı JSON geç, devam et
        }
    }
}

// Yeni bir Excel dosyası oluştur ve verileri yaz
const output_workbook = xlsx.utils.book_new();
const output_sheet = xlsx.utils.aoa_to_sheet(output_data);
xlsx.utils.book_append_sheet(output_workbook, output_sheet, 'Sheet1');

// Çıkış Excel dosyasını kaydet
xlsx.writeFile(output_workbook, output_file);

console.log('İşlem tamamlandı.');
