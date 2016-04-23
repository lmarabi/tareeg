/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package osmextractor;

/**
 *
 * @author turtle
 */
public class Point {

    private Long id;
    private double x;
    private double y;

    public Point() {
    }

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Point(String x, String y) {
        this.x = Double.parseDouble(x);
        this.y = Double.parseDouble(y);
    }

    public Point(String id, String x, String y) {
        this.id = Long.parseLong(id);
        this.x = Double.parseDouble(x);
        this.y = Double.parseDouble(y);
    }

    public void setX(double x) {
        this.x = x;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    @Override
    public String toString() {
        return this.id + "," + this.x + "," + this.y;
    }

    @Override
    public int hashCode() {
        return id.hashCode();
    }
    /**
     * if the passed parameter is greater than the invoker.
     * @param obj
     * @return 
     */
    public boolean isGreater(Point obj){
        if(this.x <= obj.getX() && this.y <= this.getY() )
            return true; 
        else 
            return false;
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (obj instanceof Point) {
            Point s1 = (Point) obj;

            if (s1.getId().equals(this.getId())) {
                return true;
            }
        }
        return false;
    }
}
