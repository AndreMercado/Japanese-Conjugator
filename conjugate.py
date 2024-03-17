from sudachipy import Dictionary
import determine


def part_of_speech(verb):
    tokenizer = Dictionary().create()
    morphemes = tokenizer.tokenize(verb)
    token = morphemes[-1]
    part_of_speech = str(token.part_of_speech()[4])

    godan_groups = [
        "五段-ワア行", "五段-カ行", "五段-サ行", "五段-タ行", "五段-ナ行", "五段-マ行",
        "五段-ラ行", "五段-ガ行", "五段-バ行"
    ]

    if verb == 'する' or verb == '来る' or verb == '行く':
        return 'exception_suffixes.json'
    elif part_of_speech in godan_groups:
        return 'godan_suffixes.json'
    elif part_of_speech == '下一段-バ行' or part_of_speech == '上一段-カ行' or '上一段-マ行' or '下一段-ラ行':
        return 'ichidan_suffixes.json'


class conjugate:
    def __init__(self):
        self.verb = None

    def define(self, verb):
        self.verb = verb

    def conjugate(self, conjugation="present", formality='plain', energy="positive"):
        det = determine.determine(self.verb, part_of_speech(self.verb))

        match conjugation:
            case "stem":
                return det.stem(formality, energy)
            case "te-form":
                return det.te_form(formality, energy)
            case "infinitive":
                return det.infinitive(formality, energy)
            case "present":
                return det.present(formality, energy)
            case "past":
                return det.past(formality, energy)
            case "potential":
                return det.potential(formality, energy)
            case "causative":
                return det.causative(formality, energy)
            case "passive":
                return det.passive(formality, energy)
            case "causative_passive":
                return det.causative_passive(formality, energy)
            case "present-progressive":
                return det.present_progressive(formality, energy)
            case "past-progressive":
                return det.past_progressive(formality, energy)
            case "conditional-eba":
                return det.conditional_eba(formality, energy)
            case "conditional-tara":
                return det.conditional_tara(formality, energy)
            case "imperative":
                return det.imperative(formality, energy)
            case "volitional":
                return det.volitional(formality, energy)
