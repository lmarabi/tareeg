/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package kmlgenerator;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author rami
 */
public class Edge {
    String tag;
    List<Long> edge = new ArrayList(2);
    
    public Edge(String x, List<Long> y) {
        tag = x;
        edge = y;
    }
}
