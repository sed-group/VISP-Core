import plotly.express as px
from doepy import build
from hud import volume

factors_ar = {
    'FullHorizontalFOV': [5, 15],
    'FullVerticalFOV': [2, 6],
    'VirtualImageDistance': [10000, 30000],
    'EyeboxToMirror1': [500, 1500],
    'EyeboxFullWidth': [70, 210],
    'EyeboxFullHeight': [30, 90],
    'Mirror1ObliquityAngle': [15, 45]
}

num_samples = 1000

lhs = build.space_filling_lhs(factors_ar, num_samples=num_samples)

for index, row in lhs.iterrows():
    inputs = {
        "FullHorizontalFOV": row['FullHorizontalFOV'],
        "FullVerticalFOV": row['FullVerticalFOV'],
        "VirtualImageDistance": row['VirtualImageDistance'],
        "EyeboxToMirror1": row['EyeboxToMirror1'],
        "EyeboxFullWidth": row['EyeboxFullWidth'],
        "EyeboxFullHeight": row['EyeboxFullHeight'],
        "Mirror1ObliquityAngle": row['Mirror1ObliquityAngle'],
        "HUD_SCREEN_10x5_FOV_BASELINE_WIDTH": 70,
        "MechanicalVolumeIncrease": 20,
        "M1M2OverlapFraction": 0,
        "PGUVolumeEstimate": 0.5
    }

    volume = volume.TotalMechanicalVolumeOfHUD(inputs)
    lhs.at[index, 'volume'] = volume


df = lhs
fig = px.parallel_coordinates(
    df,
    color="volume",
    labels={
        "FullHorizontalFOV": "Full Horizontal FOV",
        "FullVerticalFOV": "Full Vertical FOV",
        "VirtualImageDistance": "Virtual Image Distance",
        "EyeboxToMirror1": "Eyebox To Mirror 1",
        "EyeboxFullWidth": "Eyebox Full Width",
        "EyeboxFullHeight": "Eyebox Full Height",
        "Mirror1ObliquityAngle": "Mirror 1 Obliquity Angle",
    },
    color_continuous_scale=px.colors.diverging.Tealrose)
fig.show()
