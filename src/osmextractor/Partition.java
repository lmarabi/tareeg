/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package osmextractor;

import java.io.File;

/**
 *
 * @author turtle
 */
public class Partition {
    private File partition;
    private MBR area;

    public Partition() {
    }

    public Partition(File partition, MBR area) {
        this.partition = partition;
        this.area = area;
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
    
    
    
}
