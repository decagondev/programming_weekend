public class Hello {
    private void bob() {
        System.out.println("My Name is Bob");
    }

    public String sayHello() {
        bob();
    }

    protected String sharedSayHello() {
        System.out.println("Cookies");
    }
 }