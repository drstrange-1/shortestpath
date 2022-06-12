import folium
from folium import plugins
from numpy import append
from django.shortcuts import render


def home(request):
    sources={
        '1':'Bus Stop',
        '11':'Srishti PG',
        '12':'Benaka Boys Hostel',
    }
    destinations ={
         '1':'Bus Stop',
        '11':'Srishti PG',
        '12':'Benaka Boys Hostel',
        '29':'TT Quick Bites',
        '4':'Homely',
        '9':'Delhi Mess',
        '22':'Urmidi Fastfoods',
        '21':'More SuperMarket',
        '23':'Anjaneya Swami Temple',
        '26':'Ground',
        '2':'Laundry'
    }
    return render(request,'shortestpath/home.html',{'sources':sources,'destinations':destinations})
# defining default location to center the map
defaultLocation = (13.034702, 77.565557)
myMap = folium.Map(location = defaultLocation, width = "75%", zoom_start = 18)
# myMap

# Locaiton data format [Latitude,Longitude]
location1 = [13.0356972563827, 77.5645387172699]
location2 = [13.0354032838366, 77.564478367567]
location3 = [13.0350387573945, 13.0350387573945]
location4 = [13.0346846828094, 77.5642450153828]
location5 = [13.0356345422688, 77.5648377835751]
location6 = [13.0351667990016, 77.5647546350956]
location7 = [13.0356593666075, 77.5651274621487]
location8 = [13.03509232583, 77.5650429725647]
location9 = [13.0348754389218, 77.565009444952]
location10 = [13.0342156311953, 77.5647841393948]
location11 = [13.0356253964592, 77.5654788315296]
location12 = [13.0339575871009, 77.5650905817747]
location13 = [13.0356123310163, 77.5657477229834]
location14 = [13.0345527213031, 77.5655418634415]
location15 = [13.0342887980794, 77.5654935836792]
location16 = [13.0340327138903, 77.5654372572899]
location17 = [13.0338341178062, 77.5653809309006]
location18 = [13.0337374328128, 77.565284371376]
location19 = [13.0355639888717, 77.5660702586174]
location20 = [13.0352843881743, 77.5660461187363]
location21 = [13.0347826739814, 77.5659415125847]
location22 = [13.0335283840494, 77.5655847787857]
location23 = [13.0355744412281, 77.5665114820004]
location24 = [13.0352478048821, 77.5665128231048]
location25 = [13.0347173465377, 77.5664511322975]
location26 = [13.0343867894081, 77.5664243102074]
location27 = [13.0341842739526, 77.5664028525353]
location28 = [13.0339412551872, 77.5663626194]
location29 = [13.0337113017271, 77.5663411617279]
location30 = [13.0334787349422, 77.5663009285927]


MAXM, INF = 100, 10**7
dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]

V = 30

graph = [
    [0, 3, INF, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [3, 0, 4, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 4, 0, 4, INF, INF, INF, INF, 6, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, 4, 0, INF, INF, INF, INF, INF, 7, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [3, INF, INF, INF, 0, 5, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, 5, 0, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, 3, INF, 0, 6, INF, INF, 4, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, 3, 6, 0, 3, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, 6, INF, INF, INF, INF, 3, 0, 10, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, 7, INF, INF, INF, INF, 7, 0, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, 4, INF, INF, INF, 0, 20, 2, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, INF, 0, INF, INF, INF,
        INF, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 2, INF, 0, 12, INF,
        INF, INF, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 12, 0, 3,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 9, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, 0,
        3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 8, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3,
        0, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 8, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, 3, 0, 2, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 8, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, INF, INF, INF,
        INF, 2, 0, INF, INF, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, INF, INF,
        INF, INF, INF, 0, 3, INF, INF, 5, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, 3, 0, 7, INF, INF, 5, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, 7, 0, INF, INF, INF, 5, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, 3, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, 6],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, 5, INF, INF, INF, 0, 4, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, 5, INF, INF, 4, 0, 6, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, 5, INF, INF, 6, 0, 4, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 9, INF,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, 0, 3, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 8,
        INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, 0, 3, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, 8, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, 0, 3, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, 8, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, 0, 3],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
        INF, INF, INF, INF, INF, INF, INF, 6, INF, INF, INF, INF, INF, INF, 3, 0]
]

