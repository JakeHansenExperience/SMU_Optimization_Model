from .models import Plant, Demand, Function, Layout, PlantResult, Station
from gekko import GEKKO


def cutSeamFab(stations):
    ih, ig, lc, ls, sp = 0.0,0.0,0.0,0.0,0.0
    ihMax, igMax, lcMax, lsMax, spMax = 0,0,0,0,0
    catches = ['Cutting' , 'Seaming' , 'Fabrication']
    for station in stations:
        for catch in catches:
            if catch in station.name:
                #ih
                if station.interior_heavy_capacity > 0:
                    ih += float(station.variable_dollar_hr)
                    if station.interior_heavy_capacity > ihMax:
                        ihMax = float(station.interior_heavy_capacity)
                #ig
                if station.insulated_glass_capacity > 0:
                    ig += float(station.variable_dollar_hr)
                    if station.insulated_glass_capacity > igMax:
                        igMax = float(station.insulated_glass_capacity)

                #lc
                if station.laminated_complex_capacity > 0:
                    lc += float(station.variable_dollar_hr)
                    if station.laminated_complex_capacity > lcMax:
                        lcMax = float(station.laminated_complex_capacity)
                #ls
                if station.laminated_simple_capacity > 0:
                    ls += float(station.variable_dollar_hr)
                    if station.laminated_simple_capacity > lsMax:
                        lsMax = float(station.laminated_simple_capacity)

                #sp
                if station.specialty_capacity > 0:
                    sp += float(station.variable_dollar_hr)
                    if station.specialty_capacity > spMax:
                        spMax = float(station.specialty_capacity)

    try:
        returnIH = ih/ihMax
    except:
        returnIH = 0
    try:
        returnIG = ig/igMax
    except:
        returnIG = 0
    try:
        returnLC = lc/lcMax
    except:
        returnLC = 0
    try:
        returnLS = ls/lsMax
    except:
        returnLS = 0
    try:
        returnSP = sp/spMax
    except:
        returnSP = 0
    return returnIH,returnIG,returnLC,returnLS,returnSP


def tempering(stations):
    ih, ig, lc, ls, sp = 0.0,0.0,0.0,0.0,0.0
    ihMax, igMax, lcMax, lsMax, spMax = 0,0,0,0,0
    for station in stations:
        if 'Tempering' in station.name:
            #ih
            if station.interior_heavy_capacity > 0:
                ih += float(station.variable_dollar_hr)
                if station.interior_heavy_capacity > ihMax:
                    ihMax = float(station.interior_heavy_capacity)
            #ig
            if station.insulated_glass_capacity > 0:
                ig += float(station.variable_dollar_hr)
                if station.insulated_glass_capacity > igMax:
                    igMax = float(station.insulated_glass_capacity)

            #lc
            if station.laminated_complex_capacity > 0:
                lc += float(station.variable_dollar_hr)
                if station.laminated_complex_capacity > lcMax:
                    lcMax = float(station.laminated_complex_capacity)
            #ls
            if station.laminated_simple_capacity > 0:
                ls += float(station.variable_dollar_hr)
                if station.laminated_simple_capacity > lsMax:
                    lsMax = float(station.laminated_simple_capacity)

            #sp
            if station.specialty_capacity > 0:
                sp += float(station.variable_dollar_hr)
                if station.specialty_capacity > spMax:
                    spMax = float(station.specialty_capacity)

    try:
        returnIH = ih/ihMax
    except:
        returnIH = 0
    try:
        returnIG = ig/igMax
    except:
        returnIG = 0
    try:
        returnLC = lc/lcMax
    except:
        returnLC = 0
    try:
        returnLS = ls/lsMax
    except:
        returnLS = 0
    try:
        returnSP = sp/spMax
    except:
        returnSP = 0
    return returnIH,returnIG,returnLC,returnLS,returnSP

def lamination(stations):
    ih, ig, lc, ls, sp = 0.0,0.0,0.0,0.0,0.0
    ihMax, igMax, lcMax, lsMax, spMax = 0,0,0,0,0
    catches = ['Lamination']
    for station in stations:
        for catch in catches:
            if catch in station.name:
                #ih
                if station.interior_heavy_capacity > 0:
                    ih += float(station.variable_dollar_hr)
                    if station.interior_heavy_capacity > ihMax:
                        ihMax = float(station.interior_heavy_capacity)
                #ig
                if station.insulated_glass_capacity > 0:
                    ig += float(station.variable_dollar_hr)
                    if station.insulated_glass_capacity > igMax:
                        igMax = float(station.insulated_glass_capacity)

                #lc
                if station.laminated_complex_capacity > 0:
                    lc += float(station.variable_dollar_hr)
                    if station.laminated_complex_capacity > lcMax:
                        lcMax = float(station.laminated_complex_capacity)
                #ls
                if station.laminated_simple_capacity > 0:
                    ls += float(station.variable_dollar_hr)
                    if station.laminated_simple_capacity > lsMax:
                        lsMax = float(station.laminated_simple_capacity)

                #sp
                if station.specialty_capacity > 0:
                    sp += float(station.variable_dollar_hr)
                    if station.specialty_capacity > spMax:
                        spMax = float(station.specialty_capacity)

    try:
        returnIH = ih/ihMax
    except:
        returnIH = 0
    try:
        returnIG = ig/igMax
    except:
        returnIG = 0
    try:
        returnLC = lc/lcMax
    except:
        returnLC = 0
    try:
        returnLS = ls/lsMax
    except:
        returnLS = 0
    try:
        returnSP = sp/spMax
    except:
        returnSP = 0
    return returnIH,returnIG,returnLC,returnLS,returnSP


