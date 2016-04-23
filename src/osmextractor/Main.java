/*
 * This is the main program that handel the request to the delievery 
 * The objective of this module is the following 
 * 1- receive user request. /
 * 2- send email to the user 
 * 3- call the query program. /
 * 4- store the rquest of the user into file. /
 * 
 */
package osmextractor;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.io.UnsupportedEncodingException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.mail.MessagingException;

import edu.umn.cs.spatialHadoop.osm.OSMToKML;

/**
 *
 * @author turtle
 */
public class Main {

    /**
     * csv named with the csv exported file .
     */
    public enum dataType {

        road_edges, lake_edges, park_edges, river_edges, building_edges,
        cemetery_edges, sport_edges, border_edges, resident_edges,
        commerce_edges, worship_edges, services_edges, education_edges,
        desert_edges, region_edges, district_edges, city_edges,
        neighborhood_edges, administrative_edges, postal_edges,
        maritime_edges, political_edges, national_edges, coast_edges;
    }
    public static String folderPath = "/Users/louai/MEGA/antProjects/dataset/osm/";   
    									//"/export/scratch/louai/scratch1/workspace/dataset/osm/osmIndex/";
 
    public static String exportPath = System.getProperty("user.dir") + "/userData/";
    public static String emailPath = System.getProperty("user.dir") + "/email/";
    public static String emailFlag;

