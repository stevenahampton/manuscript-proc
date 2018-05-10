<?xml version="1.0" encoding="ISO-8859-1"?>
<!-- add these details here so they're in git -->
<!DOCTYPE manuscript SYSTEM "manuscript.dtd" [<!ENTITY aelig "&#230;"><!ENTITY AElig "&#198;"><!ENTITY thorn "&#254;"><!ENTITY Thorn "&#222;"><!ENTITY THORN "&#222;"><!ENTITY Eth "&#208;"><!ENTITY ETH "&#208;"><!ENTITY eth "&#240;"><!ENTITY times "&#215;"><!ENTITY dagger "&#8224;" ><!ENTITY acirc "&#226;" ><!ENTITY oacute "&#243;" ><!ENTITY agrave "&#224;" ><!ENTITY auml "&#228;" ><!ENTITY eacute "&#233;" ><!ENTITY uuml "&#252;" ><!ENTITY Ouml "&#214;" ><!ENTITY ouml "&#246;"><!ENTITY ccedil "&#231;" ><!ENTITY aelig "&#230;" ><!ENTITY mdash "&#8212;" ><!ENTITY ndash "&#8211;" ><!ENTITY hellip "&#8230;" ><!ENTITY egrave "&#232;" ><!ENTITY dotac '&#60;char name="dotac"&#62;.&#60;char name="dotacSlash"&#62;/&#60;/char&#62;&#60;/char&#62;'><!-- Greek alphabet uppercase --><!ENTITY Alpha    "&#913;" ><!ENTITY Beta     "&#914;" ><!ENTITY Gamma    "&#915;" ><!ENTITY Delta    "&#916;" ><!ENTITY Epsilon  "&#917;" ><!ENTITY Zeta     "&#918;" ><!ENTITY Eta      "&#919;" ><!ENTITY Theta    "&#920;" ><!ENTITY Iota     "&#921;" ><!ENTITY Kappa    "&#922;" ><!ENTITY Lambda   "&#923;" ><!ENTITY Mu       "&#924;" ><!ENTITY Nu       "&#925;" ><!ENTITY Xi       "&#926;" ><!ENTITY Omicron  "&#927;" ><!ENTITY Pi       "&#928;" ><!ENTITY Rho      "&#929;" ><!-- there is no Sigmaf, and no U+03A2 character either --><!ENTITY Sigma    "&#931;" ><!ENTITY Tau      "&#932;" ><!ENTITY Upsilon  "&#933;" ><!ENTITY Phi      "&#934;" ><!ENTITY Chi      "&#935;" ><!ENTITY Psi      "&#936;" ><!ENTITY Omega    "&#937;" ><!-- Greek alphabet lowercase --><!ENTITY alpha    "&#945;" ><!ENTITY beta     "&#946;" ><!ENTITY gamma    "&#947;" ><!ENTITY delta    "&#948;" ><!ENTITY epsilon  "&#949;" ><!ENTITY zeta     "&#950;" ><!ENTITY eta      "&#951;" ><!ENTITY theta    "&#952;" ><!ENTITY iota     "&#953;" ><!ENTITY kappa    "&#954;" ><!ENTITY lambda   "&#955;" ><!ENTITY mu       "&#956;" ><!ENTITY nu       "&#957;" ><!ENTITY xi       "&#958;" ><!ENTITY omicron  "&#959;" ><!ENTITY pi       "&#960;" ><!ENTITY rho      "&#961;" ><!ENTITY sigmaf   "&#962;" ><!ENTITY sigma    "&#963;" ><!ENTITY tau      "&#964;" ><!ENTITY upsilon  "&#965;" ><!ENTITY phi      "&#966;" ><!ENTITY chi      "&#967;" ><!ENTITY psi      "&#968;" ><!ENTITY omega    "&#969;" ><!ENTITY thetasym "&#977;" ><!ENTITY upsih    "&#978;" ><!ENTITY piv      "&#982;" >]>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html"/> 

    <xsl:template match="/">
        <html><body>
            <xsl:apply-templates select="manuscript"/>
        </body></html>
    </xsl:template>

    <xsl:template match="manuscript">
        <xsl:apply-templates/>
    </xsl:template>

    <xsl:template match="section">
        <div class="section">
            <xsl:attribute name="id"><xsl:value-of select="@id"/></xsl:attribute>
            <xsl:apply-templates/>
        </div>
    </xsl:template>

    <xsl:template match="section_num">
        <div class="section_num"><xsl:apply-templates/></div>
    </xsl:template>

    <xsl:template match="section_title">
        <div class="section_title"><xsl:apply-templates/></div>
    </xsl:template>

    <xsl:template match="freetext">
        <div class="freetext"><xsl:apply-templates/></div>
    </xsl:template>

    <xsl:template match="p">
        <p><xsl:apply-templates/></p>
    </xsl:template>

    <xsl:template match="link">
        <a>
            <xsl:attribute name="class">link <xsl:value-of select="@type"/></xsl:attribute>
            <xsl:attribute name="href"><xsl:value-of select="@ref"/></xsl:attribute>
            <xsl:apply-templates/>
        </a>
    </xsl:template>

    <xsl:template match="notes">
        <notes>
            <xsl:attribute name="id"><xsl:value-of select="@id"/></xsl:attribute>
            <xsl:attribute name="type"><xsl:value-of select="@type"/></xsl:attribute>
            <xsl:apply-templates/>
        </notes>
    </xsl:template>

    <xsl:template match="note">
        <note>
            <xsl:attribute name="id"><xsl:value-of select="@id"/></xsl:attribute>
            <xsl:attribute name="type"><xsl:value-of select="@type"/></xsl:attribute>
            <xsl:apply-templates/>
        </note>
    </xsl:template>

    <xsl:template match="image">
        <image><xsl:apply-templates/></image>
    </xsl:template>
    
    <xsl:template match="caption">
        <caption><xsl:apply-templates/></caption>
    </xsl:template>
    
    <xsl:template match="desc">
        <desc><xsl:apply-templates/></desc>
    </xsl:template>
    
</xsl:stylesheet>

