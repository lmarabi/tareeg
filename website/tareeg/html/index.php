<?php
if (isset($_POST['down'])) {
    $files = array('node.txt', 'edge.txt');
    $zipname = 'files.zip';
    $zip = new ZipArchive;
    $zip->open($zipname, ZipArchive::CREATE);
    foreach ($files as $file) {
        $zip->addFile($file);
    }
    $zip->close();
    if (file_exists($zipname)) {
        header('Content-Description: File Transfer');
        header('Content-Type: application/zip');
        header('Content-Disposition: attachment; filename=' . basename($zipname));
        header('Content-Length: ' . filesize($zipname));
        ob_clean();
        flush();
        readfile($zipname);
    }
}
?>
<!DOCTYPE html>
<html>
    <head>

        <link href="interface.css" rel="stylesheet" type="text/css" />
        <link href="tabcontent.css" rel="stylesheet" type="text/css" />
        <script src="tabcontent.js" type="text/javascript"></script>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>TAREEG Spatial information Extraction</title>
        <script src="jquery-1.8.3.min.js"></script>
        <script src="http://www.openlayers.org/api/OpenLayers.js"></script>
        <script type="text/javascript" src="osm_tools.js"></script>
        <script type="text/javascript" src="Export.js"></script>
        <script type="text/javascript" src="Import.js"></script>
        <script type="text/javascript" src="Path.js"></script>
	<script src="http://maps.google.com/maps/api/js?v=3.6&amp;sensor=false"></script>
<!-- Start: Copyright 2015 TraceMyIP.org Service Code (160158-12022015)- DO NOT MODIFY //-->
<div style="line-height:16px;text-align:center;display:none;"><script type="text/javascript" src="http://s2.tracemyip.org/tracker/lgUrl.php?stlVar2=1500|1449071991|10*2|0061E0*FFFBC4*FA0000*003091|1*1*0*1*0&amp;rgtype=4684NR-IPIB&amp;pidnVar2=75452&amp;prtVar2=11&amp;scvVar2=12"></script><div style="line-height:0px;"><a title="my ip" href="http://www.tracemyip.org/"><img src="http://log.tracemyip.org/tracker/script.gif" alt="my ip" style="border:0px;" /></a></div><noscript><div><img src="http://s2.tracemyip.org/tracker/1500|1449071991|10*2|0061E0*FFFBC4*FA0000*003091|1*1*0*1*0/4684NR-IPIB/75452/11/12/ans/" alt="my ip" style="border:0px;" /></div></noscript></div>
<!-- End: TraceMyIP.org Service Code //-->

    </head>



<Script>
$(document).ready(function(){
i	     //Add the current date of the day
	      var currentTime = new Date();
	      document.getElementById("TrafficRequest.name").value = "OSM Data "+currentTime;
	      document.getElementById("TrafficRequest.email").value = "user@org";
 
	
}); 
</script>



    <body>
        <div id="header">
<div style="font-family:verdana;padding:0px;border-radius:0px;border:6px solid #EE872A;">
            <img src="tareeglogosm.jpg" alt="Mountain View" style="width:304px;height:[D228px">
<table><tr><td>
                      <input id = "address" name = "searchValue" type = "text" size = "14"   onkeydown="if (event.keyCode == 13) codeAddress()"/></td>
                            <td><input type = "button" onclick = "codeAddress()"  name = "search" value = "Search Location"/></td></tr>

</table>&nbsp;&nbsp;
            <ul class="tabs">
                <li onclick="reset()"><a href="#" rel="view2">Extract</a></li>
                <li onclick="reset()"><a href="#" rel="view3">Visualize</a></li>
                <li onclick="reset()"><a href="#" rel="view1">About</a></li>
            </ul>

            <div class="tabcontents">
                <div id="view1" class="tabcontent">
		Publication: <br>
		<br><br>
		1- Louai Alarabi, Ahmed Eldawy, Rami Alghamdi, Mohamed F. Mokbel
                "<a href="http://www-users.cs.umn.edu/~louai/TAREEG_sigspatial2014.pdf" target="_blank"><font color="#0000ff">"TAREEG: A MapReduce-Based System for Extracting Spatial Data from OpenStreetMap </a></font>
             22nd ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (ACM SIGSPATIAL GIS 2014) <b>SIGSPATIAL 2014</b>

<br><br>
 2- Louai Alarabi, Ahmed Eldawy, Rami Alghamdi, Mohamed F. Mokbel.
                "<a href="http://www-users.cs.umn.edu/~louai/TAREEG_Sigmod2014.pdf" target="_blank"><font color="#0000ff">"TAREEG: A MapReduce-Based Web Service for Extracting Spatial Data from OpenStreetMap </a></font>
            To appear in Proceedings of ACM SIGMOD Conference on Management of Data, <b>SIGMOD 2014</b>, Snowbird, UT, USA, Jun, 2014. <br ><br>

			</div>
			<div id="view2" class="tabcontent">
			    <form name="export">
				Drag and draw to choose area : <br>
				<input type="radio" name="area" value="none" id="noneToggle" onclick="toggleControl(this);"checked> 
				<label for="noneToggle">Drag</label><br>
				<input type="radio" name="area" value="box" id="boxToggle" onclick="toggleControl(this);">
				<label for="boxToggle">Draw Box</label><br>
				Choose export type:
				<select id="type">
				   <option>Choose</option>
				    <option>Road Network</option>
				    <option>Lakes</option>
				    <!-- <option>Rivers</option> --!>
				    <option>Border - Coast line</option>
				    <option>Borders - National\Country</option>
				    <option>Borders - State\Region\Province</option>
				    <option>Borders - County\District\Prefectures</option>
				    <option>Borders - City\Municipality\Town</option>
				    <option>Borders - Neighborhood\Suburb</option>
				    <option>Borders - region</option>
				    <option>Borders - district</option>
				    <option>Borders - city</option>
				    <option>Borders - administrative</option>
				    <option>Borders - postal</option>
				    <option>Borders - maritime</option>
				    <option>Borders - political</option>
				    <option>Borders - national</option>
				    <option>Borders - All</option>
				    <option>Parks</option>
				    <option>Buildings - Residential</option>
				    <option>Buildings - Commercial</option>
				    <option>Buildings - Services</option>
				    <option>Buildings - Sport</option>
                            <option>Buildings - Schools</option>
                            <option>Buildings - Worship</option>
                            <option>Buildings - All</option>
                            <option>Cemetery</option>
			    <option>desert</option>	
                        </select><br>
                        <input Style="display:none" type="text" id="boxC" value="" name="coords">
		 <br></br>
                 <div id="panelForm">
		    Please enter the following information to request data:<br><br>
                    <input name="TrafficRequest.name1" id="name"  size="20" type="hidden" value="userrequest"><br>
                    Email: <input name="TrafficRequest.email1" id="email" size="20" type="text"><br>
                    <br>
                    <input type="button" value="Extract" onclick="exportForm()">
                 </div>
                         
                    </form>
                    <form method="POST" name="down"></form>
                </div>
                <div id="view3" class="tabcontent">

                    <br><text id="nodeErr">Choose a node file</text>
                    <input id="Nodes" type="file" value="Nodes file"/></button>
                    <button onclick="doErase('Nodes')"/>clear</button>

                    <br><text id="edgeErr">Choose a edge file</text>
                    <input id="Edges" type="file" value="Edges file"/></button>
                    <button onclick="doErase('Edges')"/>clear</button>

                    <button type="submit" id="startBtn"onclick="Importer()"/>Submit</button><br>


                </div>
            </div>
        </div>
</div>
        <div id="osm-map"></div>

    </body>

</html>

