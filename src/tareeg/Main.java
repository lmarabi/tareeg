package tareeg;

import java.io.DataInput;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;

import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;

import edu.umn.cs.spatialHadoop.core.RTree;
import edu.umn.cs.spatialHadoop.core.Rectangle;
import edu.umn.cs.spatialHadoop.core.ResultCollector;
import edu.umn.cs.spatialHadoop.osm.OSMEdge;
import edu.umn.cs.spatialHadoop.osm.OSMPolygon;
import edu.umn.cs.spatialHadoop.osm.OSMToKML;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		System.out.println("Strat reading information form partition");
		RTree<OSMEdge> rtree = new RTree<OSMEdge>();
		rtree.setStockObject(new OSMEdge());
		String pathname = "/export/scratch/louai/scratch1/workspace/dataset/osm/osmIndex/river_network.rtree/part-00000.rtree";
		
		Path file = new Path(pathname);
		org.apache.hadoop.conf.Configuration conf = new  org.apache.hadoop.conf.Configuration();
		FileSystem fs = file.getFileSystem(conf);
		System.out.println("Path: "+file.getName());
		FSDataInputStream in = fs.open(file);
		in.skip(8);
		rtree.readFields(in);
		//minlon, minlat , maxlong maxlat 
		Rectangle mbr = new Rectangle(-180, -90, 180, 90);
		
		String outputfile = "/export/scratch/louai/scratch1/workspace/dataset/osm/osmIndex/outputFile_network";
		final OutputStreamWriter writer = new OutputStreamWriter(new FileOutputStream(outputfile));
		
		ResultCollector<OSMEdge> output = new ResultCollector<OSMEdge>() {
			
			@Override
			public void collect(OSMEdge arg0) {
				//System.out.println(arg0.toText(new Text()).toString());
				try {
					writer.write(arg0.toText(new Text()).toString()+"\n");
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				

			}
		};
		
		
		
		int results = rtree.search(mbr, output);
		System.out.println("number of restuts: "+results);
		String[] parameter = {outputfile,"/export/scratch/louai/scratch1/workspace/dataset/osm/osmIndex/outputFile_network.kml "};
		writer.close();
		OSMToKML.main(parameter);
		System.out.println("End");

	}
	
	
	/**
	 * This must give the exact partion that you want to query from. 
	 * First step: find the exact partition from the master code. 
	 * Next then 
	 * @throws IOException
	 */
	public static void QueryOSMPolygon() throws IOException{
		System.out.println("Strat reading information form partition");
		RTree<OSMPolygon> rtree = new RTree<OSMPolygon>();
		rtree.setStockObject(new OSMPolygon());
		String pathname = "/export/scratch/louai/scratch1/workspace/dataset/osm/osmIndex/postal_codes.rtree/part-00003.rtree";
		
		Path file = new Path(pathname);
		org.apache.hadoop.conf.Configuration conf = new  org.apache.hadoop.conf.Configuration();
		FileSystem fs = file.getFileSystem(conf);
		System.out.println("Path: "+file.getName());
		FSDataInputStream in = fs.open(file);
		in.skip(8);
		rtree.readFields(in);
		//minlon, minlat , maxlong maxlat 
		Rectangle mbr = new Rectangle(-180, -90, 180, 90);
		
		String outputfile = "/export/scratch/louai/scratch1/workspace/dataset/osm/osmIndex/outputFile";
		final OutputStreamWriter writer = new OutputStreamWriter(new FileOutputStream(outputfile));
		
		ResultCollector<OSMPolygon> output = new ResultCollector<OSMPolygon>() {
			
			@Override
			public void collect(OSMPolygon arg0) {
				System.out.println(arg0.toText(new Text()).toString());
				try {
					writer.write(arg0.toText(new Text()).toString()+"\n");
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				

			}
		};
		
		
		
		int results = rtree.search(mbr, output);
		System.out.println("number of restuts: "+results);
		String[] parameter = {outputfile,"/export/scratch/louai/scratch1/workspace/dataset/osm/osmIndex/outputFile2.kml "};
		writer.close();
		OSMToKML.main(parameter);
		System.out.println("End");
	}
	
	

}
