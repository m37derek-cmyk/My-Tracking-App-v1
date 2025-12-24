import json

# هذا الكود سيحول ملف مفاتيحك إلى الصيغة التي يطلبها الموقع
with open("credentials.json", "r") as f:
    data = json.load(f)

print("[google_credentials]")
for key, value in data.items():
    # تنظيف القيم لتناسب الصيغة الجديدة
    value = value.replace("\n", "\\n")
    print(f'{key} = "{value}"')