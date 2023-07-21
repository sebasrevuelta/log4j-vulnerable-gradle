import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.Level;

//Test class
public class HelloLog2 {

    private static final Logger logger = LogManager.getLogger();

    public static void main(String[] args) {
        String userInput = "${jndi:http://localhost/AAAA/BBBB}";

        // passing user input into the logger, it a log4j critical vuln
        logger.info("Test: "+userInput);

        // %m{nolookups} has no effect for the following line
        logger.printf(Level.INFO,"Test: %s", userInput);

        // %m{nolookups} has no effect for the following line
        logger.printf(Level.ERROR,"Test: %s", userInput);
    }
}
