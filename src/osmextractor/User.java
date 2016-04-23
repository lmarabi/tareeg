/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package osmextractor;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;
import osmextractor.Main.dataType;

/**
 *
 * @author turtle
 */
public class User {
    private String id;
    private String name;
    private String email;
    private Point max;
    private Point min;
    private String outputFile;
    private String reportTime;
    private String requestTime;
    private Main.dataType extractedType;
    private String location = "OpenStreetMap";

    public User() {
        this.id = "";
        this.name = "";
        this.email = "";
        this.min = new Point();
        this.max = new Point();
        this.extractedType = dataType.desert_edges;
        this.outputFile = outputFile;
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = new Date(); 
        this.requestTime = dateFormat.format(date);
    }

    public User(String id,String name, String email, MBR request,
            Main.dataType extractedType,String outputFile) {
        this.id = id;
        this.name = name.replace(",", ":");
        this.email = email;
        this.min = request.getMin();
        this.max = request.getMax();
        this.extractedType = extractedType;
        this.outputFile = outputFile;
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = new Date(); 
        this.requestTime = dateFormat.format(date);
        //this.location = getLocationName();
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setMax(Point max) {
        this.max = max;
    }

    public void setMin(Point min) {
        this.min = min;
    }

    public Point getMax() {
        return max;
    }

    public Point getMin() {
        return min;
    }

    public void setExtractedType(dataType extractedType) {
        this.extractedType = extractedType;
    }

    public dataType getExtractedType() {
        return extractedType;
    }

    public void setOutputFile(String outputFile) {
        this.outputFile = outputFile;
    }

    public String getOutputFile() {
        return outputFile;
    }

    public String getReportTime() {
        return reportTime;
    }
    
     public String getRequestParameter(){
         return "Extracted data: "+this.extractedType.toString().replace("_", " ") +"\n"
                 + "Area as (lattitude,longitude):  ("+this.max.getX()+","
                 + this.max.getY()+") - ("+this.min.getX()+","
                 + this.min.getY()+")\n"
                 + location
                 + " \nRequested on :"+ this.requestTime + "\n"
                 + "Reported on :"+ this.reportTime;
     }

    
 public void setRequestTime() {
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = new Date(); 
        this.requestTime = dateFormat.format(date);
    }
 
    public void setReportTime() {
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = new Date(); 
        this.reportTime = dateFormat.format(date);
    }
    
    
     public String getLocationName() {

        
         
        String semanticlocation = null;

        double lat = (this.min.getX() + this.max.getX()) / 2;
        double lng = (this.min.getY() + this.max.getY()) / 2;
        double n = this.max.getX();
        double w = this.max.getY();
        double s = this.min.getX();
        double e = this.min.getY();


        URL geourl;
        URLConnection geourlConn;
        DataInputStream geodis;
        //String[] ss = location.split("%20");
        //loc.split(" ");
        String googlemapapi = "http://maps.googleapis.com/maps/api/geocode/json?address=";
        googlemapapi = googlemapapi + lat + "," + lng + "&sensor=false&bounds=" + s + "," + w + "|" + n + "," + e;

        ////}
        JsonParser jp = new JsonParser();
        //googlemapapi += "&sensor=false";
        // System.out.println(googlemapapi);
        System.out.println(googlemapapi);
        try {
            geourl = new URL(googlemapapi);

            geourlConn = geourl.openConnection();
            String line;
            StringBuilder builder = new StringBuilder();
            BufferedReader reader = new BufferedReader(new InputStreamReader(geourlConn.getInputStream()));
            line = reader.readLine();

            while ((line = reader.readLine()) != null) {

                builder.append(line);
            }
            System.out.println(builder.toString());
            // System.out.println("{"+builder.toString()+"}");
            JsonElement geojson = jp.parse("{" + builder.toString() + "}");
            System.out.println(builder.toString());
            //JsonObject geoJO=geojson.getAsJsonObject();
            // JSONObject geoJO= new JSONObject(builder.toString());
            JsonObject geojo = geojson.getAsJsonObject();
           
            JsonElement mylocation = geojo.get("results").getAsJsonArray().get(0).getAsJsonObject().get("formatted_address");
           
            semanticlocation = mylocation.toString();
            System.out.println(mylocation.toString());

        } catch (Exception ex) {
            System.out.println("Problem accure here ");
            Logger.getLogger(User.class.getName()).log(Level.SEVERE, null, ex);
        }
        return semanticlocation.replace(",", ":");
        
    }
    
    /**
     * The return format of this method is as following 
     * NowTime,user name, user email, Extracted data, reportTime,
     * max latitude, max longitude, min latitude, min longitude, location name.
     * @return 
     */
    @Override
    public String toString() {
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = new Date();
        return  this.id+","+dateFormat.format(date)+","+this.name+","+this.email+","+
                this.extractedType.toString()+","+
                //this.reportTime+","+
                this.max.getX()+","+
                this.max.getY()+","+
                this.min.getX()+","+
                this.min.getY()+","+location;
    }
    
    
}
