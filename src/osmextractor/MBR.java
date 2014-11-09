/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package osmextractor;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;

import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;

import edu.umn.cs.spatialHadoop.core.RTree;
import edu.umn.cs.spatialHadoop.core.Rectangle;
import edu.umn.cs.spatialHadoop.core.ResultCollector;
import edu.umn.cs.spatialHadoop.osm.OSMPolygon;

/**
 *
 * @author turtle
 */
public class MBR {

    private Point max;
    private Point min;
    List<Edge> edges;
    List<Point> nodes;
    HashSet<Point> nodehased;
    List<String> idsedge;

    public MBR() {
    }

    public MBR(Point max, Point min) {
        this.max = max;
        this.min = min;
        this.edges = new ArrayList<Edge>();
        this.nodes = new ArrayList<Point>();
        this.nodehased = new HashSet<Point>(new LinkedHashSet<Point>());
        this.idsedge = new ArrayList<String> ();
    }


    public Point getMax() {
        return max;
    }

    public Point getMin() {
        return min;
    }

    public List<Edge> getEdges() {
        return edges;
    }

    public List<Point> getNodes() {
        return nodes;
    }

    public void setMin(Point min) {
        this.min = min;
    }

    public void setMax(Point max) {
        this.max = max;
    }

    public HashSet<Point> getNodehased() {
        return nodehased;
    }

    /**
     * This method check whether the MBR is intersect with the MB
     *
     * @param pmax
     * @param pmin
     * @return true if there is intersect otherwise it will return false
     */
    public boolean Intersect(Point pmax, Point pmin) {
        //RectA1: this.main = x1,y1 ; this.max = x2,y2
        //RectB2: pmin = x3,y3 ; pmax= x4,y4
        //return !(x2 < x3 || x1 > x2 || y2 > y3 || y1 < y4)
        //if (RectA.X1 < RectB.X2 && RectA.X2 > RectB.X1 &&
        //    RectA.Y1 < RectB.Y2 && RectA.Y2 > RectB.Y1) 
        if (this.min.getLon() < pmax.getLon()
                && this.max.getLon() > pmin.getLon()
                && this.min.getLat() < pmax.getLat()
                && this.max.getLat() > pmin.getLat()) {
            return true;
        } else {
            return false;
        }
    }

    /**
     * This method check whether the point inside the MBR or not
     *
     * @param point
     * @return true if the point inside the area other wise return false
     */
    public boolean insideMBR(Point point) {
        if (point.getLat() <= this.max.getLat()
                && point.getLat() >= this.min.getLat()
                && point.getLon() <= this.max.getLon()
                && point.getLon() >= this.min.getLon()) {
            return true;
        } else {
            return false;
        }
    }

