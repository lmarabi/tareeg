<?php

if ($_POST['action']=="coords") {

$type = $_POST['type'];
    switch ($type) {
        case 'Road Network':
            $table = 'road_edges';
            break;
        case 'Lakes':
            $table = 'lake_edges';
            break;
        case 'Rivers':
            $table = 'river_edges';
            break;
        case 'Borders - National\Country':
            $table = 'national_edges';
            break;
        case 'Borders - State\Region\Province':
            $table = 'region_edges';
            break;
        case 'Borders - County\District\Prefectures':
            $table = 'district_edges';
            break;
        case 'Borders - City\Municipality\Town':
            $table = 'city_edges';
            ;break;
        case 'Borders - Neighborhood\Suburb':
            $table = 'neighborhood_edges';
            ;break;
        case 'Borders - All':
            $table = 'border_edges';
            ;break;
        case 'Parks':
            $table = 'park_edges';
            ;break;
        case 'Buildings - Residential':
            $table = 'resident_edges';
            ;break;
        case 'Buildings - Commercial':
            $table = 'commerce_edges';
            ;break;
        case 'Buildings - Services':
            $table = 'services_edges';
            ;break;
        case 'Buildings - Sport':
            $table = 'sport_edges';
            ;break;
        case 'Buildings - Schools':
            $table = 'Education_edges';
            ;break;
        case 'Buildings - Worship':
            $table = 'worship_edges';
            ;break;
        case 'Buildings - All':
            $table = 'building_edges';
            ;break;
	case 'Cemetery':
            $table = 'cemetery_edges';
            ;break;
	case 'desert':
            $table = 'desert_edges';
            ;break;
	case 'Borders - region':
            $table = 'region_edges';
            ;break;
	case 'Borders - district':
            $table = 'district_edges';
            ;break;
	case 'Borders - city':
            $table = 'city_edges';
            ;break;
	case 'Borders - administrative':
            $table = 'administrative_edges';
            ;break;
	case 'Borders - postal':
            $table = 'postal_edges';
            ;break;
	case 'Borders - maritime':
            $table = 'maritime_edges';
            ;break;
	case 'Borders - political':
            $table = 'political_edges';
            ;break;
	case 'Borders - national':
            $table = 'national_edges';
            ;break;
        case 'Border - Coast line':
            $table = 'coast_edges';
            break;

    }

$coords = split(',', $_POST['coords']);
$latmax = $coords[0];
$latmin = $coords[1];
$lonmax = $coords[2];
$lonmin = $coords[3];

//$rName = $_POST['rName'];
$rName = 'Beta';
$rEmail = $_POST['rEmail'];
   
//args in the jar as following name  of the user, email, type , location, datafolder , exportfolder, email folder
//exec("java -jar -Xmx1024m /home/yackel/public_html/app/webroot/osme/OSMExtractor.jar $rName $rEmail $table $latmax $lonmax $latmin $lonmin /media/Louai/osm/ /home/yackel/public_html/app/webroot/downloads/userData/ /media/Louai/usersData/email/ 1");
exec("java -jar -Xmx2024m /home/yackel/public_html/app/webroot/osme/OSMExtractor.jar $rName $rEmail $table $latmax $lonmax $latmin $lonmin /media/osmeDataset/spatialHadoopPhase/ /home/yackel/public_html/app/webroot/downloads/userData/ /media/Louai/usersData/email/ 1");

  
 }
?>
