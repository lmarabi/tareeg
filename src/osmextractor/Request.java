/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package osmextractor;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

/**
 *
 * @author turtle
 */
public class Request {

    private OutputStreamWriter[] outwriter;
    private MBR area;
    private static double startTime;
    private static double endTime;
    private static OutputStreamWriter statusLog;
    private enum exportType {

        node, edge,unsortedNode
    }

    public Request() {
        area = new MBR();
    }

    public MBR getArea() {
        return area;
    }
    
    
    
    /**
     * Get the result and remove the redundant edge and nodes 
     * @param id
     * @param maxLat
     * @param maxLon
     * @param minLat
     * @param minLon
     * @param dataPath
     * @param exportPath
     * @throws FileNotFoundException
     * @throws UnsupportedEncodingException
     * @throws IOException 
     */
    public void GetResult(String id, double maxLat, double maxLon, double minLat,
            double minLon, String dataPath, String exportPath)
            throws FileNotFoundException, UnsupportedEncodingException, IOException {
        this.outwriter = new OutputStreamWriter[exportType.values().length];
        exportPath +=  id + "/";
        File dir = new File(exportPath);
        dir.mkdir();
//        this.outwriter[exportType.node.ordinal()] =
//                new OutputStreamWriter(
//                new FileOutputStream(
//                exportPath + exportType.node.toString() + ".txt"), "UTF-8");
        this.outwriter[exportType.edge.ordinal()] =
                new OutputStreamWriter(
                new FileOutputStream(
                exportPath + exportType.edge.toString() + ".txt"), "UTF-8");
        this.outwriter[exportType.edge.ordinal()] =
                new OutputStreamWriter(
                new FileOutputStream(
                exportPath + exportType.unsortedNode.toString() + ".txt"), "UTF-8");
        //Set the area of interest in the MBR 
        this.area = new MBR(new Point(maxLat, maxLon), new Point(minLat, minLon));
        // Get the set of Files that intersect with the area.
        List<Partition> files = ReadMaster(dataPath);
        //read eachfile and output the result.
        for (Partition f : files) {
            //Build the edge and the node  from the file 
            area.BuildNodeEdges(f.getPartition());
        }
        //Write the output in the file
        for (Point p : area.getNodes()) {
            outwriter[exportType.node.ordinal()].write(p.toString()+"\n");
           
        }
        for (Edge e : area.getEdges()) {
            outwriter[exportType.edge.ordinal()].write(e.toString()+"\n");
        }
        
        outwriter[exportType.edge.ordinal()].close();
        outwriter[exportType.node.ordinal()].close();
    }
    
    /**
     * This method output the result directly without check for redundant tuples
     * @param id
     * @param maxLat
     * @param maxLon
     * @param minLat
     * @param minLon
     * @param dataPath
     * @param exportPath
     * @throws FileNotFoundException
     * @throws UnsupportedEncodingException
     * @throws IOException 
     */
    public void GetOutput(String id, String maxLat, String maxLon, String minLat,
            String minLon, String dataPath, String exportPath)
            throws FileNotFoundException, UnsupportedEncodingException, IOException {
        this.outwriter = new OutputStreamWriter[exportType.values().length];
        exportPath +=  id + "/";
        File dir = new File(exportPath);
        dir.mkdir();
        this.outwriter[exportType.node.ordinal()] =
                new OutputStreamWriter(
                new FileOutputStream(
                exportPath + exportType.node.toString() + ".txt"), "UTF-8");
        this.outwriter[exportType.edge.ordinal()] =
                new OutputStreamWriter(
                new FileOutputStream(
                exportPath + exportType.edge.toString() + ".txt"), "UTF-8");
        //Set the area of interest in the MBR 
        this.area = new MBR(new Point(maxLat, maxLon), new Point(minLat, minLon));
        // Get the set of Files that intersect with the area.
        logStart("start reading the master files");
        List<Partition> files = ReadMaster(dataPath);
        logEnd("end reading master file and selected ("+files.size()+")");
        //read eachfile and output the result.
        logStart("start reading from selected files");
        for (Partition f : files) {
            System.out.println("Start Reading file "+f.getPartition().getName());
            //Build the edge and the node  from the file 
            area.BuildNodeEdges(f,outwriter[exportType.edge.ordinal()],
                    outwriter[exportType.node.ordinal()]);
            System.out.println("End reading file "+f.getPartition().getName());
        }
        
        //Write the output in the file because node need to be store in 
        // memory to remove duplicate.
//        for (Point p : area.getNodes()) {
//            outwriter[exportType.node.ordinal()].write(p.toString()+"\n");
//           
//        }
        Iterator itr = area.getNodehased().iterator();
        while(itr.hasNext()){
            Object element = itr.next();
            outwriter[exportType.node.ordinal()].write(element.toString()+"\n");
        }
        logEnd("end reading files");
        outwriter[exportType.edge.ordinal()].close();
        outwriter[exportType.node.ordinal()].close();
    }
    
