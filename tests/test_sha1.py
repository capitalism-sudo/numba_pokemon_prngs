"""Tests for SHA-1 hash function"""
from __future__ import annotations
import numpy as np
from numba_pokemon_prngs.sha1 import SHA1
from numba_pokemon_prngs.enums import Language, Game, DSType


def test_initial_seed():
    """Test Gen 5 initial seed generation"""

    def generate_seed(
        sha1: SHA1,
        button: np.uint32,
        timer0: np.uint32,
        vcount: np.uint32,
        date: tuple[np.uint16],
        time: tuple[np.uint8],
    ) -> int:
        # not setting button/timer0/date/time causes undefined behaviour as the data array is empty
        # and these values would always otherwise be present
        sha1.set_button(button)
        sha1.set_timer0(timer0, vcount)
        sha1.set_date(*date)
        sha1.set_time(*time)
        return sha1.hash_seed(sha1.precompute())

    assert tuple(
        tuple(
            tuple(
                tuple(
                    generate_seed(
                        SHA1(
                            version,
                            language,
                            ds_type,
                            0x9BF123456,
                            False,
                            6,
                            6,
                        ),
                        button,
                        0x666,
                        0x3F,
                        (2067, 10, 31, 1),
                        (16, 12, 20),
                    )
                    for button in (
                        0xFF2F0000,
                        0xFE260000,
                        0x7C2F0000,
                    )
                )
                for ds_type in DSType
            )
            for version in (Game.BLACK, Game.WHITE, Game.BLACK2, Game.WHITE2)
        )
        for language in Language
    ) == (
        (
            (
                (14644003586327074781, 10728622701197375795, 6559353976335380635),
                (11790746559858873998, 4663120394683733541, 14407139545467720376),
                (1402193967064901199, 11169786524064667149, 7575197330523148242),
            ),
            (
                (7598333160674543765, 1975196244832744074, 6506737175019595025),
                (440507746519869377, 11401097238242273083, 6065857695645131080),
                (11451338174958740241, 889307207753442202, 15429029445471918885),
            ),
            (
                (17564294079017425436, 2911102141931788225, 2037814069912075275),
                (17642436489078369488, 14135293156329923272, 5056726394304851102),
                (17986473192428503739, 2351634568753011849, 3166160342738079323),
            ),
            (
                (8997968921221641627, 9793904476950511791, 5870747966133800724),
                (9356034089156693514, 100387653102410506, 1612409004422926574),
                (5500051303891321767, 13946780075382989563, 1135792586846500690),
            ),
        ),
        (
            (
                (7249451941571676574, 4837397549165758822, 17048263132792362545),
                (1976722072150916212, 2450127695464482389, 12478862977510332324),
                (5381680555236949175, 5983039102266465160, 2419938986691894393),
            ),
            (
                (14691001768388720244, 5419599892509315162, 5373469127038833105),
                (8865761968953889600, 4094955776966326792, 13176851582540891114),
                (14656067288772048613, 2373280571163287645, 2517166050780544109),
            ),
            (
                (17878431661510205795, 15714382538817960998, 3482728319237823315),
                (15200055770472788886, 12622355228024916873, 5034968334131453087),
                (14493907147254411856, 5818527905229504459, 18232128844288500642),
            ),
            (
                (15846324534321728101, 5626970655741001373, 13394682658621912536),
                (16055432056749607493, 15327940828616460441, 14309640832018004332),
                (4861025643963064525, 16132142952270351538, 2972053293953881733),
            ),
        ),
        (
            (
                (11784653829461782719, 5366006228581028638, 11668846421795802931),
                (13103091765709450525, 5976405545607653622, 4642714123116236255),
                (8348333839278115405, 672067994241064212, 4108577700302145644),
            ),
            (
                (11965763858414880544, 12478577452885234582, 17763783714869997554),
                (13103091765709450525, 5976405545607653622, 4642714123116236255),
                (8348333839278115405, 672067994241064212, 4108577700302145644),
            ),
            (
                (11242873210536797809, 16265078806086046923, 17126386188610829293),
                (3174501681344249918, 5362652644175813912, 9562272796375544245),
                (436072468632465395, 4473903007655858740, 14071173267582796830),
            ),
            (
                (9256278417575677554, 7153344392446407119, 7142202482338660160),
                (6573690004489066917, 9266718116578780493, 4695688982412592021),
                (4656160530674156260, 5997132684102851728, 10604441977207634922),
            ),
        ),
        (
            (
                (7126331150413790754, 16498451930453720778, 1340998660606470340),
                (937210287874280475, 7777111267584366355, 2763698222146525203),
                (12033594792833605529, 16003802846749517095, 14172496830685225975),
            ),
            (
                (15310416411547692252, 7637007891926460596, 8852329188049862004),
                (937210287874280475, 7777111267584366355, 2763698222146525203),
                (12033594792833605529, 16003802846749517095, 14172496830685225975),
            ),
            (
                (15386396842152464648, 3401705493525460794, 3390143893572267736),
                (14247553064132816920, 4927653778234495042, 4201555130439866074),
                (3644985648630638123, 13161624042940596963, 11984402558278676048),
            ),
            (
                (11031263726792470576, 10061829812348883326, 4436629501455481252),
                (1209262929779479223, 18443264528045167273, 6176055407799909150),
                (5435368227259292054, 1615785166029601937, 15352087363768713165),
            ),
        ),
        (
            (
                (6476260525915531487, 17983624147004930972, 6818177924347907847),
                (3047919904854053640, 13073166072067922820, 8051459550697014566),
                (17120274909984281466, 17321840711287230152, 17550928766481677964),
            ),
            (
                (12423704366281713736, 6204054744751153716, 10011916762301079176),
                (3047919904854053640, 13073166072067922820, 8051459550697014566),
                (17120274909984281466, 17321840711287230152, 17550928766481677964),
            ),
            (
                (834938752823867724, 18302316381609875808, 13406626795859800133),
                (3318397095658744882, 7899311796455423643, 12893820703318627191),
                (18050784674611099682, 4053054972115097286, 3929381353224793872),
            ),
            (
                (9845284595122484532, 6521142768204624956, 10515790902307708134),
                (13389632259357017445, 11895150060597153281, 16040428794740670351),
                (18142926356713595654, 15025593275361129029, 9544464499556503446),
            ),
        ),
        (
            (
                (12512615999465640029, 8258976521829195541, 8171314812132911820),
                (3047919904854053640, 13073166072067922820, 8051459550697014566),
                (17120274909984281466, 17321840711287230152, 17550928766481677964),
            ),
            (
                (12512615999465640029, 8258976521829195541, 8171314812132911820),
                (3047919904854053640, 13073166072067922820, 8051459550697014566),
                (17120274909984281466, 17321840711287230152, 17550928766481677964),
            ),
            (
                (5412809518967499930, 7369322025931963488, 17831980776658583422),
                (10238351584713989001, 598386131844934420, 5284187054335148187),
                (2430806425183857158, 6130053760812284442, 4483972227966500526),
            ),
            (
                (3007595741769706506, 9312501586690824143, 1326062896222828784),
                (14675895550495900423, 13463160963320679484, 5453001496154984688),
                (17135374343583562913, 285151700319753912, 17197804922636351458),
            ),
        ),
        (
            (
                (10997353737939279544, 9602452066708374458, 8811999495836930576),
                (14153578444651924338, 2516546270568367347, 17336076056080720501),
                (6982726386691421765, 15655097458557070035, 16861424706930526263),
            ),
            (
                (10997353737939279544, 9602452066708374458, 8811999495836930576),
                (14153578444651924338, 2516546270568367347, 17336076056080720501),
                (6982726386691421765, 15655097458557070035, 16861424706930526263),
            ),
            (
                (9343164327031575089, 11882122714868094012, 5902191924864963835),
                (13964029859730753844, 3890990149280583836, 8300691135265463364),
                (6101412515014281393, 3755166278974137513, 3174618077470676336),
            ),
            (
                (10594827938166313193, 9603428117135713120, 7673830585076033686),
                (8306172196944703800, 10330964859741976359, 1157731469300103403),
                (2036983192250102517, 10516257748674369778, 10665575797274778504),
            ),
        ),
    )
