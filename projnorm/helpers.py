def helper_steamer_pitcher_roles(sp_pct, rp_pct):
    starter = float(sp_pct) >= 1.0
    reliever = float(rp_pct) > 0.0

    if starter and reliever:
        return ['P', 'SP', 'RP']
    elif starter:
        return ['P', 'SP']
    elif reliever:
        return ['P', 'RP']
    else:
        return ['P']
