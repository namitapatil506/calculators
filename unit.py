class Unit_conversion:

    def conversion(self, unit, num, u):

        if unit=='ft³':
            text=''
            if u=='m³':
                text=f'{num}*35.3147'
                num=float(num)*35.3147
            elif u=='cm³':
                text = f'{num}/28317'
                num=float(num)/28317
            elif u=='in³':
                text = f'{num}/1728'
                num=float(num)/1728
            elif u=='yd³':
                text = f'{num}*27'
                num=float(num)*27
            elif u=='mL':
                text = f'{num}/28317'
                num=float(num)/28317
            elif u=='L':
                text = f'{num}/28.317'
                num=float(num)/28.317
            elif u=='US gal':
                text = f'{num}/7.481'
                num=float(num)/7.481
            elif u=='UK gal':
                text = f'{num}/6.229'
                num=float(num)/6.229
            elif u=='US fl oz':
                text = f'{num}/958'
                num=float(num)/958
            elif u=='UK fl oz':
                text = f'{num}/997'
                num=float(num)/997
            return num,text

        # for per 'u3' to per m3 conversion
        if unit=='m³':
            text = ''
            if u=='ft³':
                text = f"{num}*35.3147"
                num=float(num)*35.3147
            elif u=='cm³':
                text = f"{num}*(1e+6)"
                num=float(num)*(1e+6)
            elif u=='dm³':
                text = f"{num}*1000"
                num=float(num)*1000
            elif u=='mm³':
                text = f"{num}*(1e+9)"
                num=float(num)*(1e+9)
            elif u=='in³':
                text = f"{num}*61024"
                num=float(num)*61024
            elif u=='yd³':
                text = f"{num}*1.308"
                num=float(num)*1.308
            elif u=='mL':
                text = f"{num}*(1e+6)"
                num=float(num)*(1e+6)
            elif u=='cL':
                text = f"{num}*(1e+5)"
                num=float(num)*(1e+5)
            elif u=='L':
                text = f"{num}*1000"
                num=float(num)*1000
            elif u=='US gal':
                text = f"{num}*264"
                num=float(num)*264
            elif u=='UK gal':
                text = f"{num}*220"
                num=float(num)*220
            elif u=='US fl oz':
                text = f"{num}*33814"
                num=float(num)*33814
            elif u=='UK fl oz':
                text = f"{num}*35195"
                num=float(num)*35195
            return num,text


        elif unit=='Pa':
            text=''
            if u=='bar':
                text=f'{num}*10**5'
                num=float(num)*10**5
            elif u=='psi':
                text = f'{num}*6895'
                num=float(num)*6895
            elif u=='at':
                text = f'{num}*98066.5'
                num=float(num)*98066.5
            elif u=='atm':
                text = f'{num}*101325'
                num=float(num)*101325
            elif u=='Torr':
                text = f'{num}*133'
                num=float(num)*133
            elif u=='hPa':
                text = f'{num}*100'
                num=float(num)*100
            elif u=='kPa':
                text = f'{num}*1000'
                num=float(num)*1000
            elif u=='MPa':
                text = f'{num}*10**6'
                num=float(num)*10**6
            elif u=='GPa':
                text = f'{num}*10**9'
                num=float(num)*10**9
            elif u=='in Hg':
                text = f'{num}*3386'
                num=float(num)*3386
            elif u=='mm Hg':
                text = f'{num}*133'
                num=float(num)*133
            elif u=='lbs/ft²':
                text = f'{num}*47.88'
                num=float(num)*47.88
            return num,text

        elif unit=='hp(E)':
            text=''
            if u=='mW':
                text=f'{num}/746000'
                num=float(num)/746000
            elif u=='W':
                text = f'{num}/746'
                num=float(num)/746
            elif u=='kW':
                text = f'{num}/0.746'
                num=float(num)/0.746
            elif u=='MW':
                text = f'{num}/0.000746'
                num=float(num)/0.000746
            elif u=='hp(l)':
                text = f'{num}/1'
                num=float(num)/1
            elif u=='hp(M)':
                text = f'{num}/1.014'
                num=float(num)/1.014
            elif u=='ahp':
                text = f'{num}/1.00041'
                num=float(num)/1.00041
            return num,text

        if unit=='kg':
            text=''
            if u=='µg':
                text = f'{num}/(1e+9)'
                num=float(num)/(1e+9)
            elif u=='g':
                text = f'{num}/1000'
                num=float(num)/1000
            elif u=='mg':
                text = f'{num}/(1e+6)'
                num=float(num)/(1e+6)
            elif u=='dag':
                text = f'{num}/100'
                num=float(num)/100
            elif u=='t':
                text = f'{num}*1000'
                num=float(num)*1000
            elif u=='gr':
                text = f'{num}/15432'
                num=float(num)/15432
            elif u=='dr':
                text = f'{num}*0.0017718451953125'
                num=float(num)*0.0017718451953125
            elif u=='oz':
                text = f'{num}*0.02834952'
                num=float(num)*0.02834952
            elif u=='lb':
                text = f'{num}*0.45359237'
                num=float(num)*0.45359237
            elif u=='stone':
                text = f'{num}*6.35'
                num=float(num)*6.35
            elif u=='US ton':
                text = f'{num}*907'
                num=float(num)*907
            elif u=='Long ton':
                text = f'{num}/1016'
                num=float(num)/1016
            elif u=='Earths':
                text = f'{num}*(5.9760000000002E+24)'
                num=float(num)*(5.9760000000002E+24)
            elif u=='Suns':
                text = f'{num}*(1.999999999E+30)'
                num=float(num)*(1.999999999E+30)
            elif u=='me':
                text = f'{num}/(9.223E+18)'
                num=float(num)/(9.223E+18)
            elif u=='u':
                text = f'{num}*(1.6605402E-27)'
                num=float(num)*(1.6605402E-27)
            elif u=='oz t':
                text = f'{num}*0.031'
                num=float(num)*0.031
            return num,text


        elif unit=='m':
            text=''
            if u=='km':
                text = f'{num}*1000'
                num=float(num)*1000
            elif u=='yd':
                text = f'{num}/1.094'
                num=float(num)/1.094
            elif u=='mi':
                text = f'{num}*1609'
                num=float(num)*1609
            elif u=='R⊕':
                text = f'{num}*6378160'
                num=float(num)*6378160
            elif u=='R⊙':
                text = f'{num}*696000000'
                num=float(num)*696000000
            elif u=='cm':
                text = f'{num}/100'
                num=float(num)/100
            elif u=='µm':
                text = f'{num}/(1e+6)'
                num=float(num)/(1e+6)
            elif u=='nm':
                text = f'{num}/(1e+9)'
                num=float(num)/(1e+9)
            elif u=='pm':
                text = f'{num}/(1e+12)'
                num=float(num)/(1e+12)
            elif u=='Å':
                text = f'{num}/(1e+10)'
                num=float(num)/(1e+10)
            elif u=='mm':
                text = f'{num}/1000'
                num=float(num)/1000
            elif u=='in':
                text = f'{num}/39.37'
                num=float(num)/39.37
            elif u=='ft':
                text = f'{num}/3.281'
                num=float(num)/3.281
            return num,text

        elif unit=='mm':
            text=''
            if u=='cm':
                text = f'{num}*10'
                num=float(num)*10
            elif u=='m':
                text = f'{num}*1000'
                num=float(num)*1000
            elif u=='in':
                text = f'{num}*25.4'
                num=float(num)*25.4
            elif u=='ft':
                text = f'{num}*305'
                num=float(num)*305
            elif u=='yd':
                text = f'{num}*914'
                num=float(num)*914
            return num,text

        elif unit=='cm':
            text=''
            if u=='m':
                text=f'{num}*100'
                num=float(num)*100
            elif u=='mm':
                text = f'{num}/10'
                num=float(num)/10
            elif u=='km':
                text = f'{num}*100000'
                num=float(num)*100000
            elif u=='in':
                text = f'{num}*2.54'
                num=float(num)*2.54
            elif u=='ft':
                text = f'{num}*30.48'
                num=float(num)*30.48
            elif u=='yd':
                text = f'{num}*91.44'
                num=float(num)*91.44
            elif u=='mi':
                text = f'{num}*160934'
                num=float(num)*160934
            elif u=='nmi':
                text = f'{num}*185200'
                num=float(num)*185200
            return num,text


        elif unit=='m/s²':
            text = ''
            if u=='g':
                text=f'{num}*9.81'
                num=float(num)*9.81
            elif u=='ft/s²':
                text=f'{num}*32.17'
                num=float(num)*32.17
            return num,text

        elif unit=='Nm':
            text = ''
            if u=='kg-cm':
                text=f'{num}*0.09807'
                num=float(num)*0.09807
            elif u=='J/rad':
                text=f'{num}*1'
                num=float(num)*1
            elif u=='ft-lb':
                text=f'{num}*1.356'
                num=float(num)*1.356
            return num,text

        elif unit=='RPM':
            text = ''
            if u=='Hz':
                text=f'{num}*60'
                num=float(num)*60
            elif u=='kHz':
                text=f'{num}*60000'
                num=float(num)*60000
            elif u=='MHz':
                text=f'{num}*60000000'
                num=float(num)*60000000
            elif u=='GHz':
                text=f'{num}*60000000000'
                num=float(num)*60000000000
            elif u=='THz':
                text=f'{num}*60000000024000 '
                num=float(num)*60000000024000
            return num,text

        elif unit=='m/s':
            text=''
            if u=='km/s':
                text=f'{num}*1000'
                num=float(num)*1000
            elif u=='km/h':
                text = f'{num}/3.6'
                num=float(num)/3.6
            elif u=='mph':
                text = f'{num}/2.237'
                num=float(num)/2.237
            elif u=='mi/s':
                text = f'{num}*1609'
                num=float(num)*1609
            elif u=='c':
                text = f'{num}*2.998e+8'
                num=float(num)*2.998e+8
            elif u=='ft/s':
                text = f'{num}/3.281'
                num=float(num)/3.281
            elif u=='ft/min':
                text = f'{num}/197'
                num=float(num)/197
            elif u=='knots':
                text = f'{num}/1.944'
                num=float(num)/1.944
            return num,text



        elif unit=='joules':
            text=''
            if u=='kJ':
                text=f'{num}*1000'
                num=float(num)*1000
            elif u=='MJ':
                text = f'{num}*10**6'
                num=float(num)*10**6
            elif u=='Wh':
                text = f'{num}*3600'
                num=float(num)*3600
            elif u=='kWh':
                text = f'{num}*(3.6e+6)'
                num=float(num)*(3.6e+6)
            elif u=='ft-lb':
                text = f'{num}*1.356'
                num=float(num)*1.356
            elif u=='kcal':
                text = f'{num}*4184'
                num=float(num)*4184
            elif u=='eV':
                text = f'{num}/(6.242e+18)'
                num=float(num)/(6.242e+18)
            return num,text

        elif unit=='eV':
            text=''
            if u=='nJ':
                text=f'{num}*6241506363.094'
                num=float(num)*6241506363.094
            elif u=='neV':
                text = f'{num}/(1e+9)'
                num=float(num)/(1e+9)
            elif u=='µeV':
                text = f'{num}/(1e+6)'
                num=float(num)/(1e+6)
            elif u=='meV':
                text = f'{num}/1000'
                num=float(num)/1000
            elif u=='keV':
                text = f'{num}*1000'
                num=float(num)*1000
            elif u=='MeV':
                text = f'{num}*(1e+6)'
                num=float(num)*(1e+6)
            return num,text

        elif unit=='J/kg.K':
            text=''
            if u=='J/g.K':
                text=f'{num}*1000'
                num=float(num)*1000
            elif u=='cal/kg.K':
                text = f'{num}*4.184'
                num=float(num)*4.184
            elif u=='cal/g.K':
                text = f'{num}*4184'
                num=float(num)*4184
            elif u=='kcal/kg.K':
                text = f'{num}/4184'
                num=float(num)/4184
            elif u=='J/kg.°C':
                text = f'{num}'
                num=float(num)
            elif u=='J/g.°C':
                text = f'{num}*1000'
                num=float(num)*1000
            elif u=='cal/kg.°C':
                text = f'{num}/4.1868'
                num=float(num)/4.1868
            elif u=='cal/g.°C':
                text = f'{num}/4186.8'
                num=float(num)/4186.8
            elif u=='kcal/kg.°C':
                text = f'{num}/4186.8'
                num=float(num)/4186.8
            return num,text


        elif unit=='sec':
            text=''
            if u=='min':
                text=f'{num}*60'
                num=float(num)*60
            elif u=='hrs':
                text = f'{num}*3600'
                num=float(num)*3600
            elif u=='days':
                text = f'{num}*86400'
                num=float(num)*86400
            elif u=='weeks':
                text = f'{num}*604800'
                num=float(num)*604800
            elif u=='months':
                text = f'{num}*(2.628e+6)'
                num=float(num)*(2.628e+6)
            elif u=='years':
                text = f'{num}*(3.154e+7)'
                num=float(num)*(3.154e+7)
            return num,text

        elif unit=='K':
            text=''
            if u=='°C':
                text=f'{num}+273.15'
                num=float(num)+273.15
            elif u=='°F':
                text = f'({num}-32)*5/9+273.15'
                num=(float(num)-32)*5/9+273.15
            return num,text

        elif unit=='°C':
            if u=='K':
                num=float(num)-273.15
            elif u=='°F':
                num=(float(num)-32)/2
            return num

        elif unit=='%':
            if u=='‰':
                num=float(num)*0.1
            elif u=='‱':
                num=float(num)*0.01
            return num


        elif unit=='kg/m³':
            text=''
            if u=='kg/dm³':
                text = f"{num}*1000"
                num=float(num)*1000
            elif u=='kg/L':
                text = f"{num}*1000"
                num=float(num)*1000
            elif u=='g/mL':
                text = f"{num}*1000"
                num=float(num)*1000
            elif u=='t/m³':
                text = f"{num}*1000"
                num=float(num)*1000
            elif u=='g/cm³':
                text = f"{num}*1000"
                num=float(num)*1000
            elif u=='oz/cu in':
                text = f"{num}*1730"
                num=float(num)*1730
            elif u=='lb/cu in':
                text = f"{num}*27680"
                num=float(num)*27680
            elif u=='lb/cu ft':
                text = f"{num}*16.018"
                num=float(num)*16.018
            elif u=='lb/cu yd':
                text = f"{num}*0.5932"
                num=float(num)*0.5932
            elif u=='lb/US gal':
                text = f"{num}*120"
                num=float(num)*120
            elif u=='g/L':
                text = f"{num}*1"
                num=float(num)*1
            elif u=='g/dL':
                text = f"{num}*10"
                num=float(num)/10
            elif u=='mg/L':
                text = f"{num}*0.0010"
                num=float(num)*0.0010
            return num,text

        elif unit=='W':
            text=''
            if u=='kW':
                text=f'{num}*1000'
                num=float(num)*1000
            elif u=='MW':
                text = f'{num}*(1e+6)'
                num=float(num)*(1e+6)
            elif u=='mW':
                text = f'{num}/1000'
                num=float(num)/1000
            elif u=='GW':
                text = f'{num}*(1e+9)'
                num=float(num)*(1e+9)
            elif u=='BTU/h':
                text = f'{num}*0.29307107'
                num=float(num)*0.29307107
            elif u=='hp(l)':
                text = f'{num}*746'
                num=float(num)*746
            return num,text

        elif unit=='A':
            text=''
            if u=='mA':
                text=f'{num}/1000'
                num=float(num)/1000
            elif u=='μA':
                text = f'{num}/(1e+6)'
                num=float(num)/1000000
            return num,text

        elif unit=='GW':
            text=''
            if u=='L☉':
                text=f'{num}*(3.827e+17)'
                num=float(num)*(3.827e+17)
            return num,text

        elif unit=='pcs':
            text=''
            if u=='m':
                text=f'{num}*(3.2407e-17)'
                num=float(num)*(3.2407e-17)
            elif u=='km':
                text=f'{num}*(3.2407e-14)'
                num=float(num)*(3.2407e-14)
            elif u=='mi':
                text=f'{num}*(5.215e-14)'
                num=float(num)*(5.215e-14)
            elif u=='ly':
                text=f'{num}*0.30660'
                num=float(num)*0.30660
            return num,text

        elif unit=='km':
            text=''
            if u=='m':
                text=f'{num}/1000'
                num=float(num)/1000
            elif u=='mi':
                text = f'{num}*1.609'
                num=float(num)*1.609
            elif u=='R☉':
                text = f'{num}*695700'
                num=float(num)*695700
            return num,text

        elif unit=='T':
            text=''
            if u=='mT':
                text=f'{num}/1000'
                num=float(num)/1000
            elif u=='μT':
                text = f'{num}/(1e+6)'
                num=float(num)/1000000
            return num,text

        elif unit=='H':
            text=''
            if u=='mH':
                text=f'{num}/1000'
                num=float(num)/1000
            elif u=='µH':
                text = f'{num}/(1e+6)'
                num=float(num)/1000000
            elif u=='nH':
                text = f'{num}/(1e+9)'
                num=float(num)/1000000000
            return num,text

        elif unit=='V':
            text=''
            if u=='mV':
                text=f'{num}/1000'
                num=float(num)/1000
            elif u=='kV':
                text = f'{num}*1000'
                num=float(num)*1000
            elif u=='MV':
                text = f'{num}*(1e+6)'
                num=float(num)*1000000
            return num,text

        elif unit=='N':
            text=''
            if u=='kN':
                text=f'{num}*1000'
                num=float(num)*1000
            elif u=='MN':
                text = f'{num}*(1e+6)'
                num=float(num)*(1e+6)
            elif u=='GN':
                text = f'{num}*(1e+9)'
                num=float(num)*(1e+9)
            elif u=='TN':
                text = f'{num}*(1e+12)'
                num=float(num)*(1e+12)
            elif u=='pdl':
                text = f'{num}/7.233'
                num=float(num)/7.233
            elif u=='dyn':
                text = f'{num}/100000'
                num=float(num)/100000
            elif u=='lbf':
                text = f'{num}*4.448'
                num=float(num)*4.448
            return num,text

        elif unit=='deg':
            text=''
            if u=='rad':
                text=f'{num}*57.29'
                num=float(num)*57.29
            elif u=='arcmin':
                text=f'{num}/60'
                num=float(num)/60
            elif u=='arcsec':
                text=f'{num}/3600'
                num=float(num)/3600
            elif u=='mrad':
                text=f'{num}*0.0572'
                num=float(num)*0.0572
            return num,text

        elif unit=='C':
            text=''
            if u=='pC':
                text=f'{num}/1e+12'
                num=float(num)/(1e+12)
            elif u=='mC':
                text = f'{num}/1000'
                num=float(num)/1000
            elif u=='µC':
                text = f'{num}/(1e+6)'
                num=float(num)/(1e+6)
            elif u=='nC':
                text = f'{num}/(1e+9)'
                num=float(num)/(1e+9)
            elif u=='e':
                text = f'{num}*(6.242e+18)'
                num=float(num)*(6.242e+18)
            return num,text

        elif unit=='N/C':
            text=''
            if u=='kN/C':
                text=f'{num}*1000'
                num=float(num)*1000
            elif u=='mN/C':
                text = f'{num}/1000'
                num=float(num)/1000
            elif u=='µN/C':
                text = f'{num}/(1e+6)'
                num=float(num)/(1e+6)
            elif u=='nN/C':
                text = f'{num}/(1e+9)'
                num=float(num)/(1e+9)
            elif u=='e':
                text = f'{num}*(6.242e+18)'
                num=float(num)*(6.242e+18)
            return num,text

        elif unit=='F':
            text=''
            if u=='mF':
                text=f'{num}/1000'
                num=float(num)/1000
            elif u=='µF':
                text = f'{num}/(1e+6)'
                num=float(num)/(1e+6)
            elif u=='nF':
                text = f'{num}/(1e+9)'
                num=float(num)/(1e+9)
            elif u=='pF':
                text = f'{num}/(1e+12)'
                num=float(num)/(1e+12)
            return num,text

        elif unit=='Ω':
            text=''
            if u=='mΩ':
                text=f'{num}/1000'
                num=float(num)/1000
            elif u=='kΩ':
                text = f'{num}*1000'
                num=float(num)*1000
            elif u=='MΩ':
                text = f'{num}*(1e+6)'
                num=float(num)*(1e+6)
            return num,text

        elif unit=='Hz':
            text=''
            if u=='kHz':
                text=f'{num}*1000'
                num=float(num)*1000
            elif u=='MHz':
                text = f'{num}*(1e+6)'
                num=float(num)*(1e+6)
            elif u=='GHz':
                text = f'{num}*(1e+9)'
                num=float(num)*(1e+9)
            elif u=='THz':
                text = f'{num}*(1e+12)'
                num=float(num)*(1e+12)
            elif u=='RPM':
                text = f'{num}*0.016667'
                num=float(num)*0.016667
            return num,text

        elif unit=='per sec':
            text=''
            if u=='per min':
                text=f'{num}/60'
                num=float(num)/60
            elif u=='per hrs':
                text = f'{num}/3600'
                num=float(num)/3600
            elif u=='per days':
                text = f'{num}/86400'
                num=float(num)/86400
            elif u=='per weeks':
                text = f'{num}/604800'
                num=float(num)/604800
            elif u=='per months':
                text = f'{num}/2.628e+6'
                num=float(num)/2.628e+6
            elif u=='per years':
                text = f'{num}/3.154e+7'
                num=float(num)/3.154e+7
            return num,text

        elif unit=='m²':
            text=''
            if u=='cm²':
                text = f"{num}/10000"
                num=float(num)/10000
            elif u=='dm²':
                text = f"{num}/100"
                num=float(num)/100
            elif u=='mm²':
                text = f"{num}/(1e+6)"
                num=float(num)/(1e+6)
            elif u=='km²':
                text = f"{num}*(1e+6)"
                num=float(num)*(1e+6)
            elif u=='in²':
                text = f"{num}/1550"
                num=float(num)/1550
            elif u=='ft²':
                text = f"{num}/10.764"
                num=float(num)/10.764
            elif u=='yd²':
                text = f"{num}/1.196"
                num=float(num)/1.196
            elif u=='mi²':
                text = f"{num}*(2.59e+6)"
                num=float(num)*(2.59e+6)
            elif u=='a':
                text = f"{num}*100"
                num=float(num)*100
            elif u=='da':
                text = f"{num}*10"
                num=float(num)*10
            elif u=='ha':
                text = f"{num}*10000"
                num=float(num)*10000
            elif u=='ac':
                text = f"{num}*4047"
                num=float(num)*4047
            elif u=='soccer fields':
                text = f"{num}/7142"
                num=float(num)/7142
            return num,text



    def check(self, conv_unit, value, unit):
        if unit != conv_unit:
            changed_value = self.conversion(conv_unit, value, unit)
            return changed_value

        else:
            return value

    def check1(self, conv_unit, value, unit, name):
        if unit != conv_unit:
            changed_value = self.conversion(conv_unit, value, unit)
            text =f"{value} in {conv_unit} is {changed_value} {conv_unit}"
            print(changed_value, text)

            return changed_value, text

        else:
            return value, ''


class Type:
    def type_conversion(self, num):
        if num.isdigit():
            Number = int(num)

        else:
            Number = float(num)

        return Number

# u=Unit_conversion()
# a=u.conversion('A', 4, 'μA')
# print(a)
