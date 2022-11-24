from unittest import TestCase
from iso_enum.iso639.ISOLanguage import ISOLanguage


class TestISOLanguage(TestCase):

    def test_value(self):
        
        self.assertEqual(ISOLanguage.AB.value, "ab")
        self.assertEqual(ISOLanguage.AB, ISOLanguage("ab"))
        self.assertEqual(ISOLanguage.AB, ISOLanguage("AB"))
        self.assertEqual(ISOLanguage.AB.code, "ab")
        self.assertEqual(ISOLanguage.AB.identifier, "ab")
        self.assertEqual(str(ISOLanguage.AB), "ab")
        
        self.assertEqual(ISOLanguage.OM.value, "om")
        self.assertEqual(ISOLanguage.OM, ISOLanguage("om"))
        self.assertEqual(ISOLanguage.OM, ISOLanguage("OM"))
        self.assertEqual(ISOLanguage.OM.code, "om")
        self.assertEqual(ISOLanguage.OM.identifier, "om")
        self.assertEqual(str(ISOLanguage.OM), "om")
        
        self.assertEqual(ISOLanguage.AA.value, "aa")
        self.assertEqual(ISOLanguage.AA, ISOLanguage("aa"))
        self.assertEqual(ISOLanguage.AA, ISOLanguage("AA"))
        self.assertEqual(ISOLanguage.AA.code, "aa")
        self.assertEqual(ISOLanguage.AA.identifier, "aa")
        self.assertEqual(str(ISOLanguage.AA), "aa")
        
        self.assertEqual(ISOLanguage.AF.value, "af")
        self.assertEqual(ISOLanguage.AF, ISOLanguage("af"))
        self.assertEqual(ISOLanguage.AF, ISOLanguage("AF"))
        self.assertEqual(ISOLanguage.AF.code, "af")
        self.assertEqual(ISOLanguage.AF.identifier, "af")
        self.assertEqual(str(ISOLanguage.AF), "af")
        

    def test_english(self):
        
        self.assertEqual(ISOLanguage.AB.en, "Abkhazian")
        self.assertEqual(ISOLanguage.AB.english[0], "Abkhazian")
        self.assertEqual(ISOLanguage.AB, "Abkhazian")
        self.assertEqual(ISOLanguage.AB, "ABKHAZIAN")
        self.assertEqual(ISOLanguage.AB, ISOLanguage("Abkhazian"))
        self.assertEqual(ISOLanguage.AB, ISOLanguage("ABKHAZIAN"))
        self.assertEqual(ISOLanguage.AB.english[1], "Abkhaz")
        self.assertEqual(ISOLanguage.AB, "Abkhaz")
        self.assertEqual(ISOLanguage.AB, "ABKHAZ")
        self.assertEqual(ISOLanguage.AB, ISOLanguage("Abkhaz"))
        self.assertEqual(ISOLanguage.AB, ISOLanguage("ABKHAZ"))
        
        
        self.assertEqual(ISOLanguage.OM.en, "Afan Oromo")
        self.assertEqual(ISOLanguage.OM.english[0], "Afan Oromo")
        self.assertEqual(ISOLanguage.OM, "Afan Oromo")
        self.assertEqual(ISOLanguage.OM, "AFAN OROMO")
        self.assertEqual(ISOLanguage.OM, ISOLanguage("Afan Oromo"))
        self.assertEqual(ISOLanguage.OM, ISOLanguage("AFAN OROMO"))
        self.assertEqual(ISOLanguage.OM.english[1], "Oromo")
        self.assertEqual(ISOLanguage.OM, "Oromo")
        self.assertEqual(ISOLanguage.OM, "OROMO")
        self.assertEqual(ISOLanguage.OM, ISOLanguage("Oromo"))
        self.assertEqual(ISOLanguage.OM, ISOLanguage("OROMO"))
        self.assertEqual(ISOLanguage.OM.english[2], "Galla")
        self.assertEqual(ISOLanguage.OM, "Galla")
        self.assertEqual(ISOLanguage.OM, "GALLA")
        self.assertEqual(ISOLanguage.OM, ISOLanguage("Galla"))
        self.assertEqual(ISOLanguage.OM, ISOLanguage("GALLA"))
        
        
        self.assertEqual(ISOLanguage.AA.en, "Afar")
        self.assertEqual(ISOLanguage.AA.english[0], "Afar")
        self.assertEqual(ISOLanguage.AA, "Afar")
        self.assertEqual(ISOLanguage.AA, "AFAR")
        self.assertEqual(ISOLanguage.AA, ISOLanguage("Afar"))
        self.assertEqual(ISOLanguage.AA, ISOLanguage("AFAR"))
        
        
        self.assertEqual(ISOLanguage.AF.en, "Afrikaans")
        self.assertEqual(ISOLanguage.AF.english[0], "Afrikaans")
        self.assertEqual(ISOLanguage.AF, "Afrikaans")
        self.assertEqual(ISOLanguage.AF, "AFRIKAANS")
        self.assertEqual(ISOLanguage.AF, ISOLanguage("Afrikaans"))
        self.assertEqual(ISOLanguage.AF, ISOLanguage("AFRIKAANS"))
        
        

    def test_french(self):
        
        self.assertEqual(ISOLanguage.AB.fr, "abkhaze")
        self.assertEqual(ISOLanguage.AB.french[0], "abkhaze")
        self.assertEqual(ISOLanguage.AB, "abkhaze")
        self.assertEqual(ISOLanguage.AB, "ABKHAZE")
        self.assertEqual(ISOLanguage.AB, ISOLanguage("abkhaze"))
        self.assertEqual(ISOLanguage.AB, ISOLanguage("ABKHAZE"))
        self.assertEqual(ISOLanguage.AB.french[1], "abkhazien")
        self.assertEqual(ISOLanguage.AB, "abkhazien")
        self.assertEqual(ISOLanguage.AB, "ABKHAZIEN")
        self.assertEqual(ISOLanguage.AB, ISOLanguage("abkhazien"))
        self.assertEqual(ISOLanguage.AB, ISOLanguage("ABKHAZIEN"))
        
        
        self.assertEqual(ISOLanguage.OM.fr, "oromo")
        self.assertEqual(ISOLanguage.OM.french[0], "oromo")
        self.assertEqual(ISOLanguage.OM, "oromo")
        self.assertEqual(ISOLanguage.OM, "OROMO")
        self.assertEqual(ISOLanguage.OM, ISOLanguage("oromo"))
        self.assertEqual(ISOLanguage.OM, ISOLanguage("OROMO"))
        self.assertEqual(ISOLanguage.OM.french[1], "afan oromo")
        self.assertEqual(ISOLanguage.OM, "afan oromo")
        self.assertEqual(ISOLanguage.OM, "AFAN OROMO")
        self.assertEqual(ISOLanguage.OM, ISOLanguage("afan oromo"))
        self.assertEqual(ISOLanguage.OM, ISOLanguage("AFAN OROMO"))
        self.assertEqual(ISOLanguage.OM.french[2], "galla")
        self.assertEqual(ISOLanguage.OM, "galla")
        self.assertEqual(ISOLanguage.OM, "GALLA")
        self.assertEqual(ISOLanguage.OM, ISOLanguage("galla"))
        self.assertEqual(ISOLanguage.OM, ISOLanguage("GALLA"))
        
        
        self.assertEqual(ISOLanguage.AA.fr, "afar")
        self.assertEqual(ISOLanguage.AA.french[0], "afar")
        self.assertEqual(ISOLanguage.AA, "afar")
        self.assertEqual(ISOLanguage.AA, "AFAR")
        self.assertEqual(ISOLanguage.AA, ISOLanguage("afar"))
        self.assertEqual(ISOLanguage.AA, ISOLanguage("AFAR"))
        
        
        self.assertEqual(ISOLanguage.AF.fr, "afrikaans")
        self.assertEqual(ISOLanguage.AF.french[0], "afrikaans")
        self.assertEqual(ISOLanguage.AF, "afrikaans")
        self.assertEqual(ISOLanguage.AF, "AFRIKAANS")
        self.assertEqual(ISOLanguage.AF, ISOLanguage("afrikaans"))
        self.assertEqual(ISOLanguage.AF, ISOLanguage("AFRIKAANS"))
        
        

    def test_indigenous(self):
        
        self.assertEqual(ISOLanguage.AB.ind, "apsua byszwa")
        self.assertEqual(ISOLanguage.AB.indigenous[0], "apsua byszwa")
        self.assertEqual(ISOLanguage.AB, "apsua byszwa")
        self.assertEqual(ISOLanguage.AB, "APSUA BYSZWA")
        self.assertEqual(ISOLanguage.AB, ISOLanguage("apsua byszwa"))
        self.assertEqual(ISOLanguage.AB, ISOLanguage("APSUA BYSZWA"))
        
        
        self.assertEqual(ISOLanguage.OM.ind, "(afan) oromo")
        self.assertEqual(ISOLanguage.OM.indigenous[0], "(afan) oromo")
        self.assertEqual(ISOLanguage.OM, "(afan) oromo")
        self.assertEqual(ISOLanguage.OM, "(AFAN) OROMO")
        self.assertEqual(ISOLanguage.OM, ISOLanguage("(afan) oromo"))
        self.assertEqual(ISOLanguage.OM, ISOLanguage("(AFAN) OROMO"))
        
        
        self.assertEqual(ISOLanguage.AA.ind, "afar")
        self.assertEqual(ISOLanguage.AA.indigenous[0], "afar")
        self.assertEqual(ISOLanguage.AA, "afar")
        self.assertEqual(ISOLanguage.AA, "AFAR")
        self.assertEqual(ISOLanguage.AA, ISOLanguage("afar"))
        self.assertEqual(ISOLanguage.AA, ISOLanguage("AFAR"))
        
        
        self.assertEqual(ISOLanguage.AF.ind, "Afrikaans")
        self.assertEqual(ISOLanguage.AF.indigenous[0], "Afrikaans")
        self.assertEqual(ISOLanguage.AF, "Afrikaans")
        self.assertEqual(ISOLanguage.AF, "AFRIKAANS")
        self.assertEqual(ISOLanguage.AF, ISOLanguage("Afrikaans"))
        self.assertEqual(ISOLanguage.AF, ISOLanguage("AFRIKAANS"))
        
        

    def test_pickle(self):
        pass
