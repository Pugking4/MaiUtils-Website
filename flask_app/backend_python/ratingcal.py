def calculate_rating(constant, achievement, rating):
    custom_fac = 0
    if constant:
        constant = float(constant)
    else:
        constant = 0
    
    if achievement:
        achievement = float(achievement)
    else:
        achievement = 0

    if rating:
        rating = int(rating)
    else:
        rating = 0

    factors = {
        0.97: 20,
        0.98: 20.3,
        0.99: 20.8,
        0.995: 21.1,
        1.00: 21.6,
        1.005: 22.4
    }
    rt_constants = []

    achievement = achievement / 100

    if achievement >= 0.97 and achievement < 0.98:
        custom_fac = 20
    elif achievement >= 0.98 and achievement < 0.99:
        custom_fac = 20.3
    elif achievement >= 0.99 and achievement < 0.995:
        custom_fac = 20.8
    elif achievement >= 0.995 and achievement < 1.00:
        custom_fac = 21.1
    elif achievement >= 1.00 and achievement < 1.005:
        custom_fac = 21.6
    elif achievement >= 1.005:
        custom_fac = 22.4
    else:
        custom_fac = 0

    print(f"Rating: {rating}")

    if rating == 0:
        print("Rating is 0")
        s_rating = round((20 * 0.97) * constant, 0)
        splus_rating = round((20.3 * 0.98) * constant, 0)
        ss_rating = round((20.8 * 0.99) * constant, 0)
        ssplus_rating = round((21.1 * 0.995) * constant, 0)
        sss_rating = round((21.6 * 1.00) * constant, 0)
        sssplus_rating = round((22.4 * 1.005) * constant, 0)
        custom_rating = round((custom_fac * achievement) * constant, 0)
        return int(s_rating), int(splus_rating), int(ss_rating), int(ssplus_rating), int(sss_rating), int(sssplus_rating), int(custom_rating)
    else:
        print("Rating is not 0")
        for factor in factors:
            rt_constant = round(rating / (factor * factors[factor]), 1)
            if rt_constant > 15:
                rt_constant = 'Null'
            #rt_constants[factors[factor]] = rt_constant
            rt_constants.append(rt_constant)
        try:
            rt_constant = round(rating / (achievement * custom_fac), 1)
        except:
            rt_constant = 'Null'
        rt_constants.append(rt_constant)

        return rt_constants[0], rt_constants[1], rt_constants[2], rt_constants[3], rt_constants[4], rt_constants[5], rt_constants[6]