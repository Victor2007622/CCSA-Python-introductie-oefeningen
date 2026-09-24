def bereken_verpakking(aantal_appels):
    APPELS_PER_KIST = 20
    KISTEN_PER_PALLET = 35

    # Totaal aantal appels op één volle pallet (35 * 20 = 700)
    APPELS_PER_PALLET = KISTEN_PER_PALLET * APPELS_PER_KIST

    # 1. Aantal volle palletten
    palletten = aantal_appels // APPELS_PER_PALLET
    overgebleven_appels = aantal_appels % APPELS_PER_PALLET

    # 2. Aantal volle kisten van de overgebleven appels
    kisten = overgebleven_appels // APPELS_PER_KIST

    # 3. Appels die nog overblijven
    losse_appels = overgebleven_appels % APPELS_PER_KIST

    return palletten, kisten, losse_appels