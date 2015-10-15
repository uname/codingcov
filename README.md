# codingcov
![](/snapshort.png)
批量修改文件编码的Python脚本
默认递归当前目录下的所有文件，如有修改目录或过滤文件需要，只需简单修改脚本即可。

脚本依赖的命令行工具:
1. file   用于判断文件编码类型
2. gawk   处理file的输出
3. iconv  转换编码

本目录已包含Windows下可用的上述命令行工具(推荐安装cygwin获取更多Unix工具集)

