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
public class Polygon {
    List<List<Double>> nodes;
    String tags;
    
    public Polygon() {
        nodes = new ArrayList();
        //tags = new ArrayList();
    }
}