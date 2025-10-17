import random
from collections import Counter

class Poker:
    def __init__(self, numar_jucatori=2):
        self.culori = {"♥", "♦", "♣", "♠"}
        self.ranguri = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        self.valori_carti = {rang: i+2 for i, rang in enumerate(self.ranguri)}
        self.pachet = self._creeaza_pachet()
        
        self.numar_jucatori = numar_jucatori
        self.jucatori = [[] for _ in range(numar_jucatori)]
        self.masa = []

    def _creeaza_pachet(self):
        """Creează și amestecă pachetul de cărți"""
        pachet = [rang + culoare for culoare in self.culori for rang in self.ranguri]
        random.shuffle(pachet)
        return pachet

    def da_carti(self):
        """Împarte cărți jucătorilor și pe masă"""
        # Împarte 2 cărți fiecărui jucător
        for _ in range(2):
            for j in range(self.numar_jucatori):
                if self.pachet:
                    self.jucatori[j].append(self.pachet.pop())
        
        # Împarte 5 cărți pe masă
        self.masa = [self.pachet.pop() for _ in range(5)] if len(self.pachet) >= 5 else []

    def _extrage_valoare(self, carte):
        """Extrage valoarea numerică a unei cărți"""
        return self.valori_carti[carte[:-1]]

    def _extrage_culoare(self, carte):
        """Extrage culoarea unei cărți"""
        return carte[-1]

    def _evaluare_mana(self, mana):
        """Evaluare completă a unei mâini de poker"""
        valori = [self._extrage_valoare(c) for c in mana]
        culori = [self._extrage_culoare(c) for c in mana]
        
        return self._gaseste_cea_mai_buna_mana(valori, culori)

    def _gaseste_cea_mai_buna_mana(self, valori, culori):
        """Găsește cea mai bună mână posibilă din 7 cărți"""
        counter_valori = Counter(valori)
        counter_culori = Counter(culori)
        
        maini_posibile = []
        
        # 1. Royal flush & Straight flush
        flush_carti = self._gaseste_flush(valori, culori)
        if flush_carti:
            chinta_flush = self._gaseste_chinta(flush_carti)
            if chinta_flush:
                if max(chinta_flush) == 14:  # Royal flush
                    maini_posibile.append((9, "Royal flush", chinta_flush))
                else:  # Straight flush
                    maini_posibile.append((8, f"Chintă de culoare cu {max(chinta_flush)}", chinta_flush))
        
        # 2. Patru de un fel
        patru = self._gaseste_patroaca(counter_valori)
        if patru:
            maini_posibile.append((7, f"Patru de {patru[0]}", patru))
        
        # 3. Full house
        full = self._gaseste_full_house(counter_valori)
        if full:
            maini_posibile.append((6, f"Full house: {full[0]} peste {full[1]}", full))
        
        # 4. Flush (doar dacă nu am gasit deja flush superior)
        if flush_carti and not any(m[0] >= 8 for m in maini_posibile):
            top5_flush = sorted(flush_carti, reverse=True)[:5]
            maini_posibile.append((5, f"Culoare cu {top5_flush[0]}", top5_flush))
        
        # 5. Chintă (doar dacă nu am gasit deja chintă superioră)
        chinta = self._gaseste_chinta(valori)
        if chinta and not any(m[0] >= 4 for m in maini_posibile):
            maini_posibile.append((4, f"Chintă cu {max(chinta)}", chinta))
        
        # 6. Trei de un fel
        trei = self._gaseste_trei(counter_valori, valori)
        if trei:
            maini_posibile.append((3, f"Trei de {trei[0]}", trei))
        
        # 7. Două perechi
        doua_perechi = self._gaseste_doua_perechi(counter_valori, valori)
        if doua_perechi:
            maini_posibile.append((2, f"Două perechi: {doua_perechi[0]} și {doua_perechi[1]}", doua_perechi))
        
        # 8. Pereche
        pereche = self._gaseste_pereche(counter_valori, valori)
        if pereche:
            maini_posibile.append((1, f"Pereche de {pereche[0]}", pereche))
        
        # 9. High card (mereu există)
        high_card = self._gaseste_high_card(valori)
        maini_posibile.append((0, f"High card: {high_card[0]}", high_card))
        
        # Returnează cea mai bună mână
        return max(maini_posibile, key=lambda x: (x[0], x[2]))

    def _gaseste_flush(self, valori, culori):
        """Găsește cărțile pentru flush dacă există"""
        counter_culori = Counter(culori)
        culoare_flush = next((c for c, count in counter_culori.items() if count >= 5), None)
        
        if culoare_flush:
            # Returnează valorile cărților de culoarea respectivă
            flush_valori = []
            for i, culoare in enumerate(culori):
                if culoare == culoare_flush:
                    flush_valori.append(valori[i])
            return sorted(flush_valori, reverse=True)
        return None

    def _gaseste_chinta(self, valori):
        """Găsește cea mai bună chintă"""
        valori_unice = sorted(set(valori))
        
        # Verifică chinta standard (5 cărți consecutive)
        for i in range(len(valori_unice) - 4):
            if valori_unice[i + 4] - valori_unice[i] == 4:
                return sorted(valori_unice[i:i+5], reverse=True)
        
        # Verifică chinta A-2-3-4-5
        if all(x in valori_unice for x in [14, 2, 3, 4, 5]):
            return [5, 4, 3, 2, 14]  # A (14) este considerat ca 1
        
        return None

    def _gaseste_patroaca(self, counter_valori):
        """Găsește patru de un fel și kicker"""
        for val, count in counter_valori.items():
            if count == 4:
                kicker = max(k for k in counter_valori.keys() if k != val)
                return [val, kicker]
        return None

    def _gaseste_full_house(self, counter_valori):
        """Găsește full house"""
        trei = None
        doi = None
        
        for val, count in counter_valori.items():
            if count == 3:
                if trei is None or val > trei:
                    trei = val
            elif count >= 2:
                if doi is None or val > doi:
                    doi = val
        
        if trei and doi:
            return [trei, doi]
        
        # Caz special: două seturi de trei
        trei_list = [val for val, count in counter_valori.items() if count == 3]
        if len(trei_list) >= 2:
            trei_list.sort(reverse=True)
            return [trei_list[0], trei_list[1]]
        
        return None

    def _gaseste_trei(self, counter_valori, valori):
        """Găsește trei de un fel și kickeri"""
        trei_val = None
        for val, count in counter_valori.items():
            if count == 3:
                if trei_val is None or val > trei_val:
                    trei_val = val
        
        if trei_val:
            kickers = [v for v in sorted(set(valori), reverse=True) if v != trei_val][:2]
            return [trei_val] + kickers
        return None

    def _gaseste_doua_perechi(self, counter_valori, valori):
        """Găsește două perechi și kicker"""
        perechi = [val for val, count in counter_valori.items() if count == 2]
        if len(perechi) >= 2:
            perechi.sort(reverse=True)
            perechi = perechi[:2]
            kicker = max(v for v in valori if v not in perechi)
            return perechi + [kicker]
        return None

    def _gaseste_pereche(self, counter_valori, valori):
        """Găsește pereche și kickeri"""
        pereche_val = None
        for val, count in counter_valori.items():
            if count == 2:
                if pereche_val is None or val > pereche_val:
                    pereche_val = val
        
        if pereche_val:
            kickers = [v for v in sorted(set(valori), reverse=True) if v != pereche_val][:3]
            return [pereche_val] + kickers
        return None

    def _gaseste_high_card(self, valori):
        """Găsește cele mai bune 5 cărți pentru high card"""
        return sorted(valori, reverse=True)[:5]

    def joaca(self):
        """Rulează un joc complet de poker"""
        self.da_carti()
        
        print("\n=== Cărțile de pe masă ===")
        print(" ".join(self.masa))
        print()

        scoruri = []
        for i, mana_juc in enumerate(self.jucatori):
            mana_completa = mana_juc + self.masa
            scor = self._evaluare_mana(mana_completa)
            scoruri.append((scor, i))
            
            print(f"Jucător {i+1}: {' '.join(mana_juc)}")
            print(f"  → {scor[1]}")

        # Sortează corect pentru poker
        scoruri.sort(key=lambda x: (
            -x[0][0],  # Rangul mâinii
            [-v for v in x[0][2]]  # Toți kickerii în ordine
        ))
        
        castigator = scoruri[0][1]
        print(f"\n🏆 Câștigător: Jucător {castigator+1}")
        
        # Afișează clasamentul pentru claritate
        print("\n🔢 Clasament:")
        for i, (scor, jucator) in enumerate(scoruri):
            print(f"{i+1}. Jucător {jucator+1}: {scor[1]}")

# Exemplu de utilizare
if __name__ == "__main__":
    joc = Poker(numar_jucatori=5)
    joc.joaca()

