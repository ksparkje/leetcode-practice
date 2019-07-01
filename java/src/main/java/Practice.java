public class Practice {

    private int calories;
    private Type type;
    private String name;

    public Practice(int calories, Type type, String name) {
        this.calories = calories;
        this.type = type;
        this.name = name;
    }

    public int getCalories() {
        return calories;
    }

    public Type getType() {
        return type;
    }

    public String getName() {
        return name;
    }

    public enum Type {
        Fish, Meat, Other
    }

    @Override
    public String toString() {
        return name;
    }

    public void nothing() {
        System.out.println("haha");
    }
}
