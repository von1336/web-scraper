import csv
import json
from pathlib import Path

class Exporter:
    """Сохраняет данные в разные форматы"""

    def save(self, data, output, fmt):
        Path("exports").mkdir(exist_ok=True)
        path = Path("exports") / f"{output}.{fmt}"

        if fmt == "json":
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        elif fmt == "csv":
            if not data:
                return path
            with open(path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        elif fmt == "xlsx":
            try:
                import openpyxl
            except ImportError:
                raise RuntimeError("Для xlsx установи openpyxl: pip install openpyxl")
            wb = openpyxl.Workbook()
            ws = wb.active
            if data:
                ws.append(list(data[0].keys()))
                for row in data:
                    ws.append(list(row.values()))
            wb.save(path)
        else:
            raise ValueError(f"Неизвестный формат: {fmt}")

        return path
