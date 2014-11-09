/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package osmextractor;

/**
 *
 * @author turtle
 */
public class Edge {
    private long edgeid;
    private long startNode;
    private Point startPoint;
    private long endNode;
    private Point endPoint;
    private String tags;

    public Edge() {
    }

    public Edge(String edgeid, String startNode, Point startPoint,
            String endNode, Point endPoint, String tags) {
        this.edgeid = Long.parseLong(edgeid);
        this.startNode = Long.parseLong(startNode);
        this.startPoint = startPoint;
        this.endNode = Long.parseLong(endNode);
        this.endPoint = endPoint;
        this.tags = tags;
    }

    public long getEdgeid() {
        return edgeid;
    }

    public void setEdgeid(long edgeid) {
        this.edgeid = edgeid;
    }

    public long getStartNode() {
        return startNode;
    }

    public void setStartNode(long startNode) {
        this.startNode = startNode;
    }

    public Point getStartPoint() {
        return startPoint;
    }

    public void setStartPoint(Point startPoint) {
        this.startPoint = startPoint;
    }

    public long getEndNode() {
        return endNode;
    }

    public void setEndNode(long endNode) {
        this.endNode = endNode;
    }

    public Point getEndPoint() {
        return endPoint;
    }

    public void setEndPoint(Point endPoint) {
        this.endPoint = endPoint;
    }

    public String getTags() {
        return tags;
    }

    public void setTags(String tags) {
        this.tags = tags;
    }

    @Override
    public String toString() {
        return this.edgeid+","+this.startNode+","+this.endNode+","+this.tags;
    }
    
    
    
    
    
    
}
