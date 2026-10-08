import csv
import json
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import TypedDict

HERE = Path(__file__).resolve().parent


class Report(TypedDict):
    unique_orders: int
    duplicate_rows_skipped: int
    total_pln: str
    by_segment_pln: dict[str, str]


def read_rows(path: Path, required: set[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(
                f"{path.name}: missing columns {sorted(required - set(reader.fieldnames or []))}"
            )
        return list(reader)


def build_report(directory: Path) -> Report:
    customers = {
        row["customer_id"]: row["segment"]
        for row in read_rows(directory / "customers.csv", {"customer_id", "segment"})
    }
    totals: dict[str, Decimal] = defaultdict(Decimal)
    seen: set[str] = set()
    duplicate_count = 0
    for row in read_rows(
        directory / "orders.csv",
        {"order_id", "customer_id", "order_date", "amount_pln"},
    ):
        order_id = row["order_id"].strip()
        if not order_id:
            raise ValueError("order_id cannot be blank")
        if order_id in seen:
            duplicate_count += 1
            continue
        seen.add(order_id)
        customer_id = row["customer_id"].strip()
        if customer_id not in customers:
            raise ValueError(f"{order_id}: unknown customer {customer_id}")
        date.fromisoformat(row["order_date"])
        try:
            amount = Decimal(row["amount_pln"])
        except InvalidOperation as error:
            raise ValueError(f"{order_id}: invalid amount") from error
        if not amount.is_finite() or amount < 0:
            raise ValueError(f"{order_id}: amount must be nonnegative and finite")
        totals[customers[customer_id]] += amount
    return {
        "unique_orders": len(seen),
        "duplicate_rows_skipped": duplicate_count,
        "total_pln": str(sum(totals.values(), Decimal(0)).quantize(Decimal("0.01"))),
        "by_segment_pln": {
            segment: str(total.quantize(Decimal("0.01")))
            for segment, total in sorted(totals.items())
        },
    }


def write_report(report: Report, directory: Path) -> None:
    (directory / "output.json").write_text(json.dumps(report, indent=2) + "\n")
    with (directory / "report.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["customer_segment", "revenue_pln"])
        writer.writerows(report["by_segment_pln"].items())


if __name__ == "__main__":
    report = build_report(HERE)
    assert report["unique_orders"] == 4
    assert report["total_pln"] == "278.00"
    write_report(report, HERE)
    print(json.dumps(report, ensure_ascii=False, indent=2))
