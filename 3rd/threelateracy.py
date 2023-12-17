def ThreeLateracy(try_pts, cubeside):
    x1, x2, x3 = try_pts[0]['X'], try_pts[1]['X'], try_pts[2]['X']
    y1, y2, y3 = try_pts[0]['Y'], try_pts[1]['Y'], try_pts[2]['Y']
    z1, z2, z3 = try_pts[0]['Z'], try_pts[1]['Z'], try_pts[2]['Z']
    r1, r2, r3 = try_pts[0]['dist'], try_pts[1]['dist'], try_pts[2]['dist']

    k1 = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2 - z1**2 + z2**2
    a1 = 2 * (x2 - x1)
    b1 = 2 * (y2 - y1)
    c1 = 2 * (z2 - z1)
    k3 = r3**2 - r2**2 - x3**2 + x2**2 - y3**2 + y2**2 - z3**2 + z2**2
    a3 = 2 * (x2 - x3)
    b3 = 2 * (y2 - y3)
    c3 = 2 * (z2 - z3)

    if a1 == 0:
        e = -c1 / b1
        f = k1 / b1
    elif a3 == 0:
        e = -c3 / b3
        f = k3 / b3		
    else:
        a31 = a3 / a1
        e = - ((a31 * c1 - c3) / (a31 * b1 - b3))
        f = (a31 * k1 - k3) / (a31 * b1 - b3)
	
    if b1 == 0:
        g = -c1 / a1
        h = k1 / a1
    elif b3 == 0:
        g = -c3 / a3
        h = k3 / a3
    else:
        b31 = b3 / b1
        g = - ((b31 * c1 - c3) / (b31 * a1 - a3))
        h = (b31 * k1 - k3) / (b31 * a1 - a3)

    A = g**2 + e**2 + 1;
    B = -x1 * g - y1 * e - 2 * z1 - x1 * g - y1 * e + 2 * g * h + 2 * e * f
    C = x1**2 + y1**2 + z1**2 - 2 * x1 * h - 2 * y1 * f + h**2 + f**2 - r1**2
	
    rootD = (B * B - 4 * A * C)**0.5
    z = round((-B + rootD) / (2 * A), 4)
    z_ = round((-B - rootD) / (2 * A), 4)
		
    x = round(g * z + h, 4)
    x_ = round(g * z_ + h, 4)

    y = round(e * z + f, 4)
    y_ = round(e * z_ + f, 4)

    answer = []

    # Перевіряємо граничні умови для кожної точки та формуємо відвповідь
    if (0 <= x <= cubeside) and \
        (0 <= y <= cubeside) and \
        (0 <= z <= cubeside):
        answer.append({'X': x, 'Y': y, 'Z': z}) 
    if (0 <= x_ <= cubeside) and \
        (0 <= y_ <= cubeside) and \
        (0 <= z_ <= cubeside):
        answer.append({'X': x_, 'Y': y_, 'Z': z_}) 
	
    return answer