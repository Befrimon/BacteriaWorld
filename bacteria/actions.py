class Actions:
    @staticmethod
    def photosynthesis(bact):
        bact.energy += 2
        return 1

    @staticmethod
    def cold_resistance(bact):
        bact.minT = -10
        return 2

    @staticmethod
    def heat_resistance(bact):
        bact.maxT = 35
        return 2
