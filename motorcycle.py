class Motoca():
    def __init__(self, model, cv, rpm_cv, kgfm, rpm_kgfm, kg):
        self._model = model
        self._cv = cv
        self._rpm_cv = rpm_cv
        self._kgfm = kgfm
        self._rpm_kgfm = rpm_kgfm
        self._kg = kg

        # weight/power:
        self._kg_cv = self._kg / self._cv

        # weight/tork:
        # tork*rpm results in a lower ratio
        # tork/rpm results in higher ratio
        self._kg_kgfm = self._kg / (self._kgfm / self._rpm_kgfm)

        # index1
        self._index = self._kg_cv + self._kg_kgfm


class Garage():
    def __init__(self):
        self._motocas = []

    def add_motoca(self, model, cv, rpm_cv, kgfm, rpm_kgfm, kg):
        self._motocas.append(Motoca(model, cv, rpm_cv, kgfm, rpm_kgfm, kg))

    def remove_motoca(self, position):
        self._motocas.pop(position)
