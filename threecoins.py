import os
import tkinter as tk
from tkinter import ttk, font
HEXAGRAMS = {
    0: ("䷀", "The Creative", "Pure, dynamic energy and the force of creation."),
    1: ("䷁", "The Receptive", "Receptivity, nurturance and supportiveness."),
    2: ("䷂", "Difficulty at the Beginning", "Initial hurdles or obstacles."),
    3: ("䷃", "Youthful Folly", "The need for discernment and guidance."),
    4: ("䷄", "Waiting", "Patience and readiness for the right timing."),
    5: ("䷅", "Conflict", "Opposition or tension that requires balancing."),
    6: ("䷆", "The Army", "Discipline and collective efforts."),
    7: ("䷇", "Holding Together", "Harmony and mutual support."),
    8: ("䷈", "Small Taming", "Modest influence or gentle guidance."),
    9: ("䷉", "Treading", "Careful consideration and measured steps."),
    10: ("䷊", "Peace", "Serenity, tranquility and stability."),
    11: ("䷋", "Standstill", "Stagnation or a period of reflection and preparation."),
    12: ("䷌", "Fellowship", "Common goals and collective journey."),
    13: ("䷍", "Great Possession", "Abundance, responsibility or awareness of its value."),
    14: ("䷎", "Humbling", "Modesty or unassuming nature."),
    15: ("䷏", "Enthusiasm", "Excitement and creative spark."),
    16: ("䷐", "Following", "Adaptation and going with the flow."),
    17: ("䷑", "Work on the Decayed", "Renovation and rectifying errors."),
    18: ("䷒", "Approach", "Favourable momentum or advancing step."),
    19: ("䷓", "Contemplation", "Looking inward or inner inquiry."),
    20: ("䷔", "Biting Through", "Perseverance in the face of adversity."),
    21: ("䷕", "Grace", "Beauty and elegant appearance."),
    22: ("䷖", "Splitting Apart", "Transformation, separation from what's no longer needed."),
    23: ("䷗", "Return", "Renewal, restoration, cautious progress after a setback."),
    24: ("䷘", "Innocence", "Pure intentions, naturalness and spontaneity."),
    25: ("䷙", "Great Taming", "Mastery over oneself or one's circumstances."),
    26: ("䷚", "Mouth Corners", "Sustenance for body and soul."),
    27: ("䷛", "Critical Mass", "Accumulation or threshold that invites transformation."),
    28: ("䷜", "The Abysmal Water", "Threats or unknown waters."),
    29: ("䷝", "The Clinging Fire", "Illumination or fervent devotion."),
    30: ("䷞", "Influence", "Intrinsic power or gentle persuasion."),
    31: ("䷟", "Duration", "Perseverance and endurance."),
    32: ("䷠", "Retreat", "Tactical retreat and reorientation."),
    33: ("䷡", "Great Power", "Strength, authority or influence."),
    34: ("䷢", "Progress", "Advancement and gradual unfolding."),
    35: ("䷣", "Darkening of the Light", "Challenge or darkness that invites illumination."),
    36: ("䷤", "The Family", "Primary relationships or close bonds."),
    37: ("䷥", "Opposition", "Opposing polarities and the need for reconciliation."),
    38: ("䷦", "Obstruction", "Obstacles or setbacks that require adjustment."),
    39: ("䷧", "Deliverance", "Liberation or breakthrough."),
    40: ("䷨", "Decrease", "Releasing or surrendering what no longer serves."),
    41: ("䷩", "Increase", "Growth or amplification."),
    42: ("䷪", "Breakthrough", "Persistent effort or breaking through barriers."),
    43: ("䷫", "Coming to Meet", "Encounter or meeting that fosters understanding."),
    44: ("䷬", "Gathering Together", "Unification or shared purpose."),
    45: ("䷭", "Pushing Upward", "Ascent or upward momentum."),
    46: ("䷮", "Oppression", "Weight or pressure that demands release."),
    47: ("䷯", "The Well", "Sustenance or revitalization."),
    48: ("䷰", "Revolution", "Radical transformation."),
    49: ("䷱", "The Cauldron", "Transmutation, transformation and refinement."),
    50: ("䷲", "The Arousing Thunder", "New energy or sudden change."),
    51: ("䷳", "The Keeping Still Mountain", "Contemplative silence or inner quiet."),
    52: ("䷴", "Development", "Evolution or gradual unfolding."),
    53: ("䷵", "The Marrying Maiden", "Yielding or accommodation."),
    54: ("䷶", "Abundance", "Abundance and the joy of fulfilment."),
    55: ("䷷", "The Wanderer", "Journeying, transience and impermanence."),
    56: ("䷸", "The Gentle Wind", "Influence through gentle persistence."),
    57: ("䷹", "The Joyous Lake", "Blissful harmony and equilibrium"),
    58: ("䷺", "Dispersion", "Dissolving what no longer serves, clearing a blocked path."),
    59: ("䷻", "Limitation", "Setting boundaries, knowing limits or recognition of constraints."),
    60: ("䷼", "Inner Truth", "Authenticity or inner wisdom."),
    61: ("䷽", "Small Exceeding", "Perseverance through small actions."),
    62: ("䷾", "After Completion", "Accomplishment, fulfilment and new beginnings."),
    63: ("䷿", "Before Completion", "The final stages of a cycle or project.")
}
BINARY_TO_HEXAGRAM = {
    0b111111: 0,
    0b000000: 1,
    0b100010: 2,
    0b010001: 3,
    0b111010: 4,
    0b010111: 5,
    0b010000: 6,
    0b000010: 7,
    0b111011: 8,
    0b110111: 9,
    0b111000: 10,
    0b000111: 11,
    0b101111: 12,
    0b111101: 13,
    0b001000: 14,
    0b000100: 15,
    0b100110: 16,
    0b011001: 17,
    0b110000: 18,
    0b000011: 19,
    0b100101: 20,
    0b101001: 21,
    0b000001: 22,
    0b100000: 23,
    0b100111: 24,
    0b111001: 25,
    0b100001: 26,
    0b011110: 27,
    0b010010: 28,
    0b101101: 29,
    0b001110: 30,
    0b011100: 31,
    0b001111: 32,
    0b111100: 33,
    0b000101: 34,
    0b101000: 35,
    0b101011: 36,
    0b110101: 37,
    0b001010: 38,
    0b010100: 39,
    0b110001: 40,
    0b100011: 41,
    0b111110: 42,
    0b011111: 43,
    0b000110: 44,
    0b011000: 45,
    0b010110: 46,
    0b011010: 47,
    0b101110: 48,
    0b011101: 49,
    0b100100: 50,
    0b001001: 51,
    0b001011: 52,
    0b110100: 53,
    0b101100: 54,
    0b001101: 55,
    0b011011: 56,
    0b110110: 57,
    0b010011: 58,
    0b110010: 59,
    0b110011: 60,
    0b001100: 61,
    0b101010: 62,
    0b010101: 63
}
def binary_to_hexagram(binary):
    return BINARY_TO_HEXAGRAM[binary]
