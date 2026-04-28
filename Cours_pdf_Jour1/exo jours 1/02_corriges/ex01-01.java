import java.time.LocalDate;
import java.util.Objects;

class CollectiveContract {
    private final CoveragePeriod coveragePeriod;

    CollectiveContract(CoveragePeriod coveragePeriod) {
        this.coveragePeriod = Objects.requireNonNull(coveragePeriod);
    }

    boolean isActiveOn(LocalDate date) {
        return coveragePeriod.includes(date);
    }

}

final class CoveragePeriod {
    private final LocalDate startDate;
    private final LocalDate endDate;

    public CoveragePeriod(LocalDate startDate, LocalDate endDate) {
        this.startDate = Objects.requireNonNull(startDate);
        this.endDate = Objects.requireNonNull(endDate);

        if (endDate.isBefore(startDate)) {
            throw new IllegalArgumentException("Start date must be before end date");
        }
    }

    boolean includes(LocalDate date) {
        return !date.isBefore(startDate) && !date.isAfter(endDate);
    }

}