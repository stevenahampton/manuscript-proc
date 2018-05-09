<?xml version="1.0" encoding="ISO-8859-1"?>

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