def assembly(stations):
    ih, ig, lc, ls, sp = 0.0,0.0,0.0,0.0,0.0
    ihMax, igMax, lcMax, lsMax, spMax = 0,0,0,0,0
    catches = ['Assembly']
    for station in stations:
        for catch in catches:
            if catch in station.name:
                #ih
                if station.interior_heavy_capacity > 0:
                    ih += float(station.variable_dollar_hr)
                    if station.interior_heavy_capacity > ihMax:
                        ihMax = float(station.interior_heavy_capacity)
                #ig
                if station.insulated_glass_capacity > 0:
                    ig += float(station.variable_dollar_hr)
                    if station.insulated_glass_capacity > igMax:
                        igMax = float(station.insulated_glass_capacity)

                #lc
                if station.laminated_complex_capacity > 0:
                    lc += float(station.variable_dollar_hr)
                    if station.laminated_complex_capacity > lcMax:
                        lcMax = float(station.laminated_complex_capacity)
                #ls
                if station.laminated_simple_capacity > 0:
                    ls += float(station.variable_dollar_hr)
                    if station.laminated_simple_capacity > lsMax:
                        lsMax = float(station.laminated_simple_capacity)

                #sp
                if station.specialty_capacity > 0:
                    sp += float(station.variable_dollar_hr)
                    if station.specialty_capacity > spMax:
                        spMax = float(station.specialty_capacity)

    try:
        returnIH = ih/ihMax
    except:
        returnIH = 0
    try:
        returnIG = ig/igMax
    except:
        returnIG = 0
    try:
        returnLC = lc/lcMax
    except:
        returnLC = 0
    try:
        returnLS = ls/lsMax
    except:
        returnLS = 0
    try:
        returnSP = sp/spMax
    except:
        returnSP = 0
    return returnIH,returnIG,returnLC,returnLS,returnSP

def shipping(stations):
    ih, ig, lc, ls, sp = 0.0,0.0,0.0,0.0,0.0
    ihMax, igMax, lcMax, lsMax, spMax = 0,0,0,0,0
    catches = ['Shipping']
    for station in stations:
        for catch in catches:
            if catch in station.name:
                #ih
                if station.interior_heavy_capacity > 0:
                    ih += float(station.variable_dollar_hr)
                    if station.interior_heavy_capacity > ihMax:
                        ihMax = float(station.interior_heavy_capacity)
                #ig
                if station.insulated_glass_capacity > 0:
                    ig += float(station.variable_dollar_hr)
                    if station.insulated_glass_capacity > igMax:
                        igMax = float(station.insulated_glass_capacity)

                #lc
                if station.laminated_complex_capacity > 0:
                    lc += float(station.variable_dollar_hr)
                    if station.laminated_complex_capacity > lcMax:
                        lcMax = float(station.laminated_complex_capacity)
                #ls
                if station.laminated_simple_capacity > 0:
                    ls += float(station.variable_dollar_hr)
                    if station.laminated_simple_capacity > lsMax:
                        lsMax = float(station.laminated_simple_capacity)

                #sp
                if station.specialty_capacity > 0:
                    sp += float(station.variable_dollar_hr)
                    if station.specialty_capacity > spMax:
                        spMax = float(station.specialty_capacity)

    try:
        returnIH = ih/ihMax
    except:
        returnIH = 0
    try:
        returnIG = ig/igMax
    except:
        returnIG = 0
    try:
        returnLC = lc/lcMax
    except:
        returnLC = 0
    try:
        returnLS = ls/lsMax
    except:
        returnLS = 0
    try:
        returnSP = sp/spMax
    except:
        returnSP = 0
    return returnIH,returnIG,returnLC,returnLS,returnSP

def calculateCost(stations):
    totalIH, totalIG, totalLC, totalLS, totalSP = 0,0,0,0,0

    #Cutting, Seaming, Fabrication
    ih1, ig1, lc1, ls1, sp1 = cutSeamFab(stations)

    #Tempering
    ih2, ig2, lc2, ls2, sp2 = tempering(stations)
    #lamination
    ih3, ig3, lc3, ls3, sp3 = lamination(stations)
    # assembly
    ih4, ig4, lc4, ls4, sp4 = assembly(stations)
    # shipping
    ih5, ig5, lc5, ls5, sp5 = shipping(stations)
    totalIH = ih1 + ih2 + ih3 + ih4 + ih5
    totalIG = ig1 + ig2 + ig3 + ig4 + ig5
    totalLC = lc1 + lc2 + lc3 + lc4 + lc5
    totalLS = ls1 + ls2 + ls3 + ls4 + ls5
    totalSP = sp1 + sp2 + sp3 + sp4 + sp5
    return totalIH, totalIG, totalLC, totalLS, totalSP

