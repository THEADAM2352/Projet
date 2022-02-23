
class FileRepo:
        #x ici == a point.x //y
    
    def exportDataToString(self,x,t,y):  #x abscisse, y ordonnée, t temps
        for i in range (len(t)):
            print(str(x[i]),",",str(y[i]),",",str(t[i]),";")  #chaine de caractère"x,y,t,x1;y1..."
    
    def exportDataToCSV(self,):
        
        f=open(self.nom + '.csv',mode='w')
        f.write('exportDataToString(x,t,y)')
        f.close()
    
    def nom(self):
        self.nom=input('//')
    
    
        
