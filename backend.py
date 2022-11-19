import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib as mpl
import matplotlib.patheffects


def schulgraph(ax=None, centerx=0, centery=0, corner_val=[-5,5,-5,5],label=['x','y']):
    """Centers the axis spines at <centerx, centery> on the axis "ax", and
    places arrows at the end of the axis spines."""
    if ax is None:
        ax = plt.gca()

    # Set the axis's spines to be centered at the given point
    # (Setting all 4 spines so that the tick marks go in both directions)
    ax.spines['left'].set_position(('data', centerx))
    ax.spines['bottom'].set_position(('data', centery))
    ax.spines['right'].set_position(('data', centerx - 1))
    ax.spines['top'].set_position(('data', centery - 1))

    ax.axis(corner_val)
    
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    
    ax.plot([corner_val[0],corner_val[1]],[0,0],'k')
    ax.plot([0,0],[corner_val[2],corner_val[3]],'k')
    ax.set_xlabel(label[0])
    ax.xaxis.set_label_coords(1.0, 0.485)
    ax.set_ylabel(label[1],rotation=0)
    ax.yaxis.set_label_coords(0.47, 0.98)

    # Hide the line (but not ticks) for "extra" spines
    for side in ['right', 'top']:
        ax.spines[side].set_color('none')

    # On both the x and y axes...
    for axis, center in zip([ax.xaxis, ax.yaxis], [centerx, centery]):
        # Turn on minor and major gridlines and ticks
        #axis.set_ticks_position('both')
        axis.grid(True, 'major', ls='solid', lw=0.5, color='gray')
        axis.grid(True, 'minor', ls='solid', lw=0.1, color='gray')
        axis.set_minor_locator(mpl.ticker.AutoMinorLocator())

        # Hide the ticklabels at <centerx, centery>
        formatter = CenteredFormatter()
        formatter.center = center
        axis.set_major_formatter(formatter)

class CenteredFormatter(mpl.ticker.ScalarFormatter):
    """Acts exactly like the default Scalar Formatter, but yields an empty
    label for ticks at "center"."""
    center = 0
    def __call__(self, value, pos=None):
        if value == self.center:
            return ''
        else:
            return mpl.ticker.ScalarFormatter.__call__(self, value, pos)
        

def func(i):
    i+=2
    x = np.linspace(-5,5,100)
    if i==0:
        y= 2*x-3
        sli_x_loc=np.array([-1,1,3]) #maximal 10 verschiedene Stück ? self.sli[i][j] weil j nicht mehr kann???
        yprime_loc=2+(sli_x_loc-sli_x_loc)
        yprime=2+(x-x)
    if i==1:
        y= 0.5*x+1
        sli_x_loc=np.array([-4,1,2])
        yprime_loc=0.5+(sli_x_loc-sli_x_loc)
        yprime=0.5+(x-x)
    if i==2:
        y=-3*x+2
        sli_x_loc=np.array([-3,2])
        yprime_loc=-3+(sli_x_loc-sli_x_loc)
        yprime=-3+(x-x)
    if i==3:
        y=0.5* x**2
        sli_x_loc=np.array([-2,0,1]) 
        yprime_loc=sli_x_loc
        yprime=x
    if i==4:
        y=-0.25* x**2+1
        sli_x_loc=np.array([-3,0,2]) 
        yprime_loc=-0.5*sli_x_loc
        yprime=-0.5*x
    if i==5:
        y= 1/6*x**3
        sli_x_loc=np.array([-2,0,3])
        yprime_loc=0.5*sli_x_loc**2
        yprime=0.5*x**2
    if i==6:
        y= 1/2*x**3-3*x
        sli_x_loc=np.array([-1.4,0,1.4]) 
        yprime_loc=3/2*sli_x_loc**2-3
        yprime=3/2*x**2-3
    if i==7:
        y=np.exp(0.25*x)
        sli_x_loc=np.array([-3,-2,-1,0,1,2,3,4]) 
        yprime_loc=0.25*np.exp(0.25*sli_x_loc)
        yprime=0.25*np.exp(0.25*x)
    if i==8:
        y= np.arctan(x)
        sli_x_loc=np.array([-1,0,1,3])
        yprime_loc=1/(1+sli_x_loc**2)
        yprime=1/(1+x**2)
    if i==9:
        y= 1/8*x**4-x**2
        sli_x_loc=np.array([-2,0,1,2]) 
        yprime_loc=1/2*sli_x_loc**3-2*sli_x_loc
        yprime=1/2*x**3-2*x
    if i==10:
        y= 0.5*(x-2)**2-1
        sli_x_loc=np.array([0,2,3]) 
        yprime_loc=sli_x_loc-2
        yprime=x-2
    if i==11:
        y= 2*np.sin(np.pi/2*x)
        sli_x_loc=np.array([-2,-1,1,3]) 
        yprime_loc=np.pi*np.cos(np.pi/2*sli_x_loc)
        yprime=np.pi*np.cos(np.pi/2*x)

    #ergänze hier weitere funktionen
    return x , y , sli_x_loc , yprime_loc, yprime

