def calculate_rating(constant=13.9, achievement=0, rating=0):
    custom_fac = 0
    constant = float(constant)
    achievement = float(achievement)
    rating = float(rating)
    factors = {
        0: 0,
        0.97: 20,
        0.98: 20.3,
        0.99: 20.8,
        0.995: 21.1,
        1.00: 21.6,
        1.005: 22.4
    }

    achievement = achievement / 100
    for key in factors:
        if isinstance(key, tuple):
            if key[0] <= achievement <= key[1]:
                custom_fac = factors[key]
                break
        elif key == achievement:
            custom_fac = factors[key]
            break

    if rating == 0:
        s_rating = round((20 * 0.97) * constant, 0)
        splus_rating = round((20.3 * 0.98) * constant, 0)
        ss_rating = round((20.8 * 0.99) * constant, 0)
        ssplus_rating = round((21.1 * 0.995) * constant, 0)
        sss_rating = round((21.6 * 1.00) * constant, 0)
        sssplus_rating = round((22.4 * 1.005) * constant, 0)
        custom_rating = (custom_fac * achievement) * constant
        return int(s_rating), int(splus_rating), int(ss_rating), int(ssplus_rating), int(sss_rating), int(sssplus_rating), int(custom_rating)

s_rating, splus_rating, ss_rating, ssplus_rating, sss_rating, sssplus_rating, custom_rating = calculate_rating(achievement=99.5)

#print(s_rating, sssplus_rating, custom_rating)
