<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="2" name="Route2" color="1" fill="3" visible="no" active="no"/>
<layer number="3" name="Route3" color="4" fill="3" visible="no" active="no"/>
<layer number="4" name="Route4" color="1" fill="4" visible="no" active="no"/>
<layer number="5" name="Route5" color="4" fill="4" visible="no" active="no"/>
<layer number="6" name="Route6" color="1" fill="8" visible="no" active="no"/>
<layer number="7" name="Route7" color="4" fill="8" visible="no" active="no"/>
<layer number="8" name="Route8" color="1" fill="2" visible="no" active="no"/>
<layer number="9" name="Route9" color="4" fill="2" visible="no" active="no"/>
<layer number="10" name="Route10" color="1" fill="7" visible="no" active="no"/>
<layer number="11" name="Route11" color="4" fill="7" visible="no" active="no"/>
<layer number="12" name="Route12" color="1" fill="5" visible="no" active="no"/>
<layer number="13" name="Route13" color="4" fill="5" visible="no" active="no"/>
<layer number="14" name="Route14" color="1" fill="6" visible="no" active="no"/>
<layer number="15" name="Route15" color="4" fill="6" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="15" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="con-JST SH">
<description>
&lt;b&gt;JST Connectors&lt;/b&gt; - SH Series, 1.00mm pitch disconnectable crimp style connectors&lt;p&gt;

&lt;p&gt;THIS LIBRARY IS PROVIDED AS IS AND WITHOUT WARRANTY OF ANY KIND, EXPRESSED OR IMPLIED.&lt;br&gt;
USE AT YOUR OWN RISK!&lt;p&gt;

&lt;author&gt;Author: kylie &lt;/author&gt;, 04/2018&lt;p&gt;

&lt;a href="http://www.jst-mfg.com/product/detail_e.php?series=231"&gt;
&lt;img src="http://www.jst-mfg.com/product/images/pict/sh.jpg"  &gt;&lt;/a&gt;&lt;p&gt;
&lt;a href="http://www.jst-mfg.com/product/pdf/eng/eSH.pdf"&gt; Data sheet (PDF)&lt;/a&gt;&lt;p&gt;
&lt;p&gt; similar to:&lt;p&gt;
</description>
<packages>
<package name="BM04B-SRSS-TB">
<description>

&lt;b&gt;JST SH series header&lt;/b&gt; 1.00mm pitch disconnectable crimp style connectors, SMT vertical (top entry type), 4 pins&lt;p&gt;

