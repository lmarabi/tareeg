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
import java.util.Iterator;
import java.util.List;

import edu.umn.cs.spatialHadoop.osm.OSMToKML;
import osmextractor.Main.dataType;

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

		node, edge, unsortedNode, wkt,output
	}

	public Request() {
		area = new MBR();
	}

	public MBR getArea() {
		return area;
	}

	/**
	 * Get the result and remove the redundant edge and nodes
	 * 
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
	public void GetResult(String id, double minLon, double minLat,
			double maxLon, double maxLat, String dataPath, String exportPath)
			throws FileNotFoundException, UnsupportedEncodingException,
			IOException {
		this.outwriter = new OutputStreamWriter[exportType.values().length];
		exportPath += id + "/";
		File dir = new File(exportPath);
		dir.mkdir();
		// this.outwriter[exportType.node.ordinal()] =
		// new OutputStreamWriter(
		// new FileOutputStream(
		// exportPath + exportType.node.toString() + ".txt"), "UTF-8");
		this.outwriter[exportType.edge.ordinal()] = new OutputStreamWriter(
				new FileOutputStream(exportPath + exportType.edge.toString()
						+ ".txt"), "UTF-8");
		this.outwriter[exportType.edge.ordinal()] = new OutputStreamWriter(
				new FileOutputStream(exportPath
						+ exportType.unsortedNode.toString() + ".txt"), "UTF-8");
		// Set the area of interest in the MBR
		this.area = new MBR(new Point(minLon, minLat),
				new Point(maxLon, maxLat));
		// Get the set of Files that intersect with the area.
		List<Partition> files = ReadMaster(dataPath);
		// read eachfile and output the result.
		for (Partition f : files) {
			// Build the edge and the node from the file
			area.BuildNodeEdges(f.getPartition());
		}
		// Write the output in the file
		for (Point p : area.getNodes()) {
			outwriter[exportType.node.ordinal()].write(p.toString() + "\n");

		}
		for (Edge e : area.getEdges()) {
			outwriter[exportType.edge.ordinal()].write(e.toString() + "\n");
		}

		outwriter[exportType.edge.ordinal()].close();
		outwriter[exportType.node.ordinal()].close();
	}

	/**
	 * This method output the result directly without check for redundant tuples
	 * 
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
	public void GetOutput(String id, String minLon, String minLat,
			String maxLon, String maxLat, String dataPath, String exportPath)
			throws FileNotFoundException, UnsupportedEncodingException,
			IOException {
		this.outwriter = new OutputStreamWriter[exportType.values().length];
		exportPath += id + "/";
		File dir = new File(exportPath);
		dir.mkdir();
		this.outwriter[exportType.node.ordinal()] = new OutputStreamWriter(
				new FileOutputStream(exportPath + exportType.node.toString()
						+ ".txt"), "UTF-8");
		this.outwriter[exportType.edge.ordinal()] = new OutputStreamWriter(
				new FileOutputStream(exportPath + exportType.edge.toString()
						+ ".txt"), "UTF-8");
		// Set the area of interest in the MBR
		this.area = new MBR(new Point(minLon, minLat),
				new Point(maxLon, maxLat));
		// Get the set of Files that intersect with the area.
		logStart("start reading the master files");
		List<Partition> files = ReadMaster(dataPath);
		logEnd("end reading master file and selected (" + files.size() + ")");
		// read eachfile and output the result.
		logStart("start reading from selected files");
		for (Partition f : files) {
			System.out.println("Start Reading file "
					+ f.getPartition().getName());
			// Build the edge and the node from the file
			area.BuildNodeEdges(f, outwriter[exportType.edge.ordinal()],
					outwriter[exportType.node.ordinal()]);
			System.out
					.println("End reading file " + f.getPartition().getName());
		}

		// Write the output in the file because node need to be store in
		// memory to remove duplicate.
		// for (Point p : area.getNodes()) {
		// outwriter[exportType.node.ordinal()].write(p.toString()+"\n");
		//
		// }
		Iterator itr = area.getNodehased().iterator();
		while (itr.hasNext()) {
			Object element = itr.next();
			outwriter[exportType.node.ordinal()].write(element.toString()
					+ "\n");
		}
		logEnd("end reading files");
		outwriter[exportType.edge.ordinal()].close();
		outwriter[exportType.node.ordinal()].close();
	}

	public void GetSmartOutput(String id, String minLon, String minLat,
			String maxLon, String maxLat, String dataPath, String exportPath,
			dataType type) throws FileNotFoundException,
			UnsupportedEncodingException, IOException {
		this.outwriter = new OutputStreamWriter[exportType.values().length];
		exportPath += id + "/";
		File dir = new File(exportPath);
		dir.mkdir();
		this.statusLog = new OutputStreamWriter(new FileOutputStream(exportPath
				+ "log.txt"), "UTF-8");
		this.outwriter[exportType.wkt.ordinal()] = new OutputStreamWriter(
				new FileOutputStream(exportPath + exportType.wkt.toString()
						+ ".WKT"), "UTF-8");
		this.outwriter[exportType.output.ordinal()] = new OutputStreamWriter(
				new FileOutputStream(exportPath + exportType.output.toString())
				, "UTF-8");
		if (type.equals(dataType.road_edges)
				|| type.equals(dataType.river_edges)) {
			this.outwriter[exportType.unsortedNode.ordinal()] = new OutputStreamWriter(
					new FileOutputStream(exportPath
							+ exportType.unsortedNode.toString() + ".txt"),
					"UTF-8");
			this.outwriter[exportType.edge.ordinal()] = new OutputStreamWriter(
					new FileOutputStream(exportPath
							+ exportType.edge.toString() + ".txt"), "UTF-8");
			// add header in edge file
			outwriter[exportType.edge.ordinal()]
					.write("Edge_id,Start_Node_id,End_Node_id,Tags\n");
			this.outwriter[exportType.wkt.ordinal()]
					.write("edgeId"+"\t"+"geometry"+"\t"+"tags\n");
		}

		// Set the area of interest in the MBR
		this.area = new MBR(new Point(minLon, minLat),
				new Point(maxLon, maxLat));
		// Get the set of Files that intersect with the area.
		logStart("start reading the master files");
		List<Partition> files = ReadMaster(dataPath);
		logEnd("end reading master file and selected (" + files.size() + ")");
		// read eachfile and output the result.
		logStart("start reading from selected files");
		for (Partition f : files) {
			logStart("Start Reading file " + f.getPartition().getName());
			// Build the edge and the node from the file
			if (type.equals(dataType.road_edges)
					|| type.equals(dataType.river_edges)) {
				area.smartBuildNodeEdges(f,
						outwriter[exportType.edge.ordinal()],
						outwriter[exportType.unsortedNode.ordinal()],
						outwriter[exportType.wkt.ordinal()],
						outwriter[exportType.output.ordinal()]);
			} else {
				area.rangeQueryRtree(f, outwriter[exportType.wkt.ordinal()]);
			}
			logEnd("End reading file " + f.getPartition().getName());
		}

		// Iterator itr = area.getNodehased().iterator();
		// while(itr.hasNext()){
		// Object element = itr.next();
		// outwriter[exportType.node.ordinal()].write(element.toString()+"\n");
		// }
		logEnd("end reading files");
		outwriter[exportType.wkt.ordinal()].close();
		outwriter[exportType.output.ordinal()].close();
		if (type.equals(dataType.road_edges)
				|| type.equals(dataType.river_edges)) {
			outwriter[exportType.edge.ordinal()].close();
			outwriter[exportType.unsortedNode.ordinal()].close();

			String arg0[] = { exportPath + "output",
					exportPath + id + "_result.kml" };
			OSMToKML.main(arg0);
			logStart("Remove duplicate nodes");
			String commandLine = "sh " + System.getProperty("user.dir")
					+ "/Extensions/getNode.sh " + exportPath
					+ exportType.unsortedNode.toString() + ".txt " + exportPath
					+ exportType.node.toString() + ".txt";
			System.out.println(commandLine);
			Process process = Runtime.getRuntime().exec(commandLine);
			logEnd("End duplicate nodes");
		}

	}

	/**
	 * output message and start a timer to check the time
	 * 
	 * @param text
	 */
	public static void logStart(String text) throws IOException {
		startTime = System.currentTimeMillis();
		text += "\n";
		System.out.print(text);
		statusLog.write(text);
	}

	/**
	 * End the message and show the time in second
	 * 
	 * @param text
	 */
	public static void logEnd(String text) throws IOException {
		endTime = System.currentTimeMillis();
		text = text + " which took" + " " + ((endTime - startTime) / 1000)
				+ " seconds\n";
		System.out.print(text);
		statusLog.write(text);
	}

	// this method to close the log.
	public static void closeLog() throws IOException {
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
	private List<Partition> ReadMaster(String path)
			throws FileNotFoundException, IOException {
		File master;
		List<Partition> result = new ArrayList<Partition>();
		master = new File(path + "_master.rtree");
		BufferedReader br = new BufferedReader(new FileReader(master));
		String line = null;

		while ((line = br.readLine()) != null) {
			String[] temp = line.split(",");
			// The file has the following format as Aggreed with the interface
			// between hadoop and this program
			// #filenumber,minLat,minLon,maxLat,maxLon
			if (temp.length == 8) {
				Partition part = new Partition(line, path);
				if (area.Intersect(part.getArea().getMin(), part.getArea()
						.getMax())) {
					result.add(part);
				}
			}
		}
		br.close();
		return result;
	}
}