def smuModel(plants, demands, input_name):
    equations = []
    variables = []
    objective = []
    gekkoVariables = {}
    m = GEKKO()
    print("BEGGINING")
    for plantname in plants:

        #Determine Cost per square foot
        curPlant = Plant.objects.get(plant_name = plantname)
        stations = Station.objects.filter(plant=curPlant)
        ihCost, igCost, lcCost, lsCost, spCost = calculateCost(stations)

        # create Gekko Plant Variables and subsequent part of the objective function
        gekkoVariables[plantname] = {}
        glassTypes = ['ih', 'ig', 'lc', 'ls', 'sp']
        for thing in glassTypes:
            gekkoVariables[plantname][thing] = m.Var(lb=0, integer=True, ub=2000000, name= plantname + ' ' + thing)
            if thing == 'ih':
                m.Obj(gekkoVariables[plantname][thing]*ihCost)
            if thing == 'ig':
                m.Obj(gekkoVariables[plantname][thing]*igCost)
            if thing == 'lc':
                m.Obj(gekkoVariables[plantname][thing]*lcCost)
            if thing == 'ls':
                m.Obj(gekkoVariables[plantname][thing]*lsCost)
            if thing == 'sp':
                m.Obj(gekkoVariables[plantname][thing]*spCost)
        #Create Station Specific Equations
        for station in stations:
            RHS = station.time_hr_month
            try:
                ihvar = 1/station.interior_heavy_capacity
            except:
                ihvar = 0
            try:
                igvar = 1/station.insulated_glass_capacity
            except:
                igvar = 0
            try:
                lcvar = 1/station.laminated_complex_capacity
            except:
                lcvar = 0
            try:
                lsvar = 1/station.laminated_simple_capacity
            except:
                lsvar = 0
            try:
                spvar = 1/station.specialty_capacity
            except:
                spvar = 0

            LHS = ihvar*gekkoVariables[plantname]['ih'] + igvar*gekkoVariables[plantname]['ig'] + lcvar*gekkoVariables[plantname]['lc'] + lsvar*gekkoVariables[plantname]['ls'] + spvar*gekkoVariables[plantname]['sp']
            m.Equation(LHS < RHS)


    #Demands
    print("Printing Demands")
    for demand in demands:
        curDemand = Demand.objects.get(demand_name=demand)
        ihDemand = curDemand.interior_heavy_demand
        igDemand = curDemand.insulated_glass_demand
        lcDemand = curDemand.laminated_complex_demand
        lsDemand = curDemand.laminated_simple_demand
        spDemand = curDemand.specialty_demand
        ihTemp = [gekkoVariables[index]['ih'] for index in plants]
        igTemp = [gekkoVariables[index]['ig'] for index in plants]
        lcTemp = [gekkoVariables[index]['lc'] for index in plants]
        lsTemp = [gekkoVariables[index]['ls'] for index in plants]
        spTemp = [gekkoVariables[index]['sp'] for index in plants]
        m.Equation(sum(ihTemp) >= ihDemand)
        m.Equation(sum(igTemp) >= igDemand)
        m.Equation(sum(lcTemp) >= lcDemand)
        m.Equation(sum(lsTemp) >= lsDemand)
        m.Equation(sum(spTemp) >= spDemand)

    #Solve That Bitch
    m.solve()

    for plant in gekkoVariables:
        for type in gekkoVariables[plant]:
            print(plant, ': ', type, ': ', gekkoVariables[plant][type].value)

    #create new Layout

    print("HERERERERERERERERER")
    print(input_name)
    thisLayout = Layout(layout_name=input_name)
    thisLayout.save()
    print("nowHREREEERER")


    for plantN in gekkoVariables:
        thisPlant = Plant.objects.get(plant_name = plantN)
        ihval = str(gekkoVariables[plantN]['ih'].value)
        ihval = float(ihval[1:-1])
        igval = str(gekkoVariables[plantN]['ig'].value)
        igval = float(igval[1:-1])
        lcval = str(gekkoVariables[plantN]['lc'].value)
        lcval = float(lcval[1:-1])
        lsval = str(gekkoVariables[plantN]['ls'].value)
        lsval = float(lsval[1:-1])
        spval = str(gekkoVariables[plantN]['sp'].value)
        spval = float(spval[1:-1])
        savingPlant = PlantResult(plant=thisPlant, result=thisLayout, interior_heavy_result=ihval, insulated_glass_result=igval, laminated_complex_result=lcval, laminated_simple_result=lsval, specialty_result=spval)
        savingPlant.save()


def optimizeFunction(plants, demands, functionName, input_name ):
    try:
        if functionName[0] == 'SMU Model':
            print("Here we go! ")
            smuModel(plants, demands, input_name)
    except:
        pass 


plants = ['Plant 1', 'Plant 2', 'Plant 3']
demand = 'SMU Model'

# smuModel(plants, demand)
