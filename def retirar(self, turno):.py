def retirar(self, turno):
        if self.cabeza is None:
            return False

        if self.cabeza.turno == turno:
            self.cabeza = self.cabeza.siguiente
            return True

        anterior = self.cabeza
        while anterior.siguiente is not None:
            if anterior.siguiente.turno == turno:
                anterior.siguiente = anterior.siguiente.siguiente
                return True
            anterior = anterior.siguiente

        return False