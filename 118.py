file=open('page.html','w+')
file.write('<!DOCTYPE html>\n')
file.write('<html>\n')
file.write('    <head>\n')
file.write('        <title>mypage</title>\n')
file.write('    </head>\n')
file.write('    <body>\n')
file.write('        <h1>python world</h1>')
file.write('    </body>\n')
file.write('</html>\n')
file.close()
import os
os.system('page.html')
