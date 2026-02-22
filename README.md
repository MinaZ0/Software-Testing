# HackerRank Algorithms & Unit Testing Assignment

งานนี้เป็นการนำเสนอการแก้โจทย์ Algorithm จาก HackerRank จำนวน 5 ข้อ โดยเน้นความถูกต้องของ Logic การทำ Unit Testing ให้ได้ Coverage 100% และการรักษาประวัติการทำงานด้วย Git (Commit Early, Commit Often)

## ข้อมูลผู้จัดทำ
- **ชื่อ-นามสกุล:** เอกนฤน ฟองสุวรรณ (Guy)
- **รหัสนักศึกษา:** 6810110433
- **สาขา:** AI Engineering, มหาวิทยาลัยสงขลานครินทร์

## โจทย์ที่ดำเนินการ (HackerRank)
1. **Funny String**: วิเคราะห์ค่าความต่าง ASCII ของสตริงปกติและสตริงย้อนกลับ
2. **Alternating Characters**: นับจำนวนตัวอักษรที่ต้องลบเพื่อให้ตัวอักษรที่ติดกันไม่ซ้ำกัน
3. **Caesar Cipher**: การเข้ารหัสด้วยการเลื่อนตำแหน่งตัวอักษร (Shift Cipher)
4. **Two Characters**: หาความยาวที่มากที่สุดของสตริงที่ประกอบด้วยตัวอักษร 2 ชนิดสลับกัน
5. **Grid Challenge**: ตรวจสอบการเรียงลำดับตัวอักษรใน Grid ทั้งแนวแถวและแนวคอลัมน์

## การทดสอบ (Testing & Coverage)
โปรเจกต์นี้ใช้ `unittest` และ `coverage.py` ในการทดสอบเพื่อให้มั่นใจว่า Algorithm ทำงานได้อย่างถูกต้องและครอบคลุมทุกเงื่อนไข (Test coverage 100%)

### วิธีการรัน Test
```bash
python -m unittest discover tests