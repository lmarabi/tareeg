package osmextractor;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.Properties;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;
import javax.mail.Address;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class Emailer {

    public static String HOST_NAME = "ibn-battuta-umh.cs.umn.edu";
    private static final String SMTP_HOST_NAME = "smtp.gmail.com";
    private static final int SMTP_HOST_PORT = 465;
    private static final String SMTP_AUTH_USER = "tareeg.cs.umn@gmail.com";//"openstreetmapextractor@gmail.com";
    private static final String SMTP_AUTH_PWD = "tareeg.louai";//"osmelouai";
    private static Main.dataType datatype;

    public static String downloadData(User userRquest) {
        String result;
        String path = Main.exportPath.substring(
                Main.exportPath.indexOf("downloads"), Main.exportPath.length());
        result =  "http://" + HOST_NAME + "/" + path
                + userRquest.getId() + "/Data.zip\n\n";
//                "CSV Format:\nhttp://" + HOST_NAME + "/" + path
//                + userRquest.getId() + "/node.txt.\n"
//                + "http://" + HOST_NAME + "/" + path
//                + userRquest.getId() + "/edge.txt.\n"
//                + "KML FILE:\n" + "http://" + HOST_NAME + "/" + path
//                + userRquest.getId() + "/result.kml.\n"
//                + "SHAPE FILES :\n" + "http://" + HOST_NAME + "/" + path
//                + userRquest.getId() + "/shapefile.shp\n"
//                + "http://" + HOST_NAME + "/" + path
//                + userRquest.getId() + "/shapefile.shx\n"
//                + "http://" + HOST_NAME + "/" + path
//                + userRquest.getId() + "/shapefile.prj\n"
//                + "http://" + HOST_NAME + "/" + path
//                + userRquest.getId() + "/shapefile.dbf\n\n";

        return result;
    }

    public static void sendEmail(User userRequest, int result)
            throws MessagingException, UnsupportedEncodingException, IOException {
        System.out.println(Main.emailPath + userRequest.getId() + ".txt");
        File file = new File(Main.emailPath + userRequest.getId() + ".txt");
        file.createNewFile();

        BufferedWriter br = null;
        try {
            br = new BufferedWriter(new FileWriter(file));
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            br.write("is going to get email parameters\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            br.write("setting email properties\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        Properties props = new Properties();

        props.put("mail.transport.protocol", "smtps");
        props.put("mail.smtps.host", SMTP_HOST_NAME);
        props.put("mail.smtps.auth", "true");

        try {
            br.write("creating mail session\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        Session mailSession = Session.getDefaultInstance(props);
        mailSession.setDebug(false);
        Transport transport = mailSession.getTransport();

        try {
            br.write("setting message content\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("reading file - louai");
        File nodeFile = new File(Main.exportPath + userRequest.getId() + "/node.txt");
        File edgeFile = new File(Main.exportPath + userRequest.getId() + "/edge.txt");
        File kmlFile = new File(Main.exportPath + userRequest.getId() + "/kml.KML");
        File shpFile = new File(Main.exportPath + userRequest.getId() + "/output.shp");
        File shxFile = new File(Main.exportPath + userRequest.getId() + "/output.shx");
        File dbfFile = new File(Main.exportPath + userRequest.getId() + "/output.dbf");
        File prjFile = new File(Main.exportPath + userRequest.getId() + "/output.prj");
        // Zip files into one zip file
        FileOutputStream fos = new FileOutputStream(Main.exportPath + userRequest.getId() + "/Data.zip");
        ZipOutputStream zos = new ZipOutputStream(fos);
        if(!shxFile.exists()|| 
                !kmlFile.exists() || !shpFile.exists() || !dbfFile.exists()
                || !prjFile.exists()){
            for(;;){
                if(shxFile.exists()&& kmlFile.exists() && shpFile.exists() && dbfFile.exists()
                &&prjFile.exists())
                    break;
            }
        }
        System.out.println("add zip file - louai");

        addToZipFile(nodeFile, zos);
        addToZipFile(edgeFile, zos);
        addToZipFile(kmlFile, zos);
        addToZipFile(shpFile, zos);
        addToZipFile(shxFile, zos);
        addToZipFile(dbfFile, zos);
        addToZipFile(prjFile, zos);
        zos.close();
        fos.close();
        
        int unkonwnSize = 12;
        /*
     15M	./result.kml
     7.1M	./shapefile.dbf
     * 
     4.0K	./shapefile.prj
     3.9M	./shapefile.shp
     360K	./shapefile.shx
         */
        long kmlSize = ((long) kmlFile.length() / 1024);
        long shpSize = ((long) shpFile.length() / 1024);
        long nodeSize = ((long) nodeFile.length() / 1024);
        long edgeSize = ((long) edgeFile.length() / 1024);
        long shxSize = ((long) shxFile.length() / 1024);
        long dbfSize = ((long) dbfFile.length() / 1024);
        long prjSize = ((long) prjFile.length() / 1024);
        nodeSize = (nodeSize == 0) ? unkonwnSize : nodeSize;
        edgeSize = (edgeSize == 0) ? unkonwnSize : edgeSize;
        kmlSize = (kmlSize == 0) ? (long)((nodeSize+edgeSize)*3.33333) : kmlSize;
        shpSize = (shpSize == 0) ? (long)(kmlSize*0.26) : shpSize;
        shxSize = (shxSize == 0) ? (long)(kmlSize*0.0234375) : shxSize;
        dbfSize = (dbfSize == 0) ? (long)(kmlSize*0.47) : dbfSize;
        prjSize = (prjSize == 0) ? (long)(kmlSize*0.000260417) : prjSize;
        //Delete files
//        nodeFile.delete();
//        edgeFile.delete();
//        kmlFile.delete();
//        shpFile.delete();
//        shxFile.delete();
//        dbfFile.delete();
//        prjFile.delete();
        
        MimeMessage message = new MimeMessage(mailSession);
        message.setSubject("TAREEG Request #" + userRequest.getId() + " has finished being processed.");
        String content = "";
        if (result == 1) {
            content = "Hi, Sir/Madam\n\n"
                    + "Your extracted spatial data, "
                    + " with the following parameters:\n"
                    + userRequest.getRequestParameter()
                    + " \n has finished.\n\n  You can download the data \n"
                    + downloadData(userRequest)
                    + " The estimated size of the node file is :"
                    + nodeSize + " KB \n"
                    + " The estimated size of the edge file is "
                    + edgeSize + " KB. \n"
                    + " The estimated size of the KML file is "
                    + kmlSize + " KB. \n"
                    + " The estimated size of the shape (shp) files is "
                    + shpSize + " KB. \n"
                    + " The estimated size of the shape (shx) files is "
                    + shxSize + " KB. \n"
                    + " The estimated size of the shape (prj) files is "
                    + prjSize + " KB. \n"
                    + " The estimated size of the shape (dbf) files is "
                    + dbfSize + " KB. \n"
                    + "The links of extracted data may be expired in one week.\n"
                    + ".\n\n You can also visualize the extracted data at the Visualize option on our website \n"
                    + "http://tareeg.org \n"
                    + "Please be adviced, the visualization maybe very slow or fail, when the data file is large\r\n\n"
                    + "If you have any comments, please  email us at tareeg.cs.umn@gmail.com.\r\n\r\n"
                    + "Thanks for using tareeg: mapreduce web-based spatial extractor ,\r\n"
                    + "KACST GIS Innovation Center - Louai Alarabi";


        } else {

            content = "Hi, Sir/Madam\n\n"
                    + "I'm sorry to inform you that your request, "
                    + "with the following parameters:\n"
                    + userRequest.getRequestParameter()
                    + "is failed. \n"
                    + "Most likely, "
                    + "the exported data is not supported yet.\n"
                    + "If you still get problems , please contact tareeg.cs.umn@gmail.com\n"
                     + "Thanks for using tareeg: mapreduce web-based spatial extractor ,\r\n"
                    + "KACST GIS Innovation Center- Louai Alarabi";
        }

        message.setContent(content, "text/plain");

        try {
            br.write("adding receiptant\nMessage Content:" + content + "\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        InternetAddress[] mntgAddress = new InternetAddress[1];
        mntgAddress[0] = new InternetAddress("tareeg.cs.umn@gmail.com", "TAREEG"); //here we set our email alias and the desired display name
        InternetAddress customer_email = new InternetAddress(userRequest.getEmail());//customer email

        message.addRecipient(Message.RecipientType.TO, customer_email);
        message.addRecipients(Message.RecipientType.CC, mntgAddress);
        message.addRecipients(Message.RecipientType.BCC, mntgAddress);

        try {
            br.write("adding reply to headers\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        message.setFrom(mntgAddress[0]);
        message.setReplyTo(mntgAddress);
        message.setSender(mntgAddress[0]);

        try {
            br.write("connecting to mail server\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        transport.connect(SMTP_HOST_NAME, SMTP_HOST_PORT, SMTP_AUTH_USER,
                SMTP_AUTH_PWD);

        try {
            br.write("seding the message\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        Address[] recipientsTo = message.getRecipients(Message.RecipientType.TO);
        Address[] recipientsCC = message.getRecipients(Message.RecipientType.CC);
        Address[] recipientsBCC = message.getRecipients(Message.RecipientType.BCC);

        Address[] allRecipients = new Address[recipientsTo.length + recipientsCC.length + recipientsBCC.length];
        int allIndex = 0;
        for (int i = 0; i < recipientsTo.length; ++i, ++allIndex) {
            allRecipients[allIndex] = recipientsTo[i];
        }
        for (int i = 0; i < recipientsCC.length; ++i, ++allIndex) {
            allRecipients[allIndex] = recipientsCC[i];
        }
        for (int i = 0; i < recipientsBCC.length; ++i, ++allIndex) {
            allRecipients[allIndex] = recipientsBCC[i];
        }

        transport.sendMessage(message, allRecipients);

        try {
            br.write("closing the connection\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
        transport.close();

        try {
            br.write("Done! message sent\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        InternetAddress notifyAddress = new InternetAddress("tareeg.cs.umn@gmail.com", "TAREEG Admin"); //here we set our email alias and the desired display name
        // sendEmail(mntgAddress[0], notifyAddress,
        //      "Minnesota Traffic Generator has been used today and the results for request #" + trafficRequest.getRequestId() + " has been submitted to the user on " + trafficRequest.getEmail() + ".", trafficRequest.getEmail());
        //InternetAddress notifyAddress2 = new InternetAddress("amr@cs.umn.edu", "Amr Magdy"); //here we set our email alias and the desired display name
        //sendEmail(mntgAddress[0],notifyAddress2,
        //		"Minnesota Traffic Generator has been used today and the results for request #"+trafficRequest.getRequestId()+" has been submitted to the user.");

        /*
         InternetAddress notifyAddress3 = new InternetAddress("mokbel@cs.umn.edu", "Mohamed Mokbel"); //here we set our email alias and the desired display name
         sendEmail(mntgAddress[0], notifyAddress3,
         "Minnesota Traffic Generator has been used today and the results for request #" + trafficRequest.getRequestId() + " has been submitted to the user on " + trafficRequest.getEmail() + "." , trafficRequest.getEmail());
         * 
         */

        try {
            br.write("Done sending notification messages\n");
            br.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            br.flush();
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void sendEmail(InternetAddress from, InternetAddress to, String content, String requester)
            throws MessagingException, UnsupportedEncodingException {

        Properties props = new Properties();

        props.put("mail.transport.protocol", "smtps");
        props.put("mail.smtps.host", SMTP_HOST_NAME);
        props.put("mail.smtps.auth", "true");

        Session mailSession = Session.getDefaultInstance(props);
        mailSession.setDebug(false);
        Transport transport = mailSession.getTransport();

        MimeMessage message = new MimeMessage(mailSession);
        message.setSubject("MN Traffic Generation is completed for " + requester);
        message.setContent(content, "text/plain");

        message.addRecipient(Message.RecipientType.TO, to);

        InternetAddress[] replyto = new InternetAddress[1];
        replyto[0] = from;

        message.setFrom(from);
        message.setReplyTo(replyto);
        message.setSender(from);

        transport.connect(SMTP_HOST_NAME, SMTP_HOST_PORT, SMTP_AUTH_USER,
                SMTP_AUTH_PWD);

        transport.sendMessage(message,
                message.getRecipients(Message.RecipientType.TO));

        transport.close();

    }
    
    public static void addToZipFile(File file, ZipOutputStream zos) throws FileNotFoundException, IOException {

		FileInputStream fis = new FileInputStream(file);
		ZipEntry zipEntry = new ZipEntry(file.getName());
		zos.putNextEntry(zipEntry);

		byte[] bytes = new byte[1024];
		int length;
		while ((length = fis.read(bytes)) >= 0) {
			zos.write(bytes, 0, length);
		}

		zos.closeEntry();
		fis.close();
	}
    
}