#Variables for the found path from one node to another and antPath
path = []
antPath = []
totalDistance = 0
    
    
    
    
    
    
    
# function to initialize the arrays 'dis' and 'Next'
def initialise(V):
    global dis, Next

    for i in range(V):
        for j in range(V):
            dis[i][j] = graph[i][j]

            # No edge between node
            # i and j
            if (graph[i][j] == INF):
                Next[i][j] = -1
            else:
                Next[i][j] = j

# function to construct antPath
def constructAntPath(u):
    global antPath

    if u == 0:
        antPath.append(location1)
    if u == 1:
        antPath.append(location2)
    if u == 2:
        antPath.append(location3)
    if u == 3:
        antPath.append(location4)
    if u == 4:
        antPath.append(location5)
    if u == 5:
        antPath.append(location6)
    if u == 6:
        antPath.append(location7)
    if u == 7:
        antPath.append(location8)
    if u == 8:
        antPath.append(location9)
    if u == 9:
        antPath.append(location10)
    if u == 10:
        antPath.append(location11)
    if u == 11:
        antPath.append(location12)
    if u == 12:
        antPath.append(location13)
    if u == 13:
        antPath.append(location14)
    if u == 14:
        antPath.append(location15)
    if u == 15:
        antPath.append(location16)
    if u == 16:
        antPath.append(location17)
    if u == 17:
        antPath.append(location18)
    if u == 18:
        antPath.append(location19)
    if u == 19:
        antPath.append(location20)
    if u == 20:
        antPath.append(location21)
    if u == 21:
        antPath.append(location22)
    if u == 22:
        antPath.append(location23)
    if u == 23:
        antPath.append(location24)
    if u == 24:
        antPath.append(location25)
    if u == 25:
        antPath.append(location26)
    if u == 26:
        antPath.append(location27)
    if u == 27:
        antPath.append(location28)
    if u == 28:
        antPath.append(location29)
    if u == 29:
        antPath.append(location30)

#function to construct the shortest path
def constructPath(u, v):
    global graph, Next,antPath,totalDistance

    antPath.clear()

    # if no path exist
    if (Next[u][v] == -1):
        return {}

    # Storing the path in a vector
    path = [u]
    constructAntPath(u)
    while (u != v):
        u = Next[u][v]
        constructAntPath(u)
        path.append(u)

    return path


def floydWarshall(V):
    global dist, Next
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if (dis[i][k] == INF or dis[k][j] == INF):
                    continue
                if (dis[i][j] > dis[i][k] + dis[k][j]):
                    dis[i][j] = dis[i][k] + dis[k][j]
                    Next[i][j] = Next[i][k]

# Print the shortest path
def printPath(path):
    n = len(path)
    for i in range(n - 1):
        print(path[i], end=" -> ")
    print(path[n - 1])


#function to calculte the total distance between two points
def calculateTotalDistance(path):
    global totalDistance
    i = 0

    while i < len(path)-1:
      totalDistance = totalDistance + dis[path[i]][path[i+1]]
      i = i+1

# Driver Program
def path(request):
    

    # initializing the 'dis' and 'Next'
    initialise(V)

   
    floydWarshall(V)

    
    
    # source = input("Enter the starting point : ")
    # source = int(source)

    # destination = input("Enter the destination point : ")
    # destination = int(destination)



    # calling to find path between two specified nodes
    source = int(request.POST.get('source'))
    destination = int(request.POST.get('destination'))
    path = constructPath((source-1), (destination-1))
    # calculateTotalDistance(path)
    # print(totalDistance)
    # print(path)
    

    #antPath animation
    folium.plugins.AntPath([antPath]).add_to(myMap)
    # markers = "/content/drive/MyDrive/LocationMap/markedLocations.geojson"
    # folium.GeoJson(markers, name="geojson").add_to(myMap)
# myMap.save(outfile = 'index.html')
    myMap.save('shortestpath/templates/shortestpath/map.html')
    return render(request, 'shortestpath/map.html')

