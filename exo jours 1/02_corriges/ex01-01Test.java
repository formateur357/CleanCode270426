import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

class CollectiveContractTest {
    @Test
    void contractIsActiveWithinCoveragePeriod() {
        // Arrange
        CollectiveContract contract = new CollectiveContract(new CoveragePeriod(new LocalDate(2024, 1, 1), new LocalDate(2024, 12, 31)));

        // Act
        // Assert
        assertTrue(contract.isActiveOn(new CoveragePeriod(new LocalDate(2024, 6, 1), new LocalDate(2024, 6, 30))));
    }

    @Test
    void contractIsNotActiveBeforeCoveragePeriod() {
        // Arrange
        CollectiveContract contract = new CollectiveContract(new CoveragePeriod(new LocalDate(2024, 1, 1), new LocalDate(2024, 12, 31))); 

        // Act
        // Assert
        assertFalse(contract.isActiveOn(new CoveragePeriod(new LocalDate(2023, 12, 31), new LocalDate(2023, 12, 31))));
    }

    @Test
    void contractIsActiveOnStartDateAndEndDate() {
        // Arrange
        CollectiveContract contract = new CollectiveContract(new CoveragePeriod(new LocalDate(2024, 1, 1), new LocalDate(2024, 12, 31)));

        // Act
        // Assert
        assertTrue(contract.isActiveOn(new CoveragePeriod(new LocalDate(2024, 1, 1), new LocalDate(2024, 1, 1))));
        assertTrue(contract.isActiveOn(new CoveragePeriod(new LocalDate(2024, 12, 31), new LocalDate(2024, 12, 31))));
    }

    @Test
    void coveragePeriodConstructorThrowsExceptionIfEndDateIsBeforeStartDate() {
        // Arrange
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            new CoveragePeriod(new LocalDate(2024, 12, 31), new LocalDate(2024, 1, 1));
        });
    }
}