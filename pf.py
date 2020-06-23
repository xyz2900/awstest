# Money Managementç¡ãã§å¸ã«ïæ
rdata = pd.DataFrame([], columns=['date', 'cont', 'cont2', 'result', 'result2', 'total', 'total2'])

# DD drawdown1:ä¡æ¼ 
ddlist = pd.DataFrame([], columns=['date', 'drawdown1'])
ddlist2 = pd.DataFrame([], columns=['date', 'drawdownp'])

# é£çåã¡è ãã®æ°
cclist = pd.DataFrame([], columns=['date', 'count1', 'count2'])

total = 1000000
total2 = 1000000
win_cnt = 0
win_total = 0
win_total2 = 0
los_cnt = 0
los_total = 0
los_total2 = 0
max_total = 0
max_total_date = ""
max_total2 = 0
max_total2_date = ""
max_dd = 0
max_dd_date = ""
max_dd2 = 0
max_dd2_date = ""
max_ddp = 0
max_ddp_date = ""
max_ddp2 = 0
max_ddp2_date = ""
max_win = 0
max_win_date = ""
max_win2 = 0
max_win2_date = ""
max_los = 0
max_los_date = ""
max_los2 = 0
max_los2_date = ""
pcnt = 0
pdata = []
avg_los = 0
max_los = 0
con_win = 0 # é£çåã¡æ°
con_los = 0 # é£çè ãæ°
max_con_win = 0
max_con_los = 0
max_con_win_date = ""
max_con_los_date = ""
last_result = None

for index, row in df.iterrows():
    result = row['result']
    
    cont = 1
 
    total = total + int(result * cont)
    pdata.append(result)

    if result > 0:
        win_cnt   = win_cnt + 1
        win_total = win_total + result
        if last_result and last_result > 0:
            con_win += 1
            con_los = 0
            if con_win > max_con_win:
                max_con_win = con_win
                max_con_win_date = row['exit_date']
    else:
        los_cnt   = los_cnt + 1
        los_total = los_total + result
        if last_result and last_result < 0:
            con_los += 1
            con_win = 0
            if con_los > max_con_los:
                max_con_los = con_los
                max_con_los_date = row['exit_date']
                
    cclist = cclist.append(pd.DataFrame([[row['exit_date'], con_win, con_los]], columns=['date', 'count1', 'count2']), ignore_index=True, sort=False)
        
    if max_win == 0 or result > max_win:
        max_win = result
        max_win_date = row['exit_date']
        
    if max_los == 0 or result < max_los:
        max_los = result
        max_los_date = row['exit_date']
        
    if total > max_total:
        max_total = total
        max_total_date = row['exit_date']
        
    draw_down = max_total - total
    
    ddlist = ddlist.append(pd.DataFrame([[row['exit_date'], draw_down]], columns=['date', 'drawdown1']), ignore_index=True, sort=False)

    if draw_down > max_dd:
        max_dd = draw_down
        max_dd_date = row['exit_date']
   
    draw_downp = (max_total - total) / max_total * 100
    if draw_downp > max_ddp:
        max_ddp = draw_downp
        max_ddp_date = row['exit_date']
        
    ddlist2 = ddlist2.append(pd.DataFrame([[row['exit_date'], draw_downp]], columns=['date', 'drawdownp']), ignore_index=True, sort=False)
        
    rdata = rdata.append(pd.DataFrame([[row['exit_date'], row.cont, cont, result, total]], columns=['date', 'cont', 'cont1', 'result', 'total']), ignore_index=True, sort=False)

    last_result = result
    
buy_rdata = rdata[rdata['cont'] > 0].loc[:,['date', 'result']]
buy_rdata = buy_rdata.rename(columns={'result': 'buy_result'})
buy_rdata = buy_rdata.set_index('date')
sell_rdata = rdata[rdata['cont'] < 0].loc[:,['date','cont1', 'result']]
sell_rdata = sell_rdata.rename(columns={'result': 'sell_result'})
sell_rdata = sell_rdata.set_index('date')
                                                          
rdata = rdata.set_index('date')
rdata = pd.concat([rdata, buy_rdata, sell_rdata], axis=1)
ddlist = ddlist.set_index('date')
ddlist.index = pd.to_datetime(ddlist.index)
rdata['mean'] = rdata['result'].mean()
rdata['std'] = rdata['result'].std()
rdata['sharp'] = rdata['mean'] / rdata['std']
rdata['buy_total'] = rdata['buy_result'].cumsum()
rdata['sell_total'] = rdata['sell_result'].cumsum()

cclist = cclist.set_index('date')
cclist.index = pd.to_datetime(cclist.index)

avg_win = (win_total / win_cnt)
avg_los = (los_total / los_cnt)
print("total=%d" % total)
print("max_total=%d %s" %(max_total, max_total_date))
print("max_dd=%d %s" % (max_dd, max_dd_date))
print("max_ddp=%5.2f %s" % (max_ddp, max_ddp_date))
print("max_win=%d %s" % (max_win, max_win_date))
print("max_los=%d %s" % (max_los, max_los_date))
print("max_con_win=%d %s " % (max_con_win, max_con_win_date))
print("max_con_los=%d %s " % (max_con_los, max_con_los_date))
print("avg_win=%5.2f" % (win_total / win_cnt))
print("avg_los=%5.2f" % (los_total / los_cnt))
print("win_total=%d" % win_total)
print("los_total=%d" % los_total)
print("PF=%5.2f" % abs(win_total / los_total))
print("PR=%5.2f" % abs(avg_win / avg_los))
print("SR=%5.2f" % rdata['sharp'].iloc[-1])

winp = 0.0
if win_cnt > 0 and los_cnt > 0:
    winp = win_cnt / (win_cnt + los_cnt)
print("win=%d los=%d winp=%5.2f" % (win_cnt, los_cnt, winp))
print("EV=%5.2f" % ((winp * avg_win) - ((1 - winp) * abs(avg_los))))  # æåå¤
print("current drawdown=%d" % (max_total - total))
print("current drawdownp=%5.2f" % ((max_total - total) / max_total * 100))

rdata['total2'] = rdata['result'].cumsum()
rdata2 = rdata[rdata.cont > 0]
rdata2['total2'] = rdata2['result'].cumsum()
rdata3 = rdata[rdata.cont < 0]
rdata3['total2'] = rdata3['result'].cumsum()

fig, ax = plt.subplots()
#ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
#ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

ax.plot(rdata.index, rdata.total2, color='red', label='total')
ax.plot(rdata2.index, rdata2.total2, color='green', label='cont > 0')
ax.plot(rdata3.index, rdata3.total2, color='blue', label='cont < 0')

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m'))

#rdata['total'].plot(color='yellow')
#rdata['total2'].plot(color='red')
#rdata2['total2'].plot(color='green')
#rdata3['total2'].plot(color='blue')

plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=18)

labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, fontsize=10);

#plt.xticks(rotation=45)
#rdata['buy_total'].plot()
#rdata['sell_total'].plot()

#rdata['result'].plot()
plt.show()
