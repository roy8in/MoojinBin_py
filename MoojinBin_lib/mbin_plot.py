#%%
# 필요한 Library 호출
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
font_path = 'C:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#%%
# Palette 지정
color0 = 'darkslategray'
color1 = 'mediumseagreen'
color2 = 'tan'
color3 = 'red'
color4= 'darkcyan'
color5= 'cornflowerblue'
colors = [color0, color1, color2, color3, color4, color5]


#%%
def plot_11(df, label, unit=None, ma=None, multi_line=False, st=False):
    fig, ax = plt.subplots(figsize=(6,3.5))
    
    if multi_line:
        for i in range(len(label)):
            if i < 4:
                ax.plot(df[df.columns[i]], label=label[i], color=colors[i], zorder=10-i)
            else:
                ax.plot(df[df.columns[i]], label=label[i], color=(colors+colors)[i], zorder=10-i, linestyle='--')
    else:
        if (ma != None and ma > 0):
            ax.plot(df, color=color0, alpha=0.5)
            ax.plot(df.rolling(ma).mean(), label=label, color=color0)
        else:
            ax.plot(df, color=color0, label=label)
    
    if unit != None:
        ax.set_ylabel(unit, ha='left', y=1.03, rotation=0)
    
    ax.grid(linestyle='--')
    
    if st:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('`%y.%m'))
    
    plt.legend(framealpha=0)    


#%%
def plot_11_dual(df0, label0, df1, label1, unit0=None, unit1=None, st=False):
    fig, ax0 = plt.subplots(figsize=(6,3.5))
    
    ln0 = ax0.plot(df0, color=color0, label=label0)
    if unit0!=None:
        ax0.set_ylabel(unit0, ha='left', y=1.03, rotation=0, rotation_mode="anchor", verticalalignment='baseline')
        
    ax1 = ax0.twinx()
    ln1 = ax1.plot(df1, color=color1, label=label1)
    if unit1!=None:
        ax1.set_ylabel(unit1, ha='right', y=1.03, rotation=0, rotation_mode="anchor", verticalalignment='baseline')
        
    lns = ln0 + ln1
    lab = [l.get_label() for l in lns]
    
    if st:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('`%y.%m'))
    
    ax0.legend(lns, lab, framealpha=0)


#%%
def plot_21(df0, label0, df1, label1, unit0=None, ma0=None, unit1=None, ma1=None):
  
    fig = plt.figure(figsize=(6,6))
    plt.subplots_adjust(hspace=0.1)
    gs = fig.add_gridspec(2,1)
    
    ax0 = plt.subplot(gs[0,0])            
    if (ma0 != None and ma0 > 0):
        ax0.plot(df0, color=color0, label=label0, alpha=0.5)
        ax0.plot(df0.rolling(ma0).mean(), color=color0)
    else:
        ax0.plot(df0, color=color0, label=label0)
    ax0.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ax0.spines[['bottom']].set_visible(False)
        
    ax1 = plt.subplot(gs[1,0], sharex=ax0)
    if (ma1 != None and ma1 > 0):
        ax1.plot(df1, color=color1, alpha=0.5)
        ax1.plot(df1.rolling(ma1).mean(), label=label1, color=color1)
    else:
        ax1.plot(df1, color=color1, label=label1)
    ax1.spines[['top']].set_visible(False)
        
    for i in [ax0, ax1]:
        i.legend()
        
    if unit0 != None:
        ax0.set_ylabel(unit0, ha='left', y=1, rotation=0)
    if unit1 != None:
        ax1.set_ylabel(unit1, ha='left', y=1, rotation=0)


#%%
def plot_yc(df, x, period=[5, 22, 65], unit='(%)'):
    # Period: 1 x 3 series
    fig, ax = plt.subplots(figsize=(6,3.5))
    y0 = df.iloc[-1]
    y1 = df.iloc[-period[0]]
    y2 = df.iloc[-period[1]]
    y3 = df.iloc[-period[2]]
    
    plt.plot(x, y0, color=colors[0], label='Current', marker='o')
    plt.plot(x, y1, color=colors[1], label='-%.0fD'%period[0], marker='o')
    plt.plot(x, y2, color=colors[2], label='-%.0fD'%period[1], marker='o')
    plt.plot(x, y3, color=colors[3], label='-%.0fD'%period[2], marker='o')
    plt.legend()
    ax.set_ylabel(unit, ha='left', y=1, rotation=0)
    

#%%
def plot_21_dual(df00, label00, unit00, df01, label01, unit01, df10, label10, unit10, df11, label11, unit11, scale0=False, scale1=False, st=False):
    
    fig = plt.figure(figsize=(6,6))
    plt.subplots_adjust(hspace=0.1)
    gs = fig.add_gridspec(2, 1)
    
    ax00 = plt.subplot(gs[0, 0])
    ln00 = ax00.plot(df00, label=label00, color=color0)
    ax00.set_ylabel(unit00, ha='left', y=1.03, rotation=0, rotation_mode="anchor", verticalalignment='baseline')
        
    ax01 = ax00.twinx()
    ln01 = ax01.plot(df01, label=label01, color=color1)
    ax01.set_ylabel(unit01, ha='right', y=1.03, rotation=0, rotation_mode="anchor", verticalalignment='baseline')
        
    lns0 = ln00 + ln01
    lab0 = [l.get_label() for l in lns0]
    ax00.legend(lns0, lab0, frameon=False)
    
    ax00.spines[['bottom']].set_visible(False)
    ax00.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ax01.spines[['bottom']].set_visible(False)
    ax01.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    
    if scale0:
        l00, h00 = ax00.get_ylim()
        l01, h01 = ax01.get_ylim()
        ax00.set_ylim([min(l00, l01), max(h00, h01)])
        ax01.set_ylim([min(l00, l01), max(h00, h01)])
    
    
    ax10 = plt.subplot(gs[1,0], sharex=ax00)
    ln10 = ax10.plot(df10, label=label10, color=color0)
    ax10.set_ylabel(unit10, ha='left', y=1.03, rotation=0, rotation_mode="anchor", verticalalignment='baseline')
        
    ax11 = ax10.twinx()
    ln11 = ax11.plot(df11, label=label11, color=color1)
    ax11.set_ylabel(unit11, ha='right', y=1.03, rotation=0, rotation_mode="anchor", verticalalignment='baseline')
    
    lns1 = ln10 + ln11
    lab1 = [l.get_label() for l in lns1]
    ax10.legend(lns1, lab1, frameon=False)
        
    ax10.spines[['top']].set_visible(False)
    ax11.spines[['top']].set_visible(False)
    
    if scale1:
        l10, h10 = ax10.get_ylim()
        l11, h11 = ax11.get_ylim()
        ax10.set_ylim([min(l10, l11), max(h10, h11)])
        ax11.set_ylim([min(l10, l11), max(h10, h11)])
    
    if st:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('`%y.%m'))
    
    