</description>
<smd name="1" x="1.5" y="0" dx="0.6" dy="1.55" layer="1"/>
<smd name="2" x="0.5" y="0" dx="0.6" dy="1.55" layer="1"/>
<smd name="3" x="-0.5" y="0" dx="0.6" dy="1.55" layer="1"/>
<smd name="4" x="-1.5" y="0" dx="0.6" dy="1.55" layer="1"/>
<smd name="M1" x="2.8" y="-2.525" dx="1.2" dy="1.8" layer="1"/>
<smd name="M2" x="-2.8" y="-2.525" dx="1.2" dy="1.8" layer="1"/>
<text x="4.04" y="-1.905" size="1.016" layer="25" rot="R270" align="bottom-center">&gt;NAME</text>
<text x="1.5" y="1.27" size="1.016" layer="27" align="bottom-right">&gt;VALUE</text>
<wire x1="-3" y1="-0.325" x2="-2" y2="-0.325" width="0.1524" layer="21"/>
<wire x1="2" y1="-0.325" x2="3" y2="-0.325" width="0.1524" layer="21"/>
<wire x1="3" y1="-0.325" x2="3" y2="-1.45" width="0.1524" layer="21"/>
<wire x1="2" y1="-3.225" x2="-2" y2="-3.225" width="0.1524" layer="21"/>
<wire x1="-3" y1="-1.45" x2="-3" y2="-0.325" width="0.1524" layer="21"/>
<wire x1="-3" y1="-0.325" x2="3" y2="-0.325" width="0.1524" layer="51"/>
<wire x1="3" y1="-0.325" x2="3" y2="-3.225" width="0.1524" layer="51"/>
<wire x1="3" y1="-3.225" x2="-3" y2="-3.225" width="0.1524" layer="51"/>
<wire x1="-3" y1="-3.225" x2="-3" y2="-0.325" width="0.1524" layer="51"/>
<wire x1="-2.2" y1="-0.725" x2="2.2" y2="-0.725" width="0.1524" layer="51"/>
<wire x1="-2.2" y1="-0.725" x2="-2.2" y2="-1.725" width="0.1524" layer="51"/>
<wire x1="-2.2" y1="-1.725" x2="-2.56" y2="-1.725" width="0.1524" layer="51"/>
<wire x1="-2.56" y1="-1.725" x2="-2.56" y2="-2.325" width="0.1524" layer="51"/>
<wire x1="-2.56" y1="-2.325" x2="-2.2" y2="-2.325" width="0.1524" layer="51"/>
<wire x1="-2.2" y1="-2.325" x2="-2.2" y2="-2.825" width="0.1524" layer="51"/>
<wire x1="-2.2" y1="-2.825" x2="2.2" y2="-2.825" width="0.1524" layer="51"/>
<wire x1="2.2" y1="-0.725" x2="2.2" y2="-1.725" width="0.1524" layer="51"/>
<wire x1="2.2" y1="-1.725" x2="2.56" y2="-1.725" width="0.1524" layer="51"/>
<wire x1="2.56" y1="-1.725" x2="2.56" y2="-2.325" width="0.1524" layer="51"/>
<wire x1="2.56" y1="-2.325" x2="2.2" y2="-2.325" width="0.1524" layer="51"/>
<wire x1="2.2" y1="-2.325" x2="2.2" y2="-2.825" width="0.1524" layer="51"/>
<rectangle x1="1.4" y1="-2.405" x2="1.6" y2="-2.055" layer="51"/>
<rectangle x1="1.4" y1="-0.325" x2="1.6" y2="0.375" layer="51"/>
<rectangle x1="0.4" y1="-2.405" x2="0.6" y2="-2.055" layer="51"/>
<rectangle x1="0.4" y1="-0.325" x2="0.6" y2="0.375" layer="51"/>
<rectangle x1="-0.6" y1="-2.405" x2="-0.4" y2="-2.055" layer="51"/>
<rectangle x1="-0.6" y1="-0.325" x2="-0.4" y2="0.375" layer="51"/>
<rectangle x1="-1.6" y1="-2.405" x2="-1.4" y2="-2.055" layer="51"/>
<rectangle x1="-1.6" y1="-0.325" x2="-1.4" y2="0.375" layer="51"/>
<polygon width="0.1524" layer="51">
<vertex x="1.5" y="-3.2"/>
<vertex x="1.3" y="-2.85"/>
<vertex x="1.7" y="-2.85"/>
</polygon>
</package>
</packages>
<symbols>
<symbol name="M_1R04">
<wire x1="3.81" y1="-7.62" x2="-1.27" y2="-7.62" width="0.4064" layer="94"/>
<wire x1="1.27" y1="0" x2="2.54" y2="0" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-2.54" x2="2.54" y2="-2.54" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-5.08" x2="2.54" y2="-5.08" width="0.6096" layer="94"/>
<wire x1="-1.27" y1="5.08" x2="-1.27" y2="-7.62" width="0.4064" layer="94"/>
<wire x1="3.81" y1="-7.62" x2="3.81" y2="5.08" width="0.4064" layer="94"/>
<wire x1="-1.27" y1="5.08" x2="3.81" y2="5.08" width="0.4064" layer="94"/>
<wire x1="1.27" y1="2.54" x2="2.54" y2="2.54" width="0.6096" layer="94"/>
<text x="-1.27" y="-10.16" size="1.778" layer="96">&gt;VALUE</text>
<text x="-1.27" y="5.842" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="7.62" y="-5.08" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="2" x="7.62" y="-2.54" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="3" x="7.62" y="0" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="4" x="7.62" y="2.54" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="BM04B-SRSS" prefix="X">
<description>
&lt;b&gt;JST SH series header&lt;/b&gt; 1.00mm pitch disconnectable crimp style connectors, vertical (side entry type), 4 pins&lt;p&gt;
</description>
<gates>
<gate name="G$1" symbol="M_1R04" x="0" y="0"/>
</gates>
<devices>
<device name="-TB" package="BM04B-SRSS-TB">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="USB4115-03-C_REVA">
<packages>
<package name="GCT_USB4115-03-C_REVA">
<wire x1="3.54" y1="0.29" x2="3.96" y2="0.29" width="0" layer="46"/>
<wire x1="3.96" y1="0.29" x2="4.25" y2="0" width="0" layer="46" curve="-90"/>
<wire x1="4.25" y1="0" x2="3.96" y2="-0.29" width="0" layer="46" curve="-90"/>
<wire x1="3.96" y1="-0.29" x2="3.54" y2="-0.29" width="0" layer="46"/>
<wire x1="3.54" y1="-0.29" x2="3.25" y2="0" width="0" layer="46" curve="-90"/>
<wire x1="3.25" y1="0" x2="3.54" y2="0.29" width="0" layer="46" curve="-90"/>
<wire x1="-4.47" y1="1.9" x2="4.47" y2="1.9" width="0.1" layer="51"/>
<wire x1="4.47" y1="1.9" x2="4.47" y2="-1.9" width="0.1" layer="51"/>
<wire x1="4.47" y1="-1.9" x2="-4.47" y2="-1.9" width="0.1" layer="51"/>
<wire x1="-4.47" y1="-1.9" x2="-4.47" y2="1.9" width="0.1" layer="51"/>
<wire x1="-3.35" y1="1.9" x2="-4.47" y2="1.9" width="0.2" layer="21"/>
<wire x1="-4.47" y1="1.9" x2="-4.47" y2="-1.9" width="0.2" layer="21"/>
<wire x1="-4.47" y1="-1.9" x2="-3.35" y2="-1.9" width="0.2" layer="21"/>
<wire x1="3.35" y1="1.9" x2="4.47" y2="1.9" width="0.2" layer="21"/>
<wire x1="4.47" y1="1.9" x2="4.47" y2="-1.9" width="0.2" layer="21"/>
<wire x1="4.47" y1="-1.9" x2="3.35" y2="-1.9" width="0.2" layer="21"/>
<circle x="-5" y="1" radius="0.1" width="0.2" layer="21"/>
<circle x="-5" y="1" radius="0.1" width="0.2" layer="51"/>
<wire x1="-4.72" y1="2.95" x2="4.72" y2="2.95" width="0.05" layer="39"/>
<wire x1="4.72" y1="2.95" x2="4.72" y2="-2.95" width="0.05" layer="39"/>
<wire x1="4.72" y1="-2.95" x2="-4.72" y2="-2.95" width="0.05" layer="39"/>
<wire x1="-4.72" y1="-2.95" x2="-4.72" y2="2.95" width="0.05" layer="39"/>
<text x="-5.08" y="3.81" size="1.27" layer="25">&gt;NAME</text>
<text x="-5.08" y="-5.08" size="1.27" layer="27">&gt;VALUE</text>
<hole x="-3.75" y="0" drill="0.66"/>
<hole x="3.75" y="0" drill="0.58"/>
<pad name="S1" x="-2.4" y="2.15" drill="0.7" diameter="1.1"/>
<pad name="S2" x="-2.4" y="-2.15" drill="0.7" diameter="1.1"/>
<pad name="S3" x="2.4" y="-2.15" drill="0.7" diameter="1.1"/>
<pad name="S4" x="2.4" y="2.15" drill="0.7" diameter="1.1"/>
<smd name="A1" x="-2.75" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A2" x="-2.25" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A3" x="-1.75" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A4" x="-1.25" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A5" x="-0.75" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A6" x="-0.25" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A7" x="0.25" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A8" x="0.75" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A9" x="1.25" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A10" x="1.75" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A11" x="2.25" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="A12" x="2.75" y="0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B1" x="2.75" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B2" x="2.25" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B3" x="1.75" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B4" x="1.25" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B5" x="0.75" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B6" x="0.25" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B7" x="-0.25" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B8" x="-0.75" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B9" x="-1.25" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B10" x="-1.75" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B11" x="-2.25" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
<smd name="B12" x="-2.75" y="-0.835" dx="0.3" dy="0.85" layer="1"/>
</package>
</packages>
<symbols>
<symbol name="USB4115-03-C_REVA">
<wire x1="-12.7" y1="15.24" x2="12.7" y2="15.24" width="0.254" layer="94"/>
<wire x1="12.7" y1="15.24" x2="12.7" y2="-17.78" width="0.254" layer="94"/>
<wire x1="12.7" y1="-17.78" x2="-12.7" y2="-17.78" width="0.254" layer="94"/>
<wire x1="-12.7" y1="-17.78" x2="-12.7" y2="15.24" width="0.254" layer="94"/>
<text x="-12.7" y="16.002" size="1.778" layer="95">&gt;NAME</text>
<text x="-12.7" y="-18.542" size="1.778" layer="96" rot="MR180">&gt;VALUE</text>
<pin name="GND_A" x="-17.78" y="-10.16" length="middle" direction="pwr"/>
<pin name="SSTXN1" x="-17.78" y="7.62" length="middle"/>
<pin name="SSTXP1" x="-17.78" y="10.16" length="middle"/>
<pin name="VBUS_A" x="-17.78" y="12.7" length="middle" direction="pwr"/>
<pin name="DP1" x="-17.78" y="2.54" length="middle"/>
<pin name="CC1" x="-17.78" y="5.08" length="middle"/>
<pin name="SBU1" x="-17.78" y="-2.54" length="middle"/>
<pin name="DN1" x="-17.78" y="0" length="middle"/>
<pin name="SSRXN2" x="-17.78" y="-5.08" length="middle"/>
<pin name="SSRXP2" x="-17.78" y="-7.62" length="middle"/>
<pin name="SHIELD" x="-17.78" y="-15.24" length="middle" direction="pas"/>
<pin name="GND_B" x="17.78" y="-10.16" length="middle" direction="pwr" rot="R180"/>
<pin name="SSTXN2" x="17.78" y="-5.08" length="middle" rot="R180"/>
<pin name="SSTXP2" x="17.78" y="-7.62" length="middle" rot="R180"/>
<pin name="VBUS_B" x="17.78" y="12.7" length="middle" direction="pwr" rot="R180"/>
<pin name="DP2" x="17.78" y="0" length="middle" rot="R180"/>
<pin name="CC2" x="17.78" y="-2.54" length="middle" rot="R180"/>
<pin name="SBU2" x="17.78" y="5.08" length="middle" rot="R180"/>
<pin name="DN2" x="17.78" y="2.54" length="middle" rot="R180"/>
<pin name="SSRXN1" x="17.78" y="7.62" length="middle" rot="R180"/>
<pin name="SSRXP1" x="17.78" y="10.16" length="middle" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="USB4115-03-C_REVA" prefix="J">
<description> &lt;a href="https://pricing.snapeda.com/parts/USB4115-03-C/Global%20Connector%20Technology/view-part?ref=eda"&gt;Check prices&lt;/a&gt;</description>
<gates>
<gate name="G$1" symbol="USB4115-03-C_REVA" x="0" y="0"/>
</gates>
<devices>
<device name="" package="GCT_USB4115-03-C_REVA">
<connects>
<connect gate="G$1" pin="CC1" pad="A5"/>
<connect gate="G$1" pin="CC2" pad="B5"/>
<connect gate="G$1" pin="DN1" pad="A7"/>
<connect gate="G$1" pin="DN2" pad="B7"/>
<connect gate="G$1" pin="DP1" pad="A6"/>
<connect gate="G$1" pin="DP2" pad="B6"/>
<connect gate="G$1" pin="GND_A" pad="A1 A12"/>
<connect gate="G$1" pin="GND_B" pad="B1 B12"/>
<connect gate="G$1" pin="SBU1" pad="A8"/>
<connect gate="G$1" pin="SBU2" pad="B8"/>
<connect gate="G$1" pin="SHIELD" pad="S1 S2 S3 S4"/>
<connect gate="G$1" pin="SSRXN1" pad="B10"/>
<connect gate="G$1" pin="SSRXN2" pad="A10"/>
<connect gate="G$1" pin="SSRXP1" pad="B11"/>
<connect gate="G$1" pin="SSRXP2" pad="A11"/>
<connect gate="G$1" pin="SSTXN1" pad="A3"/>
<connect gate="G$1" pin="SSTXN2" pad="B3"/>
<connect gate="G$1" pin="SSTXP1" pad="A2"/>
<connect gate="G$1" pin="SSTXP2" pad="B2"/>
<connect gate="G$1" pin="VBUS_A" pad="A4 A9"/>
<connect gate="G$1" pin="VBUS_B" pad="B4 B9"/>
</connects>
<technologies>
<technology name="">
<attribute name="AVAILABILITY" value="In Stock"/>
<attribute name="DESCRIPTION" value=" USB 3.1 Connector Type C Vertical Receptacle, 9.25mm profile, 24 Pins, Surface mount, Top mount, low cost "/>
<attribute name="MF" value="Global Connector Technology"/>
<attribute name="MP" value="USB4115-03-C"/>
<attribute name="PACKAGE" value="None"/>
<attribute name="PRICE" value="None"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply1" urn="urn:adsk.eagle:library:371">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
 GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
 Please keep in mind, that these devices are necessary for the
 automatic wiring of the supply signals.&lt;p&gt;
 The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
 In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
 &lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="GND" urn="urn:adsk.eagle:symbol:26925/1" library_version="1">
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GND" urn="urn:adsk.eagle:component:26954/1" prefix="GND" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="X1" library="con-JST SH" deviceset="BM04B-SRSS" device="-TB"/>
<part name="J1" library="USB4115-03-C_REVA" deviceset="USB4115-03-C_REVA" device=""/>
<part name="GND1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="X1" gate="G$1" x="88.9" y="35.56" smashed="yes" rot="R180">
<attribute name="VALUE" x="90.17" y="45.72" size="1.778" layer="96" rot="R180"/>
<attribute name="NAME" x="90.17" y="29.718" size="1.778" layer="95" rot="R180"/>
</instance>
<instance part="J1" gate="G$1" x="40.64" y="40.64" smashed="yes">
<attribute name="NAME" x="27.94" y="56.642" size="1.778" layer="95"/>
<attribute name="VALUE" x="27.94" y="22.098" size="1.778" layer="96" rot="MR180"/>
</instance>
<instance part="GND1" gate="1" x="22.86" y="17.78" smashed="yes">
<attribute name="VALUE" x="20.32" y="15.24" size="1.778" layer="96"/>
</instance>
<instance part="GND2" gate="1" x="58.42" y="17.78" smashed="yes">
<attribute name="VALUE" x="55.88" y="15.24" size="1.778" layer="96"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="GND" class="0">
<segment>
<pinref part="J1" gate="G$1" pin="SHIELD"/>
<pinref part="J1" gate="G$1" pin="GND_A"/>
<wire x1="22.86" y1="25.4" x2="22.86" y2="30.48" width="0.1524" layer="91"/>
<pinref part="GND1" gate="1" pin="GND"/>
<wire x1="22.86" y1="25.4" x2="22.86" y2="20.32" width="0.1524" layer="91"/>
<junction x="22.86" y="25.4"/>
</segment>
<segment>
<pinref part="J1" gate="G$1" pin="GND_B"/>
<pinref part="GND2" gate="1" pin="GND"/>
<wire x1="58.42" y1="30.48" x2="58.42" y2="20.32" width="0.1524" layer="91"/>
<pinref part="X1" gate="G$1" pin="4"/>
<wire x1="81.28" y1="33.02" x2="81.28" y2="30.48" width="0.1524" layer="91"/>
<wire x1="81.28" y1="30.48" x2="58.42" y2="30.48" width="0.1524" layer="91"/>
<junction x="58.42" y="30.48"/>
</segment>
</net>
<net name="VCC" class="0">
<segment>
<pinref part="X1" gate="G$1" pin="1"/>
<pinref part="J1" gate="G$1" pin="VBUS_B"/>
<wire x1="81.28" y1="40.64" x2="81.28" y2="53.34" width="0.1524" layer="91"/>
<wire x1="81.28" y1="53.34" x2="58.42" y2="53.34" width="0.1524" layer="91"/>
<wire x1="58.42" y1="53.34" x2="58.42" y2="58.42" width="0.1524" layer="91"/>
<wire x1="58.42" y1="58.42" x2="22.86" y2="58.42" width="0.1524" layer="91"/>
<junction x="58.42" y="53.34"/>
<pinref part="J1" gate="G$1" pin="VBUS_A"/>
<wire x1="22.86" y1="58.42" x2="22.86" y2="53.34" width="0.1524" layer="91"/>
<label x="78.74" y="58.42" size="1.778" layer="95"/>
</segment>
</net>
<net name="D-" class="0">
<segment>
<pinref part="X1" gate="G$1" pin="2"/>
<wire x1="81.28" y1="38.1" x2="66.04" y2="38.1" width="0.1524" layer="91"/>
<wire x1="66.04" y1="38.1" x2="66.04" y2="43.18" width="0.1524" layer="91"/>
<pinref part="J1" gate="G$1" pin="DN2"/>
<wire x1="66.04" y1="43.18" x2="58.42" y2="43.18" width="0.1524" layer="91"/>
<pinref part="J1" gate="G$1" pin="DN1"/>
<wire x1="22.86" y1="40.64" x2="15.24" y2="40.64" width="0.1524" layer="91"/>
<wire x1="15.24" y1="40.64" x2="15.24" y2="66.04" width="0.1524" layer="91"/>
<wire x1="15.24" y1="66.04" x2="66.04" y2="66.04" width="0.1524" layer="91"/>
<wire x1="66.04" y1="66.04" x2="66.04" y2="43.18" width="0.1524" layer="91"/>
<junction x="66.04" y="43.18"/>
<label x="68.58" y="40.64" size="1.778" layer="95"/>
</segment>
</net>
<net name="D+" class="0">
<segment>
<pinref part="X1" gate="G$1" pin="3"/>
<wire x1="81.28" y1="35.56" x2="73.66" y2="35.56" width="0.1524" layer="91"/>
<wire x1="73.66" y1="35.56" x2="63.5" y2="35.56" width="0.1524" layer="91"/>
<wire x1="63.5" y1="35.56" x2="63.5" y2="40.64" width="0.1524" layer="91"/>
<pinref part="J1" gate="G$1" pin="DP2"/>
<wire x1="63.5" y1="40.64" x2="58.42" y2="40.64" width="0.1524" layer="91"/>
<pinref part="J1" gate="G$1" pin="DP1"/>
<wire x1="22.86" y1="43.18" x2="17.78" y2="43.18" width="0.1524" layer="91"/>
<wire x1="17.78" y1="43.18" x2="17.78" y2="63.5" width="0.1524" layer="91"/>
<wire x1="17.78" y1="63.5" x2="73.66" y2="63.5" width="0.1524" layer="91"/>
<wire x1="73.66" y1="63.5" x2="73.66" y2="35.56" width="0.1524" layer="91"/>
<junction x="73.66" y="35.56"/>
<label x="71.12" y="33.02" size="1.778" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
<errors>
<approved hash="104,1,22.86,30.48,J1,GND_A,GND,,,"/>
<approved hash="104,1,22.86,53.34,J1,VBUS_A,VCC,,,"/>
<approved hash="104,1,58.42,30.48,J1,GND_B,GND,,,"/>
<approved hash="104,1,58.42,53.34,J1,VBUS_B,VCC,,,"/>
</errors>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, EAGLE supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports URNs for individual library
assets (packages, symbols, and devices). The URNs of those assets
will not be understood (or retained) with this version.
</note>
</compatibility>
</eagle>
