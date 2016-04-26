/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package osmextractor;

import java.io.File;

import osmextractor.Main.dataType;

public class Partition {
	private int id;
	private File partition;
	private MBR area;
	private long cardinality;

	public Partition() {
	}

	// public Partition(File partition, MBR area) {
	// this.partition = partition;
	// this.area = area;
	// }

	public Partition(String line, String path,dataType type) {
		String[] temp = line.split(",");
		if (temp.length == 8) {
			this.id = Integer.parseInt(temp[0]);
			Point pointMin;
			Point pointMax;
			if(type.equals(dataType.road_edges)){
				 pointMin = new Point(temp[2], temp[1]);
				 pointMax = new Point(temp[4], temp[3]);
			}else{
				 pointMin = new Point(temp[1], temp[2]);
				 pointMax = new Point(temp[3], temp[4]);
			}
			this.area = new MBR(pointMin,pointMax);
			this.partition = new File(path + temp[7]);
			this.cardinality = Long.parseLong(temp[5]);
		}
	}

	public File getPartition() {
		return partition;
	}

	public void setPartition(File partition) {
		this.partition = partition;
	}

	public MBR getArea() {
		return area;
	}

	public void setArea(MBR area) {
		this.area = area;
	}

	public void setCardinality(long cardinality) {
		this.cardinality = cardinality;
	}
	
	public int getId(){
		return this.id;
	}

	/**
	 * Cardinality of the partition is the number of rows in this partition
	 * 
	 * @return
	 */
	public long getCardinality() {
		return cardinality;
	}

}
