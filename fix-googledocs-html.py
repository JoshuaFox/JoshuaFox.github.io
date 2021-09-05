#!/usr/bin/python3
import os
ua = 'UA-24142341-1'
analytics = \
f"""
<!-- Google Analytics -->
    <script>
        (function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
        (i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        }})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', '{ua}', 'auto');
        ga('send', 'pageview');
    </script>
    <!-- End Google Analytics -->
"""
folder="./yiddish"
for file in os.listdir(folder):
     filename = './' + folder +'/'+ os.fsdecode(file)
     inserted = None
     if filename.endswith(".html"):
        with open(filename, 'r') as file:
          data = file.read()

          if ua in data:
            print('did not add  Google Analytics in', filename)
          else:
            inserted = data.replace("</body>", analytics + "\n</body>")
            print('added Google Analytics in', filename)


        if inserted: # Do this after filehandle for read is closed
          with open(filename, 'wt') as fileout:
            fileout.write(inserted)

rtl_style= "body{direction:rtl}</style>"

home = \
"""  <h1 dir="rtl">
    <a href="/">
	(אַהיים)
	</a>
 </h1>"""
for file in os.listdir(folder):
     filename = './' + folder +'/'+ os.fsdecode(file)

     if filename.endswith(".html"):
        with open(filename, 'r') as file:
          data1 = file.read()
          data2 = data1.replace(";text-align:left", "")
          if data1 != data2:
              print("removed text-align:left in", filename)
          else:
              print("did not remove text-align:left in", filename)

          if rtl_style not in data2:
                data3 = data2.replace("</style>",rtl_style)
                print("inserted RTL in", filename)
          else:
              data3 = data2
              print("did not insert RTL in", filename)



        # Do this after filehandle for read is closed
        with open(filename, 'wt') as fileout:
            fileout.write(data3)
