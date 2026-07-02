from dogs_simple import bussi_total_dailys, mila_total_dailys

print("=== Dog Walk Comparison: Bussi vs Mila ===\n")

avg_bussi = sum(bussi_total_dailys) / len(bussi_total_dailys)
avg_mila  = sum(mila_total_dailys) / len(mila_total_dailys)

total_bussi = sum(bussi_total_dailys)
total_mila  = sum(mila_total_dailys)

print(f"Total minutes:     Bussi {total_bussi:3d}  |  Mila {total_mila:3d}")
print(f"Daily avg:         Bussi {avg_bussi:.1f}  |  Mila {avg_mila:.1f}")
print(f"Max day:           Bussi {max(bussi_total_dailys):3d}  |  Mila {max(mila_total_dailys):3d}")
print(f"Min day:           Bussi {min(bussi_total_dailys):3d}  |  Mila {min(mila_total_dailys):3d}")

print("\nDay-by-day (Bussi | Mila | Diff)")
for i, (b, m) in enumerate(zip(bussi_total_dailys, mila_total_dailys), 1):
    diff = b - m
    print(f"  {i}:  {b:3d}  |  {m:3d}  |  {diff:+3d}")

bussi_wins = sum(b > m for b, m in zip(bussi_total_dailys, mila_total_dailys))
mila_wins  = sum(m > b for b, m in zip(bussi_total_dailys, mila_total_dailys))
ties = len(bussi_total_dailys) - bussi_wins - mila_wins

print(f"\nBussi walked more: {bussi_wins} day(s)")
print(f"Mila walked more:  {mila_wins} day(s)")
print(f"Ties:              {ties} day(s)")