    /**
     * This method extract nodes and edges from a file. It remove the redundant
     * Edge and node from the Node and edge list.
     *
     * @param file
     * @throws FileNotFoundException
     * @throws UnsupportedEncodingException
     * @throws IOException
     */
    public void BuildNodeEdges(File file) throws FileNotFoundException, UnsupportedEncodingException, IOException {
        StringBuilder result = new StringBuilder();
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(
                new FileInputStream(file), "UTF-8"));
        String tuple;
        while ((tuple = reader.readLine()) != null) {
            String[] attr = tuple.split(",");
            if (attr.length == 9) {
                Point startNode = new Point(attr[1], attr[2], attr[3]);
                Point endNode = new Point(attr[4], attr[5], attr[6]);
                //Check whether the each of the point in the edge inside the MBR 
                if (this.insideMBR(startNode) || this.insideMBR(endNode)) {
                    // Put the edge in the area if it does not exist
                    Edge tempEdge = new Edge(attr[0], attr[1], startNode,
                            attr[4], endNode, attr[8]);
                    if (!this.edges.contains(tempEdge)) {
                        this.edges.add(tempEdge);
                    }
                    // put the nodes in the area if it doesn't exist 
                    if (!this.nodes.contains(startNode)) {

                        this.nodes.add(startNode);

                    }
                    if (!this.nodes.contains(endNode)) {
                        this.nodes.add(endNode);
                    }
                }

            }
        }
    }

    /**
     * This method Write the edge as is and make sure that it remove the
     * redundant nodes, This is the recommended for speed up process.
     *
     * @param f
     * @param outEdge
     * @throws FileNotFoundException
     * @throws IOException
     */
    public void BuildNodeEdges(Partition part, OutputStreamWriter outEdge, OutputStreamWriter outNode) throws FileNotFoundException, IOException {

        BufferedReader reader;
        reader = new BufferedReader(
                new InputStreamReader(
                new FileInputStream(part.getPartition()), "UTF-8"));
        String tuple;
        //get the range file
        while ((tuple = reader.readLine()) != null) {
            String[] attr = tuple.split(",");
            if (attr.length == 9) {
                Point startNode = new Point(attr[1], attr[2], attr[3]);
                Point endNode = new Point(attr[4], attr[5], attr[6]);
//                MBR edgeMbr;
//                if (startNode.isGreater(endNode)) {
//                    edgeMbr = new MBR(endNode, startNode);
//                } else {
//                    edgeMbr = new MBR(startNode, endNode);
//                }
//                if (part.getArea().Intersect(edgeMbr.max, edgeMbr.min)) {
////                    MBR intersected = new MBR(
////                            new Point(edgeMbr.max.getLat(), edgeMbr.max.getLon()),
////                            new Point(edgeMbr.min.getLat(), this.getMin().getLon()));
//                    if (part.getArea().insideMBR(new Point(edgeMbr.min.getLat(), this.getMin().getLon()))) {
//                        outEdge.write(attr[0]);
//                        outEdge.write(",");
//                        outEdge.write(attr[1]);
//                        outEdge.write(",");
//                        outEdge.write(attr[4]);
//                        outEdge.write(",");
//                        outEdge.write(attr[8]);
//                        outEdge.write("\n");
//                        this.nodehased.add(startNode);
//                        this.nodehased.add(endNode);
//                    }
//                }
                //Check whether the each of the point in the edge inside the MBR 
            if(this.insideMBR(startNode) || this.insideMBR(endNode)){
                // output the edege directly without check for redundant
                //Write edgeid,startNodeID,endNodeID,tags
                if(!idsedge.contains(attr[0])){
                outEdge.write(attr[0]);
                outEdge.write(",");
                outEdge.write(attr[1]);
                outEdge.write(",");
                outEdge.write(attr[4]);
                outEdge.write(",");
                outEdge.write(attr[8]);
                outEdge.write("\n");
            
            
//                // put the nodes in the area if it doesn't exist 
//                if(!this.nodes.contains(startNode)){
//                    this.nodes.add(startNode);
//                    outNode.write(startNewClassNode.toString()+"\n");
//                    
//                }
//                if(!this.nodes.contains(endNode)){
//                    this.nodes.add(endNode);
//                    outNode.write(endNode.toString()+"\n");
//                }


                this.nodehased.add(startNode);
                this.nodehased.add(endNode);
                idsedge.add(attr[0]);
                }
            }

            }
        }
    }
    
    
        /**
     * This method Write the edge as is and make sure that it remove the
     * redundant nodes, This is the recommended for speed up process.
     *
     * @param f
     * @param outEdge
     * @throws FileNotFoundException
     * @throws IOException
     */
    public void smartBuildNodeEdges(Partition part, OutputStreamWriter outEdge, OutputStreamWriter outNode) throws FileNotFoundException, IOException ,OutOfMemoryError{
        //Write the header of the file
        BufferedReader reader;
        reader = new BufferedReader(
                new InputStreamReader(
                new FileInputStream(part.getPartition()), "UTF-8"));
        String tuple;
        //get the range file
        while ((tuple = reader.readLine()) != null) {
            String[] attr = tuple.split(",");
            if (attr.length == 9) {
                Point startNode = new Point(attr[1], attr[2], attr[3]);
                Point endNode = new Point(attr[4], attr[5], attr[6]);
                MBR edgeMbr;
                if (startNode.isGreater(endNode)) {
                    edgeMbr = new MBR(endNode, startNode);
                } else {
                    edgeMbr = new MBR(startNode, endNode);
                }
                if (this.Intersect(edgeMbr.max, edgeMbr.min)) {
                    Point tempPoint = new Point();
                    
                    if(this.min.getLon() < edgeMbr.min.getLon()){
                        tempPoint.setLon(edgeMbr.getMin().getLon());
                    }else{
                        tempPoint.setLon(this.min.getLon());
                    }
                    if(this.min.getLat() < edgeMbr.min.getLat()){
                        tempPoint.setLat(edgeMbr.getMin().getLat());
                    }else{
                        tempPoint.setLat(this.min.getLat());
                    }
                    if (part.getArea().insideMBR(tempPoint)) {
                        outEdge.write(attr[0]);
                        outEdge.write(",");
                        outEdge.write(attr[1]);
                        outEdge.write(",");
                        outEdge.write(attr[4]);
                        outEdge.write(",");
                        outEdge.write(attr[8]);
                        outEdge.write("\n");
//                        this.nodehased.add(startNode);
//                        this.nodehased.add(endNode);
                        outNode.write(startNode.toString()+"\n");
                        outNode.write(endNode.toString()+"\n");
                        
                    }
                }

            }
        }
    }
    
    
    
    
    /**
     * This method Write the edge as is and make sure that it remove the
     * redundant nodes, This is the recommended for speed up process.
     *
     * @param f
     * @param outEdge
     * @throws FileNotFoundException
     * @throws IOException
     */
    public void rangeQueryRtree(Partition part, final OutputStreamWriter kwtWriter) throws FileNotFoundException, IOException ,OutOfMemoryError{
    	//init Rtree object in the partition 
    	RTree<OSMPolygon> rtree = new RTree<OSMPolygon>();
		rtree.setStockObject(new OSMPolygon());
		Path file = new Path(part.getPartition().getPath());
		org.apache.hadoop.conf.Configuration conf = new  org.apache.hadoop.conf.Configuration();
		FileSystem fs = file.getFileSystem(conf);
		FSDataInputStream in = fs.open(file);
		in.skip(8);
		rtree.readFields(in);
		Rectangle mbr = new Rectangle(this.min.getLon(), this.min.getLat(),this.max.getLon(), this.max.getLon());

		//Collector return the result 
		ResultCollector<OSMPolygon> output = new ResultCollector<OSMPolygon>() {

			@Override
			public void collect(OSMPolygon arg0) {
				System.out.println(arg0.toText(new Text ()));
				try {
					kwtWriter.write(arg0.toText(new Text()).toString()+"\n");
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

			}
		};
		
		int results = rtree.search(mbr, output);
		System.out.println("number of restuts: "+results);
    }
    
}
