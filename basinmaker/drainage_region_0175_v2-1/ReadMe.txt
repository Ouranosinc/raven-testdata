---------------------------
North American Lake-River Routing Product v 2.1, derived by BasinMaker GIS Toolbox
Readme created: April 3, 2021
---------------------------
Thank you for downloading our lake-river routing product.  In your publication using 
the version 2.1 of the routing product, please cite the following paper:

BasinMaker: a GIS toolbox for distributed watershed delineation of complex lake 
and river routing networks. Han, M., H. Shen, B. A. Tolson, J. R. Craig, J. Mai, 
S. Lin, N. Basu, F. Awol, submitted April 2021 to Environmental Modelling and Software. 

(But please also check BasinMaker website where you downloaded this for most up 
to date citation)

Note that version 1.0 of this product covered only Canada and used a different DEM 
and is described in the following paper: 
Han, M., J. Mai, B. A. Tolson, J. R. Craig, E. Gaborit, H. Liu, K. Lee, Subwatershed-based 
lake and river routing products for hydrologic and land surface models applied over 
Canada, Canadian Water Resources Journal, 45(3), doi.org/10.1080/07011784.2020.1772116.

The lake-river routing product provides a routing structure (which here refers to 
both the topology of the stream network and the contributing areas to individual 
lakes and stream reaches), to correctly represent lakes and be easily customized 
based on various user requirements. BasinMaker, which is a GIS toolbox to delineate 
watersheds with lakes, was used to develop this routing product. In this routing 
product, each lake is represented by a lake catchment. A lake catchment is defined 
by the following rules:1) The extent of the lake catchment will fully cover the lake; 
2) the outlet of the lake catchment is the same as the outlet of the lake; 3) each 
lake’s inlets are treated as a catchment outlet. In this way, both inflow and outflow 
of each lake can be explicitly simulated by hydrologic routing models.

The extent of the product covers the main drainage regions across North America 
(Canada and the USA). For user's convenience, the routing product was divided into  
separate component drainage regions across North America.  Because the extent of  
some drainage regions could still be very large, the routing product of each drainage   
region was further divided into several separate component sub-drainage regions. 

The extent and the location of each drainage region can be found in:
    http://hydrology.uwaterloo.ca/basinmaker/download_regional.html
The extent and the location of each sub-region within each drainage region can 
be found in:
    http://hydrology.uwaterloo.ca/basinmaker/download_local.html
The entire product covering all of North America can be viewed and downloaded as 
an entire domain here: 
    http://hydrology.uwaterloo.ca/basinmaker/download_global.html
 
The name of the routing product file/folder follow these rules:
    - drainage_region_0:          in this folder/zip file, the entire routing  
                                  product covering the North America is contained.
    - drainage_region_XXXX:       in this folder/zip file, the routing product  
                                  covering the drainage region XXXX is contained.
    - drainage_region_XXXX_YYYYY: in this folder/zip file, the routing product 
                                  covering the sub-region YYYYY within drainage 
                                  region XXXX is contained.
You downloaded the routing product for one of the above three sort of domains.            

Within each routing product folder/zip file, following eight GIS layers are included:
(Note that for drainage_region_0.zip, GIS files are saved in a geodatabase 
drainage_region_0_v2-0.gdb within the folder/zip file)

1.     finalcat_info.*:     the GIS layer containing catchment/subbasin polygons 
       which respect the lake inflow and outflow routing structures. Note that we  
       use the words catchment and subbasin interchangeably in this document. This 
       layer contains all the necessary information for hydrologic routing through 
       the lake-river network.
