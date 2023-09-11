package cucumber_example;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.Calendar;

public class DaysCounter {
    public static int count(String text){
        DateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        sdf.setLenient(false);
        try {
            sdf.parse(text);
        } catch (ParseException e) {
            System.out.println("Date is in wrong format.");
            return -1;
        }
        LocalDate dateBefore = LocalDate.parse(text);

        Calendar cal = Calendar.getInstance();
        LocalDate dateAfter = LocalDate.parse(sdf.format(cal.getTime()));

        long daysDiff = ChronoUnit.DAYS.between(dateBefore, dateAfter);

        if (daysDiff < 0)  {
            System.out.println("Date is in future.");
            return -1;
        }


        System.out.println("The number of days between dates: " + daysDiff);

        return (int)daysDiff;

    }
}
