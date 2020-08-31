class web:
    def create(self,body,name):
        file=open(name+'.html','w+')
        file.write('<!DOCTYPE html>\n')
        file.write('<html>\n')
        file.write('    <head>\n')
        file.write('        <title>Tab</title>\n')
        file.write('    </head>\n')
        file.write('    <body>\n')
        file.write(body)
        file.write('    </body>\n')
        file.write('</html>\n')
        
        file.close()
        import os
        os.system(name+'.html')
w1=web()
w2=web()
w3=web()
w2.create('<h1> python 2 </h1>','page2')
w3.create('<h1> python 3 </h1>','page3')
w1.create('<h1> python </h1>','page1')