class IChing:
    @staticmethod
    def secure_coin_flip():
        return ord(os.urandom(1)) & 1
    @staticmethod
    def generate_line():
        coins = [IChing.secure_coin_flip() for _ in range(3)]
        coin_values = [2 if coin == 0 else 3 for coin in coins]
        total = sum(coin_values)
        line_value = 6 if total == 6 else 7 if total == 7 else 8 if total == 8 else 9
        return coin_values, total, line_value
    @staticmethod
    def cast_hexagram():
        hexagram = []
        coin_results = []
        for _ in range(6):
            coins, total, line_value = IChing.generate_line()
            hexagram.append(line_value)
            coin_results.append((coins, total))
        primary = int(''.join(['0' if line in [6, 8] else '1' for line in hexagram]), 2)
        primary = binary_to_hexagram(primary)
        changing = [i for i, line in enumerate(hexagram) if line in [6, 9]]
        secondary = None
        if changing:
            secondary_hexagram = [line if i not in changing else 6 if line == 9 else 9 for i, line in enumerate(hexagram)]
            secondary_binary = int(''.join(['0' if line in [6, 8] else '1' for line in secondary_hexagram]), 2)
            secondary = binary_to_hexagram(secondary_binary)
        return primary, secondary, coin_results, hexagram
    @staticmethod
    def perform_divination():
        primary, secondary, coin_results, hexagram = IChing.cast_hexagram()
        result = "Coin Tosses:\n"
        for i, (coins, total) in enumerate(coin_results, 1):
            result += f"Line {i}: Coins: {coins}, Total: {total}\n"
        result += f"\nPrimary Hexagram: {hexagram}\n\n"
        result += f"Primary Hexagram:\n"
        result += f"Hexagram: {HEXAGRAMS[primary][0]}\n"
        result += f"Name: {primary + 1} {HEXAGRAMS[primary][1]}\n"
        result += f"Represents: {HEXAGRAMS[primary][2]}\n\n"
        if secondary is not None:
            result += f"Secondary Hexagram (after changes):\n"
            result += f"Hexagram: {HEXAGRAMS[secondary][0]}\n"
            result += f"Name: {secondary + 1} {HEXAGRAMS[secondary][1]}\n"
            result += f"Represents: {HEXAGRAMS[secondary][2]}"
        else:
            result += "No changing lines - no secondary hexagram."
        return result
class IChingGUI:
    def __init__(self, master):
        self.master = master
        master.title("I-Ching Divination Tool")
        master.geometry("600x475")
        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.result_text = tk.Text(self.frame, height=25, width=70, wrap=tk.WORD)
        self.result_text.grid(column=0, row=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        ttk.Button(self.frame, text="Cast Hexagram", command=self.show_divination).grid(column=0, row=1, pady=10)
        default_font = font.nametofont(self.result_text.cget("font"))
        self.result_text.tag_configure('normal', font=default_font)
        self.result_text.tag_configure('large', font=(default_font.actual()['family'], 20, 'bold'))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
    def show_divination(self):
        result = IChing.perform_divination()
        self.result_text.delete(1.0, tk.END)
        for line in result.split('\n'):
            if line.startswith("Hexagram: "):
                self.result_text.insert(tk.END, line[:10], 'normal')
                self.result_text.insert(tk.END, line[10:] + '\n', 'large')
            else:
                self.result_text.insert(tk.END, line + '\n', 'normal')
def main():
    root = tk.Tk()
    IChingGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()