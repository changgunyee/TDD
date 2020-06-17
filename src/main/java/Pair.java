public class Pair {
    private String from;
    private String to;

    Pair(String from, String to){
        this.from=from;
        this.to=to;
    }

    public boolean equals(Object object){
        Pair pair =(Pair) object;
        boolean result=from.equals(pair.from)&&to.equals(pair.to);
        return result;
    }

    public int hashCode(){
        return 0;
    }
}