2.     finalcat_info_riv.*: the GIS layer containing river network polylines in 
       each catchment polygon from #1 above. Note that some catchments from #1 
       have no polylines (river channel length of zero in #1) and these catchments 
       are not included in this layer. The columns in this layer’s attribute table 
       are the same as the columns in the finalcat_info.* attribute table. 
3.     sl_connected_lake.*: the GIS layer containing the lake polygons of lakes 
       that are connected by the finalcat_info_riv.*. Connected lakes (CL) outlets 
       are explicitly connected to a downstream non-zero length river channel in 
       the routing product. The lake polygons are obtained from HydroLAKES database 
       (Messager et al., 2016).
4.     sl_non_connected_lake.*: the GIS layer containing the lake polygons of 
       lakes that are not connected by the finalcat_info_riv.*. Note that although 
       a non-connected lake (NCL) outlet also defines a catchment outlet, and each 
       such catchment is considered to be a contributing area to flows downstream, 
       an NCL is not explicitly connected to the downstream routing network. The 
       connection is more implicit. Users routing with our network are responsible 
       for ensuring appropriate connections are established when routing with NCLs.  
       See the NCL note below for more details. The lake polygons are obtained from 
       HydroLAKES database (Messager et al., 2016).
5.     obs_gauges.* : the GIS layer containing streamflow observation gauges included 
       in the routing product. The stream flow observation gauges for watersheds 
       in Canada are obtained from HYDAT database; While the streamflow observation 
       gauges for watersheds in the USA are obtained from the USGS website. Note 
       a small fraction of streamflow gauges are not included in the product because 
       they could not be reasonably snapped to the river network. This includes 
       any gauge 1 km or more away from the closest part of the routing product 
       river network.  
6.     drainage_region_outline_XXXX_YYYYY.* : the GIS layer containing outline 
       of sub-region YYYYY within region XXXX. Note: There is also a 
       drainage_region_outline_XXXX_YYYYYY.geojson available.
7.     catchment_without_merging_lakes.*: the GIS layer containing catchment polygons
       of an incomplete routing product. In this incomplete routing product catchment 
       polygons covered by the same lake are not merged into one lake catchment 
       yet. So, these polygons are not the same polygons in GIS file #1 above. 
       This incomplete routing product layer is only intended as input to customize 
       the routing product with our BasinMaker GIS toolbox (for example by defining 
       new lake area thresholds and/or a new catchment minimum drainage area threshold). 
       Although the attribute table columns are named the same as the columns in finalcat_info.*, 
       attributes by the same name are not necessarily equivalent to one another.
8.     river_without_merging_lakes.*: the GIS layer containing river polylines 
       of an incomplete routing product. In this incomplete routing product, the 
       river polylines covered by the same lake are not merged into one river segment 
       yet. So, these polylines are not the same polylines in GIS file #2 above. 
       This incomplete routing product layer is only intended as input to customize 
       the routing product with our BasinMaker toolbox. Note that some catchments 
       from #7 have no polylines (river channel length of zero in #7) and these 
       incomplete routing product catchments are not included in this layer. 
       Although the attribute table columns are named the same as the columns in 
       finalcat_info.*, attributes by the same name are not necessarily equivalent 
       to one another. Attribute definitions are consistent here with GIS layer 
       #7 above.

The attribute table variable definitions are documented in a downloadable file 
on the BasinMaker website: http://hydrology.uwaterloo.ca/basinmaker/index.html


NOTE on non-connected lakes (NCLs):

Both connected lakes (CLs) and NCLs within a watershed are considered to be contributing 
areas of the watershed. As such, both CLs and NCLs will drain to the outlet of 
the watershed. The lake outlet for both a CL and an NCL define a catchment outlet. 
The only difference between CLs and NCLs is that CLs always drain into an explicitly 
represented river channel that is connected to the lake outlet while NCLs do not. 
NCLs exist because for smaller catchments, flow accumulation threshold settings 
can sometimes suppress the creation of a river channel at the lake outlet. As such, 
NCLs should drain directly, via a zero length flow path, into the next downstream 
catchment. Users need to ensure their hydrologic routing model accomplishes this. 
Specific hydrologic routing logic is as follows for NCLs: NCL catchment outflows 
need to be delivered to the next downstream river channel and if that river channel 
has a zero length (only possible if downstream catchment is also a lake catchment), 
that water must be delivered directly to the lake in this downstream catchment.  


---------------------------
How to use
---------------------------
There are two primary uses of the suite of GIS layers describing the routing product:
A) Use product for routing or other drainage network analysis at the current resolution. 
   For example, generating vector-based hydrologic routing model inputs (Raven 
   modelers can do this automatically via BasinMaker post-processing). In this 
   case all the data you will need is found in GIS layer #1. Layers #2 through #6 
   are included to show locations of lakes, rivers, region outlines etc. on a map.
