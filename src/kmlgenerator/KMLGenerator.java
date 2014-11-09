package kmlgenerator;

import java.util.*;
import java.io.*;

/**
 *
 * @author rami
 */
public class KMLGenerator {

    static String EDGE_FILE = "/home/turtle/NetBeansProjects/OSMToRN/Data/tareeg_experiment/edge.txt";
//    final static String EDGE_FILE = "/home/rami/Documents/research/OSM/MinnesotaLake/edge.txt";
    static String NODE_FILE = "/home/turtle/NetBeansProjects/OSMToRN/Data/tareeg_experiment/node.txt";
//    final static String NODE_FILE = "/home/rami/Documents/research/OSM/MinnesotaLake/node.txt";
    static String KML_FILE;// = "/home/rami/Documents/research/OSM/park/result.kml";
    //final static Charset ENCODING = StandardCharsets.UTF_8;
    HashMap<Long, Edge> edges = new HashMap();  //2-dimensional array
    //List<List<Double>> nodes = new ArrayList<>();  //2-dimensional array
    HashMap<Long, List<Double>> nodes = new HashMap();
    //List<String> tags = new ArrayList<>();  //All tags from edges.txt
    List<Polygon> polygonsList = new ArrayList<Polygon>();
    static OutputStream outputStream;
    static Writer writer;
    static String shapeType;
    static String KMLHeader = "<kml xmlns=`http://www.opengis.net/kml/2.2` xmlns:atom=`http://www.w3.org/2005/Atom` xmlns:gx=`http://www.google.com/kml/ext/2.2` xmlns:kml=`http://www.opengis.net/kml/2.2`>".replace('`', '"');
    static String KMLTag = "\n <Document>\n  <name>KmlFile generated by OSM Extractor</name>\n  <Folder>\n   <name>polygons</name>";
    static String KMLTagLine = "\n <Document>\n  <name>KmlFile generated by OSM Extractor</name>\n  <Folder>\n   <name>lines</name>";

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
//        EDGE_FILE = args[0].toString();
//        NODE_FILE = args[0].toString();
//        runKMLConverter(EDGE_FILE, NODE_FILE);
        runKMLConverterLine(EDGE_FILE, NODE_FILE);
    }

    public static void runKMLConverterLine(String edge, String node) {
        //shapeType = "lines";
        KMLGenerator reader = new KMLGenerator();
        reader.readEdgeFile(edge);
        log("Done reading edge file");
        reader.readNodeFile(node);
        log("Done reading node file");
        try {
            File output = new File(edge);
            outputStream = new FileOutputStream(output.getParent() + "/result.kml");
            writer = new OutputStreamWriter(outputStream, "UTF8");
            writer.write(KMLHeader + KMLTagLine);
        } catch (FileNotFoundException e) {
            log(e.getMessage());
        } catch (IOException e) {
            log(e.getMessage());
        }
        reader.extractLines();
        try {
            writer.write("\n  </Folder>" + "\n </Document>" + "\n</kml>");
            writer.close();
        } catch (IOException e) {
            log(e.getMessage());
        }
    }

    public static void runKMLConverter(String edge, String node) {
        //shapeType = "polygons";
        KMLGenerator reader = new KMLGenerator();
        reader.readEdgeFile(edge);
        log("Done reading edge file");
        reader.readNodeFile(node);
        log("Done reading node file");
        try {
            File output = new File(edge);
            outputStream = new FileOutputStream(output.getParent() + "/result.kml");
            writer = new OutputStreamWriter(outputStream, "UTF8");
            writer.write(KMLHeader + KMLTag);
        } catch (FileNotFoundException e) {
            log(e.getMessage());
        } catch (IOException e) {
            log(e.getMessage());
        }
        reader.extractNodesFromEdges();
        try {
            writer.write("\n  </Folder>" + "\n </Document>" + "\n</kml>");
            writer.close();
        } catch (IOException e) {
            log(e.getMessage());
        }
    }

    void extractLines() {
        //log(edges.size());
        int lineCounter = 0;
        
        Iterator<Long> keySetIterator;
        keySetIterator = edges.keySet().iterator();
        while (keySetIterator.hasNext()) {
            Long key = keySetIterator.next();
            //log(lineCounter);
            Edge edge = edges.get(key);
            List<Double> fNode = extractLatLon(edge.edge.get(0));
            List<Double> sNode = extractLatLon(edge.edge.get(1));
            try {
                edge.tag = edge.tag.replace("&", "&amp;");
                edge.tag = edge.tag.replace("<", "&lt;");
                edge.tag = edge.tag.replace(">", "&gt;");
                writer.write("\n   <Placemark>\n    <name>line " + lineCounter + "</name>\n    <description>" + edge.tag + "</description>");
                writer.write("\n    <LineString>\n     <tessellate>1</tessellate>\n     <altitudeMode>relativeToGround</altitudeMode>\n     <coordinates>");

                writer.write(fNode.get(1).toString() + "," + fNode.get(0).toString() + " ");
                writer.write(sNode.get(1).toString() + "," + sNode.get(0).toString() + " ");

                writer.write("</coordinates>\n    </LineString>\n   </Placemark>");
            } catch (IOException e) {
                log(e.getMessage());
            }
            lineCounter++;
        }
    }

    void extractNodesFromEdges() {
        int polygonCounter = 0;
        while (!edges.isEmpty()) {
            Polygon polygon = new Polygon();
            Edge edgeObj; //a temp array to hold the fetched rows from edges.        

            long to_Node = -1;
            long ringNode = -1;

            Iterator<Long> keySetIterator;
            long nextEdge = -1;

            boolean notFoundPolygon = true;

            while (!edges.isEmpty()) {
                if (to_Node == -1) {
                    keySetIterator = edges.keySet().iterator();
                    Long key = keySetIterator.next();
                    nextEdge = key;
                    edgeObj = edges.get(key);

                    ringNode = edgeObj.edge.get(0);
                    //polygon.nodes.add(extractLatLon(ringNode));
                    polygon.tags = edgeObj.tag.replace("&", "&amp;");
                    polygon.tags = polygon.tags.replace("<", "&lt;");
                    polygon.tags = polygon.tags.replace(">", "&gt;");
                    to_Node = edgeObj.edge.get(1);
                    polygon.nodes.add(extractLatLon(to_Node));
                    edges.remove(nextEdge);
                    nextEdge++;
                } else {
                    edgeObj = edges.get(nextEdge);

                    if (edgeObj != null) {
                        if (edgeObj.edge.get(0) == to_Node) {
                            to_Node = edgeObj.edge.get(1);
                            polygon.nodes.add(extractLatLon(to_Node));
                            if (!polygon.tags.contains(edgeObj.tag)) {
                                polygon.tags += "," + edgeObj.tag.replace("&", "&amp;");
                                polygon.tags = polygon.tags.replace("<", "&lt;");
                                polygon.tags = polygon.tags.replace(">", "&gt;");
                            }
                            edges.remove(nextEdge);
                            nextEdge++;
                        } else {
                            keySetIterator = edges.keySet().iterator();
                            boolean edgeNotFound = true;
                            while (keySetIterator.hasNext()) {
                                Long key = keySetIterator.next();
                                edgeObj = edges.get(key);
                                if (edgeObj.edge.get(0) == to_Node) {
                                    to_Node = edgeObj.edge.get(1);
                                    polygon.nodes.add(extractLatLon(to_Node));
                                    if (!polygon.tags.contains(edgeObj.tag)) {
                                        polygon.tags += "," + edgeObj.tag.replace("&", "&amp;");
                                        polygon.tags = polygon.tags.replace("<", "&lt;");
                                        polygon.tags = polygon.tags.replace(">", "&gt;");
                                    }
                                    nextEdge = key;

                                    edges.remove(nextEdge);
                                    nextEdge++;
                                    edgeNotFound = false;
                                    break;
                                }
                            }
                            if (edgeNotFound) {
                                edges.remove(nextEdge);
                                break;
                            }
                        }
                    } else {
                        keySetIterator = edges.keySet().iterator();
                        boolean edgeNotFound = true;
                        while (keySetIterator.hasNext()) {
                            Long key = keySetIterator.next();
                            edgeObj = edges.get(key);
                            if (edgeObj.edge.get(0) == to_Node) {
                                to_Node = edgeObj.edge.get(1);
                                polygon.nodes.add(extractLatLon(to_Node));
                                if (!polygon.tags.contains(edgeObj.tag)) {
                                    polygon.tags += "," + edgeObj.tag.replace("&", "&amp;");
                                    polygon.tags = polygon.tags.replace("<", "&lt;");
                                    polygon.tags = polygon.tags.replace(">", "&gt;");
                                }
                                nextEdge = key;

                                edges.remove(nextEdge);
                                nextEdge++;
                                edgeNotFound = false;
                                break;
                            }
                        }
                        if (edgeNotFound) {
                            edges.remove(nextEdge);
                            break;
                        }
                    }
                }
                if (to_Node == ringNode) {
                    notFoundPolygon = false;
                    break;
                }
            }
            if (notFoundPolygon == false) {
                //polygonsList.add(polygon);
                polygonCounter++;
                //String i = String.valueOf(polygonsList.size());
                log("Number of polygons so far is " + polygonCounter);
                int size = polygon.nodes.size();
                try {
                    writer.write("\n   <Placemark>\n    <name>polygon " + polygonCounter + "</name>\n    <description>" + polygon.tags + "</description>");
                    writer.write("\n    <Polygon>\n     <tessellate>1</tessellate>\n     <altitudeMode>relativeToGround</altitudeMode>\n     <outerBoundaryIs>\n      <LinearRing>\n       <coordinates>");
                    for (int j = 0; j < size; j++) {
                        writer.write(polygon.nodes.get(j).get(1).toString() + "," + polygon.nodes.get(j).get(0).toString() + " ");
                    }
                    writer.write(polygon.nodes.get(0).get(1).toString() + "," + polygon.nodes.get(0).get(0).toString());
                    writer.write("</coordinates>\n      </LinearRing>\n     </outerBoundaryIs>\n    </Polygon>\n   </Placemark>");
                } catch (IOException e) {
                    log(e.getMessage());
                }
            }
        }
        log("Done extracting!");
    }

    List<Double> extractLatLon(long nodeID) {
        List<Double> nodeLatLon;
        //List<Double> node;
        //int size = nodes.size();
        // Get a set of the entries
        //Set set = nodes.entrySet();
        // Get an iterator
        //Iterator iter = set.iterator();

        nodeLatLon = nodes.get(nodeID);

//        for (int i = 0; i < nodes.size(); i++) {
//            node = nodes.get(i);
//            if (node.isEmpty()) {
//                log("fuck that shit!");
//            }
//            //log(node);
//            if (node.get(0) == nodeID) {
//                nodeLatLon.add(node.get(1));
//                nodeLatLon.add(node.get(2));
//                //log(node);
//                //nodes.remove(i);
//                break;
//            }
//        }
        if (nodeLatLon.isEmpty()) {
            log("nodeLatLon is empty. NodeID: " + nodeID);
        }
        return nodeLatLon;
    }

    // This method can read large files using a buffer which reads one line everytime..
    void readEdgeFile(String aFileName) {
        try {
            File f = new File(aFileName);
            Scanner scanner = new Scanner(f, "utf-8");
            //should ignore line 1!
            int i = 0;
            if (scanner.hasNext()) {
                while (scanner.hasNextLine()) {
                    if (i == 0) {
                        i++;
                        scanner.nextLine();
                        continue;
                    }
                    //process each line
                    //log(scanner.nextLine());

                    processEdgeLine(scanner.nextLine());
                    //log(scanner.nextLine());
                }
                scanner.close();
            } else {
                log("The file " + aFileName + " is empty!");
            }
        } catch (FileNotFoundException e) {
            System.err.println(e);
        }
    }

    protected void processEdgeLine(String aLine) {
        //a second Scanner to parse the content of each line 
        Scanner scanner = new Scanner(aLine.trim());
        if (aLine.isEmpty()) {
            log("line from edge is empty");
        }
        //assumes the line has a CSV structure
        scanner.useDelimiter(",");
        if (scanner.hasNext()) {
            String tag;
            List<Long> list = new ArrayList<Long>(2);
            long id = scanner.nextInt();
            //log(id);
            list.add(scanner.nextLong());
            list.add(scanner.nextLong());
            if (scanner.hasNext()) {
                tag = scanner.next();
            } else {
                tag = "";
            }

            while (edges.containsKey(id)) {
                id += 10;
                log("shared edge found!");
            }
//            if (edges.containsKey(id)) {
//                log("shared edge found!");
//            }

            edges.put(id, new Edge(tag, list));

        } else {
            log("Unable to process line: " + aLine);
        }
    }

    // This method can read large files using a buffer which reads one line everytime..
    void readNodeFile(String aFileName) {
        //Path path = Paths.get(aFileName);        
        try {
            File f = new File(aFileName);
            Scanner scanner = new Scanner(f, "utf-8");
            //should ignore line 1!
            int i = 0;
            if (scanner.hasNext()) {
                while (scanner.hasNextLine()) {
                    if (i == 0) {
                        i++;
                        scanner.nextLine();
                        continue;
                    }
                    //process each line
                    processNodeLine(scanner.nextLine());
                    //log(scanner.nextLine());
                }
            } else {
                log("The file " + aFileName + " is empty!");
            }
        } catch (FileNotFoundException e) {
            System.err.println(e);
        }
    }

    protected void processNodeLine(String aLine) {
        //a second Scanner to parse the content of each line 
        Scanner scanner = new Scanner(aLine.trim());
        if (aLine.isEmpty()) {
            log("line is empty from Node");
        }
        //assumes the line has a CSV structure
        scanner.useDelimiter(",");
        if (scanner.hasNext()) {
            List<Double> list = new ArrayList<Double>(2);
            //List<Integer> list = new ArrayList<>(1);
            //nodes.add(list);
            long id = scanner.nextLong();
            list.add(scanner.nextDouble());
            list.add(scanner.nextDouble());
            nodes.put(id, list);
            if (list.size() <= 1) {
                log("null values in processNodeLine: " + aLine);
            }
        } else {
            log("Unable to process line: " + aLine);
        }
    }

    private static void log(Object aMsg) {
        System.out.println(String.valueOf(aMsg));
    }
}