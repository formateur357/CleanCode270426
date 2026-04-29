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

    total_contribution = 0
    processed_lines = 0
    read_lines = 0
    anomalies = []

    for i, line in enumerate(lines):
        read_lines += 1
        if line.contribution_base is None or line.contribution_base < 0:
            anomalies.append(BatchAnomaly(i + 1, "base negative"))
        else:
            total_contribution += line.contribution_base * CONTRIBUTION_RATE_PERCENT // 100
            processed_lines += 1

    return BatchProcessingReport(
        total_contribution=total_contribution,
        processed_lines=processed_lines,
        read_lines=read_lines,
        anomalies=anomalies
    )