    public void GetSmartOutput(String id, String maxLat, String maxLon, String minLat,
            String minLon, String dataPath, String exportPath)
            throws FileNotFoundException, UnsupportedEncodingException, IOException {
        this.outwriter = new OutputStreamWriter[exportType.values().length];
        exportPath +=  id + "/";
        File dir = new File(exportPath);
        dir.mkdir();
        this.statusLog = new OutputStreamWriter(
                new FileOutputStream(
                exportPath + "log.txt"), "UTF-8");
        this.outwriter[exportType.unsortedNode.ordinal()] =
                new OutputStreamWriter(
                new FileOutputStream(
                exportPath + exportType.unsortedNode.toString() + ".txt"), "UTF-8");
        this.outwriter[exportType.edge.ordinal()] =
                new OutputStreamWriter(
                new FileOutputStream(
                exportPath + exportType.edge.toString() + ".txt"), "UTF-8");
        //outwriter[exportType.node.ordinal()].write("Node_id,latitude,longitude\n");
        outwriter[exportType.edge.ordinal()].write("Edge_id,Start_Node_id,End_Node_id,Tags\n");
        //Set the area of interest in the MBR 
        this.area = new MBR(new Point(maxLat, maxLon), new Point(minLat, minLon));
        // Get the set of Files that intersect with the area.
        logStart("start reading the master files");
        List<Partition> files = ReadMaster(dataPath);
        logEnd("end reading master file and selected ("+files.size()+")");
        //read eachfile and output the result.
        logStart("start reading from selected files");
        for (Partition f : files) {
            logStart("Start Reading file "+f.getPartition().getName());
            //Build the edge and the node  from the file 
            area.smartBuildNodeEdges(f,outwriter[exportType.edge.ordinal()],
                    outwriter[exportType.unsortedNode.ordinal()]);
            logEnd("End reading file "+f.getPartition().getName());
        }
               
//        Iterator itr = area.getNodehased().iterator();
//        while(itr.hasNext()){
//            Object element = itr.next();
//            outwriter[exportType.node.ordinal()].write(element.toString()+"\n");
//        }
        logEnd("end reading files");
        outwriter[exportType.edge.ordinal()].close();
        outwriter[exportType.unsortedNode.ordinal()].close();
        logStart("Remove duplicate nodes");
        String commandLine = "sh "+System.getProperty("user.dir") + "/getNode.sh "
                +exportPath + exportType.unsortedNode.toString() + ".txt "
                +exportPath + exportType.node.toString() + ".txt";
        System.out.println(commandLine);  
        Process process = Runtime.getRuntime().exec(commandLine);
        logEnd("End duplicate nodes");
        
        
        //Runtime.getRuntime().exec(commandLine);
    }
    
    
    
    /**
     * output message and start a timer to check the time
     * @param text 
     */
    public static void logStart(String text) throws IOException{
        startTime = System.currentTimeMillis();
        text += "\n";
        System.out.print(text);
        statusLog.write(text);
    }
    
    /**
     * End the message and show the time in second 
     * @param text 
     */
    public static void logEnd(String text) throws IOException{
        endTime = System.currentTimeMillis();
        text = text +" which took"
                + " "+ ((endTime - startTime) / 1000) + " seconds\n";
        System.out.print(text);
        statusLog.write(text);
    }
    
    // this method to close the log.
    public static void closeLog() throws IOException{
        statusLog.close();
    }
    

    /**
     * This Method read all the files in the data directory and fetch only the
     * Intersect files
     *
     * @param maxLat
     * @param minLat
     * @param maxLon
     * @param minLon
     * @param path
     * @return
     */
    private List<Partition> ReadMaster(String path) throws FileNotFoundException, IOException {
        File master;
        List<Partition> result = new ArrayList<Partition>();
        master = new File(path+"_master");
        BufferedReader br = new BufferedReader(new FileReader(master));
        String line = null;
        int count = 0;// this is done to skip the flag at the first line in file
        while((line = br.readLine()) != null){
            String[] temp = line.split(",");
            // The file has the following format as Aggreed with the interface
            // between hadoop and this program 
            // #filenumber,minLat,minLon,maxLat,maxLon
            if (temp.length == 5 && count!= 0) {
                Point pointMax = new Point(temp[3], temp[4]);
                Point pointMin = new Point(temp[1], temp[2]);
                if (area.Intersect(pointMax, pointMin)) {
                    System.out.println("Chose MBR Min("+pointMin.getLat()+","
                            + pointMin.getLon()+")"+" - Max("+ pointMax.getLat()+","
                            + pointMax.getLon()+")");
                    File f = new File(path+temp[0]);
                    Partition part = new Partition(f, new MBR(pointMax, pointMin));
                    result.add(part);
                }
            }
            count++;
        }
        return result;
    }
}
