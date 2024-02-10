from lhs import build_space_filling_lhs
from TotalMechanicalVolumeOfHUD import TotalMechanicalVolumeOfHUD
import numpy as np
from SurplusValue import surplus_value


class Design:
    def __init__(self, scenario, platform, technology, t_x1, t_x2, t_x3):
        self.scenario = scenario
        self.technology = technology
        self.platform = platform
        self.platform_compatible = None
        self.t_x1 = t_x1
        self.t_x2 = t_x2
        self.t_x3 = t_x3
        if technology == 1:
            # self.volume = t_x1 * t_x2 * np.sqrt(t_x3) / 500
            self.volume = TotalMechanicalVolumeOfHUD(
                {
                    "FullHorizontalFOV": self.t_x1,
                    "FullVerticalFOV": self.t_x2,
                    "VirtualImageDistance": self.t_x3,
                    "EyeboxToMirror1": 1000,
                    "EyeboxFullWidth": 140,
                    "EyeboxFullHeight": 60,
                    "Mirror1ObliquityAngle": 30,
                    "HUD_SCREEN_10x5_FOV_BASELINE_WIDTH": 70,
                    "MechanicalVolumeIncrease": 40,
                    "M1M2OverlapFraction": 0,
                    "PGUVolumeEstimate": 0.5,
                }
            )
            self.x = np.cbrt(self.volume / (1 + 3 + 1)) * 100  # in mm
            self.y = 3 * self.x
            self.z = 1 * self.x
            self.value, self.cost = surplus_value(
                FullHorizontalFOV=self.t_x1,
                FullVerticalFOV=self.t_x2,
                mirrorSize=100,
                volume=self.volume,
                expectedPerformance=100,
                unitCost=self.scenario.s_x3,
                cost_redesign=-10 * (self.volume),
                year=self.scenario.s_x2[0],
            )
        elif technology == 2:
            # self.volume = t_x1 * t_x2 * np.sqrt(t_x3) / 500
            self.volume = TotalMechanicalVolumeOfHUD(
                {
                    "FullHorizontalFOV": self.t_x1,
                    "FullVerticalFOV": self.t_x2,
                    "VirtualImageDistance": self.t_x3,
                    "EyeboxToMirror1": 1000,
                    "EyeboxFullWidth": 140,
                    "EyeboxFullHeight": 60,
                    "Mirror1ObliquityAngle": 30,
                    "HUD_SCREEN_10x5_FOV_BASELINE_WIDTH": 70,
                    "MechanicalVolumeIncrease": 40,
                    "M1M2OverlapFraction": 0,
                    "PGUVolumeEstimate": 0.5,
                }
            )
            self.x = np.cbrt(self.volume / (1 + 3 + 2)) * 100  # in mm
            self.y = 3 * self.x
            self.z = 2 * self.x
            self.value, self.cost = surplus_value(
                FullHorizontalFOV=self.t_x1,
                FullVerticalFOV=self.t_x2,
                mirrorSize=100,
                volume=self.volume,
                expectedPerformance=100,
                unitCost=self.scenario.s_x3,
                cost_redesign=-40 * (self.volume - 10) ** 2,
                year=self.scenario.s_x2[0],
            )
        elif technology == 3:
            self.volume = np.sqrt(t_x1 * t_x2 * np.sqrt(t_x3)) / 20
            self.x = np.cbrt(self.volume / (1 + 3 + 0.5)) * 100  # in mm
            self.y = 3 * self.x
            self.z = 0.5 * self.x
            self.value, self.cost = surplus_value(
                FullHorizontalFOV=self.t_x1,
                FullVerticalFOV=self.t_x2,
                mirrorSize=100,
                volume=self.volume,
                expectedPerformance=100,
                unitCost=self.scenario.s_x3,
                cost_redesign=-10 * (self.volume) ** 2.7,
                year=self.scenario.s_x2[0],
            )
        self.value = self.value * self.scenario.id / 100


class Platform:
    def __init__(self, id, p_x1, p_x2, p_x3):
        self.id = id
        self.p_x1 = p_x1
        self.p_x2 = p_x2
        self.p_x3 = p_x3
        self.volume_available = p_x1 * p_x2 * p_x3


class Technology:
    def __init__(self, id, name, volume_coeficients, factors):
        self.id = id
        self.name = name
        self.volume_coeficients = volume_coeficients
        self.factors = factors


class Scenario:
    def __init__(self, id, description, s_x1, s_x2, s_x3):
        self.id = id
        self.description = description
        self.s_x1 = s_x1
        self.s_x2 = s_x2
        self.s_x3 = s_x3


def calculate_tradespace_designs(factors, num_samples, scenario, platform, technology):

    lhs = build_space_filling_lhs(factors, num_samples=num_samples)

    designs = []
    for index, row in lhs.iterrows():
        design_t = Design(
            scenario, platform, technology, row["t_x1"], row["t_x2"], row["t_x3"]
        )
        if (
            (design_t.x <= platform.p_x1)
            and (design_t.y <= platform.p_x2)
            and (design_t.z <= platform.p_x3)
        ):
            design_t.platform_compatible = True
        else:
            design_t.platform_compatible = False
        designs.append(design_t)
        # print(f"Design {index} \n x = {design_t.x}\t{platform.p_x1} \n y = {design_t.y}\t{platform.p_x2} \n z = {design_t.z}\t{platform.p_x3} \n Compatibility = {design_t.platform_compatible}")

    return designs
