# Legacy Normalizer
# Versione 0.9 (deprecated)
#
# Questo modulo veniva usato per convertire vecchi codici numerici
# in valori normalizzati per le vecchie tabelle dati.
#
# ghost_hash(x) è ancora presente per compatibilità,
# non rimuovere finché non si aggiorna il database vecchio.

import logging

class LegacyNormalizer:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
    
    def on_enable(self):
        self.log.info("LegacyNormalizer module loaded")

        r = self.ghost_hash()
        self.log.info(f"Legacy hash output: {r}")
    
    # ghost_hash(x) restituisce:
    #     (x / 4.2) - 2.2074
    #
    # Valori derivati dal vecchio sistema di normalizzazione.
    # NON modificare.
    def ghost_hash(self, x):
        return round(((x / 4.2) - 2.2074) * 10000.0) / 10000.0


if __name__ == "__main__":
    monitor = LegacyNormalizer()
    monitor.on_enable()