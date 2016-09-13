<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<html>
<body>
			<h2>My palant Collection</h2>
			<xsl:apply-templates/>
			<!--向 <xsl:apply-templates>
			元素添加一个 select 属性，此元素就会仅仅处理与属性值匹配的子元素。我们可以使用 select 属性来规定子节点被处理的顺序。-->
</body>
		</html>
	</xsl:template>

	<xsl:template match="PLANT">
		<p>
			<xsl:apply-templates select="COMMON"/>
			<xsl:apply-templates select="BOTANICAL"/>
		</p>
	</xsl:template>

	<xsl:template match="COMMON">
		Common:
		<span style="color:#ff0000">
			<xsl:value-of select="."/>
		</span>
		<br/>
	</xsl:template>

	<xsl:template match="BOTANICAL">
		Botanical:
		<span style="color:#00ff00">
			<xsl:value-of select="."/>
		</span>
		<br/>
	</xsl:template>

</xsl:stylesheet>