/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package osmextractor;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author turtle
 */
public class OSMExtractor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        if (args.length == 1) {
            System.out.println("To run this program you need to pass the following "
                    + "Information \n"
                    + "MNTGExtractor.jar DatasourceDir outputDir userID"
                    + "MinLat MinLon MaxLat MaxLon \n OR \n"
                    + "MNTGExtractor.jar DatasourceDir outputDir userID"
                    + "south west north east");
        } else if (args.length == 7) {
            try {
                double startTime = System.currentTimeMillis();
                String folderPath = args[0];
                Request request;
                String exportpath = args[1];
                request = new Request();
                System.out.println("Selected MBR "
                        + "Min(" + args[3] + "," + args[4] + ")  - "
                        + "Max(" + args[5] + "," + args[6] + ")");
                request.GetSmartOutput(args[2], args[5], args[6], args[3], args[4], folderPath, exportpath);
                double endTime = System.currentTimeMillis();
                System.out.println("query time = " + (endTime - startTime) + " ms");

            } catch (IOException ex) {
                Logger.getLogger(OSMExtractor.class.getName()).log(Level.SEVERE, null, ex);
                System.out.println("Error Happen");
            }

        } else if (args.length == 8) {
            try {
                double startTime = System.currentTimeMillis();
                String folderPath = args[0];
                Request request;
                String exportpath = args[1];
                request = new Request();
                System.out.println("Selected MBR "
                        + "Min(" + args[3] + "," + args[4] + ")  - "
                        + "Max(" + args[5] + "," + args[6] + ")");
                request.GetOutput(args[2], args[5], args[6], args[3], args[4], folderPath, exportpath);
                double endTime = System.currentTimeMillis();
                System.out.println("query time = " + (endTime - startTime) + " ms");

            } catch (IOException ex) {
                Logger.getLogger(OSMExtractor.class.getName()).log(Level.SEVERE, null, ex);
                System.out.println("Error Happen");
            }
        } else {
            System.out.println("Wrong args type --help");
        }


        /*
       
         try {
         double startTime = System.currentTimeMillis();
         String folderPath = System.getProperty("user.dir")+"/Data/";
         //String folderPath = "/media/turtle/Seagate Expansion Drive/Louai/osm/road_edges_partitioned/";
         Request request;
         String exportpath = System.getProperty("user.dir")+"/Export/";
         //35.707074366952604,51.195173263550096,35.77896766857732,51.29885673523019
         request = new Request();
         request.GetOutput("3",  
         "35.77896766857732","51.29885673523019",
         "35.707074366952604" ,"51.195173263550096",
         folderPath,
         exportpath);
            
         request.GetSmartOutput("4",  
         "35.77896766857732","51.29885673523019",
         "35.707074366952604" ,"51.195173263550096",
         folderPath,
         exportpath);
            
         double endTime = System.currentTimeMillis();
         System.out.println("query time = "+(endTime-startTime)+" ms");
            
         } catch (IOException ex) {
         Logger.getLogger(OSMExtractor.class.getName()).log(Level.SEVERE, null, ex);
         System.out.println("Error Happen");
         } 
         */

    }
}
