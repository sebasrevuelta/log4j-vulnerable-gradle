import org.apache.commons.fileupload.FileUploadBase;

public class HelloApache {
    public static void main(String[] args) {
        // Create an instance of FileUploadBase
        FileUploadBase fileUpload = new FileUploadBase();

        // Set the maximum file count using the setFileCountMax method
        int maxFileCount = 10;
        fileUpload.setFileCountMax(maxFileCount);

        // Access the maximum file count using the getFileCountMax method
        int currentMaxFileCount = fileUpload.getFileCountMax();
        
        // Print the maximum file count
        System.out.println("Maximum file count: " + currentMaxFileCount);
    }
}