B) Use product as an input to our BasinMaker GIS toolbox. In this case, in addition 
   to layer #1, BasinMaker requires intermediate layers #7 and #8 as inputs.  
   BasinMaker allows users to simplify or remove detail from an original lake-river 
   routing network that was already delineated.

Users are encouraged to follow the documentation available on the BasinMaker website: 
   http://hydrology.uwaterloo.ca/basinmaker/index.html

   
---------------------------
Authors
---------------------------
BasinMaker and the associated river and lake routing product was developed by the 
hydrology research group at the University of Waterloo. Primary Contributors includes 
Ming Han, Hongren Shen, Bryan A. Tolson, James R. Craig, Juliane Mai, Simon Lin, 
Nandita Basu, Frezer Awol. We also want to thank Robert Chlumsky, Étienne Gaborit, 
Hongli Liu, Konhee Lee for their secondary support in development of this product 
and their contributions to our Pan-Canadian routing product.

---------------------------
Support
---------------------------
Support for BasinMaker and the North American routing product development came 
from multiple sources:  
- Primary graduate student support for BasinMaker contributors was provided by 
  NRCan/Canadian Forest Service G&C Grants #129677 and #129816 and Dr. Tolson's 
  NSERC Discovery Grant.
- Secondary preliminary graduate student support for BasinMaker first author 
  Ming Han was provided by Canada First Research Excellence Fund provided to the 
  Lake Futures project of the Global Water Futures Project.
- Some additional secondary support was also provided via the CANARIE research 
  software program, grant #RS3-124 to co-author Juliane Mai.
  
---------------------------
Known errors and error reporting. 
---------------------------
Two kinds of errors exist in the version 2 routing product. 
1) The USGS and WSC streamflow gauges can be snapped to the wrong location. This 
   snapping error is usually negligible (in terms of streamflow simulation errors) 
   but sometimes creates significant errors that are only detectable when comparing 
   the routing product delineated drainage area with a map of known stream locations. 
   The primary indication that there *may* be a significant error in our product 
   for any specific streamflow gauge is the column ‘DA_error’ in the attribute 
   table of obs_gauges.shp. The ‘DA_error’ represent the ratio between drainage 
   area of streamflow gauges in the routing product and the recorded drainage area 
   of streamflow gauges in either USGS or WSC database. When this is far from 1.0 
   in either direction, users may wish to confirm the routing product delineated 
   watershed is reasonably consistent with known stream locations.   
2) The lake is not correctly represented; the user may find some lake polygon is 
   not fully covered by the corresponding lake catchment. This may happen when the 
   minimum distance between two lakes lake outlines smaller than 3 sec or 90 m. 
   This problem is very rare.

If you encounter any of the errors above or other errors, we would like to know 
in case we can help you address them or at least plan to address them in the next 
version of this product. Please report the errors to m43han@uwaterloo.ca or create 
a new issue in following webpage to report it. We will report and resolve all issues 
here: https://github.com/dustming/basinmaker/issues

---------------------------
Citation
---------------------------
In your publication using the routing product, please cite the following paper:
BasinMaker: a GIS toolbox for distributed watershed delineation of complex lake 
and river routing networks. Han, M., H. Shen, B. A. Tolson, J. R. Craig, J. Mai, 
S. Lin, N. Basu, F. Awol, submitted April 2021 to Environmental Modelling and Software.
(But please also check BasinMaker website where you downloaded this for most up 
to date citation)



