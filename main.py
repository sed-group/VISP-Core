from hud import volume


inputs = {
    "FullHorizontalFOV": 10,
    "FullVerticalFOV": 4,
    "VirtualImageDistance": 15000,
    "EyeboxToMirror1": 1000,
    "EyeboxFullWidth": 140,
    "EyeboxFullHeight": 60,
    "Mirror1ObliquityAngle": 30,
    "HUD_SCREEN_10x5_FOV_BASELINE_WIDTH": 70,
    "MechanicalVolumeIncrease": 40,
    "M1M2OverlapFraction": 0,
    "PGUVolumeEstimate": 0.5
}

print(volume.TotalMechanicalVolumeOfHUD(inputs))
