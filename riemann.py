def riemannsSumMidpoint(a, b, n, func):
    result = {}
    dx = (b - a)/n
    result["dx"] = dx
    xi = []
    yi = []
    # Obtemos todos los x_i
    for i in range(n+1):
        xi.append(a+(i*dx))
        yi.append(func(a+(i*dx)))
    result["xi"]=xi
    result["yi"]=yi
    yi_midpoints = []
    x_midpoints = []
    # Obtenemos los puntos medios y el resultado de su evaluación en la función
    for i in range(n):
        xmid = (xi[i] + xi[i+1])/2
        x_midpoints.append(xmid)
        yi_midpoints.append(func(xmid))
    result["x_midpoints"] = x_midpoints
    result["yi_midpoints"] = yi_midpoints
    totalArea = 0;
    rectangleAreas = []
    # Sumamos las areas de todos los rectangulos (y_i * dx)
    for i in range(n):
        rectangleArea = yi_midpoints[i] * dx
        rectangleAreas.append(rectangleArea)
        totalArea = totalArea + rectangleArea

    result["rectangleAreas"] = rectangleAreas
    result["totalArea"] = totalArea

    return result

def riemannsSumLeftpoint(a, b, n, func):
    result = {}
    dx = (b - a)/n
    xi = []
    yi = []
    # Obtemos todos los x_i
    for i in range(n+1):
        xi.append(a+(i*dx))
        yi.append(func(a+(i*dx)))
    result["xi"]=xi
    result["yi"]=yi
    yi_leftpoints = []
    x_leftpoints = []
    # Obtenemos los puntos izquierdos y el resultado de su evaluación en la función
    for i in range(n):
        xleft = xi[i]
        x_leftpoints.append(xleft)
        yi_leftpoints.append(func(xleft))
    result["x_leftpoints"] = x_leftpoints
    result["yi_leftpoints"] = yi_leftpoints
    totalArea = 0;
    rectangleAreas = []
    # Sumamos las areas de todos los rectangulos (y_i * dx)
    for i in range(n):
        rectangleArea = yi_leftpoints[i] * dx
        rectangleAreas.append(rectangleArea)
        totalArea = totalArea + rectangleArea

    result["rectangleAreas"] = rectangleAreas
    result["totalArea"] = totalArea

    return result

def riemannsSumRightpoint(a, b, n, func):
    result = {}
    dx = (b - a)/n
    xi = []
    yi = []
    # Obtemos todos los x_i
    for i in range(n+1):
        xi.append(a+(i*dx))
        yi.append(func(a+(i*dx)))
    result["xi"]=xi
    result["yi"]=yi
    yi_rightpoints = []
    x_rightpoints = []
    # Obtenemos los puntos derechos y el resultado de su evaluación en la función
    for i in range(n):
        xright = xi[i+1]
        x_rightpoints.append(xright)
        yi_rightpoints.append(func(xright))
    result["x_rightpoints"] = x_rightpoints
    result["yi_rightpoints"] = yi_rightpoints
    totalArea = 0;
    rectangleAreas = []
    # Sumamos las areas de todos los rectangulos (y_i * dx)
    for i in range(n):
        rectangleArea = yi_rightpoints[i] * dx
        rectangleAreas.append(rectangleArea)
        totalArea = totalArea + rectangleArea

    result["rectangleAreas"] = rectangleAreas
    result["totalArea"] = totalArea

    return result

# print(riemannsSumMidpoint(0,1,lamb,1))

#n = 50000000
#print(trapezoidalRiemman(-1, 2, n, lambda x : (x-1)**2 + 2))
#print(riemannsSumMidpoint(-1, 2, n, lambda x : (x-1)**2 + 2)["totalArea"])