    /**
     * args take username, email, type, maxLat,MaxLon, MinLat, MinLon
     *
     * @param args
     */
    public static void main(String args[]) throws MessagingException {
        User user = new User();
        Request request = new Request();
        args = new String[11]; // delete me after finish
        if (args.length != 11) {
            System.out.println("Argument of this program ");
            System.out.println("<name>");
            System.out.println("<email>");
            System.out.println("<type>_edges");
            System.out.println("<maxLat>");
            System.out.println("<maxLon>");
            System.out.println("<minLat>");
            System.out.println("<minLon>");
            System.out.println("<folderPath>");
            System.out.println("<exportPath>");
            System.out.println("<emailPath>");
            System.out.println("[0|1] indicate send email or not");
        } else {
            try {
                //21.541713013778292 40.57242393493422 21.396020222896393 40.40453910827428
                args[0] = "RAMtest";
                args[1] = "louai@cs.umn.edu";
                args[2] = "river_edges";
                args[3] = "-93.67492675781862";//"29.71606047815052";//maxLat // New minLon = x1
                args[4] = "44.8451592777191";//"-82.2503251624035";//maxLon // New minLat = y1 
                args[5] = "-92.98622131348593";//"29.5886598210803";// minLat // New maxLon = x2 
                args[6] = "45.16073744197329";//"-82.44189925908323";// miLon // new maxLat= y2 
                args[10] = "0";
//                folderPath = args[7];
//                exportPath = args[8];
//                emailPath = args[9];
                emailFlag = args[10];
                DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
                Date date = new Date();
                File exportDir = new File(exportPath);
                if (!exportDir.exists()) {
                    exportDir.mkdir();
                }
                String id = getRequestId();
                String name = args[0];
                String email = args[1];
                dataType type = dataType.valueOf(args[2]);
                folderPath += type.toString() + "_partitioned/";
                MBR area = new MBR(new Point(args[3], args[4]), new Point(args[5], args[6]));
                user = new User(id, name, email, area, type, exportPath + "id");
                RegisterToLog(user.toString());
                request.GetSmartOutput(id, args[3], args[4], args[5], args[6], folderPath, exportPath,type);

				GenerateKmlShapeFiles(type, request, id);

                user.setReportTime();
                if (emailFlag.equals("1")) {
                    Emailer.sendEmail(user, 1);
                }


            } catch (Exception ex) {
                try {
                    if (emailFlag.equals("1")) {
                        Emailer.sendEmail(user, 0);
                    }
                    ErrorLog(user.toString(), ex.getLocalizedMessage());
                    request.logStart("!!!!!!! Error accure");
                    final StringWriter sw = new StringWriter();
                    final PrintWriter pw = new PrintWriter(sw, true);
                    ex.printStackTrace(pw);
                    String message = sw.getBuffer().toString();
                    request.logEnd(message);

                    Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
                } catch (IOException ex1) {
                    Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex1);
                }
            } finally {
                try {
                    request.closeLog();
                } catch (IOException ex) {
                    Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        }
    }

    /**
     * This method return the request id of the user
     *
     * @return
     * @throws FileNotFoundException
     * @throws UnsupportedEncodingException
     * @throws IOException
     */
    private static String getRequestId() throws FileNotFoundException, UnsupportedEncodingException, IOException {
        Integer id = 0;
        File logFile = new File(exportPath + "log.csv");
        if (!logFile.exists()) {
            return "1";
        } else {
            InputStreamReader streamReader = new InputStreamReader(
                    new FileInputStream(logFile), "UTF-8");
            Runtime runtime = Runtime.getRuntime();
            Process process = runtime.exec("tail -n 1 " + logFile.getPath());
            BufferedReader input = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line = null;
            while ((line = input.readLine()) != null) {
                String[] array = line.split(",");
                id = Integer.parseInt(array[0]);
                id++;
            }
        }
        return id.toString();

    }

    /**
     * Add the request to the datalog file.
     *
     * @param text
     * @throws IOException
     */
    private static void RegisterToLog(String text) throws IOException {
        File logFile = new File(exportPath + "log.csv");
        boolean exist = logFile.exists();
        OutputStreamWriter outputStream;
        outputStream = new OutputStreamWriter(
                new FileOutputStream(logFile, true), "UTF-8");
        if (!exist) {
            outputStream.write("RequestId,RequestTime,userName, userEmail, DataType,"
                    + "max latitude, max longitude, "
                    + "min latitude, min longitude, location\n");
        }
        outputStream.write(text + "\n");
        outputStream.close();

    }

    /**
     * This method takes the request and the error message
     *
     * @param request
     * @param message
     * @throws IOException
     */
    private static void ErrorLog(String request, String message) throws IOException {
        File logFile = new File(exportPath + "error.csv");
        boolean exist = logFile.exists();
        OutputStreamWriter outputStream;
        outputStream = new OutputStreamWriter(
                new FileOutputStream(logFile, true), "UTF-8");
        if (!exist) {
            outputStream.write("RequestId,RequestTime,userName, userEmail, DataType,"
                    + "max latitude, max longitude, "
                    + "min latitude, min longitude, location ,Error message\n");
        }
        outputStream.write(request + "," + message.replace(",", "[comma]") + "\n");
        outputStream.close();
    }

    private static void GenerateKmlShapeFiles(dataType type, Request request, String id)
            throws IOException {
        if (type.equals(dataType.road_edges )
                || type.equals(dataType.river_edges)
//                || type.equals(dataType.coast_edges)
//                || type.equals(dataType.border_edges)
//                || type.equals(dataType.administrative_edges)
//                || type.equals(dataType.city_edges)
//                || type.equals(dataType.district_edges)
//                || type.equals(dataType.maritime_edges)
//                || type.equals(dataType.national_edges)
//                || type.equals(dataType.neighborhood_edges)
//                || type.equals(dataType.political_edges)
//                || type.equals(dataType.postal_edges)
//                || type.equals(dataType.region_edges)
//                || type.equals(dataType.region_edges)
                ) {
        	
        	//Generate kml file
//            request.logStart("Generate KML file");
//            kmlgenerator.KMLGenerator.runKMLConverterLine(
//                    exportPath + id + "/" + "edge.txt",
//                    exportPath + id + "/" + "node.txt");
//            request.logEnd("end generate KML file");
            
        } else {
        	//Generate kml file
        	String arg0[] = {
        			exportPath + id + "/" + "wkt.WKT",
        			exportPath + id + "/" + "result.kml "
        	}; 
        	OSMToKML.main(arg0);
        }
    	
        
        
        //Generate Shape file 
            request.logStart("Generate shape file");
            String commandLine = "sh " + System.getProperty("user.dir") + "/Extensions/kml2shape.sh "
                    + exportPath + id + "/" + id+".KML "
                    + exportPath + id + "/";
            System.out.println(commandLine);
            Process process = Runtime.getRuntime().exec(commandLine);
            request.logEnd("End generating shape file");
    }
    
   

    
}
