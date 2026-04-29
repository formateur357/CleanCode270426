# def process(bases):
#     total = 0
#     for base in bases:
#         if base is None or base < 0:
#             raise ValueError("bad line")
#         total += base * 8 // 100
#     print("total=", total)
#     return total

from dataclasses import dataclass
from typing import Optional


CONTRIBUTION_RATE_PERCENT = 8

@dataclass(Frozen=True)
class ContributionLine:
    contribution_base: Optional[int]

@dataclass(Frozen=True)  
class BatchAnomaly:
    line_number: int
    reason: str

@dataclass(Frozen=True)  
class BatchProcessingReport:
    total_contribution: int
    processed_lines: int
    read_lines: int
    anomalies: list[BatchAnomaly]