def slider_position(sli_x_loc,corner, corner_val):
    sli_width=0.03
    botmidy=corner[2]
    botmidx=corner[0]-sli_width/2+(sli_x_loc-corner_val[0])*(corner[1]-corner[0])/(corner_val[1]-corner_val[0])
    sli_height=(corner[3]-corner[2])/2-corner[4]/5  # die fünf ist über den Daumen gepeilt. Hier ist andernfalls etwas recherche notwendig
    return [botmidx, botmidy, sli_width, sli_height]



class Ableitungquiz:
    def __init__(self,n):

        self.Nquest=n
        self.corner=[0.05,0.95,0.05,0.95,0.2]
        self.corner_val=[-5, 5, -5, 5]

        #question
        
        self.fig=[0]*self.Nquest
        self.ax=[0]*self.Nquest
        self.axsol=[0]*self.Nquest
        self.sli=[[0,0,0,0,0,0,0,0,0,0] for _ in range(self.Nquest)] # a maximum of 10 slider per question
        self.ax_sli=[[0,0,0,0,0,0,0,0,0,0] for _ in range(self.Nquest)]

        
        #evaluation
        self.deviation=[[0,0,0,0,0,0,0,0,0,0] for _ in range(self.Nquest)]
        self.question_dev=[0]*self.Nquest

        
    def questions(self,i):
        #build figures
        self.fig[i] = plt.figure()
        self.ax[i]=self.fig[i].add_subplot(211)
        self.axsol[i]=self.fig[i].add_subplot(212)
        

        #geometry and style
        self.fig[i].subplots_adjust(left=self.corner[0], right=self.corner[1], bottom=self.corner[2], top=self.corner[3], hspace=self.corner[4])
        schulgraph(self.ax[i])
        schulgraph(self.axsol[i])

        #setup each and every slider
        x,y,sli_x_loc,yprime_loc,yprime=func(i)
        for j in range(len(sli_x_loc)):
            sli_loc=slider_position(sli_x_loc[j],self.corner,self.corner_val)
            self.ax_sli[i][j] = self.fig[i].add_axes(sli_loc)
            self.sli[i][j] = Slider(self.ax_sli[i][j], "Nr."+str(j+1), self.corner_val[2],self.corner_val[3], valinit=0, orientation="vertical",alpha=0.0, initcolor='none')
            self.sli[i][j].valtext.set_y(0.05)
            self.sli[i][j].track.set_alpha(0.5)
            
        # show function of this question
        self.ax[i].plot(x, y)

        #finally be not friendly this time and give no hint for the solution (dashed line)
        #intro_axsol.plot(x, yprime,'--')  
        
        plt.show()

        
    def close_and_save_last_question(self,i):
        x,_,_,yprime_loc,yprime=func(i)
        val=0
        for j in range(len(yprime_loc)):
            pos = self.sli[i][j].val
            self.deviation[i][j]=abs(pos-yprime_loc[j])
        plt.close(fig=self.fig[i])

        
    def evaluation(self):    
        for i in range(self.Nquest):
            self.question_dev[i]=sum(self.deviation[i])
        total_deviation=sum(self.question_dev)
        
        for i in range(self.Nquest):
            x,_,_,_,yprime=func(i)
            self.axsol[i].plot(x, yprime,'--')
            self.fig[i].show()
            print("Bei dieser Frage war die Abweichung:",self.question_dev[i])
        print("_____________________________________________________________________")
        print("Frage                  Abweichung")
        for i in range(self.Nquest):
            print(i,"                    ",self.question_dev[i])
        print("                      __________")
        print("Gesamtabweichung:     ", total_deviation)
              
        
        

        



