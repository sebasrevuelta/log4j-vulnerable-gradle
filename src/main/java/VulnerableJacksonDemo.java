import com.fasterxml.jackson.databind.ObjectMapper;

public class VulnerableJacksonDemo {
    public static void main(String[] args) {
        try {
            String maliciousJson = 
                "{ \"@type\": \"org.apache.commons.collections.functors.InvokerTransformer\", " +
                "  \"iMethodName\": \"toString\" }";

            ObjectMapper mapper = new ObjectMapper();
            Object obj = mapper.readValue(maliciousJson, Object.class);

            System.out.println("Deserialized object: " + obj);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
