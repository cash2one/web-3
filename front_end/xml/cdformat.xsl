<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- <xsl:stylesheet>
  ，定义此文档是一个 XSLT 样式表文档-->
  <xsl:template match="/">
    <!-- 构建模板，定义了写到输出结果的 HTML 代码。-->
    <!-- match 属性的值是 XPath 表达式（match="/" ，把此模板与 XML 源文档的根相联系）。-->
    <html>
<body>

      <h2>My CD Collection</h2>
      <table border="1">
        <tr bgcolor="#9acd32">
          <th align="left">Title</th>
          <th align="left">Artist</th>
        </tr>
        <xsl:for-each select="CATALOG/CD">
          <!-- <xsl:for-each>
          用于选取指定的节点集中的每个 XML 元素。-->
          <!--
            在<xsl:for-each>
          中添加一个选择属性的判别式（select="CATALOG/CD[ARTIST='Bob Dylan']"），过滤 XML 文件输出的结果。
            合法的过滤运算符:= (等于)!= (不等于)&lt; (小于)&gt; (大于)
             -->
          <xsl:sort select="ARTIST"/>
          <!--对结果进行排序-->
          <xsl:if test="PRICE &gt; 8">
            <!-- 放置针对 XML 文件内容的条件测试 -->

            <tr>
              <td>
                <xsl:value-of select="TITLE"/>
                <!--提取某个选定节点的值，并把值添加到转换的输出流中-->
                <!--select 属性的值是一个 XPath 表达式。--> </td>

              <xsl:choose>
                <!-- <xsl:choose>
                元素用于结合
                <xsl:when>
                  和
                  <xsl:otherwise>
                    来表达多重条件测试 -->
                    <xsl:when test="PRICE &gt; 10">
                      <td bgcolor="#ff00ff">
                        <xsl:value-of select="ARTIST"/>
                      </td>
                    </xsl:when>

                    <xsl:when test="PRICE &gt; 9">
                      <td bgcolor="#cccccc">
                        <xsl:value-of select="ARTIST"/>
                      </td>
                    </xsl:when>

                    <xsl:otherwise>
                      <td>
                        <xsl:value-of select="ARTIST"/>
                      </td>
                    </xsl:otherwise>

                  </xsl:choose>

                </tr>
              </xsl:if>
            </xsl:for-each>
          </table>
</body>
        </html>
      </xsl:template>

    </xsl:stylesheet>