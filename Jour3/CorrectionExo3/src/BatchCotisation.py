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

@dataclass(frozen=True)
class ContributionLine:
    contribution_base: Optional[int]

@dataclass(frozen=True)  
class BatchAnomaly:
    line_number: int
    reason: str

@dataclass(frozen=True)  
class BatchProcessingReport:
    total_contribution: int
    processed_lines: int
    read_lines: int
    anomalies: list[BatchAnomaly]
    
def calculate_contribution(contribution_base: int) -> int:
    return contribution_base * CONTRIBUTION_RATE_PERCENT // 100

def find_line_anomalies(line_number: int, contribution_line: ContributionLine) -> Optional[BatchAnomaly]:
    if contribution_line.contribution_base is None:
        return BatchAnomaly(line_number, "base missing")
    if contribution_line.contribution_base < 0:
        return BatchAnomaly(line_number, "base negative")
    return None

def process_batch(contribution_lines: list[ContributionLine]) -> BatchProcessingReport:
    total_contribution = 0
    processed_lines = 0
    anomalies: list[BatchAnomaly] = []
    
    for line_number, line in enumerate(contribution_lines, start=1):
        anomaly = find_line_anomalies(line_number, line)
        if anomaly is not None:
            anomalies.append(anomaly)
            continue
        
        contribution = calculate_contribution(line.contribution_base)
        total_contribution += contribution
        processed_lines += 1
    
    return BatchProcessingReport(
        total_contribution=total_contribution,
        processed_lines=processed_lines,
        read_lines=len(contribution_lines),
        anomalies=anomalies
    )