public class PC {
    private int memory;
    private int ssd;
    private String processor;
    private String video;
    private String status;

    public PC(int memory, int ssd, String video, String processor) {
        this.memory = memory;
        this.ssd = ssd;
        this.processor = processor;
        this.video = video;
        this.status = "desligado";
    }

    public void powerOn() {
        if (this.status.equals("desligado")) {
            System.out.println("PC ligado");
            this.status = "ligado";
        } else {
            System.out.println("O PC já está ligado");
        }
    }

    public void powerOff() {
        if (this.status.equals("ligado")) {
            System.out.println("PC desligado");
            this.status = "desligado";
        } else {
            System.out.println("O PC já está desligado");
        }
    }

    public void getInfo() {
        System.out.println(this.video);
        System.out.println(this.memory);
        System.out.println(this.ssd);
        System.out.println(this.processor);
    }

    public void upgrade(String newProcessor, int newSsd, int newMemory, String newVideo) {
        this.processor = newProcessor;
        if (newSsd > 0) {
            this.ssd = newSsd;
        } else {
            System.out.println("Erro: O novo SSD deve ser um inteiro positivo.");
        }

        this.memory = newMemory;
        this.video = newVideo;
    }

    public static void main(String[] args) {
        // Criar uma instância da classe PC
        PC pc1 = new PC(16, 256, "GEFORCE 2080 TI", "i9");
    }
}