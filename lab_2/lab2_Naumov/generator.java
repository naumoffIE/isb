import java.util.Random;

class Main{

    public static void main(String[] args) {

        // Creating the instance of Random class
        Random r= new Random();

        byte[] bytes = new byte[16]; // 16 байт * 8 бит/байт = 128 бит
        r.nextBytes(bytes);
        StringBuilder binaryString = new StringBuilder();
        for (byte b : bytes) {
            String binaryByte = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
            binaryString.append(binaryByte);
        }

        System.out.println("Generated Binary Sequence:");
        System.out.println(binaryString.toString());
    }
}