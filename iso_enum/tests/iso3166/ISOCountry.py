from unittest import TestCase
from iso_enum.iso3166.ISOCountry import ISOCountry


class TestISOCountry(TestCase):

    def test_equality(self):
        
        
        
        self.assertEqual(ISOCountry.AD, 20)
        self.assertEqual(ISOCountry.AD, "AD")
        self.assertEqual(ISOCountry.AD, "AND")
        self.assertEqual(ISOCountry.AD, "Andorra")
        self.assertEqual(ISOCountry.AD, "ANDORRA")
        self.assertEqual(ISOCountry.AD, "the Principality of Andorra")
        self.assertEqual(ISOCountry.AD, "THE PRINCIPALITY OF ANDORRA")
        self.assertEqual(str(ISOCountry.AD), "AD")
        self.assertEqual(ISOCountry.AD.numeric, 20)
        
        self.assertEqual(ISOCountry.AE, 784)
        self.assertEqual(ISOCountry.AE, "AE")
        self.assertEqual(ISOCountry.AE, "ARE")
        self.assertEqual(ISOCountry.AE, "United Arab Emirates (the)")
        self.assertEqual(ISOCountry.AE, "UNITED ARAB EMIRATES (THE)")
        self.assertEqual(ISOCountry.AE, "the United Arab Emirates")
        self.assertEqual(ISOCountry.AE, "THE UNITED ARAB EMIRATES")
        self.assertEqual(str(ISOCountry.AE), "AE")
        self.assertEqual(ISOCountry.AE.numeric, 784)
        
        self.assertEqual(ISOCountry.AF, 4)
        self.assertEqual(ISOCountry.AF, "AF")
        self.assertEqual(ISOCountry.AF, "AFG")
        self.assertEqual(ISOCountry.AF, "Afghanistan")
        self.assertEqual(ISOCountry.AF, "AFGHANISTAN")
        self.assertEqual(ISOCountry.AF, "the Islamic Republic of Afghanistan")
        self.assertEqual(ISOCountry.AF, "THE ISLAMIC REPUBLIC OF AFGHANISTAN")
        self.assertEqual(str(ISOCountry.AF), "AF")
        self.assertEqual(ISOCountry.AF.numeric, 4)
        
        self.assertEqual(ISOCountry.AG, 28)
        self.assertEqual(ISOCountry.AG, "AG")
        self.assertEqual(ISOCountry.AG, "ATG")
        self.assertEqual(ISOCountry.AG, "Antigua and Barbuda")
        self.assertEqual(ISOCountry.AG, "ANTIGUA AND BARBUDA")
        
        
        
        self.assertEqual(ISOCountry.AI, 660)
        self.assertEqual(ISOCountry.AI, "AI")
        self.assertEqual(ISOCountry.AI, "AIA")
        self.assertEqual(ISOCountry.AI, "Anguilla")
        self.assertEqual(ISOCountry.AI, "ANGUILLA")
        
        
        self.assertEqual(ISOCountry.AL, 8)
        self.assertEqual(ISOCountry.AL, "AL")
        self.assertEqual(ISOCountry.AL, "ALB")
        self.assertEqual(ISOCountry.AL, "Albania")
        self.assertEqual(ISOCountry.AL, "ALBANIA")
        self.assertEqual(ISOCountry.AL, "the Republic of Albania")
        self.assertEqual(ISOCountry.AL, "THE REPUBLIC OF ALBANIA")
        self.assertEqual(str(ISOCountry.AL), "AL")
        self.assertEqual(ISOCountry.AL.numeric, 8)
        
        self.assertEqual(ISOCountry.AM, 51)
        self.assertEqual(ISOCountry.AM, "AM")
        self.assertEqual(ISOCountry.AM, "ARM")
        self.assertEqual(ISOCountry.AM, "Armenia")
        self.assertEqual(ISOCountry.AM, "ARMENIA")
        self.assertEqual(ISOCountry.AM, "the Republic of Armenia")
        self.assertEqual(ISOCountry.AM, "THE REPUBLIC OF ARMENIA")
        self.assertEqual(str(ISOCountry.AM), "AM")
        self.assertEqual(ISOCountry.AM.numeric, 51)
        
        
        self.assertEqual(ISOCountry.AO, 24)
        self.assertEqual(ISOCountry.AO, "AO")
        self.assertEqual(ISOCountry.AO, "AGO")
        self.assertEqual(ISOCountry.AO, "Angola")
        self.assertEqual(ISOCountry.AO, "ANGOLA")
        self.assertEqual(ISOCountry.AO, "the Republic of Angola")
        self.assertEqual(ISOCountry.AO, "THE REPUBLIC OF ANGOLA")
        self.assertEqual(str(ISOCountry.AO), "AO")
        self.assertEqual(ISOCountry.AO.numeric, 24)
        
        
        self.assertEqual(ISOCountry.AQ, 10)
        self.assertEqual(ISOCountry.AQ, "AQ")
        self.assertEqual(ISOCountry.AQ, "ATA")
        self.assertEqual(ISOCountry.AQ, "Antarctica")
        self.assertEqual(ISOCountry.AQ, "ANTARCTICA")
        
        
        self.assertEqual(ISOCountry.AR, 32)
        self.assertEqual(ISOCountry.AR, "AR")
        self.assertEqual(ISOCountry.AR, "ARG")
        self.assertEqual(ISOCountry.AR, "Argentina")
        self.assertEqual(ISOCountry.AR, "ARGENTINA")
        self.assertEqual(ISOCountry.AR, "the Argentine Republic")
        self.assertEqual(ISOCountry.AR, "THE ARGENTINE REPUBLIC")
        self.assertEqual(str(ISOCountry.AR), "AR")
        self.assertEqual(ISOCountry.AR.numeric, 32)
        
        self.assertEqual(ISOCountry.AS, 16)
        self.assertEqual(ISOCountry.AS, "AS")
        self.assertEqual(ISOCountry.AS, "ASM")
        self.assertEqual(ISOCountry.AS, "American Samoa")
        self.assertEqual(ISOCountry.AS, "AMERICAN SAMOA")
        
        
        self.assertEqual(ISOCountry.AT, 40)
        self.assertEqual(ISOCountry.AT, "AT")
        self.assertEqual(ISOCountry.AT, "AUT")
        self.assertEqual(ISOCountry.AT, "Austria")
        self.assertEqual(ISOCountry.AT, "AUSTRIA")
        self.assertEqual(ISOCountry.AT, "the Republic of Austria")
        self.assertEqual(ISOCountry.AT, "THE REPUBLIC OF AUSTRIA")
        self.assertEqual(str(ISOCountry.AT), "AT")
        self.assertEqual(ISOCountry.AT.numeric, 40)
        
        self.assertEqual(ISOCountry.AU, 36)
        self.assertEqual(ISOCountry.AU, "AU")
        self.assertEqual(ISOCountry.AU, "AUS")
        self.assertEqual(ISOCountry.AU, "Australia")
        self.assertEqual(ISOCountry.AU, "AUSTRALIA")
        
        
        self.assertEqual(ISOCountry.AW, 533)
        self.assertEqual(ISOCountry.AW, "AW")
        self.assertEqual(ISOCountry.AW, "ABW")
        self.assertEqual(ISOCountry.AW, "Aruba")
        self.assertEqual(ISOCountry.AW, "ARUBA")
        
        
        self.assertEqual(ISOCountry.AX, 248)
        self.assertEqual(ISOCountry.AX, "AX")
        self.assertEqual(ISOCountry.AX, "ALA")
        self.assertEqual(ISOCountry.AX, "Åland Islands")
        self.assertEqual(ISOCountry.AX, "ÅLAND ISLANDS")
        
        
        self.assertEqual(ISOCountry.AZ, 31)
        self.assertEqual(ISOCountry.AZ, "AZ")
        self.assertEqual(ISOCountry.AZ, "AZE")
        self.assertEqual(ISOCountry.AZ, "Azerbaijan")
        self.assertEqual(ISOCountry.AZ, "AZERBAIJAN")
        self.assertEqual(ISOCountry.AZ, "the Republic of Azerbaijan")
        self.assertEqual(ISOCountry.AZ, "THE REPUBLIC OF AZERBAIJAN")
        self.assertEqual(str(ISOCountry.AZ), "AZ")
        self.assertEqual(ISOCountry.AZ.numeric, 31)
        
        self.assertEqual(ISOCountry.BA, 70)
        self.assertEqual(ISOCountry.BA, "BA")
        self.assertEqual(ISOCountry.BA, "BIH")
        self.assertEqual(ISOCountry.BA, "Bosnia and Herzegovina")
        self.assertEqual(ISOCountry.BA, "BOSNIA AND HERZEGOVINA")
        
        
        self.assertEqual(ISOCountry.BB, 52)
        self.assertEqual(ISOCountry.BB, "BB")
        self.assertEqual(ISOCountry.BB, "BRB")
        self.assertEqual(ISOCountry.BB, "Barbados")
        self.assertEqual(ISOCountry.BB, "BARBADOS")
        
        
        self.assertEqual(ISOCountry.BD, 50)
        self.assertEqual(ISOCountry.BD, "BD")
        self.assertEqual(ISOCountry.BD, "BGD")
        self.assertEqual(ISOCountry.BD, "Bangladesh")
        self.assertEqual(ISOCountry.BD, "BANGLADESH")
        self.assertEqual(ISOCountry.BD, "the People's Republic of Bangladesh")
        self.assertEqual(ISOCountry.BD, "THE PEOPLE'S REPUBLIC OF BANGLADESH")
        self.assertEqual(str(ISOCountry.BD), "BD")
        self.assertEqual(ISOCountry.BD.numeric, 50)
        
        self.assertEqual(ISOCountry.BE, 56)
        self.assertEqual(ISOCountry.BE, "BE")
        self.assertEqual(ISOCountry.BE, "BEL")
        self.assertEqual(ISOCountry.BE, "Belgium")
        self.assertEqual(ISOCountry.BE, "BELGIUM")
        self.assertEqual(ISOCountry.BE, "the Kingdom of Belgium")
        self.assertEqual(ISOCountry.BE, "THE KINGDOM OF BELGIUM")
        self.assertEqual(str(ISOCountry.BE), "BE")
        self.assertEqual(ISOCountry.BE.numeric, 56)
        
        self.assertEqual(ISOCountry.BF, 854)
        self.assertEqual(ISOCountry.BF, "BF")
        self.assertEqual(ISOCountry.BF, "BFA")
        self.assertEqual(ISOCountry.BF, "Burkina Faso")
        self.assertEqual(ISOCountry.BF, "BURKINA FASO")
        
        
        self.assertEqual(ISOCountry.BG, 100)
        self.assertEqual(ISOCountry.BG, "BG")
        self.assertEqual(ISOCountry.BG, "BGR")
        self.assertEqual(ISOCountry.BG, "Bulgaria")
        self.assertEqual(ISOCountry.BG, "BULGARIA")
        self.assertEqual(ISOCountry.BG, "the Republic of Bulgaria")
        self.assertEqual(ISOCountry.BG, "THE REPUBLIC OF BULGARIA")
        self.assertEqual(str(ISOCountry.BG), "BG")
        self.assertEqual(ISOCountry.BG.numeric, 100)
        
        self.assertEqual(ISOCountry.BH, 48)
        self.assertEqual(ISOCountry.BH, "BH")
        self.assertEqual(ISOCountry.BH, "BHR")
        self.assertEqual(ISOCountry.BH, "Bahrain")
        self.assertEqual(ISOCountry.BH, "BAHRAIN")
        self.assertEqual(ISOCountry.BH, "the Kingdom of Bahrain")
        self.assertEqual(ISOCountry.BH, "THE KINGDOM OF BAHRAIN")
        self.assertEqual(str(ISOCountry.BH), "BH")
        self.assertEqual(ISOCountry.BH.numeric, 48)
        
        self.assertEqual(ISOCountry.BI, 108)
        self.assertEqual(ISOCountry.BI, "BI")
        self.assertEqual(ISOCountry.BI, "BDI")
        self.assertEqual(ISOCountry.BI, "Burundi")
        self.assertEqual(ISOCountry.BI, "BURUNDI")
        self.assertEqual(ISOCountry.BI, "the Republic of Burundi")
        self.assertEqual(ISOCountry.BI, "THE REPUBLIC OF BURUNDI")
        self.assertEqual(str(ISOCountry.BI), "BI")
        self.assertEqual(ISOCountry.BI.numeric, 108)
        
        self.assertEqual(ISOCountry.BJ, 204)
        self.assertEqual(ISOCountry.BJ, "BJ")
        self.assertEqual(ISOCountry.BJ, "BEN")
        self.assertEqual(ISOCountry.BJ, "Benin")
        self.assertEqual(ISOCountry.BJ, "BENIN")
        self.assertEqual(ISOCountry.BJ, "the Republic of Benin")
        self.assertEqual(ISOCountry.BJ, "THE REPUBLIC OF BENIN")
        self.assertEqual(str(ISOCountry.BJ), "BJ")
        self.assertEqual(ISOCountry.BJ.numeric, 204)
        
        self.assertEqual(ISOCountry.BL, 652)
        self.assertEqual(ISOCountry.BL, "BL")
        self.assertEqual(ISOCountry.BL, "BLM")
        self.assertEqual(ISOCountry.BL, "Saint Barthélemy")
        self.assertEqual(ISOCountry.BL, "SAINT BARTHÉLEMY")
        
        
        self.assertEqual(ISOCountry.BM, 60)
        self.assertEqual(ISOCountry.BM, "BM")
        self.assertEqual(ISOCountry.BM, "BMU")
        self.assertEqual(ISOCountry.BM, "Bermuda")
        self.assertEqual(ISOCountry.BM, "BERMUDA")
        
        
        self.assertEqual(ISOCountry.BN, 96)
        self.assertEqual(ISOCountry.BN, "BN")
        self.assertEqual(ISOCountry.BN, "BRN")
        self.assertEqual(ISOCountry.BN, "Brunei Darussalam")
        self.assertEqual(ISOCountry.BN, "BRUNEI DARUSSALAM")
        
        
        self.assertEqual(ISOCountry.BO, 68)
        self.assertEqual(ISOCountry.BO, "BO")
        self.assertEqual(ISOCountry.BO, "BOL")
        self.assertEqual(ISOCountry.BO, "Bolivia (Plurinational State of)")
        self.assertEqual(ISOCountry.BO, "BOLIVIA (PLURINATIONAL STATE OF)")
        self.assertEqual(ISOCountry.BO, "the Plurinational State of Bolivia")
        self.assertEqual(ISOCountry.BO, "THE PLURINATIONAL STATE OF BOLIVIA")
        self.assertEqual(str(ISOCountry.BO), "BO")
        self.assertEqual(ISOCountry.BO.numeric, 68)
        
        
        self.assertEqual(ISOCountry.BQ, 535)
        self.assertEqual(ISOCountry.BQ, "BQ")
        self.assertEqual(ISOCountry.BQ, "BES")
        self.assertEqual(ISOCountry.BQ, "Bonaire, Sint Eustatius and Saba")
        self.assertEqual(ISOCountry.BQ, "BONAIRE, SINT EUSTATIUS AND SABA")
        
        
        self.assertEqual(ISOCountry.BR, 76)
        self.assertEqual(ISOCountry.BR, "BR")
        self.assertEqual(ISOCountry.BR, "BRA")
        self.assertEqual(ISOCountry.BR, "Brazil")
        self.assertEqual(ISOCountry.BR, "BRAZIL")
        self.assertEqual(ISOCountry.BR, "the Federative Republic of Brazil")
        self.assertEqual(ISOCountry.BR, "THE FEDERATIVE REPUBLIC OF BRAZIL")
        self.assertEqual(str(ISOCountry.BR), "BR")
        self.assertEqual(ISOCountry.BR.numeric, 76)
        
        self.assertEqual(ISOCountry.BS, 44)
        self.assertEqual(ISOCountry.BS, "BS")
        self.assertEqual(ISOCountry.BS, "BHS")
        self.assertEqual(ISOCountry.BS, "Bahamas (the)")
        self.assertEqual(ISOCountry.BS, "BAHAMAS (THE)")
        self.assertEqual(ISOCountry.BS, "the Commonwealth of the Bahamas")
        self.assertEqual(ISOCountry.BS, "THE COMMONWEALTH OF THE BAHAMAS")
        self.assertEqual(str(ISOCountry.BS), "BS")
        self.assertEqual(ISOCountry.BS.numeric, 44)
        
        self.assertEqual(ISOCountry.BT, 64)
        self.assertEqual(ISOCountry.BT, "BT")
        self.assertEqual(ISOCountry.BT, "BTN")
        self.assertEqual(ISOCountry.BT, "Bhutan")
        self.assertEqual(ISOCountry.BT, "BHUTAN")
        self.assertEqual(ISOCountry.BT, "the Kingdom of Bhutan")
        self.assertEqual(ISOCountry.BT, "THE KINGDOM OF BHUTAN")
        self.assertEqual(str(ISOCountry.BT), "BT")
        self.assertEqual(ISOCountry.BT.numeric, 64)
        
        
        self.assertEqual(ISOCountry.BV, 74)
        self.assertEqual(ISOCountry.BV, "BV")
        self.assertEqual(ISOCountry.BV, "BVT")
        self.assertEqual(ISOCountry.BV, "Bouvet Island")
        self.assertEqual(ISOCountry.BV, "BOUVET ISLAND")
        
        
        self.assertEqual(ISOCountry.BW, 72)
        self.assertEqual(ISOCountry.BW, "BW")
        self.assertEqual(ISOCountry.BW, "BWA")
        self.assertEqual(ISOCountry.BW, "Botswana")
        self.assertEqual(ISOCountry.BW, "BOTSWANA")
        self.assertEqual(ISOCountry.BW, "the Republic of Botswana")
        self.assertEqual(ISOCountry.BW, "THE REPUBLIC OF BOTSWANA")
        self.assertEqual(str(ISOCountry.BW), "BW")
        self.assertEqual(ISOCountry.BW.numeric, 72)
        
        
        
        self.assertEqual(ISOCountry.BY, 112)
        self.assertEqual(ISOCountry.BY, "BY")
        self.assertEqual(ISOCountry.BY, "BLR")
        self.assertEqual(ISOCountry.BY, "Belarus")
        self.assertEqual(ISOCountry.BY, "BELARUS")
        self.assertEqual(ISOCountry.BY, "the Republic of Belarus")
        self.assertEqual(ISOCountry.BY, "THE REPUBLIC OF BELARUS")
        self.assertEqual(str(ISOCountry.BY), "BY")
        self.assertEqual(ISOCountry.BY.numeric, 112)
        
        self.assertEqual(ISOCountry.BZ, 84)
        self.assertEqual(ISOCountry.BZ, "BZ")
        self.assertEqual(ISOCountry.BZ, "BLZ")
        self.assertEqual(ISOCountry.BZ, "Belize")
        self.assertEqual(ISOCountry.BZ, "BELIZE")
        
        
        self.assertEqual(ISOCountry.CA, 124)
        self.assertEqual(ISOCountry.CA, "CA")
        self.assertEqual(ISOCountry.CA, "CAN")
        self.assertEqual(ISOCountry.CA, "Canada")
        self.assertEqual(ISOCountry.CA, "CANADA")
        
        
        self.assertEqual(ISOCountry.CC, 166)
        self.assertEqual(ISOCountry.CC, "CC")
        self.assertEqual(ISOCountry.CC, "CCK")
        self.assertEqual(ISOCountry.CC, "Cocos (Keeling) Islands (the)")
        self.assertEqual(ISOCountry.CC, "COCOS (KEELING) ISLANDS (THE)")
        
        
        self.assertEqual(ISOCountry.CD, 180)
        self.assertEqual(ISOCountry.CD, "CD")
        self.assertEqual(ISOCountry.CD, "COD")
        self.assertEqual(ISOCountry.CD, "Congo (the Democratic Republic of the)")
        self.assertEqual(ISOCountry.CD, "CONGO (THE DEMOCRATIC REPUBLIC OF THE)")
        self.assertEqual(ISOCountry.CD, "the Democratic Republic of the Congo")
        self.assertEqual(ISOCountry.CD, "THE DEMOCRATIC REPUBLIC OF THE CONGO")
        self.assertEqual(str(ISOCountry.CD), "CD")
        self.assertEqual(ISOCountry.CD.numeric, 180)
        
        self.assertEqual(ISOCountry.CF, 140)
        self.assertEqual(ISOCountry.CF, "CF")
        self.assertEqual(ISOCountry.CF, "CAF")
        self.assertEqual(ISOCountry.CF, "Central African Republic (the)")
        self.assertEqual(ISOCountry.CF, "CENTRAL AFRICAN REPUBLIC (THE)")
        self.assertEqual(ISOCountry.CF, "the Central African Republic")
        self.assertEqual(ISOCountry.CF, "THE CENTRAL AFRICAN REPUBLIC")
        self.assertEqual(str(ISOCountry.CF), "CF")
        self.assertEqual(ISOCountry.CF.numeric, 140)
        
        self.assertEqual(ISOCountry.CG, 178)
        self.assertEqual(ISOCountry.CG, "CG")
        self.assertEqual(ISOCountry.CG, "COG")
        self.assertEqual(ISOCountry.CG, "Congo (the)")
        self.assertEqual(ISOCountry.CG, "CONGO (THE)")
        self.assertEqual(ISOCountry.CG, "the Republic of the Congo")
        self.assertEqual(ISOCountry.CG, "THE REPUBLIC OF THE CONGO")
        self.assertEqual(str(ISOCountry.CG), "CG")
        self.assertEqual(ISOCountry.CG.numeric, 178)
        
        self.assertEqual(ISOCountry.CH, 756)
        self.assertEqual(ISOCountry.CH, "CH")
        self.assertEqual(ISOCountry.CH, "CHE")
        self.assertEqual(ISOCountry.CH, "Switzerland")
        self.assertEqual(ISOCountry.CH, "SWITZERLAND")
        self.assertEqual(ISOCountry.CH, "the Swiss Confederation")
        self.assertEqual(ISOCountry.CH, "THE SWISS CONFEDERATION")
        self.assertEqual(str(ISOCountry.CH), "CH")
        self.assertEqual(ISOCountry.CH.numeric, 756)
        
        self.assertEqual(ISOCountry.CI, 384)
        self.assertEqual(ISOCountry.CI, "CI")
        self.assertEqual(ISOCountry.CI, "CIV")
        self.assertEqual(ISOCountry.CI, "Côte d'Ivoire")
        self.assertEqual(ISOCountry.CI, "CÔTE D'IVOIRE")
        self.assertEqual(ISOCountry.CI, "the Republic of Côte d'Ivoire")
        self.assertEqual(ISOCountry.CI, "THE REPUBLIC OF CÔTE D'IVOIRE")
        self.assertEqual(str(ISOCountry.CI), "CI")
        self.assertEqual(ISOCountry.CI.numeric, 384)
        
        self.assertEqual(ISOCountry.CK, 184)
        self.assertEqual(ISOCountry.CK, "CK")
        self.assertEqual(ISOCountry.CK, "COK")
        self.assertEqual(ISOCountry.CK, "Cook Islands (the)")
        self.assertEqual(ISOCountry.CK, "COOK ISLANDS (THE)")
        
        
        self.assertEqual(ISOCountry.CL, 152)
        self.assertEqual(ISOCountry.CL, "CL")
        self.assertEqual(ISOCountry.CL, "CHL")
        self.assertEqual(ISOCountry.CL, "Chile")
        self.assertEqual(ISOCountry.CL, "CHILE")
        self.assertEqual(ISOCountry.CL, "the Republic of Chile")
        self.assertEqual(ISOCountry.CL, "THE REPUBLIC OF CHILE")
        self.assertEqual(str(ISOCountry.CL), "CL")
        self.assertEqual(ISOCountry.CL.numeric, 152)
        
        self.assertEqual(ISOCountry.CM, 120)
        self.assertEqual(ISOCountry.CM, "CM")
        self.assertEqual(ISOCountry.CM, "CMR")
        self.assertEqual(ISOCountry.CM, "Cameroon")
        self.assertEqual(ISOCountry.CM, "CAMEROON")
        self.assertEqual(ISOCountry.CM, "the Republic of Cameroon")
        self.assertEqual(ISOCountry.CM, "THE REPUBLIC OF CAMEROON")
        self.assertEqual(str(ISOCountry.CM), "CM")
        self.assertEqual(ISOCountry.CM.numeric, 120)
        
        self.assertEqual(ISOCountry.CN, 156)
        self.assertEqual(ISOCountry.CN, "CN")
        self.assertEqual(ISOCountry.CN, "CHN")
        self.assertEqual(ISOCountry.CN, "China")
        self.assertEqual(ISOCountry.CN, "CHINA")
        self.assertEqual(ISOCountry.CN, "the People's Republic of China")
        self.assertEqual(ISOCountry.CN, "THE PEOPLE'S REPUBLIC OF CHINA")
        self.assertEqual(str(ISOCountry.CN), "CN")
        self.assertEqual(ISOCountry.CN.numeric, 156)
        
        self.assertEqual(ISOCountry.CO, 170)
        self.assertEqual(ISOCountry.CO, "CO")
        self.assertEqual(ISOCountry.CO, "COL")
        self.assertEqual(ISOCountry.CO, "Colombia")
        self.assertEqual(ISOCountry.CO, "COLOMBIA")
        self.assertEqual(ISOCountry.CO, "the Republic of Colombia")
        self.assertEqual(ISOCountry.CO, "THE REPUBLIC OF COLOMBIA")
        self.assertEqual(str(ISOCountry.CO), "CO")
        self.assertEqual(ISOCountry.CO.numeric, 170)
        
        
        
        self.assertEqual(ISOCountry.CR, 188)
        self.assertEqual(ISOCountry.CR, "CR")
        self.assertEqual(ISOCountry.CR, "CRI")
        self.assertEqual(ISOCountry.CR, "Costa Rica")
        self.assertEqual(ISOCountry.CR, "COSTA RICA")
        self.assertEqual(ISOCountry.CR, "the Republic of Costa Rica")
        self.assertEqual(ISOCountry.CR, "THE REPUBLIC OF COSTA RICA")
        self.assertEqual(str(ISOCountry.CR), "CR")
        self.assertEqual(ISOCountry.CR.numeric, 188)
        
        
        
        
        self.assertEqual(ISOCountry.CU, 192)
        self.assertEqual(ISOCountry.CU, "CU")
        self.assertEqual(ISOCountry.CU, "CUB")
        self.assertEqual(ISOCountry.CU, "Cuba")
        self.assertEqual(ISOCountry.CU, "CUBA")
        self.assertEqual(ISOCountry.CU, "the Republic of Cuba")
        self.assertEqual(ISOCountry.CU, "THE REPUBLIC OF CUBA")
        self.assertEqual(str(ISOCountry.CU), "CU")
        self.assertEqual(ISOCountry.CU.numeric, 192)
        
        self.assertEqual(ISOCountry.CV, 132)
        self.assertEqual(ISOCountry.CV, "CV")
        self.assertEqual(ISOCountry.CV, "CPV")
        self.assertEqual(ISOCountry.CV, "Cabo Verde")
        self.assertEqual(ISOCountry.CV, "CABO VERDE")
        self.assertEqual(ISOCountry.CV, "the Republic of Cabo Verde")
        self.assertEqual(ISOCountry.CV, "THE REPUBLIC OF CABO VERDE")
        self.assertEqual(str(ISOCountry.CV), "CV")
        self.assertEqual(ISOCountry.CV.numeric, 132)
        
        self.assertEqual(ISOCountry.CW, 531)
        self.assertEqual(ISOCountry.CW, "CW")
        self.assertEqual(ISOCountry.CW, "CUW")
        self.assertEqual(ISOCountry.CW, "Curaçao")
        self.assertEqual(ISOCountry.CW, "CURAÇAO")
        
        
        self.assertEqual(ISOCountry.CX, 162)
        self.assertEqual(ISOCountry.CX, "CX")
        self.assertEqual(ISOCountry.CX, "CXR")
        self.assertEqual(ISOCountry.CX, "Christmas Island")
        self.assertEqual(ISOCountry.CX, "CHRISTMAS ISLAND")
        
        
        self.assertEqual(ISOCountry.CY, 196)
        self.assertEqual(ISOCountry.CY, "CY")
        self.assertEqual(ISOCountry.CY, "CYP")
        self.assertEqual(ISOCountry.CY, "Cyprus")
        self.assertEqual(ISOCountry.CY, "CYPRUS")
        self.assertEqual(ISOCountry.CY, "the Republic of Cyprus")
        self.assertEqual(ISOCountry.CY, "THE REPUBLIC OF CYPRUS")
        self.assertEqual(str(ISOCountry.CY), "CY")
        self.assertEqual(ISOCountry.CY.numeric, 196)
        
        self.assertEqual(ISOCountry.CZ, 203)
        self.assertEqual(ISOCountry.CZ, "CZ")
        self.assertEqual(ISOCountry.CZ, "CZE")
        self.assertEqual(ISOCountry.CZ, "Czechia")
        self.assertEqual(ISOCountry.CZ, "CZECHIA")
        self.assertEqual(ISOCountry.CZ, "the Czech Republic")
        self.assertEqual(ISOCountry.CZ, "THE CZECH REPUBLIC")
        self.assertEqual(str(ISOCountry.CZ), "CZ")
        self.assertEqual(ISOCountry.CZ.numeric, 203)
        
        
        self.assertEqual(ISOCountry.DE, 276)
        self.assertEqual(ISOCountry.DE, "DE")
        self.assertEqual(ISOCountry.DE, "DEU")
        self.assertEqual(ISOCountry.DE, "Germany")
        self.assertEqual(ISOCountry.DE, "GERMANY")
        self.assertEqual(ISOCountry.DE, "the Federal Republic of Germany")
        self.assertEqual(ISOCountry.DE, "THE FEDERAL REPUBLIC OF GERMANY")
        self.assertEqual(str(ISOCountry.DE), "DE")
        self.assertEqual(ISOCountry.DE.numeric, 276)
        
        
        self.assertEqual(ISOCountry.DJ, 262)
        self.assertEqual(ISOCountry.DJ, "DJ")
        self.assertEqual(ISOCountry.DJ, "DJI")
        self.assertEqual(ISOCountry.DJ, "Djibouti")
        self.assertEqual(ISOCountry.DJ, "DJIBOUTI")
        self.assertEqual(ISOCountry.DJ, "the Republic of Djibouti")
        self.assertEqual(ISOCountry.DJ, "THE REPUBLIC OF DJIBOUTI")
        self.assertEqual(str(ISOCountry.DJ), "DJ")
        self.assertEqual(ISOCountry.DJ.numeric, 262)
        
        self.assertEqual(ISOCountry.DK, 208)
        self.assertEqual(ISOCountry.DK, "DK")
        self.assertEqual(ISOCountry.DK, "DNK")
        self.assertEqual(ISOCountry.DK, "Denmark")
        self.assertEqual(ISOCountry.DK, "DENMARK")
        self.assertEqual(ISOCountry.DK, "the Kingdom of Denmark")
        self.assertEqual(ISOCountry.DK, "THE KINGDOM OF DENMARK")
        self.assertEqual(str(ISOCountry.DK), "DK")
        self.assertEqual(ISOCountry.DK.numeric, 208)
        
        self.assertEqual(ISOCountry.DM, 212)
        self.assertEqual(ISOCountry.DM, "DM")
        self.assertEqual(ISOCountry.DM, "DMA")
        self.assertEqual(ISOCountry.DM, "Dominica")
        self.assertEqual(ISOCountry.DM, "DOMINICA")
        self.assertEqual(ISOCountry.DM, "the Commonwealth of Dominica")
        self.assertEqual(ISOCountry.DM, "THE COMMONWEALTH OF DOMINICA")
        self.assertEqual(str(ISOCountry.DM), "DM")
        self.assertEqual(ISOCountry.DM.numeric, 212)
        
        self.assertEqual(ISOCountry.DO, 214)
        self.assertEqual(ISOCountry.DO, "DO")
        self.assertEqual(ISOCountry.DO, "DOM")
        self.assertEqual(ISOCountry.DO, "Dominican Republic (the)")
        self.assertEqual(ISOCountry.DO, "DOMINICAN REPUBLIC (THE)")
        self.assertEqual(ISOCountry.DO, "the Dominican Republic")
        self.assertEqual(ISOCountry.DO, "THE DOMINICAN REPUBLIC")
        self.assertEqual(str(ISOCountry.DO), "DO")
        self.assertEqual(ISOCountry.DO.numeric, 214)
        
        
        
        self.assertEqual(ISOCountry.DZ, 12)
        self.assertEqual(ISOCountry.DZ, "DZ")
        self.assertEqual(ISOCountry.DZ, "DZA")
        self.assertEqual(ISOCountry.DZ, "Algeria")
        self.assertEqual(ISOCountry.DZ, "ALGERIA")
        self.assertEqual(ISOCountry.DZ, "the People's Democratic Republic of Algeria")
        self.assertEqual(ISOCountry.DZ, "THE PEOPLE'S DEMOCRATIC REPUBLIC OF ALGERIA")
        self.assertEqual(str(ISOCountry.DZ), "DZ")
        self.assertEqual(ISOCountry.DZ.numeric, 12)
        
        
        self.assertEqual(ISOCountry.EC, 218)
        self.assertEqual(ISOCountry.EC, "EC")
        self.assertEqual(ISOCountry.EC, "ECU")
        self.assertEqual(ISOCountry.EC, "Ecuador")
        self.assertEqual(ISOCountry.EC, "ECUADOR")
        self.assertEqual(ISOCountry.EC, "the Republic of Ecuador")
        self.assertEqual(ISOCountry.EC, "THE REPUBLIC OF ECUADOR")
        self.assertEqual(str(ISOCountry.EC), "EC")
        self.assertEqual(ISOCountry.EC.numeric, 218)
        
        self.assertEqual(ISOCountry.EE, 233)
        self.assertEqual(ISOCountry.EE, "EE")
        self.assertEqual(ISOCountry.EE, "EST")
        self.assertEqual(ISOCountry.EE, "Estonia")
        self.assertEqual(ISOCountry.EE, "ESTONIA")
        self.assertEqual(ISOCountry.EE, "the Republic of Estonia")
        self.assertEqual(ISOCountry.EE, "THE REPUBLIC OF ESTONIA")
        self.assertEqual(str(ISOCountry.EE), "EE")
        self.assertEqual(ISOCountry.EE.numeric, 233)
        
        
        self.assertEqual(ISOCountry.EG, 818)
        self.assertEqual(ISOCountry.EG, "EG")
        self.assertEqual(ISOCountry.EG, "EGY")
        self.assertEqual(ISOCountry.EG, "Egypt")
        self.assertEqual(ISOCountry.EG, "EGYPT")
        self.assertEqual(ISOCountry.EG, "the Arab Republic of Egypt")
        self.assertEqual(ISOCountry.EG, "THE ARAB REPUBLIC OF EGYPT")
        self.assertEqual(str(ISOCountry.EG), "EG")
        self.assertEqual(ISOCountry.EG.numeric, 818)
        
        self.assertEqual(ISOCountry.EH, 732)
        self.assertEqual(ISOCountry.EH, "EH")
        self.assertEqual(ISOCountry.EH, "ESH")
        self.assertEqual(ISOCountry.EH, "Western Sahara*")
        self.assertEqual(ISOCountry.EH, "WESTERN SAHARA*")
        
        
        
        
        self.assertEqual(ISOCountry.ER, 232)
        self.assertEqual(ISOCountry.ER, "ER")
        self.assertEqual(ISOCountry.ER, "ERI")
        self.assertEqual(ISOCountry.ER, "Eritrea")
        self.assertEqual(ISOCountry.ER, "ERITREA")
        self.assertEqual(ISOCountry.ER, "the State of Eritrea")
        self.assertEqual(ISOCountry.ER, "THE STATE OF ERITREA")
        self.assertEqual(str(ISOCountry.ER), "ER")
        self.assertEqual(ISOCountry.ER.numeric, 232)
        
        self.assertEqual(ISOCountry.ES, 724)
        self.assertEqual(ISOCountry.ES, "ES")
        self.assertEqual(ISOCountry.ES, "ESP")
        self.assertEqual(ISOCountry.ES, "Spain")
        self.assertEqual(ISOCountry.ES, "SPAIN")
        self.assertEqual(ISOCountry.ES, "the Kingdom of Spain")
        self.assertEqual(ISOCountry.ES, "THE KINGDOM OF SPAIN")
        self.assertEqual(str(ISOCountry.ES), "ES")
        self.assertEqual(ISOCountry.ES.numeric, 724)
        
        self.assertEqual(ISOCountry.ET, 231)
        self.assertEqual(ISOCountry.ET, "ET")
        self.assertEqual(ISOCountry.ET, "ETH")
        self.assertEqual(ISOCountry.ET, "Ethiopia")
        self.assertEqual(ISOCountry.ET, "ETHIOPIA")
        self.assertEqual(ISOCountry.ET, "the Federal Democratic Republic of Ethiopia")
        self.assertEqual(ISOCountry.ET, "THE FEDERAL DEMOCRATIC REPUBLIC OF ETHIOPIA")
        self.assertEqual(str(ISOCountry.ET), "ET")
        self.assertEqual(ISOCountry.ET.numeric, 231)
        
        
        
        
        
        self.assertEqual(ISOCountry.FI, 246)
        self.assertEqual(ISOCountry.FI, "FI")
        self.assertEqual(ISOCountry.FI, "FIN")
        self.assertEqual(ISOCountry.FI, "Finland")
        self.assertEqual(ISOCountry.FI, "FINLAND")
        self.assertEqual(ISOCountry.FI, "the Republic of Finland")
        self.assertEqual(ISOCountry.FI, "THE REPUBLIC OF FINLAND")
        self.assertEqual(str(ISOCountry.FI), "FI")
        self.assertEqual(ISOCountry.FI.numeric, 246)
        
        self.assertEqual(ISOCountry.FJ, 242)
        self.assertEqual(ISOCountry.FJ, "FJ")
        self.assertEqual(ISOCountry.FJ, "FJI")
        self.assertEqual(ISOCountry.FJ, "Fiji")
        self.assertEqual(ISOCountry.FJ, "FIJI")
        self.assertEqual(ISOCountry.FJ, "the Republic of Fiji")
        self.assertEqual(ISOCountry.FJ, "THE REPUBLIC OF FIJI")
        self.assertEqual(str(ISOCountry.FJ), "FJ")
        self.assertEqual(ISOCountry.FJ.numeric, 242)
        
        self.assertEqual(ISOCountry.FK, 238)
        self.assertEqual(ISOCountry.FK, "FK")
        self.assertEqual(ISOCountry.FK, "FLK")
        self.assertEqual(ISOCountry.FK, "Falkland Islands (the) [Malvinas]")
        self.assertEqual(ISOCountry.FK, "FALKLAND ISLANDS (THE) [MALVINAS]")
        
        
        
        self.assertEqual(ISOCountry.FM, 583)
        self.assertEqual(ISOCountry.FM, "FM")
        self.assertEqual(ISOCountry.FM, "FSM")
        self.assertEqual(ISOCountry.FM, "Micronesia (Federated States of)")
        self.assertEqual(ISOCountry.FM, "MICRONESIA (FEDERATED STATES OF)")
        self.assertEqual(ISOCountry.FM, "the Federated States of Micronesia")
        self.assertEqual(ISOCountry.FM, "THE FEDERATED STATES OF MICRONESIA")
        self.assertEqual(str(ISOCountry.FM), "FM")
        self.assertEqual(ISOCountry.FM.numeric, 583)
        
        self.assertEqual(ISOCountry.FO, 234)
        self.assertEqual(ISOCountry.FO, "FO")
        self.assertEqual(ISOCountry.FO, "FRO")
        self.assertEqual(ISOCountry.FO, "Faroe Islands (the)")
        self.assertEqual(ISOCountry.FO, "FAROE ISLANDS (THE)")
        
        
        
        self.assertEqual(ISOCountry.FR, 250)
        self.assertEqual(ISOCountry.FR, "FR")
        self.assertEqual(ISOCountry.FR, "FRA")
        self.assertEqual(ISOCountry.FR, "France")
        self.assertEqual(ISOCountry.FR, "FRANCE")
        self.assertEqual(ISOCountry.FR, "the French Republic")
        self.assertEqual(ISOCountry.FR, "THE FRENCH REPUBLIC")
        self.assertEqual(str(ISOCountry.FR), "FR")
        self.assertEqual(ISOCountry.FR.numeric, 250)
        
        
        self.assertEqual(ISOCountry.GA, 266)
        self.assertEqual(ISOCountry.GA, "GA")
        self.assertEqual(ISOCountry.GA, "GAB")
        self.assertEqual(ISOCountry.GA, "Gabon")
        self.assertEqual(ISOCountry.GA, "GABON")
        self.assertEqual(ISOCountry.GA, "the Gabonese Republic")
        self.assertEqual(ISOCountry.GA, "THE GABONESE REPUBLIC")
        self.assertEqual(str(ISOCountry.GA), "GA")
        self.assertEqual(ISOCountry.GA.numeric, 266)
        
        self.assertEqual(ISOCountry.GB, 826)
        self.assertEqual(ISOCountry.GB, "GB")
        self.assertEqual(ISOCountry.GB, "GBR")
        self.assertEqual(ISOCountry.GB, "United Kingdom of Great Britain and Northern Ireland (the)")
        self.assertEqual(ISOCountry.GB, "UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND (THE)")
        self.assertEqual(ISOCountry.GB, "the United Kingdom of Great Britain and Northern Ireland")
        self.assertEqual(ISOCountry.GB, "THE UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND")
        self.assertEqual(str(ISOCountry.GB), "GB")
        self.assertEqual(ISOCountry.GB.numeric, 826)
        
        
        self.assertEqual(ISOCountry.GD, 308)
        self.assertEqual(ISOCountry.GD, "GD")
        self.assertEqual(ISOCountry.GD, "GRD")
        self.assertEqual(ISOCountry.GD, "Grenada")
        self.assertEqual(ISOCountry.GD, "GRENADA")
        
        
        
        self.assertEqual(ISOCountry.GE, 268)
        self.assertEqual(ISOCountry.GE, "GE")
        self.assertEqual(ISOCountry.GE, "GEO")
        self.assertEqual(ISOCountry.GE, "Georgia")
        self.assertEqual(ISOCountry.GE, "GEORGIA")
        
        
        self.assertEqual(ISOCountry.GF, 254)
        self.assertEqual(ISOCountry.GF, "GF")
        self.assertEqual(ISOCountry.GF, "GUF")
        self.assertEqual(ISOCountry.GF, "French Guiana")
        self.assertEqual(ISOCountry.GF, "FRENCH GUIANA")
        
        
        self.assertEqual(ISOCountry.GG, 831)
        self.assertEqual(ISOCountry.GG, "GG")
        self.assertEqual(ISOCountry.GG, "GGY")
        self.assertEqual(ISOCountry.GG, "Guernsey")
        self.assertEqual(ISOCountry.GG, "GUERNSEY")
        
        
        self.assertEqual(ISOCountry.GH, 288)
        self.assertEqual(ISOCountry.GH, "GH")
        self.assertEqual(ISOCountry.GH, "GHA")
        self.assertEqual(ISOCountry.GH, "Ghana")
        self.assertEqual(ISOCountry.GH, "GHANA")
        self.assertEqual(ISOCountry.GH, "the Republic of Ghana")
        self.assertEqual(ISOCountry.GH, "THE REPUBLIC OF GHANA")
        self.assertEqual(str(ISOCountry.GH), "GH")
        self.assertEqual(ISOCountry.GH.numeric, 288)
        
        self.assertEqual(ISOCountry.GI, 292)
        self.assertEqual(ISOCountry.GI, "GI")
        self.assertEqual(ISOCountry.GI, "GIB")
        self.assertEqual(ISOCountry.GI, "Gibraltar")
        self.assertEqual(ISOCountry.GI, "GIBRALTAR")
        
        
        self.assertEqual(ISOCountry.GL, 304)
        self.assertEqual(ISOCountry.GL, "GL")
        self.assertEqual(ISOCountry.GL, "GRL")
        self.assertEqual(ISOCountry.GL, "Greenland")
        self.assertEqual(ISOCountry.GL, "GREENLAND")
        
        
        self.assertEqual(ISOCountry.GM, 270)
        self.assertEqual(ISOCountry.GM, "GM")
        self.assertEqual(ISOCountry.GM, "GMB")
        self.assertEqual(ISOCountry.GM, "Gambia (the)")
        self.assertEqual(ISOCountry.GM, "GAMBIA (THE)")
        self.assertEqual(ISOCountry.GM, "the Republic of the Gambia")
        self.assertEqual(ISOCountry.GM, "THE REPUBLIC OF THE GAMBIA")
        self.assertEqual(str(ISOCountry.GM), "GM")
        self.assertEqual(ISOCountry.GM.numeric, 270)
        
        self.assertEqual(ISOCountry.GN, 324)
        self.assertEqual(ISOCountry.GN, "GN")
        self.assertEqual(ISOCountry.GN, "GIN")
        self.assertEqual(ISOCountry.GN, "Guinea")
        self.assertEqual(ISOCountry.GN, "GUINEA")
        self.assertEqual(ISOCountry.GN, "the Republic of Guinea")
        self.assertEqual(ISOCountry.GN, "THE REPUBLIC OF GUINEA")
        self.assertEqual(str(ISOCountry.GN), "GN")
        self.assertEqual(ISOCountry.GN.numeric, 324)
        
        self.assertEqual(ISOCountry.GP, 312)
        self.assertEqual(ISOCountry.GP, "GP")
        self.assertEqual(ISOCountry.GP, "GLP")
        self.assertEqual(ISOCountry.GP, "Guadeloupe")
        self.assertEqual(ISOCountry.GP, "GUADELOUPE")
        
        
        self.assertEqual(ISOCountry.GQ, 226)
        self.assertEqual(ISOCountry.GQ, "GQ")
        self.assertEqual(ISOCountry.GQ, "GNQ")
        self.assertEqual(ISOCountry.GQ, "Equatorial Guinea")
        self.assertEqual(ISOCountry.GQ, "EQUATORIAL GUINEA")
        self.assertEqual(ISOCountry.GQ, "the Republic of Equatorial Guinea")
        self.assertEqual(ISOCountry.GQ, "THE REPUBLIC OF EQUATORIAL GUINEA")
        self.assertEqual(str(ISOCountry.GQ), "GQ")
        self.assertEqual(ISOCountry.GQ.numeric, 226)
        
        self.assertEqual(ISOCountry.GR, 300)
        self.assertEqual(ISOCountry.GR, "GR")
        self.assertEqual(ISOCountry.GR, "GRC")
        self.assertEqual(ISOCountry.GR, "Greece")
        self.assertEqual(ISOCountry.GR, "GREECE")
        self.assertEqual(ISOCountry.GR, "the Hellenic Republic")
        self.assertEqual(ISOCountry.GR, "THE HELLENIC REPUBLIC")
        self.assertEqual(str(ISOCountry.GR), "GR")
        self.assertEqual(ISOCountry.GR.numeric, 300)
        
        self.assertEqual(ISOCountry.GS, 239)
        self.assertEqual(ISOCountry.GS, "GS")
        self.assertEqual(ISOCountry.GS, "SGS")
        self.assertEqual(ISOCountry.GS, "South Georgia and the South Sandwich Islands")
        self.assertEqual(ISOCountry.GS, "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS")
        
        
        self.assertEqual(ISOCountry.GT, 320)
        self.assertEqual(ISOCountry.GT, "GT")
        self.assertEqual(ISOCountry.GT, "GTM")
        self.assertEqual(ISOCountry.GT, "Guatemala")
        self.assertEqual(ISOCountry.GT, "GUATEMALA")
        self.assertEqual(ISOCountry.GT, "the Republic of Guatemala")
        self.assertEqual(ISOCountry.GT, "THE REPUBLIC OF GUATEMALA")
        self.assertEqual(str(ISOCountry.GT), "GT")
        self.assertEqual(ISOCountry.GT.numeric, 320)
        
        self.assertEqual(ISOCountry.GU, 316)
        self.assertEqual(ISOCountry.GU, "GU")
        self.assertEqual(ISOCountry.GU, "GUM")
        self.assertEqual(ISOCountry.GU, "Guam")
        self.assertEqual(ISOCountry.GU, "GUAM")
        
        
        self.assertEqual(ISOCountry.GW, 624)
        self.assertEqual(ISOCountry.GW, "GW")
        self.assertEqual(ISOCountry.GW, "GNB")
        self.assertEqual(ISOCountry.GW, "Guinea-Bissau")
        self.assertEqual(ISOCountry.GW, "GUINEA-BISSAU")
        self.assertEqual(ISOCountry.GW, "the Republic of Guinea-Bissau")
        self.assertEqual(ISOCountry.GW, "THE REPUBLIC OF GUINEA-BISSAU")
        self.assertEqual(str(ISOCountry.GW), "GW")
        self.assertEqual(ISOCountry.GW.numeric, 624)
        
        self.assertEqual(ISOCountry.GY, 328)
        self.assertEqual(ISOCountry.GY, "GY")
        self.assertEqual(ISOCountry.GY, "GUY")
        self.assertEqual(ISOCountry.GY, "Guyana")
        self.assertEqual(ISOCountry.GY, "GUYANA")
        self.assertEqual(ISOCountry.GY, "the Co-operative Republic of Guyana")
        self.assertEqual(ISOCountry.GY, "THE CO-OPERATIVE REPUBLIC OF GUYANA")
        self.assertEqual(str(ISOCountry.GY), "GY")
        self.assertEqual(ISOCountry.GY.numeric, 328)
        
        self.assertEqual(ISOCountry.HK, 344)
        self.assertEqual(ISOCountry.HK, "HK")
        self.assertEqual(ISOCountry.HK, "HKG")
        self.assertEqual(ISOCountry.HK, "Hong Kong")
        self.assertEqual(ISOCountry.HK, "HONG KONG")
        self.assertEqual(ISOCountry.HK, "the Hong Kong Special Administrative Region of China")
        self.assertEqual(ISOCountry.HK, "THE HONG KONG SPECIAL ADMINISTRATIVE REGION OF CHINA")
        self.assertEqual(str(ISOCountry.HK), "HK")
        self.assertEqual(ISOCountry.HK.numeric, 344)
        
        self.assertEqual(ISOCountry.HM, 334)
        self.assertEqual(ISOCountry.HM, "HM")
        self.assertEqual(ISOCountry.HM, "HMD")
        self.assertEqual(ISOCountry.HM, "Heard Island and McDonald Islands")
        self.assertEqual(ISOCountry.HM, "HEARD ISLAND AND MCDONALD ISLANDS")
        
        
        self.assertEqual(ISOCountry.HN, 340)
        self.assertEqual(ISOCountry.HN, "HN")
        self.assertEqual(ISOCountry.HN, "HND")
        self.assertEqual(ISOCountry.HN, "Honduras")
        self.assertEqual(ISOCountry.HN, "HONDURAS")
        self.assertEqual(ISOCountry.HN, "the Republic of Honduras")
        self.assertEqual(ISOCountry.HN, "THE REPUBLIC OF HONDURAS")
        self.assertEqual(str(ISOCountry.HN), "HN")
        self.assertEqual(ISOCountry.HN.numeric, 340)
        
        self.assertEqual(ISOCountry.HR, 191)
        self.assertEqual(ISOCountry.HR, "HR")
        self.assertEqual(ISOCountry.HR, "HRV")
        self.assertEqual(ISOCountry.HR, "Croatia")
        self.assertEqual(ISOCountry.HR, "CROATIA")
        self.assertEqual(ISOCountry.HR, "the Republic of Croatia")
        self.assertEqual(ISOCountry.HR, "THE REPUBLIC OF CROATIA")
        self.assertEqual(str(ISOCountry.HR), "HR")
        self.assertEqual(ISOCountry.HR.numeric, 191)
        
        self.assertEqual(ISOCountry.HT, 332)
        self.assertEqual(ISOCountry.HT, "HT")
        self.assertEqual(ISOCountry.HT, "HTI")
        self.assertEqual(ISOCountry.HT, "Haiti")
        self.assertEqual(ISOCountry.HT, "HAITI")
        self.assertEqual(ISOCountry.HT, "the Republic of Haiti")
        self.assertEqual(ISOCountry.HT, "THE REPUBLIC OF HAITI")
        self.assertEqual(str(ISOCountry.HT), "HT")
        self.assertEqual(ISOCountry.HT.numeric, 332)
        
        self.assertEqual(ISOCountry.HU, 348)
        self.assertEqual(ISOCountry.HU, "HU")
        self.assertEqual(ISOCountry.HU, "HUN")
        self.assertEqual(ISOCountry.HU, "Hungary")
        self.assertEqual(ISOCountry.HU, "HUNGARY")
        
        
        
        
        
        self.assertEqual(ISOCountry.ID, 360)
        self.assertEqual(ISOCountry.ID, "ID")
        self.assertEqual(ISOCountry.ID, "IDN")
        self.assertEqual(ISOCountry.ID, "Indonesia")
        self.assertEqual(ISOCountry.ID, "INDONESIA")
        self.assertEqual(ISOCountry.ID, "the Republic of Indonesia")
        self.assertEqual(ISOCountry.ID, "THE REPUBLIC OF INDONESIA")
        self.assertEqual(str(ISOCountry.ID), "ID")
        self.assertEqual(ISOCountry.ID.numeric, 360)
        
        self.assertEqual(ISOCountry.IE, 372)
        self.assertEqual(ISOCountry.IE, "IE")
        self.assertEqual(ISOCountry.IE, "IRL")
        self.assertEqual(ISOCountry.IE, "Ireland")
        self.assertEqual(ISOCountry.IE, "IRELAND")
        
        
        self.assertEqual(ISOCountry.IL, 376)
        self.assertEqual(ISOCountry.IL, "IL")
        self.assertEqual(ISOCountry.IL, "ISR")
        self.assertEqual(ISOCountry.IL, "Israel")
        self.assertEqual(ISOCountry.IL, "ISRAEL")
        self.assertEqual(ISOCountry.IL, "the State of Israel")
        self.assertEqual(ISOCountry.IL, "THE STATE OF ISRAEL")
        self.assertEqual(str(ISOCountry.IL), "IL")
        self.assertEqual(ISOCountry.IL.numeric, 376)
        
        self.assertEqual(ISOCountry.IM, 833)
        self.assertEqual(ISOCountry.IM, "IM")
        self.assertEqual(ISOCountry.IM, "IMN")
        self.assertEqual(ISOCountry.IM, "Isle of Man")
        self.assertEqual(ISOCountry.IM, "ISLE OF MAN")
        
        
        self.assertEqual(ISOCountry.IN, 356)
        self.assertEqual(ISOCountry.IN, "IN")
        self.assertEqual(ISOCountry.IN, "IND")
        self.assertEqual(ISOCountry.IN, "India")
        self.assertEqual(ISOCountry.IN, "INDIA")
        self.assertEqual(ISOCountry.IN, "the Republic of India")
        self.assertEqual(ISOCountry.IN, "THE REPUBLIC OF INDIA")
        self.assertEqual(str(ISOCountry.IN), "IN")
        self.assertEqual(ISOCountry.IN.numeric, 356)
        
        self.assertEqual(ISOCountry.IO, 86)
        self.assertEqual(ISOCountry.IO, "IO")
        self.assertEqual(ISOCountry.IO, "IOT")
        self.assertEqual(ISOCountry.IO, "British Indian Ocean Territory (the)")
        self.assertEqual(ISOCountry.IO, "BRITISH INDIAN OCEAN TERRITORY (THE)")
        
        
        self.assertEqual(ISOCountry.IQ, 368)
        self.assertEqual(ISOCountry.IQ, "IQ")
        self.assertEqual(ISOCountry.IQ, "IRQ")
        self.assertEqual(ISOCountry.IQ, "Iraq")
        self.assertEqual(ISOCountry.IQ, "IRAQ")
        self.assertEqual(ISOCountry.IQ, "the Republic of Iraq")
        self.assertEqual(ISOCountry.IQ, "THE REPUBLIC OF IRAQ")
        self.assertEqual(str(ISOCountry.IQ), "IQ")
        self.assertEqual(ISOCountry.IQ.numeric, 368)
        
        self.assertEqual(ISOCountry.IR, 364)
        self.assertEqual(ISOCountry.IR, "IR")
        self.assertEqual(ISOCountry.IR, "IRN")
        self.assertEqual(ISOCountry.IR, "Iran (Islamic Republic of)")
        self.assertEqual(ISOCountry.IR, "IRAN (ISLAMIC REPUBLIC OF)")
        self.assertEqual(ISOCountry.IR, "the Islamic Republic of Iran")
        self.assertEqual(ISOCountry.IR, "THE ISLAMIC REPUBLIC OF IRAN")
        self.assertEqual(str(ISOCountry.IR), "IR")
        self.assertEqual(ISOCountry.IR.numeric, 364)
        
        self.assertEqual(ISOCountry.IS, 352)
        self.assertEqual(ISOCountry.IS, "IS")
        self.assertEqual(ISOCountry.IS, "ISL")
        self.assertEqual(ISOCountry.IS, "Iceland")
        self.assertEqual(ISOCountry.IS, "ICELAND")
        self.assertEqual(ISOCountry.IS, "the Republic of Iceland")
        self.assertEqual(ISOCountry.IS, "THE REPUBLIC OF ICELAND")
        self.assertEqual(str(ISOCountry.IS), "IS")
        self.assertEqual(ISOCountry.IS.numeric, 352)
        
        self.assertEqual(ISOCountry.IT, 380)
        self.assertEqual(ISOCountry.IT, "IT")
        self.assertEqual(ISOCountry.IT, "ITA")
        self.assertEqual(ISOCountry.IT, "Italy")
        self.assertEqual(ISOCountry.IT, "ITALY")
        self.assertEqual(ISOCountry.IT, "the Republic of Italy")
        self.assertEqual(ISOCountry.IT, "THE REPUBLIC OF ITALY")
        self.assertEqual(str(ISOCountry.IT), "IT")
        self.assertEqual(ISOCountry.IT.numeric, 380)
        
        
        self.assertEqual(ISOCountry.JE, 832)
        self.assertEqual(ISOCountry.JE, "JE")
        self.assertEqual(ISOCountry.JE, "JEY")
        self.assertEqual(ISOCountry.JE, "Jersey")
        self.assertEqual(ISOCountry.JE, "JERSEY")
        
        
        self.assertEqual(ISOCountry.JM, 388)
        self.assertEqual(ISOCountry.JM, "JM")
        self.assertEqual(ISOCountry.JM, "JAM")
        self.assertEqual(ISOCountry.JM, "Jamaica")
        self.assertEqual(ISOCountry.JM, "JAMAICA")
        
        
        self.assertEqual(ISOCountry.JO, 400)
        self.assertEqual(ISOCountry.JO, "JO")
        self.assertEqual(ISOCountry.JO, "JOR")
        self.assertEqual(ISOCountry.JO, "Jordan")
        self.assertEqual(ISOCountry.JO, "JORDAN")
        self.assertEqual(ISOCountry.JO, "the Hashemite Kingdom of Jordan")
        self.assertEqual(ISOCountry.JO, "THE HASHEMITE KINGDOM OF JORDAN")
        self.assertEqual(str(ISOCountry.JO), "JO")
        self.assertEqual(ISOCountry.JO.numeric, 400)
        
        self.assertEqual(ISOCountry.JP, 392)
        self.assertEqual(ISOCountry.JP, "JP")
        self.assertEqual(ISOCountry.JP, "JPN")
        self.assertEqual(ISOCountry.JP, "Japan")
        self.assertEqual(ISOCountry.JP, "JAPAN")
        
        
        
        self.assertEqual(ISOCountry.KE, 404)
        self.assertEqual(ISOCountry.KE, "KE")
        self.assertEqual(ISOCountry.KE, "KEN")
        self.assertEqual(ISOCountry.KE, "Kenya")
        self.assertEqual(ISOCountry.KE, "KENYA")
        self.assertEqual(ISOCountry.KE, "the Republic of Kenya")
        self.assertEqual(ISOCountry.KE, "THE REPUBLIC OF KENYA")
        self.assertEqual(str(ISOCountry.KE), "KE")
        self.assertEqual(ISOCountry.KE.numeric, 404)
        
        self.assertEqual(ISOCountry.KG, 417)
        self.assertEqual(ISOCountry.KG, "KG")
        self.assertEqual(ISOCountry.KG, "KGZ")
        self.assertEqual(ISOCountry.KG, "Kyrgyzstan")
        self.assertEqual(ISOCountry.KG, "KYRGYZSTAN")
        self.assertEqual(ISOCountry.KG, "the Kyrgyz Republic")
        self.assertEqual(ISOCountry.KG, "THE KYRGYZ REPUBLIC")
        self.assertEqual(str(ISOCountry.KG), "KG")
        self.assertEqual(ISOCountry.KG.numeric, 417)
        
        self.assertEqual(ISOCountry.KH, 116)
        self.assertEqual(ISOCountry.KH, "KH")
        self.assertEqual(ISOCountry.KH, "KHM")
        self.assertEqual(ISOCountry.KH, "Cambodia")
        self.assertEqual(ISOCountry.KH, "CAMBODIA")
        self.assertEqual(ISOCountry.KH, "the Kingdom of Cambodia")
        self.assertEqual(ISOCountry.KH, "THE KINGDOM OF CAMBODIA")
        self.assertEqual(str(ISOCountry.KH), "KH")
        self.assertEqual(ISOCountry.KH.numeric, 116)
        
        self.assertEqual(ISOCountry.KI, 296)
        self.assertEqual(ISOCountry.KI, "KI")
        self.assertEqual(ISOCountry.KI, "KIR")
        self.assertEqual(ISOCountry.KI, "Kiribati")
        self.assertEqual(ISOCountry.KI, "KIRIBATI")
        self.assertEqual(ISOCountry.KI, "the Republic of Kiribati")
        self.assertEqual(ISOCountry.KI, "THE REPUBLIC OF KIRIBATI")
        self.assertEqual(str(ISOCountry.KI), "KI")
        self.assertEqual(ISOCountry.KI.numeric, 296)
        
        self.assertEqual(ISOCountry.KM, 174)
        self.assertEqual(ISOCountry.KM, "KM")
        self.assertEqual(ISOCountry.KM, "COM")
        self.assertEqual(ISOCountry.KM, "Comoros (the)")
        self.assertEqual(ISOCountry.KM, "COMOROS (THE)")
        self.assertEqual(ISOCountry.KM, "the Union of the Comoros")
        self.assertEqual(ISOCountry.KM, "THE UNION OF THE COMOROS")
        self.assertEqual(str(ISOCountry.KM), "KM")
        self.assertEqual(ISOCountry.KM.numeric, 174)
        
        self.assertEqual(ISOCountry.KN, 659)
        self.assertEqual(ISOCountry.KN, "KN")
        self.assertEqual(ISOCountry.KN, "KNA")
        self.assertEqual(ISOCountry.KN, "Saint Kitts and Nevis")
        self.assertEqual(ISOCountry.KN, "SAINT KITTS AND NEVIS")
        
        
        self.assertEqual(ISOCountry.KP, 408)
        self.assertEqual(ISOCountry.KP, "KP")
        self.assertEqual(ISOCountry.KP, "PRK")
        self.assertEqual(ISOCountry.KP, "Korea (the Democratic People's Republic of)")
        self.assertEqual(ISOCountry.KP, "KOREA (THE DEMOCRATIC PEOPLE'S REPUBLIC OF)")
        self.assertEqual(ISOCountry.KP, "the Democratic People's Republic of Korea")
        self.assertEqual(ISOCountry.KP, "THE DEMOCRATIC PEOPLE'S REPUBLIC OF KOREA")
        self.assertEqual(str(ISOCountry.KP), "KP")
        self.assertEqual(ISOCountry.KP.numeric, 408)
        
        self.assertEqual(ISOCountry.KR, 410)
        self.assertEqual(ISOCountry.KR, "KR")
        self.assertEqual(ISOCountry.KR, "KOR")
        self.assertEqual(ISOCountry.KR, "Korea (the Republic of)")
        self.assertEqual(ISOCountry.KR, "KOREA (THE REPUBLIC OF)")
        self.assertEqual(ISOCountry.KR, "the Republic of Korea")
        self.assertEqual(ISOCountry.KR, "THE REPUBLIC OF KOREA")
        self.assertEqual(str(ISOCountry.KR), "KR")
        self.assertEqual(ISOCountry.KR.numeric, 410)
        
        self.assertEqual(ISOCountry.KW, 414)
        self.assertEqual(ISOCountry.KW, "KW")
        self.assertEqual(ISOCountry.KW, "KWT")
        self.assertEqual(ISOCountry.KW, "Kuwait")
        self.assertEqual(ISOCountry.KW, "KUWAIT")
        self.assertEqual(ISOCountry.KW, "the State of Kuwait")
        self.assertEqual(ISOCountry.KW, "THE STATE OF KUWAIT")
        self.assertEqual(str(ISOCountry.KW), "KW")
        self.assertEqual(ISOCountry.KW.numeric, 414)
        
        self.assertEqual(ISOCountry.KY, 136)
        self.assertEqual(ISOCountry.KY, "KY")
        self.assertEqual(ISOCountry.KY, "CYM")
        self.assertEqual(ISOCountry.KY, "Cayman Islands (the)")
        self.assertEqual(ISOCountry.KY, "CAYMAN ISLANDS (THE)")
        
        
        self.assertEqual(ISOCountry.KZ, 398)
        self.assertEqual(ISOCountry.KZ, "KZ")
        self.assertEqual(ISOCountry.KZ, "KAZ")
        self.assertEqual(ISOCountry.KZ, "Kazakhstan")
        self.assertEqual(ISOCountry.KZ, "KAZAKHSTAN")
        self.assertEqual(ISOCountry.KZ, "the Republic of Kazakhstan")
        self.assertEqual(ISOCountry.KZ, "THE REPUBLIC OF KAZAKHSTAN")
        self.assertEqual(str(ISOCountry.KZ), "KZ")
        self.assertEqual(ISOCountry.KZ.numeric, 398)
        
        self.assertEqual(ISOCountry.LA, 418)
        self.assertEqual(ISOCountry.LA, "LA")
        self.assertEqual(ISOCountry.LA, "LAO")
        self.assertEqual(ISOCountry.LA, "Lao People's Democratic Republic (the)")
        self.assertEqual(ISOCountry.LA, "LAO PEOPLE'S DEMOCRATIC REPUBLIC (THE)")
        self.assertEqual(ISOCountry.LA, "the Lao People's Democratic Republic")
        self.assertEqual(ISOCountry.LA, "THE LAO PEOPLE'S DEMOCRATIC REPUBLIC")
        self.assertEqual(str(ISOCountry.LA), "LA")
        self.assertEqual(ISOCountry.LA.numeric, 418)
        
        self.assertEqual(ISOCountry.LB, 422)
        self.assertEqual(ISOCountry.LB, "LB")
        self.assertEqual(ISOCountry.LB, "LBN")
        self.assertEqual(ISOCountry.LB, "Lebanon")
        self.assertEqual(ISOCountry.LB, "LEBANON")
        self.assertEqual(ISOCountry.LB, "the Lebanese Republic")
        self.assertEqual(ISOCountry.LB, "THE LEBANESE REPUBLIC")
        self.assertEqual(str(ISOCountry.LB), "LB")
        self.assertEqual(ISOCountry.LB.numeric, 422)
        
        self.assertEqual(ISOCountry.LC, 662)
        self.assertEqual(ISOCountry.LC, "LC")
        self.assertEqual(ISOCountry.LC, "LCA")
        self.assertEqual(ISOCountry.LC, "Saint Lucia")
        self.assertEqual(ISOCountry.LC, "SAINT LUCIA")
        
        
        
        self.assertEqual(ISOCountry.LI, 438)
        self.assertEqual(ISOCountry.LI, "LI")
        self.assertEqual(ISOCountry.LI, "LIE")
        self.assertEqual(ISOCountry.LI, "Liechtenstein")
        self.assertEqual(ISOCountry.LI, "LIECHTENSTEIN")
        self.assertEqual(ISOCountry.LI, "the Principality of Liechtenstein")
        self.assertEqual(ISOCountry.LI, "THE PRINCIPALITY OF LIECHTENSTEIN")
        self.assertEqual(str(ISOCountry.LI), "LI")
        self.assertEqual(ISOCountry.LI.numeric, 438)
        
        self.assertEqual(ISOCountry.LK, 144)
        self.assertEqual(ISOCountry.LK, "LK")
        self.assertEqual(ISOCountry.LK, "LKA")
        self.assertEqual(ISOCountry.LK, "Sri Lanka")
        self.assertEqual(ISOCountry.LK, "SRI LANKA")
        self.assertEqual(ISOCountry.LK, "the Democratic Socialist Republic of Sri Lanka")
        self.assertEqual(ISOCountry.LK, "THE DEMOCRATIC SOCIALIST REPUBLIC OF SRI LANKA")
        self.assertEqual(str(ISOCountry.LK), "LK")
        self.assertEqual(ISOCountry.LK.numeric, 144)
        
        self.assertEqual(ISOCountry.LR, 430)
        self.assertEqual(ISOCountry.LR, "LR")
        self.assertEqual(ISOCountry.LR, "LBR")
        self.assertEqual(ISOCountry.LR, "Liberia")
        self.assertEqual(ISOCountry.LR, "LIBERIA")
        self.assertEqual(ISOCountry.LR, "the Republic of Liberia")
        self.assertEqual(ISOCountry.LR, "THE REPUBLIC OF LIBERIA")
        self.assertEqual(str(ISOCountry.LR), "LR")
        self.assertEqual(ISOCountry.LR.numeric, 430)
        
        self.assertEqual(ISOCountry.LS, 426)
        self.assertEqual(ISOCountry.LS, "LS")
        self.assertEqual(ISOCountry.LS, "LSO")
        self.assertEqual(ISOCountry.LS, "Lesotho")
        self.assertEqual(ISOCountry.LS, "LESOTHO")
        self.assertEqual(ISOCountry.LS, "the Kingdom of Lesotho")
        self.assertEqual(ISOCountry.LS, "THE KINGDOM OF LESOTHO")
        self.assertEqual(str(ISOCountry.LS), "LS")
        self.assertEqual(ISOCountry.LS.numeric, 426)
        
        self.assertEqual(ISOCountry.LT, 440)
        self.assertEqual(ISOCountry.LT, "LT")
        self.assertEqual(ISOCountry.LT, "LTU")
        self.assertEqual(ISOCountry.LT, "Lithuania")
        self.assertEqual(ISOCountry.LT, "LITHUANIA")
        self.assertEqual(ISOCountry.LT, "the Republic of Lithuania")
        self.assertEqual(ISOCountry.LT, "THE REPUBLIC OF LITHUANIA")
        self.assertEqual(str(ISOCountry.LT), "LT")
        self.assertEqual(ISOCountry.LT.numeric, 440)
        
        self.assertEqual(ISOCountry.LU, 442)
        self.assertEqual(ISOCountry.LU, "LU")
        self.assertEqual(ISOCountry.LU, "LUX")
        self.assertEqual(ISOCountry.LU, "Luxembourg")
        self.assertEqual(ISOCountry.LU, "LUXEMBOURG")
        self.assertEqual(ISOCountry.LU, "the Grand Duchy of Luxembourg")
        self.assertEqual(ISOCountry.LU, "THE GRAND DUCHY OF LUXEMBOURG")
        self.assertEqual(str(ISOCountry.LU), "LU")
        self.assertEqual(ISOCountry.LU.numeric, 442)
        
        self.assertEqual(ISOCountry.LV, 428)
        self.assertEqual(ISOCountry.LV, "LV")
        self.assertEqual(ISOCountry.LV, "LVA")
        self.assertEqual(ISOCountry.LV, "Latvia")
        self.assertEqual(ISOCountry.LV, "LATVIA")
        self.assertEqual(ISOCountry.LV, "the Republic of Latvia")
        self.assertEqual(ISOCountry.LV, "THE REPUBLIC OF LATVIA")
        self.assertEqual(str(ISOCountry.LV), "LV")
        self.assertEqual(ISOCountry.LV.numeric, 428)
        
        self.assertEqual(ISOCountry.LY, 434)
        self.assertEqual(ISOCountry.LY, "LY")
        self.assertEqual(ISOCountry.LY, "LBY")
        self.assertEqual(ISOCountry.LY, "Libya")
        self.assertEqual(ISOCountry.LY, "LIBYA")
        self.assertEqual(ISOCountry.LY, "the State of Libya")
        self.assertEqual(ISOCountry.LY, "THE STATE OF LIBYA")
        self.assertEqual(str(ISOCountry.LY), "LY")
        self.assertEqual(ISOCountry.LY.numeric, 434)
        
        self.assertEqual(ISOCountry.MA, 504)
        self.assertEqual(ISOCountry.MA, "MA")
        self.assertEqual(ISOCountry.MA, "MAR")
        self.assertEqual(ISOCountry.MA, "Morocco")
        self.assertEqual(ISOCountry.MA, "MOROCCO")
        self.assertEqual(ISOCountry.MA, "the Kingdom of Morocco")
        self.assertEqual(ISOCountry.MA, "THE KINGDOM OF MOROCCO")
        self.assertEqual(str(ISOCountry.MA), "MA")
        self.assertEqual(ISOCountry.MA.numeric, 504)
        
        self.assertEqual(ISOCountry.MC, 492)
        self.assertEqual(ISOCountry.MC, "MC")
        self.assertEqual(ISOCountry.MC, "MCO")
        self.assertEqual(ISOCountry.MC, "Monaco")
        self.assertEqual(ISOCountry.MC, "MONACO")
        self.assertEqual(ISOCountry.MC, "the Principality of Monaco")
        self.assertEqual(ISOCountry.MC, "THE PRINCIPALITY OF MONACO")
        self.assertEqual(str(ISOCountry.MC), "MC")
        self.assertEqual(ISOCountry.MC.numeric, 492)
        
        self.assertEqual(ISOCountry.MD, 498)
        self.assertEqual(ISOCountry.MD, "MD")
        self.assertEqual(ISOCountry.MD, "MDA")
        self.assertEqual(ISOCountry.MD, "Moldova (the Republic of)")
        self.assertEqual(ISOCountry.MD, "MOLDOVA (THE REPUBLIC OF)")
        self.assertEqual(ISOCountry.MD, "the Republic of Moldova")
        self.assertEqual(ISOCountry.MD, "THE REPUBLIC OF MOLDOVA")
        self.assertEqual(str(ISOCountry.MD), "MD")
        self.assertEqual(ISOCountry.MD.numeric, 498)
        
        self.assertEqual(ISOCountry.ME, 499)
        self.assertEqual(ISOCountry.ME, "ME")
        self.assertEqual(ISOCountry.ME, "MNE")
        self.assertEqual(ISOCountry.ME, "Montenegro")
        self.assertEqual(ISOCountry.ME, "MONTENEGRO")
        
        
        self.assertEqual(ISOCountry.MF, 663)
        self.assertEqual(ISOCountry.MF, "MF")
        self.assertEqual(ISOCountry.MF, "MAF")
        self.assertEqual(ISOCountry.MF, "Saint Martin (French part)")
        self.assertEqual(ISOCountry.MF, "SAINT MARTIN (FRENCH PART)")
        
        
        self.assertEqual(ISOCountry.MG, 450)
        self.assertEqual(ISOCountry.MG, "MG")
        self.assertEqual(ISOCountry.MG, "MDG")
        self.assertEqual(ISOCountry.MG, "Madagascar")
        self.assertEqual(ISOCountry.MG, "MADAGASCAR")
        self.assertEqual(ISOCountry.MG, "the Republic of Madagascar")
        self.assertEqual(ISOCountry.MG, "THE REPUBLIC OF MADAGASCAR")
        self.assertEqual(str(ISOCountry.MG), "MG")
        self.assertEqual(ISOCountry.MG.numeric, 450)
        
        self.assertEqual(ISOCountry.MH, 584)
        self.assertEqual(ISOCountry.MH, "MH")
        self.assertEqual(ISOCountry.MH, "MHL")
        self.assertEqual(ISOCountry.MH, "Marshall Islands (the)")
        self.assertEqual(ISOCountry.MH, "MARSHALL ISLANDS (THE)")
        self.assertEqual(ISOCountry.MH, "the Republic of the Marshall Islands")
        self.assertEqual(ISOCountry.MH, "THE REPUBLIC OF THE MARSHALL ISLANDS")
        self.assertEqual(str(ISOCountry.MH), "MH")
        self.assertEqual(ISOCountry.MH.numeric, 584)
        
        
        self.assertEqual(ISOCountry.MK, 807)
        self.assertEqual(ISOCountry.MK, "MK")
        self.assertEqual(ISOCountry.MK, "MKD")
        self.assertEqual(ISOCountry.MK, "North Macedonia")
        self.assertEqual(ISOCountry.MK, "NORTH MACEDONIA")
        self.assertEqual(ISOCountry.MK, "the Republic of North Macedonia")
        self.assertEqual(ISOCountry.MK, "THE REPUBLIC OF NORTH MACEDONIA")
        self.assertEqual(str(ISOCountry.MK), "MK")
        self.assertEqual(ISOCountry.MK.numeric, 807)
        
        self.assertEqual(ISOCountry.ML, 466)
        self.assertEqual(ISOCountry.ML, "ML")
        self.assertEqual(ISOCountry.ML, "MLI")
        self.assertEqual(ISOCountry.ML, "Mali")
        self.assertEqual(ISOCountry.ML, "MALI")
        self.assertEqual(ISOCountry.ML, "the Republic of Mali")
        self.assertEqual(ISOCountry.ML, "THE REPUBLIC OF MALI")
        self.assertEqual(str(ISOCountry.ML), "ML")
        self.assertEqual(ISOCountry.ML.numeric, 466)
        
        self.assertEqual(ISOCountry.MM, 104)
        self.assertEqual(ISOCountry.MM, "MM")
        self.assertEqual(ISOCountry.MM, "MMR")
        self.assertEqual(ISOCountry.MM, "Myanmar")
        self.assertEqual(ISOCountry.MM, "MYANMAR")
        self.assertEqual(ISOCountry.MM, "the Republic of the Union of Myanmar")
        self.assertEqual(ISOCountry.MM, "THE REPUBLIC OF THE UNION OF MYANMAR")
        self.assertEqual(str(ISOCountry.MM), "MM")
        self.assertEqual(ISOCountry.MM.numeric, 104)
        
        self.assertEqual(ISOCountry.MN, 496)
        self.assertEqual(ISOCountry.MN, "MN")
        self.assertEqual(ISOCountry.MN, "MNG")
        self.assertEqual(ISOCountry.MN, "Mongolia")
        self.assertEqual(ISOCountry.MN, "MONGOLIA")
        
        
        self.assertEqual(ISOCountry.MO, 446)
        self.assertEqual(ISOCountry.MO, "MO")
        self.assertEqual(ISOCountry.MO, "MAC")
        self.assertEqual(ISOCountry.MO, "Macao")
        self.assertEqual(ISOCountry.MO, "MACAO")
        self.assertEqual(ISOCountry.MO, "Macao Special Administrative Region of China")
        self.assertEqual(ISOCountry.MO, "MACAO SPECIAL ADMINISTRATIVE REGION OF CHINA")
        self.assertEqual(str(ISOCountry.MO), "MO")
        self.assertEqual(ISOCountry.MO.numeric, 446)
        
        self.assertEqual(ISOCountry.MP, 580)
        self.assertEqual(ISOCountry.MP, "MP")
        self.assertEqual(ISOCountry.MP, "MNP")
        self.assertEqual(ISOCountry.MP, "Northern Mariana Islands (the)")
        self.assertEqual(ISOCountry.MP, "NORTHERN MARIANA ISLANDS (THE)")
        self.assertEqual(ISOCountry.MP, "the Commonwealth of the Northern Mariana Islands")
        self.assertEqual(ISOCountry.MP, "THE COMMONWEALTH OF THE NORTHERN MARIANA ISLANDS")
        self.assertEqual(str(ISOCountry.MP), "MP")
        self.assertEqual(ISOCountry.MP.numeric, 580)
        
        self.assertEqual(ISOCountry.MQ, 474)
        self.assertEqual(ISOCountry.MQ, "MQ")
        self.assertEqual(ISOCountry.MQ, "MTQ")
        self.assertEqual(ISOCountry.MQ, "Martinique")
        self.assertEqual(ISOCountry.MQ, "MARTINIQUE")
        
        
        self.assertEqual(ISOCountry.MR, 478)
        self.assertEqual(ISOCountry.MR, "MR")
        self.assertEqual(ISOCountry.MR, "MRT")
        self.assertEqual(ISOCountry.MR, "Mauritania")
        self.assertEqual(ISOCountry.MR, "MAURITANIA")
        self.assertEqual(ISOCountry.MR, "the Islamic Republic of Mauritania")
        self.assertEqual(ISOCountry.MR, "THE ISLAMIC REPUBLIC OF MAURITANIA")
        self.assertEqual(str(ISOCountry.MR), "MR")
        self.assertEqual(ISOCountry.MR.numeric, 478)
        
        self.assertEqual(ISOCountry.MS, 500)
        self.assertEqual(ISOCountry.MS, "MS")
        self.assertEqual(ISOCountry.MS, "MSR")
        self.assertEqual(ISOCountry.MS, "Montserrat")
        self.assertEqual(ISOCountry.MS, "MONTSERRAT")
        
        
        self.assertEqual(ISOCountry.MT, 470)
        self.assertEqual(ISOCountry.MT, "MT")
        self.assertEqual(ISOCountry.MT, "MLT")
        self.assertEqual(ISOCountry.MT, "Malta")
        self.assertEqual(ISOCountry.MT, "MALTA")
        self.assertEqual(ISOCountry.MT, "the Republic of Malta")
        self.assertEqual(ISOCountry.MT, "THE REPUBLIC OF MALTA")
        self.assertEqual(str(ISOCountry.MT), "MT")
        self.assertEqual(ISOCountry.MT.numeric, 470)
        
        self.assertEqual(ISOCountry.MU, 480)
        self.assertEqual(ISOCountry.MU, "MU")
        self.assertEqual(ISOCountry.MU, "MUS")
        self.assertEqual(ISOCountry.MU, "Mauritius")
        self.assertEqual(ISOCountry.MU, "MAURITIUS")
        self.assertEqual(ISOCountry.MU, "the Republic of Mauritius")
        self.assertEqual(ISOCountry.MU, "THE REPUBLIC OF MAURITIUS")
        self.assertEqual(str(ISOCountry.MU), "MU")
        self.assertEqual(ISOCountry.MU.numeric, 480)
        
        self.assertEqual(ISOCountry.MV, 462)
        self.assertEqual(ISOCountry.MV, "MV")
        self.assertEqual(ISOCountry.MV, "MDV")
        self.assertEqual(ISOCountry.MV, "Maldives")
        self.assertEqual(ISOCountry.MV, "MALDIVES")
        self.assertEqual(ISOCountry.MV, "the Republic of Maldives")
        self.assertEqual(ISOCountry.MV, "THE REPUBLIC OF MALDIVES")
        self.assertEqual(str(ISOCountry.MV), "MV")
        self.assertEqual(ISOCountry.MV.numeric, 462)
        
        self.assertEqual(ISOCountry.MW, 454)
        self.assertEqual(ISOCountry.MW, "MW")
        self.assertEqual(ISOCountry.MW, "MWI")
        self.assertEqual(ISOCountry.MW, "Malawi")
        self.assertEqual(ISOCountry.MW, "MALAWI")
        self.assertEqual(ISOCountry.MW, "the Republic of Malawi")
        self.assertEqual(ISOCountry.MW, "THE REPUBLIC OF MALAWI")
        self.assertEqual(str(ISOCountry.MW), "MW")
        self.assertEqual(ISOCountry.MW.numeric, 454)
        
        self.assertEqual(ISOCountry.MX, 484)
        self.assertEqual(ISOCountry.MX, "MX")
        self.assertEqual(ISOCountry.MX, "MEX")
        self.assertEqual(ISOCountry.MX, "Mexico")
        self.assertEqual(ISOCountry.MX, "MEXICO")
        self.assertEqual(ISOCountry.MX, "the United Mexican States")
        self.assertEqual(ISOCountry.MX, "THE UNITED MEXICAN STATES")
        self.assertEqual(str(ISOCountry.MX), "MX")
        self.assertEqual(ISOCountry.MX.numeric, 484)
        
        self.assertEqual(ISOCountry.MY, 458)
        self.assertEqual(ISOCountry.MY, "MY")
        self.assertEqual(ISOCountry.MY, "MYS")
        self.assertEqual(ISOCountry.MY, "Malaysia")
        self.assertEqual(ISOCountry.MY, "MALAYSIA")
        
        
        self.assertEqual(ISOCountry.MZ, 508)
        self.assertEqual(ISOCountry.MZ, "MZ")
        self.assertEqual(ISOCountry.MZ, "MOZ")
        self.assertEqual(ISOCountry.MZ, "Mozambique")
        self.assertEqual(ISOCountry.MZ, "MOZAMBIQUE")
        self.assertEqual(ISOCountry.MZ, "the Republic of Mozambique")
        self.assertEqual(ISOCountry.MZ, "THE REPUBLIC OF MOZAMBIQUE")
        self.assertEqual(str(ISOCountry.MZ), "MZ")
        self.assertEqual(ISOCountry.MZ.numeric, 508)
        
        self.assertEqual(ISOCountry.NA, 516)
        self.assertEqual(ISOCountry.NA, "NA")
        self.assertEqual(ISOCountry.NA, "NAM")
        self.assertEqual(ISOCountry.NA, "Namibia")
        self.assertEqual(ISOCountry.NA, "NAMIBIA")
        self.assertEqual(ISOCountry.NA, "the Republic of Namibia")
        self.assertEqual(ISOCountry.NA, "THE REPUBLIC OF NAMIBIA")
        self.assertEqual(str(ISOCountry.NA), "NA")
        self.assertEqual(ISOCountry.NA.numeric, 516)
        
        self.assertEqual(ISOCountry.NC, 540)
        self.assertEqual(ISOCountry.NC, "NC")
        self.assertEqual(ISOCountry.NC, "NCL")
        self.assertEqual(ISOCountry.NC, "New Caledonia")
        self.assertEqual(ISOCountry.NC, "NEW CALEDONIA")
        
        
        self.assertEqual(ISOCountry.NE, 562)
        self.assertEqual(ISOCountry.NE, "NE")
        self.assertEqual(ISOCountry.NE, "NER")
        self.assertEqual(ISOCountry.NE, "Niger (the)")
        self.assertEqual(ISOCountry.NE, "NIGER (THE)")
        self.assertEqual(ISOCountry.NE, "the Republic of the Niger")
        self.assertEqual(ISOCountry.NE, "THE REPUBLIC OF THE NIGER")
        self.assertEqual(str(ISOCountry.NE), "NE")
        self.assertEqual(ISOCountry.NE.numeric, 562)
        
        self.assertEqual(ISOCountry.NF, 574)
        self.assertEqual(ISOCountry.NF, "NF")
        self.assertEqual(ISOCountry.NF, "NFK")
        self.assertEqual(ISOCountry.NF, "Norfolk Island")
        self.assertEqual(ISOCountry.NF, "NORFOLK ISLAND")
        
        
        self.assertEqual(ISOCountry.NG, 566)
        self.assertEqual(ISOCountry.NG, "NG")
        self.assertEqual(ISOCountry.NG, "NGA")
        self.assertEqual(ISOCountry.NG, "Nigeria")
        self.assertEqual(ISOCountry.NG, "NIGERIA")
        self.assertEqual(ISOCountry.NG, "the Federal Republic of Nigeria")
        self.assertEqual(ISOCountry.NG, "THE FEDERAL REPUBLIC OF NIGERIA")
        self.assertEqual(str(ISOCountry.NG), "NG")
        self.assertEqual(ISOCountry.NG.numeric, 566)
        
        
        self.assertEqual(ISOCountry.NI, 558)
        self.assertEqual(ISOCountry.NI, "NI")
        self.assertEqual(ISOCountry.NI, "NIC")
        self.assertEqual(ISOCountry.NI, "Nicaragua")
        self.assertEqual(ISOCountry.NI, "NICARAGUA")
        self.assertEqual(ISOCountry.NI, "the Republic of Nicaragua")
        self.assertEqual(ISOCountry.NI, "THE REPUBLIC OF NICARAGUA")
        self.assertEqual(str(ISOCountry.NI), "NI")
        self.assertEqual(ISOCountry.NI.numeric, 558)
        
        self.assertEqual(ISOCountry.NL, 528)
        self.assertEqual(ISOCountry.NL, "NL")
        self.assertEqual(ISOCountry.NL, "NLD")
        self.assertEqual(ISOCountry.NL, "Netherlands (the)")
        self.assertEqual(ISOCountry.NL, "NETHERLANDS (THE)")
        self.assertEqual(ISOCountry.NL, "the Kingdom of the Netherlands")
        self.assertEqual(ISOCountry.NL, "THE KINGDOM OF THE NETHERLANDS")
        self.assertEqual(str(ISOCountry.NL), "NL")
        self.assertEqual(ISOCountry.NL.numeric, 528)
        
        self.assertEqual(ISOCountry.NO, 578)
        self.assertEqual(ISOCountry.NO, "NO")
        self.assertEqual(ISOCountry.NO, "NOR")
        self.assertEqual(ISOCountry.NO, "Norway")
        self.assertEqual(ISOCountry.NO, "NORWAY")
        self.assertEqual(ISOCountry.NO, "the Kingdom of Norway")
        self.assertEqual(ISOCountry.NO, "THE KINGDOM OF NORWAY")
        self.assertEqual(str(ISOCountry.NO), "NO")
        self.assertEqual(ISOCountry.NO.numeric, 578)
        
        self.assertEqual(ISOCountry.NP, 524)
        self.assertEqual(ISOCountry.NP, "NP")
        self.assertEqual(ISOCountry.NP, "NPL")
        self.assertEqual(ISOCountry.NP, "Nepal")
        self.assertEqual(ISOCountry.NP, "NEPAL")
        
        
        
        self.assertEqual(ISOCountry.NR, 520)
        self.assertEqual(ISOCountry.NR, "NR")
        self.assertEqual(ISOCountry.NR, "NRU")
        self.assertEqual(ISOCountry.NR, "Nauru")
        self.assertEqual(ISOCountry.NR, "NAURU")
        self.assertEqual(ISOCountry.NR, "the Republic of Nauru")
        self.assertEqual(ISOCountry.NR, "THE REPUBLIC OF NAURU")
        self.assertEqual(str(ISOCountry.NR), "NR")
        self.assertEqual(ISOCountry.NR.numeric, 520)
        
        
        self.assertEqual(ISOCountry.NU, 570)
        self.assertEqual(ISOCountry.NU, "NU")
        self.assertEqual(ISOCountry.NU, "NIU")
        self.assertEqual(ISOCountry.NU, "Niue")
        self.assertEqual(ISOCountry.NU, "NIUE")
        
        
        self.assertEqual(ISOCountry.NZ, 554)
        self.assertEqual(ISOCountry.NZ, "NZ")
        self.assertEqual(ISOCountry.NZ, "NZL")
        self.assertEqual(ISOCountry.NZ, "New Zealand")
        self.assertEqual(ISOCountry.NZ, "NEW ZEALAND")
        
        
        
        self.assertEqual(ISOCountry.OM, 512)
        self.assertEqual(ISOCountry.OM, "OM")
        self.assertEqual(ISOCountry.OM, "OMN")
        self.assertEqual(ISOCountry.OM, "Oman")
        self.assertEqual(ISOCountry.OM, "OMAN")
        self.assertEqual(ISOCountry.OM, "the Sultanate of Oman")
        self.assertEqual(ISOCountry.OM, "THE SULTANATE OF OMAN")
        self.assertEqual(str(ISOCountry.OM), "OM")
        self.assertEqual(ISOCountry.OM.numeric, 512)
        
        self.assertEqual(ISOCountry.PA, 591)
        self.assertEqual(ISOCountry.PA, "PA")
        self.assertEqual(ISOCountry.PA, "PAN")
        self.assertEqual(ISOCountry.PA, "Panama")
        self.assertEqual(ISOCountry.PA, "PANAMA")
        self.assertEqual(ISOCountry.PA, "the Republic of Panama")
        self.assertEqual(ISOCountry.PA, "THE REPUBLIC OF PANAMA")
        self.assertEqual(str(ISOCountry.PA), "PA")
        self.assertEqual(ISOCountry.PA.numeric, 591)
        
        
        self.assertEqual(ISOCountry.PE, 604)
        self.assertEqual(ISOCountry.PE, "PE")
        self.assertEqual(ISOCountry.PE, "PER")
        self.assertEqual(ISOCountry.PE, "Peru")
        self.assertEqual(ISOCountry.PE, "PERU")
        self.assertEqual(ISOCountry.PE, "the Republic of Peru")
        self.assertEqual(ISOCountry.PE, "THE REPUBLIC OF PERU")
        self.assertEqual(str(ISOCountry.PE), "PE")
        self.assertEqual(ISOCountry.PE.numeric, 604)
        
        self.assertEqual(ISOCountry.PF, 258)
        self.assertEqual(ISOCountry.PF, "PF")
        self.assertEqual(ISOCountry.PF, "PYF")
        self.assertEqual(ISOCountry.PF, "French Polynesia")
        self.assertEqual(ISOCountry.PF, "FRENCH POLYNESIA")
        
        
        self.assertEqual(ISOCountry.PG, 598)
        self.assertEqual(ISOCountry.PG, "PG")
        self.assertEqual(ISOCountry.PG, "PNG")
        self.assertEqual(ISOCountry.PG, "Papua New Guinea")
        self.assertEqual(ISOCountry.PG, "PAPUA NEW GUINEA")
        self.assertEqual(ISOCountry.PG, "the Independent State of Papua New Guinea")
        self.assertEqual(ISOCountry.PG, "THE INDEPENDENT STATE OF PAPUA NEW GUINEA")
        self.assertEqual(str(ISOCountry.PG), "PG")
        self.assertEqual(ISOCountry.PG.numeric, 598)
        
        self.assertEqual(ISOCountry.PH, 608)
        self.assertEqual(ISOCountry.PH, "PH")
        self.assertEqual(ISOCountry.PH, "PHL")
        self.assertEqual(ISOCountry.PH, "Philippines (the)")
        self.assertEqual(ISOCountry.PH, "PHILIPPINES (THE)")
        self.assertEqual(ISOCountry.PH, "the Republic of the Philippines")
        self.assertEqual(ISOCountry.PH, "THE REPUBLIC OF THE PHILIPPINES")
        self.assertEqual(str(ISOCountry.PH), "PH")
        self.assertEqual(ISOCountry.PH.numeric, 608)
        
        
        self.assertEqual(ISOCountry.PK, 586)
        self.assertEqual(ISOCountry.PK, "PK")
        self.assertEqual(ISOCountry.PK, "PAK")
        self.assertEqual(ISOCountry.PK, "Pakistan")
        self.assertEqual(ISOCountry.PK, "PAKISTAN")
        self.assertEqual(ISOCountry.PK, "the Islamic Republic of Pakistan")
        self.assertEqual(ISOCountry.PK, "THE ISLAMIC REPUBLIC OF PAKISTAN")
        self.assertEqual(str(ISOCountry.PK), "PK")
        self.assertEqual(ISOCountry.PK.numeric, 586)
        
        self.assertEqual(ISOCountry.PL, 616)
        self.assertEqual(ISOCountry.PL, "PL")
        self.assertEqual(ISOCountry.PL, "POL")
        self.assertEqual(ISOCountry.PL, "Poland")
        self.assertEqual(ISOCountry.PL, "POLAND")
        self.assertEqual(ISOCountry.PL, "the Republic of Poland")
        self.assertEqual(ISOCountry.PL, "THE REPUBLIC OF POLAND")
        self.assertEqual(str(ISOCountry.PL), "PL")
        self.assertEqual(ISOCountry.PL.numeric, 616)
        
        self.assertEqual(ISOCountry.PM, 666)
        self.assertEqual(ISOCountry.PM, "PM")
        self.assertEqual(ISOCountry.PM, "SPM")
        self.assertEqual(ISOCountry.PM, "Saint Pierre and Miquelon")
        self.assertEqual(ISOCountry.PM, "SAINT PIERRE AND MIQUELON")
        
        
        self.assertEqual(ISOCountry.PN, 612)
        self.assertEqual(ISOCountry.PN, "PN")
        self.assertEqual(ISOCountry.PN, "PCN")
        self.assertEqual(ISOCountry.PN, "Pitcairn")
        self.assertEqual(ISOCountry.PN, "PITCAIRN")
        
        
        self.assertEqual(ISOCountry.PR, 630)
        self.assertEqual(ISOCountry.PR, "PR")
        self.assertEqual(ISOCountry.PR, "PRI")
        self.assertEqual(ISOCountry.PR, "Puerto Rico")
        self.assertEqual(ISOCountry.PR, "PUERTO RICO")
        
        
        self.assertEqual(ISOCountry.PS, 275)
        self.assertEqual(ISOCountry.PS, "PS")
        self.assertEqual(ISOCountry.PS, "PSE")
        self.assertEqual(ISOCountry.PS, "Palestine, State of")
        self.assertEqual(ISOCountry.PS, "PALESTINE, STATE OF")
        self.assertEqual(ISOCountry.PS, "the State of Palestine")
        self.assertEqual(ISOCountry.PS, "THE STATE OF PALESTINE")
        self.assertEqual(str(ISOCountry.PS), "PS")
        self.assertEqual(ISOCountry.PS.numeric, 275)
        
        self.assertEqual(ISOCountry.PT, 620)
        self.assertEqual(ISOCountry.PT, "PT")
        self.assertEqual(ISOCountry.PT, "PRT")
        self.assertEqual(ISOCountry.PT, "Portugal")
        self.assertEqual(ISOCountry.PT, "PORTUGAL")
        self.assertEqual(ISOCountry.PT, "the Portuguese Republic")
        self.assertEqual(ISOCountry.PT, "THE PORTUGUESE REPUBLIC")
        self.assertEqual(str(ISOCountry.PT), "PT")
        self.assertEqual(ISOCountry.PT.numeric, 620)
        
        
        self.assertEqual(ISOCountry.PW, 585)
        self.assertEqual(ISOCountry.PW, "PW")
        self.assertEqual(ISOCountry.PW, "PLW")
        self.assertEqual(ISOCountry.PW, "Palau")
        self.assertEqual(ISOCountry.PW, "PALAU")
        self.assertEqual(ISOCountry.PW, "the Republic of Palau")
        self.assertEqual(ISOCountry.PW, "THE REPUBLIC OF PALAU")
        self.assertEqual(str(ISOCountry.PW), "PW")
        self.assertEqual(ISOCountry.PW.numeric, 585)
        
        self.assertEqual(ISOCountry.PY, 600)
        self.assertEqual(ISOCountry.PY, "PY")
        self.assertEqual(ISOCountry.PY, "PRY")
        self.assertEqual(ISOCountry.PY, "Paraguay")
        self.assertEqual(ISOCountry.PY, "PARAGUAY")
        self.assertEqual(ISOCountry.PY, "the Republic of Paraguay")
        self.assertEqual(ISOCountry.PY, "THE REPUBLIC OF PARAGUAY")
        self.assertEqual(str(ISOCountry.PY), "PY")
        self.assertEqual(ISOCountry.PY.numeric, 600)
        
        
        self.assertEqual(ISOCountry.QA, 634)
        self.assertEqual(ISOCountry.QA, "QA")
        self.assertEqual(ISOCountry.QA, "QAT")
        self.assertEqual(ISOCountry.QA, "Qatar")
        self.assertEqual(ISOCountry.QA, "QATAR")
        self.assertEqual(ISOCountry.QA, "the State of Qatar")
        self.assertEqual(ISOCountry.QA, "THE STATE OF QATAR")
        self.assertEqual(str(ISOCountry.QA), "QA")
        self.assertEqual(ISOCountry.QA.numeric, 634)
        
        
        
        
        self.assertEqual(ISOCountry.RE, 638)
        self.assertEqual(ISOCountry.RE, "RE")
        self.assertEqual(ISOCountry.RE, "REU")
        self.assertEqual(ISOCountry.RE, "Réunion")
        self.assertEqual(ISOCountry.RE, "RÉUNION")
        
        
        
        
        
        
        
        
        self.assertEqual(ISOCountry.RO, 642)
        self.assertEqual(ISOCountry.RO, "RO")
        self.assertEqual(ISOCountry.RO, "ROU")
        self.assertEqual(ISOCountry.RO, "Romania")
        self.assertEqual(ISOCountry.RO, "ROMANIA")
        
        
        
        self.assertEqual(ISOCountry.RS, 688)
        self.assertEqual(ISOCountry.RS, "RS")
        self.assertEqual(ISOCountry.RS, "SRB")
        self.assertEqual(ISOCountry.RS, "Serbia")
        self.assertEqual(ISOCountry.RS, "SERBIA")
        self.assertEqual(ISOCountry.RS, "the Republic of Serbia")
        self.assertEqual(ISOCountry.RS, "THE REPUBLIC OF SERBIA")
        self.assertEqual(str(ISOCountry.RS), "RS")
        self.assertEqual(ISOCountry.RS.numeric, 688)
        
        self.assertEqual(ISOCountry.RU, 643)
        self.assertEqual(ISOCountry.RU, "RU")
        self.assertEqual(ISOCountry.RU, "RUS")
        self.assertEqual(ISOCountry.RU, "Russian Federation (the)")
        self.assertEqual(ISOCountry.RU, "RUSSIAN FEDERATION (THE)")
        self.assertEqual(ISOCountry.RU, "the Russian Federation")
        self.assertEqual(ISOCountry.RU, "THE RUSSIAN FEDERATION")
        self.assertEqual(str(ISOCountry.RU), "RU")
        self.assertEqual(ISOCountry.RU.numeric, 643)
        
        self.assertEqual(ISOCountry.RW, 646)
        self.assertEqual(ISOCountry.RW, "RW")
        self.assertEqual(ISOCountry.RW, "RWA")
        self.assertEqual(ISOCountry.RW, "Rwanda")
        self.assertEqual(ISOCountry.RW, "RWANDA")
        self.assertEqual(ISOCountry.RW, "the Republic of Rwanda")
        self.assertEqual(ISOCountry.RW, "THE REPUBLIC OF RWANDA")
        self.assertEqual(str(ISOCountry.RW), "RW")
        self.assertEqual(ISOCountry.RW.numeric, 646)
        
        self.assertEqual(ISOCountry.SA, 682)
        self.assertEqual(ISOCountry.SA, "SA")
        self.assertEqual(ISOCountry.SA, "SAU")
        self.assertEqual(ISOCountry.SA, "Saudi Arabia")
        self.assertEqual(ISOCountry.SA, "SAUDI ARABIA")
        self.assertEqual(ISOCountry.SA, "the Kingdom of Saudi Arabia")
        self.assertEqual(ISOCountry.SA, "THE KINGDOM OF SAUDI ARABIA")
        self.assertEqual(str(ISOCountry.SA), "SA")
        self.assertEqual(ISOCountry.SA.numeric, 682)
        
        self.assertEqual(ISOCountry.SB, 90)
        self.assertEqual(ISOCountry.SB, "SB")
        self.assertEqual(ISOCountry.SB, "SLB")
        self.assertEqual(ISOCountry.SB, "Solomon Islands")
        self.assertEqual(ISOCountry.SB, "SOLOMON ISLANDS")
        
        
        self.assertEqual(ISOCountry.SC, 690)
        self.assertEqual(ISOCountry.SC, "SC")
        self.assertEqual(ISOCountry.SC, "SYC")
        self.assertEqual(ISOCountry.SC, "Seychelles")
        self.assertEqual(ISOCountry.SC, "SEYCHELLES")
        self.assertEqual(ISOCountry.SC, "the Republic of Seychelles")
        self.assertEqual(ISOCountry.SC, "THE REPUBLIC OF SEYCHELLES")
        self.assertEqual(str(ISOCountry.SC), "SC")
        self.assertEqual(ISOCountry.SC.numeric, 690)
        
        self.assertEqual(ISOCountry.SD, 729)
        self.assertEqual(ISOCountry.SD, "SD")
        self.assertEqual(ISOCountry.SD, "SDN")
        self.assertEqual(ISOCountry.SD, "Sudan (the)")
        self.assertEqual(ISOCountry.SD, "SUDAN (THE)")
        self.assertEqual(ISOCountry.SD, "the Republic of the Sudan")
        self.assertEqual(ISOCountry.SD, "THE REPUBLIC OF THE SUDAN")
        self.assertEqual(str(ISOCountry.SD), "SD")
        self.assertEqual(ISOCountry.SD.numeric, 729)
        
        self.assertEqual(ISOCountry.SE, 752)
        self.assertEqual(ISOCountry.SE, "SE")
        self.assertEqual(ISOCountry.SE, "SWE")
        self.assertEqual(ISOCountry.SE, "Sweden")
        self.assertEqual(ISOCountry.SE, "SWEDEN")
        self.assertEqual(ISOCountry.SE, "the Kingdom of Sweden")
        self.assertEqual(ISOCountry.SE, "THE KINGDOM OF SWEDEN")
        self.assertEqual(str(ISOCountry.SE), "SE")
        self.assertEqual(ISOCountry.SE.numeric, 752)
        
        
        self.assertEqual(ISOCountry.SG, 702)
        self.assertEqual(ISOCountry.SG, "SG")
        self.assertEqual(ISOCountry.SG, "SGP")
        self.assertEqual(ISOCountry.SG, "Singapore")
        self.assertEqual(ISOCountry.SG, "SINGAPORE")
        self.assertEqual(ISOCountry.SG, "the Republic of Singapore")
        self.assertEqual(ISOCountry.SG, "THE REPUBLIC OF SINGAPORE")
        self.assertEqual(str(ISOCountry.SG), "SG")
        self.assertEqual(ISOCountry.SG.numeric, 702)
        
        self.assertEqual(ISOCountry.SH, 654)
        self.assertEqual(ISOCountry.SH, "SH")
        self.assertEqual(ISOCountry.SH, "SHN")
        self.assertEqual(ISOCountry.SH, "Saint Helena, Ascension and Tristan da Cunha")
        self.assertEqual(ISOCountry.SH, "SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA")
        
        
        self.assertEqual(ISOCountry.SI, 705)
        self.assertEqual(ISOCountry.SI, "SI")
        self.assertEqual(ISOCountry.SI, "SVN")
        self.assertEqual(ISOCountry.SI, "Slovenia")
        self.assertEqual(ISOCountry.SI, "SLOVENIA")
        self.assertEqual(ISOCountry.SI, "the Republic of Slovenia")
        self.assertEqual(ISOCountry.SI, "THE REPUBLIC OF SLOVENIA")
        self.assertEqual(str(ISOCountry.SI), "SI")
        self.assertEqual(ISOCountry.SI.numeric, 705)
        
        self.assertEqual(ISOCountry.SJ, 744)
        self.assertEqual(ISOCountry.SJ, "SJ")
        self.assertEqual(ISOCountry.SJ, "SJM")
        self.assertEqual(ISOCountry.SJ, "Svalbard and Jan Mayen")
        self.assertEqual(ISOCountry.SJ, "SVALBARD AND JAN MAYEN")
        
        
        self.assertEqual(ISOCountry.SK, 703)
        self.assertEqual(ISOCountry.SK, "SK")
        self.assertEqual(ISOCountry.SK, "SVK")
        self.assertEqual(ISOCountry.SK, "Slovakia")
        self.assertEqual(ISOCountry.SK, "SLOVAKIA")
        self.assertEqual(ISOCountry.SK, "the Slovak Republic")
        self.assertEqual(ISOCountry.SK, "THE SLOVAK REPUBLIC")
        self.assertEqual(str(ISOCountry.SK), "SK")
        self.assertEqual(ISOCountry.SK.numeric, 703)
        
        
        self.assertEqual(ISOCountry.SL, 694)
        self.assertEqual(ISOCountry.SL, "SL")
        self.assertEqual(ISOCountry.SL, "SLE")
        self.assertEqual(ISOCountry.SL, "Sierra Leone")
        self.assertEqual(ISOCountry.SL, "SIERRA LEONE")
        self.assertEqual(ISOCountry.SL, "the Republic of Sierra Leone")
        self.assertEqual(ISOCountry.SL, "THE REPUBLIC OF SIERRA LEONE")
        self.assertEqual(str(ISOCountry.SL), "SL")
        self.assertEqual(ISOCountry.SL.numeric, 694)
        
        self.assertEqual(ISOCountry.SM, 674)
        self.assertEqual(ISOCountry.SM, "SM")
        self.assertEqual(ISOCountry.SM, "SMR")
        self.assertEqual(ISOCountry.SM, "San Marino")
        self.assertEqual(ISOCountry.SM, "SAN MARINO")
        self.assertEqual(ISOCountry.SM, "the Republic of San Marino")
        self.assertEqual(ISOCountry.SM, "THE REPUBLIC OF SAN MARINO")
        self.assertEqual(str(ISOCountry.SM), "SM")
        self.assertEqual(ISOCountry.SM.numeric, 674)
        
        self.assertEqual(ISOCountry.SN, 686)
        self.assertEqual(ISOCountry.SN, "SN")
        self.assertEqual(ISOCountry.SN, "SEN")
        self.assertEqual(ISOCountry.SN, "Senegal")
        self.assertEqual(ISOCountry.SN, "SENEGAL")
        self.assertEqual(ISOCountry.SN, "the Republic of Senegal")
        self.assertEqual(ISOCountry.SN, "THE REPUBLIC OF SENEGAL")
        self.assertEqual(str(ISOCountry.SN), "SN")
        self.assertEqual(ISOCountry.SN.numeric, 686)
        
        self.assertEqual(ISOCountry.SO, 706)
        self.assertEqual(ISOCountry.SO, "SO")
        self.assertEqual(ISOCountry.SO, "SOM")
        self.assertEqual(ISOCountry.SO, "Somalia")
        self.assertEqual(ISOCountry.SO, "SOMALIA")
        self.assertEqual(ISOCountry.SO, "the Federal Republic of Somalia")
        self.assertEqual(ISOCountry.SO, "THE FEDERAL REPUBLIC OF SOMALIA")
        self.assertEqual(str(ISOCountry.SO), "SO")
        self.assertEqual(ISOCountry.SO.numeric, 706)
        
        self.assertEqual(ISOCountry.SR, 740)
        self.assertEqual(ISOCountry.SR, "SR")
        self.assertEqual(ISOCountry.SR, "SUR")
        self.assertEqual(ISOCountry.SR, "Suriname")
        self.assertEqual(ISOCountry.SR, "SURINAME")
        self.assertEqual(ISOCountry.SR, "the Republic of Suriname")
        self.assertEqual(ISOCountry.SR, "THE REPUBLIC OF SURINAME")
        self.assertEqual(str(ISOCountry.SR), "SR")
        self.assertEqual(ISOCountry.SR.numeric, 740)
        
        self.assertEqual(ISOCountry.SS, 728)
        self.assertEqual(ISOCountry.SS, "SS")
        self.assertEqual(ISOCountry.SS, "SSD")
        self.assertEqual(ISOCountry.SS, "South Sudan")
        self.assertEqual(ISOCountry.SS, "SOUTH SUDAN")
        self.assertEqual(ISOCountry.SS, "the Republic of South Sudan")
        self.assertEqual(ISOCountry.SS, "THE REPUBLIC OF SOUTH SUDAN")
        self.assertEqual(str(ISOCountry.SS), "SS")
        self.assertEqual(ISOCountry.SS.numeric, 728)
        
        self.assertEqual(ISOCountry.ST, 678)
        self.assertEqual(ISOCountry.ST, "ST")
        self.assertEqual(ISOCountry.ST, "STP")
        self.assertEqual(ISOCountry.ST, "Sao Tome and Principe")
        self.assertEqual(ISOCountry.ST, "SAO TOME AND PRINCIPE")
        self.assertEqual(ISOCountry.ST, "the Democratic Republic of Sao Tome and Principe")
        self.assertEqual(ISOCountry.ST, "THE DEMOCRATIC REPUBLIC OF SAO TOME AND PRINCIPE")
        self.assertEqual(str(ISOCountry.ST), "ST")
        self.assertEqual(ISOCountry.ST.numeric, 678)
        
        
        self.assertEqual(ISOCountry.SV, 222)
        self.assertEqual(ISOCountry.SV, "SV")
        self.assertEqual(ISOCountry.SV, "SLV")
        self.assertEqual(ISOCountry.SV, "El Salvador")
        self.assertEqual(ISOCountry.SV, "EL SALVADOR")
        self.assertEqual(ISOCountry.SV, "the Republic of El Salvador")
        self.assertEqual(ISOCountry.SV, "THE REPUBLIC OF EL SALVADOR")
        self.assertEqual(str(ISOCountry.SV), "SV")
        self.assertEqual(ISOCountry.SV.numeric, 222)
        
        self.assertEqual(ISOCountry.SX, 534)
        self.assertEqual(ISOCountry.SX, "SX")
        self.assertEqual(ISOCountry.SX, "SXM")
        self.assertEqual(ISOCountry.SX, "Sint Maarten (Dutch part)")
        self.assertEqual(ISOCountry.SX, "SINT MAARTEN (DUTCH PART)")
        
        
        self.assertEqual(ISOCountry.SY, 760)
        self.assertEqual(ISOCountry.SY, "SY")
        self.assertEqual(ISOCountry.SY, "SYR")
        self.assertEqual(ISOCountry.SY, "Syrian Arab Republic (the)")
        self.assertEqual(ISOCountry.SY, "SYRIAN ARAB REPUBLIC (THE)")
        self.assertEqual(ISOCountry.SY, "the Syrian Arab Republic")
        self.assertEqual(ISOCountry.SY, "THE SYRIAN ARAB REPUBLIC")
        self.assertEqual(str(ISOCountry.SY), "SY")
        self.assertEqual(ISOCountry.SY.numeric, 760)
        
        self.assertEqual(ISOCountry.SZ, 748)
        self.assertEqual(ISOCountry.SZ, "SZ")
        self.assertEqual(ISOCountry.SZ, "SWZ")
        self.assertEqual(ISOCountry.SZ, "Eswatini")
        self.assertEqual(ISOCountry.SZ, "ESWATINI")
        self.assertEqual(ISOCountry.SZ, "the Kingdom of Eswatini")
        self.assertEqual(ISOCountry.SZ, "THE KINGDOM OF ESWATINI")
        self.assertEqual(str(ISOCountry.SZ), "SZ")
        self.assertEqual(ISOCountry.SZ.numeric, 748)
        
        
        self.assertEqual(ISOCountry.TC, 796)
        self.assertEqual(ISOCountry.TC, "TC")
        self.assertEqual(ISOCountry.TC, "TCA")
        self.assertEqual(ISOCountry.TC, "Turks and Caicos Islands (the)")
        self.assertEqual(ISOCountry.TC, "TURKS AND CAICOS ISLANDS (THE)")
        
        
        self.assertEqual(ISOCountry.TD, 148)
        self.assertEqual(ISOCountry.TD, "TD")
        self.assertEqual(ISOCountry.TD, "TCD")
        self.assertEqual(ISOCountry.TD, "Chad")
        self.assertEqual(ISOCountry.TD, "CHAD")
        self.assertEqual(ISOCountry.TD, "the Republic of Chad")
        self.assertEqual(ISOCountry.TD, "THE REPUBLIC OF CHAD")
        self.assertEqual(str(ISOCountry.TD), "TD")
        self.assertEqual(ISOCountry.TD.numeric, 148)
        
        self.assertEqual(ISOCountry.TF, 260)
        self.assertEqual(ISOCountry.TF, "TF")
        self.assertEqual(ISOCountry.TF, "ATF")
        self.assertEqual(ISOCountry.TF, "French Southern Territories (the)")
        self.assertEqual(ISOCountry.TF, "FRENCH SOUTHERN TERRITORIES (THE)")
        
        
        self.assertEqual(ISOCountry.TG, 768)
        self.assertEqual(ISOCountry.TG, "TG")
        self.assertEqual(ISOCountry.TG, "TGO")
        self.assertEqual(ISOCountry.TG, "Togo")
        self.assertEqual(ISOCountry.TG, "TOGO")
        self.assertEqual(ISOCountry.TG, "the Togolese Republic")
        self.assertEqual(ISOCountry.TG, "THE TOGOLESE REPUBLIC")
        self.assertEqual(str(ISOCountry.TG), "TG")
        self.assertEqual(ISOCountry.TG.numeric, 768)
        
        self.assertEqual(ISOCountry.TH, 764)
        self.assertEqual(ISOCountry.TH, "TH")
        self.assertEqual(ISOCountry.TH, "THA")
        self.assertEqual(ISOCountry.TH, "Thailand")
        self.assertEqual(ISOCountry.TH, "THAILAND")
        self.assertEqual(ISOCountry.TH, "the Kingdom of Thailand")
        self.assertEqual(ISOCountry.TH, "THE KINGDOM OF THAILAND")
        self.assertEqual(str(ISOCountry.TH), "TH")
        self.assertEqual(ISOCountry.TH.numeric, 764)
        
        self.assertEqual(ISOCountry.TJ, 762)
        self.assertEqual(ISOCountry.TJ, "TJ")
        self.assertEqual(ISOCountry.TJ, "TJK")
        self.assertEqual(ISOCountry.TJ, "Tajikistan")
        self.assertEqual(ISOCountry.TJ, "TAJIKISTAN")
        self.assertEqual(ISOCountry.TJ, "the Republic of Tajikistan")
        self.assertEqual(ISOCountry.TJ, "THE REPUBLIC OF TAJIKISTAN")
        self.assertEqual(str(ISOCountry.TJ), "TJ")
        self.assertEqual(ISOCountry.TJ.numeric, 762)
        
        self.assertEqual(ISOCountry.TK, 772)
        self.assertEqual(ISOCountry.TK, "TK")
        self.assertEqual(ISOCountry.TK, "TKL")
        self.assertEqual(ISOCountry.TK, "Tokelau")
        self.assertEqual(ISOCountry.TK, "TOKELAU")
        
        
        self.assertEqual(ISOCountry.TL, 626)
        self.assertEqual(ISOCountry.TL, "TL")
        self.assertEqual(ISOCountry.TL, "TLS")
        self.assertEqual(ISOCountry.TL, "Timor-Leste")
        self.assertEqual(ISOCountry.TL, "TIMOR-LESTE")
        self.assertEqual(ISOCountry.TL, "the Democratic Republic of Timor-Leste")
        self.assertEqual(ISOCountry.TL, "THE DEMOCRATIC REPUBLIC OF TIMOR-LESTE")
        self.assertEqual(str(ISOCountry.TL), "TL")
        self.assertEqual(ISOCountry.TL.numeric, 626)
        
        self.assertEqual(ISOCountry.TM, 795)
        self.assertEqual(ISOCountry.TM, "TM")
        self.assertEqual(ISOCountry.TM, "TKM")
        self.assertEqual(ISOCountry.TM, "Turkmenistan")
        self.assertEqual(ISOCountry.TM, "TURKMENISTAN")
        
        
        self.assertEqual(ISOCountry.TN, 788)
        self.assertEqual(ISOCountry.TN, "TN")
        self.assertEqual(ISOCountry.TN, "TUN")
        self.assertEqual(ISOCountry.TN, "Tunisia")
        self.assertEqual(ISOCountry.TN, "TUNISIA")
        self.assertEqual(ISOCountry.TN, "the Republic of Tunisia")
        self.assertEqual(ISOCountry.TN, "THE REPUBLIC OF TUNISIA")
        self.assertEqual(str(ISOCountry.TN), "TN")
        self.assertEqual(ISOCountry.TN.numeric, 788)
        
        self.assertEqual(ISOCountry.TO, 776)
        self.assertEqual(ISOCountry.TO, "TO")
        self.assertEqual(ISOCountry.TO, "TON")
        self.assertEqual(ISOCountry.TO, "Tonga")
        self.assertEqual(ISOCountry.TO, "TONGA")
        self.assertEqual(ISOCountry.TO, "the Kingdom of Tonga")
        self.assertEqual(ISOCountry.TO, "THE KINGDOM OF TONGA")
        self.assertEqual(str(ISOCountry.TO), "TO")
        self.assertEqual(ISOCountry.TO.numeric, 776)
        
        
        self.assertEqual(ISOCountry.TR, 792)
        self.assertEqual(ISOCountry.TR, "TR")
        self.assertEqual(ISOCountry.TR, "TUR")
        self.assertEqual(ISOCountry.TR, "Türkiye")
        self.assertEqual(ISOCountry.TR, "TÜRKIYE")
        self.assertEqual(ISOCountry.TR, "the Republic of Türkiye")
        self.assertEqual(ISOCountry.TR, "THE REPUBLIC OF TÜRKIYE")
        self.assertEqual(str(ISOCountry.TR), "TR")
        self.assertEqual(ISOCountry.TR.numeric, 792)
        
        self.assertEqual(ISOCountry.TT, 780)
        self.assertEqual(ISOCountry.TT, "TT")
        self.assertEqual(ISOCountry.TT, "TTO")
        self.assertEqual(ISOCountry.TT, "Trinidad and Tobago")
        self.assertEqual(ISOCountry.TT, "TRINIDAD AND TOBAGO")
        self.assertEqual(ISOCountry.TT, "the Republic of Trinidad and Tobago")
        self.assertEqual(ISOCountry.TT, "THE REPUBLIC OF TRINIDAD AND TOBAGO")
        self.assertEqual(str(ISOCountry.TT), "TT")
        self.assertEqual(ISOCountry.TT.numeric, 780)
        
        self.assertEqual(ISOCountry.TV, 798)
        self.assertEqual(ISOCountry.TV, "TV")
        self.assertEqual(ISOCountry.TV, "TUV")
        self.assertEqual(ISOCountry.TV, "Tuvalu")
        self.assertEqual(ISOCountry.TV, "TUVALU")
        
        
        self.assertEqual(ISOCountry.TW, 158)
        self.assertEqual(ISOCountry.TW, "TW")
        self.assertEqual(ISOCountry.TW, "TWN")
        self.assertEqual(ISOCountry.TW, "Taiwan (Province of China)")
        self.assertEqual(ISOCountry.TW, "TAIWAN (PROVINCE OF CHINA)")
        
        
        self.assertEqual(ISOCountry.TZ, 834)
        self.assertEqual(ISOCountry.TZ, "TZ")
        self.assertEqual(ISOCountry.TZ, "TZA")
        self.assertEqual(ISOCountry.TZ, "Tanzania, the United Republic of")
        self.assertEqual(ISOCountry.TZ, "TANZANIA, THE UNITED REPUBLIC OF")
        self.assertEqual(ISOCountry.TZ, "the United Republic of Tanzania")
        self.assertEqual(ISOCountry.TZ, "THE UNITED REPUBLIC OF TANZANIA")
        self.assertEqual(str(ISOCountry.TZ), "TZ")
        self.assertEqual(ISOCountry.TZ.numeric, 834)
        
        self.assertEqual(ISOCountry.UA, 804)
        self.assertEqual(ISOCountry.UA, "UA")
        self.assertEqual(ISOCountry.UA, "UKR")
        self.assertEqual(ISOCountry.UA, "Ukraine")
        self.assertEqual(ISOCountry.UA, "UKRAINE")
        
        
        self.assertEqual(ISOCountry.UG, 800)
        self.assertEqual(ISOCountry.UG, "UG")
        self.assertEqual(ISOCountry.UG, "UGA")
        self.assertEqual(ISOCountry.UG, "Uganda")
        self.assertEqual(ISOCountry.UG, "UGANDA")
        self.assertEqual(ISOCountry.UG, "the Republic of Uganda")
        self.assertEqual(ISOCountry.UG, "THE REPUBLIC OF UGANDA")
        self.assertEqual(str(ISOCountry.UG), "UG")
        self.assertEqual(ISOCountry.UG.numeric, 800)
        
        
        self.assertEqual(ISOCountry.UM, 581)
        self.assertEqual(ISOCountry.UM, "UM")
        self.assertEqual(ISOCountry.UM, "UMI")
        self.assertEqual(ISOCountry.UM, "United States Minor Outlying Islands (the)")
        self.assertEqual(ISOCountry.UM, "UNITED STATES MINOR OUTLYING ISLANDS (THE)")
        
        
        
        self.assertEqual(ISOCountry.US, 840)
        self.assertEqual(ISOCountry.US, "US")
        self.assertEqual(ISOCountry.US, "USA")
        self.assertEqual(ISOCountry.US, "United States of America (the)")
        self.assertEqual(ISOCountry.US, "UNITED STATES OF AMERICA (THE)")
        self.assertEqual(ISOCountry.US, "the United States of America")
        self.assertEqual(ISOCountry.US, "THE UNITED STATES OF AMERICA")
        self.assertEqual(str(ISOCountry.US), "US")
        self.assertEqual(ISOCountry.US.numeric, 840)
        
        self.assertEqual(ISOCountry.UY, 858)
        self.assertEqual(ISOCountry.UY, "UY")
        self.assertEqual(ISOCountry.UY, "URY")
        self.assertEqual(ISOCountry.UY, "Uruguay")
        self.assertEqual(ISOCountry.UY, "URUGUAY")
        self.assertEqual(ISOCountry.UY, "the Eastern Republic of Uruguay")
        self.assertEqual(ISOCountry.UY, "THE EASTERN REPUBLIC OF URUGUAY")
        self.assertEqual(str(ISOCountry.UY), "UY")
        self.assertEqual(ISOCountry.UY.numeric, 858)
        
        self.assertEqual(ISOCountry.UZ, 860)
        self.assertEqual(ISOCountry.UZ, "UZ")
        self.assertEqual(ISOCountry.UZ, "UZB")
        self.assertEqual(ISOCountry.UZ, "Uzbekistan")
        self.assertEqual(ISOCountry.UZ, "UZBEKISTAN")
        self.assertEqual(ISOCountry.UZ, "the Republic of Uzbekistan")
        self.assertEqual(ISOCountry.UZ, "THE REPUBLIC OF UZBEKISTAN")
        self.assertEqual(str(ISOCountry.UZ), "UZ")
        self.assertEqual(ISOCountry.UZ.numeric, 860)
        
        self.assertEqual(ISOCountry.VA, 336)
        self.assertEqual(ISOCountry.VA, "VA")
        self.assertEqual(ISOCountry.VA, "VAT")
        self.assertEqual(ISOCountry.VA, "Holy See (the)")
        self.assertEqual(ISOCountry.VA, "HOLY SEE (THE)")
        
        
        self.assertEqual(ISOCountry.VC, 670)
        self.assertEqual(ISOCountry.VC, "VC")
        self.assertEqual(ISOCountry.VC, "VCT")
        self.assertEqual(ISOCountry.VC, "Saint Vincent and the Grenadines")
        self.assertEqual(ISOCountry.VC, "SAINT VINCENT AND THE GRENADINES")
        
        
        
        self.assertEqual(ISOCountry.VE, 862)
        self.assertEqual(ISOCountry.VE, "VE")
        self.assertEqual(ISOCountry.VE, "VEN")
        self.assertEqual(ISOCountry.VE, "Venezuela (Bolivarian Republic of)")
        self.assertEqual(ISOCountry.VE, "VENEZUELA (BOLIVARIAN REPUBLIC OF)")
        self.assertEqual(ISOCountry.VE, "the Bolivarian Republic of Venezuela")
        self.assertEqual(ISOCountry.VE, "THE BOLIVARIAN REPUBLIC OF VENEZUELA")
        self.assertEqual(str(ISOCountry.VE), "VE")
        self.assertEqual(ISOCountry.VE.numeric, 862)
        
        self.assertEqual(ISOCountry.VG, 92)
        self.assertEqual(ISOCountry.VG, "VG")
        self.assertEqual(ISOCountry.VG, "VGB")
        self.assertEqual(ISOCountry.VG, "Virgin Islands (British)")
        self.assertEqual(ISOCountry.VG, "VIRGIN ISLANDS (BRITISH)")
        self.assertEqual(ISOCountry.VG, "British Virgin Islands (the)")
        self.assertEqual(ISOCountry.VG, "BRITISH VIRGIN ISLANDS (THE)")
        self.assertEqual(str(ISOCountry.VG), "VG")
        self.assertEqual(ISOCountry.VG.numeric, 92)
        
        self.assertEqual(ISOCountry.VI, 850)
        self.assertEqual(ISOCountry.VI, "VI")
        self.assertEqual(ISOCountry.VI, "VIR")
        self.assertEqual(ISOCountry.VI, "Virgin Islands (U.S.)")
        self.assertEqual(ISOCountry.VI, "VIRGIN ISLANDS (U.S.)")
        self.assertEqual(ISOCountry.VI, "the Virgin Islands of the United States")
        self.assertEqual(ISOCountry.VI, "THE VIRGIN ISLANDS OF THE UNITED STATES")
        self.assertEqual(str(ISOCountry.VI), "VI")
        self.assertEqual(ISOCountry.VI.numeric, 850)
        
        self.assertEqual(ISOCountry.VN, 704)
        self.assertEqual(ISOCountry.VN, "VN")
        self.assertEqual(ISOCountry.VN, "VNM")
        self.assertEqual(ISOCountry.VN, "Viet Nam")
        self.assertEqual(ISOCountry.VN, "VIET NAM")
        self.assertEqual(ISOCountry.VN, "the Socialist Republic of Viet Nam")
        self.assertEqual(ISOCountry.VN, "THE SOCIALIST REPUBLIC OF VIET NAM")
        self.assertEqual(str(ISOCountry.VN), "VN")
        self.assertEqual(ISOCountry.VN.numeric, 704)
        
        self.assertEqual(ISOCountry.VU, 548)
        self.assertEqual(ISOCountry.VU, "VU")
        self.assertEqual(ISOCountry.VU, "VUT")
        self.assertEqual(ISOCountry.VU, "Vanuatu")
        self.assertEqual(ISOCountry.VU, "VANUATU")
        self.assertEqual(ISOCountry.VU, "the Republic of Vanuatu")
        self.assertEqual(ISOCountry.VU, "THE REPUBLIC OF VANUATU")
        self.assertEqual(str(ISOCountry.VU), "VU")
        self.assertEqual(ISOCountry.VU.numeric, 548)
        
        self.assertEqual(ISOCountry.WF, 876)
        self.assertEqual(ISOCountry.WF, "WF")
        self.assertEqual(ISOCountry.WF, "WLF")
        self.assertEqual(ISOCountry.WF, "Wallis and Futuna")
        self.assertEqual(ISOCountry.WF, "WALLIS AND FUTUNA")
        self.assertEqual(ISOCountry.WF, "Wallis and Futuna Islands")
        self.assertEqual(ISOCountry.WF, "WALLIS AND FUTUNA ISLANDS")
        self.assertEqual(str(ISOCountry.WF), "WF")
        self.assertEqual(ISOCountry.WF.numeric, 876)
        
        
        
        
        
        self.assertEqual(ISOCountry.WS, 882)
        self.assertEqual(ISOCountry.WS, "WS")
        self.assertEqual(ISOCountry.WS, "WSM")
        self.assertEqual(ISOCountry.WS, "Samoa")
        self.assertEqual(ISOCountry.WS, "SAMOA")
        self.assertEqual(ISOCountry.WS, "the Independent State of Samoa")
        self.assertEqual(ISOCountry.WS, "THE INDEPENDENT STATE OF SAMOA")
        self.assertEqual(str(ISOCountry.WS), "WS")
        self.assertEqual(ISOCountry.WS.numeric, 882)
        
        
        
        self.assertEqual(ISOCountry.YE, 887)
        self.assertEqual(ISOCountry.YE, "YE")
        self.assertEqual(ISOCountry.YE, "YEM")
        self.assertEqual(ISOCountry.YE, "Yemen")
        self.assertEqual(ISOCountry.YE, "YEMEN")
        self.assertEqual(ISOCountry.YE, "the Republic of Yemen")
        self.assertEqual(ISOCountry.YE, "THE REPUBLIC OF YEMEN")
        self.assertEqual(str(ISOCountry.YE), "YE")
        self.assertEqual(ISOCountry.YE.numeric, 887)
        
        self.assertEqual(ISOCountry.YT, 175)
        self.assertEqual(ISOCountry.YT, "YT")
        self.assertEqual(ISOCountry.YT, "MYT")
        self.assertEqual(ISOCountry.YT, "Mayotte")
        self.assertEqual(ISOCountry.YT, "MAYOTTE")
        
        
        
        
        self.assertEqual(ISOCountry.ZA, 710)
        self.assertEqual(ISOCountry.ZA, "ZA")
        self.assertEqual(ISOCountry.ZA, "ZAF")
        self.assertEqual(ISOCountry.ZA, "South Africa")
        self.assertEqual(ISOCountry.ZA, "SOUTH AFRICA")
        self.assertEqual(ISOCountry.ZA, "the Republic of South Africa")
        self.assertEqual(ISOCountry.ZA, "THE REPUBLIC OF SOUTH AFRICA")
        self.assertEqual(str(ISOCountry.ZA), "ZA")
        self.assertEqual(ISOCountry.ZA.numeric, 710)
        
        self.assertEqual(ISOCountry.ZM, 894)
        self.assertEqual(ISOCountry.ZM, "ZM")
        self.assertEqual(ISOCountry.ZM, "ZMB")
        self.assertEqual(ISOCountry.ZM, "Zambia")
        self.assertEqual(ISOCountry.ZM, "ZAMBIA")
        self.assertEqual(ISOCountry.ZM, "the Republic of Zambia")
        self.assertEqual(ISOCountry.ZM, "THE REPUBLIC OF ZAMBIA")
        self.assertEqual(str(ISOCountry.ZM), "ZM")
        self.assertEqual(ISOCountry.ZM.numeric, 894)
        
        
        self.assertEqual(ISOCountry.ZW, 716)
        self.assertEqual(ISOCountry.ZW, "ZW")
        self.assertEqual(ISOCountry.ZW, "ZWE")
        self.assertEqual(ISOCountry.ZW, "Zimbabwe")
        self.assertEqual(ISOCountry.ZW, "ZIMBABWE")
        self.assertEqual(ISOCountry.ZW, "the Republic of Zimbabwe")
        self.assertEqual(ISOCountry.ZW, "THE REPUBLIC OF ZIMBABWE")
        self.assertEqual(str(ISOCountry.ZW), "ZW")
        self.assertEqual(ISOCountry.ZW.numeric, 716)

    def test_independent(self):
        
        
        
        self.assertEqual(ISOCountry.AD.independent, True)
        
        self.assertEqual(ISOCountry.AE.independent, True)
        
        self.assertEqual(ISOCountry.AF.independent, True)
        
        self.assertEqual(ISOCountry.AG.independent, True)
        
        
        self.assertEqual(ISOCountry.AI.independent, False)
        
        self.assertEqual(ISOCountry.AL.independent, True)
        
        self.assertEqual(ISOCountry.AM.independent, True)
        
        
        self.assertEqual(ISOCountry.AO.independent, True)
        
        
        self.assertEqual(ISOCountry.AQ.independent, False)
        
        self.assertEqual(ISOCountry.AR.independent, True)
        
        self.assertEqual(ISOCountry.AS.independent, False)
        
        self.assertEqual(ISOCountry.AT.independent, True)
        
        self.assertEqual(ISOCountry.AU.independent, True)
        
        self.assertEqual(ISOCountry.AW.independent, False)
        
        self.assertEqual(ISOCountry.AX.independent, False)
        
        self.assertEqual(ISOCountry.AZ.independent, True)
        
        self.assertEqual(ISOCountry.BA.independent, True)
        
        self.assertEqual(ISOCountry.BB.independent, True)
        
        self.assertEqual(ISOCountry.BD.independent, True)
        
        self.assertEqual(ISOCountry.BE.independent, True)
        
        self.assertEqual(ISOCountry.BF.independent, True)
        
        self.assertEqual(ISOCountry.BG.independent, True)
        
        self.assertEqual(ISOCountry.BH.independent, True)
        
        self.assertEqual(ISOCountry.BI.independent, True)
        
        self.assertEqual(ISOCountry.BJ.independent, True)
        
        self.assertEqual(ISOCountry.BL.independent, False)
        
        self.assertEqual(ISOCountry.BM.independent, False)
        
        self.assertEqual(ISOCountry.BN.independent, True)
        
        self.assertEqual(ISOCountry.BO.independent, True)
        
        
        self.assertEqual(ISOCountry.BQ.independent, False)
        
        self.assertEqual(ISOCountry.BR.independent, True)
        
        self.assertEqual(ISOCountry.BS.independent, True)
        
        self.assertEqual(ISOCountry.BT.independent, True)
        
        
        self.assertEqual(ISOCountry.BV.independent, False)
        
        self.assertEqual(ISOCountry.BW.independent, True)
        
        
        
        self.assertEqual(ISOCountry.BY.independent, True)
        
        self.assertEqual(ISOCountry.BZ.independent, True)
        
        self.assertEqual(ISOCountry.CA.independent, True)
        
        self.assertEqual(ISOCountry.CC.independent, False)
        
        self.assertEqual(ISOCountry.CD.independent, True)
        
        self.assertEqual(ISOCountry.CF.independent, True)
        
        self.assertEqual(ISOCountry.CG.independent, True)
        
        self.assertEqual(ISOCountry.CH.independent, True)
        
        self.assertEqual(ISOCountry.CI.independent, True)
        
        self.assertEqual(ISOCountry.CK.independent, False)
        
        self.assertEqual(ISOCountry.CL.independent, True)
        
        self.assertEqual(ISOCountry.CM.independent, True)
        
        self.assertEqual(ISOCountry.CN.independent, True)
        
        self.assertEqual(ISOCountry.CO.independent, True)
        
        
        
        self.assertEqual(ISOCountry.CR.independent, True)
        
        
        
        
        self.assertEqual(ISOCountry.CU.independent, True)
        
        self.assertEqual(ISOCountry.CV.independent, True)
        
        self.assertEqual(ISOCountry.CW.independent, False)
        
        self.assertEqual(ISOCountry.CX.independent, False)
        
        self.assertEqual(ISOCountry.CY.independent, True)
        
        self.assertEqual(ISOCountry.CZ.independent, True)
        
        
        self.assertEqual(ISOCountry.DE.independent, True)
        
        
        self.assertEqual(ISOCountry.DJ.independent, True)
        
        self.assertEqual(ISOCountry.DK.independent, True)
        
        self.assertEqual(ISOCountry.DM.independent, True)
        
        self.assertEqual(ISOCountry.DO.independent, True)
        
        
        
        self.assertEqual(ISOCountry.DZ.independent, True)
        
        
        self.assertEqual(ISOCountry.EC.independent, True)
        
        self.assertEqual(ISOCountry.EE.independent, True)
        
        
        self.assertEqual(ISOCountry.EG.independent, True)
        
        self.assertEqual(ISOCountry.EH.independent, False)
        
        
        
        self.assertEqual(ISOCountry.ER.independent, True)
        
        self.assertEqual(ISOCountry.ES.independent, True)
        
        self.assertEqual(ISOCountry.ET.independent, True)
        
        
        
        
        
        self.assertEqual(ISOCountry.FI.independent, True)
        
        self.assertEqual(ISOCountry.FJ.independent, True)
        
        self.assertEqual(ISOCountry.FK.independent, False)
        
        
        self.assertEqual(ISOCountry.FM.independent, True)
        
        self.assertEqual(ISOCountry.FO.independent, False)
        
        
        self.assertEqual(ISOCountry.FR.independent, True)
        
        
        self.assertEqual(ISOCountry.GA.independent, True)
        
        self.assertEqual(ISOCountry.GB.independent, True)
        
        
        self.assertEqual(ISOCountry.GD.independent, True)
        
        
        self.assertEqual(ISOCountry.GE.independent, True)
        
        self.assertEqual(ISOCountry.GF.independent, False)
        
        self.assertEqual(ISOCountry.GG.independent, False)
        
        self.assertEqual(ISOCountry.GH.independent, True)
        
        self.assertEqual(ISOCountry.GI.independent, False)
        
        self.assertEqual(ISOCountry.GL.independent, False)
        
        self.assertEqual(ISOCountry.GM.independent, True)
        
        self.assertEqual(ISOCountry.GN.independent, True)
        
        self.assertEqual(ISOCountry.GP.independent, False)
        
        self.assertEqual(ISOCountry.GQ.independent, True)
        
        self.assertEqual(ISOCountry.GR.independent, True)
        
        self.assertEqual(ISOCountry.GS.independent, False)
        
        self.assertEqual(ISOCountry.GT.independent, True)
        
        self.assertEqual(ISOCountry.GU.independent, False)
        
        self.assertEqual(ISOCountry.GW.independent, True)
        
        self.assertEqual(ISOCountry.GY.independent, True)
        
        self.assertEqual(ISOCountry.HK.independent, False)
        
        self.assertEqual(ISOCountry.HM.independent, False)
        
        self.assertEqual(ISOCountry.HN.independent, True)
        
        self.assertEqual(ISOCountry.HR.independent, True)
        
        self.assertEqual(ISOCountry.HT.independent, True)
        
        self.assertEqual(ISOCountry.HU.independent, True)
        
        
        
        
        self.assertEqual(ISOCountry.ID.independent, True)
        
        self.assertEqual(ISOCountry.IE.independent, True)
        
        self.assertEqual(ISOCountry.IL.independent, True)
        
        self.assertEqual(ISOCountry.IM.independent, False)
        
        self.assertEqual(ISOCountry.IN.independent, True)
        
        self.assertEqual(ISOCountry.IO.independent, False)
        
        self.assertEqual(ISOCountry.IQ.independent, True)
        
        self.assertEqual(ISOCountry.IR.independent, True)
        
        self.assertEqual(ISOCountry.IS.independent, True)
        
        self.assertEqual(ISOCountry.IT.independent, True)
        
        
        self.assertEqual(ISOCountry.JE.independent, False)
        
        self.assertEqual(ISOCountry.JM.independent, True)
        
        self.assertEqual(ISOCountry.JO.independent, True)
        
        self.assertEqual(ISOCountry.JP.independent, True)
        
        
        self.assertEqual(ISOCountry.KE.independent, True)
        
        self.assertEqual(ISOCountry.KG.independent, True)
        
        self.assertEqual(ISOCountry.KH.independent, True)
        
        self.assertEqual(ISOCountry.KI.independent, True)
        
        self.assertEqual(ISOCountry.KM.independent, True)
        
        self.assertEqual(ISOCountry.KN.independent, True)
        
        self.assertEqual(ISOCountry.KP.independent, True)
        
        self.assertEqual(ISOCountry.KR.independent, True)
        
        self.assertEqual(ISOCountry.KW.independent, True)
        
        self.assertEqual(ISOCountry.KY.independent, False)
        
        self.assertEqual(ISOCountry.KZ.independent, True)
        
        self.assertEqual(ISOCountry.LA.independent, True)
        
        self.assertEqual(ISOCountry.LB.independent, True)
        
        self.assertEqual(ISOCountry.LC.independent, True)
        
        
        self.assertEqual(ISOCountry.LI.independent, True)
        
        self.assertEqual(ISOCountry.LK.independent, True)
        
        self.assertEqual(ISOCountry.LR.independent, True)
        
        self.assertEqual(ISOCountry.LS.independent, True)
        
        self.assertEqual(ISOCountry.LT.independent, True)
        
        self.assertEqual(ISOCountry.LU.independent, True)
        
        self.assertEqual(ISOCountry.LV.independent, True)
        
        self.assertEqual(ISOCountry.LY.independent, True)
        
        self.assertEqual(ISOCountry.MA.independent, True)
        
        self.assertEqual(ISOCountry.MC.independent, True)
        
        self.assertEqual(ISOCountry.MD.independent, True)
        
        self.assertEqual(ISOCountry.ME.independent, True)
        
        self.assertEqual(ISOCountry.MF.independent, False)
        
        self.assertEqual(ISOCountry.MG.independent, True)
        
        self.assertEqual(ISOCountry.MH.independent, True)
        
        
        self.assertEqual(ISOCountry.MK.independent, True)
        
        self.assertEqual(ISOCountry.ML.independent, True)
        
        self.assertEqual(ISOCountry.MM.independent, True)
        
        self.assertEqual(ISOCountry.MN.independent, True)
        
        self.assertEqual(ISOCountry.MO.independent, False)
        
        self.assertEqual(ISOCountry.MP.independent, False)
        
        self.assertEqual(ISOCountry.MQ.independent, False)
        
        self.assertEqual(ISOCountry.MR.independent, True)
        
        self.assertEqual(ISOCountry.MS.independent, False)
        
        self.assertEqual(ISOCountry.MT.independent, True)
        
        self.assertEqual(ISOCountry.MU.independent, True)
        
        self.assertEqual(ISOCountry.MV.independent, True)
        
        self.assertEqual(ISOCountry.MW.independent, True)
        
        self.assertEqual(ISOCountry.MX.independent, True)
        
        self.assertEqual(ISOCountry.MY.independent, True)
        
        self.assertEqual(ISOCountry.MZ.independent, True)
        
        self.assertEqual(ISOCountry.NA.independent, True)
        
        self.assertEqual(ISOCountry.NC.independent, False)
        
        self.assertEqual(ISOCountry.NE.independent, True)
        
        self.assertEqual(ISOCountry.NF.independent, False)
        
        self.assertEqual(ISOCountry.NG.independent, True)
        
        
        self.assertEqual(ISOCountry.NI.independent, True)
        
        self.assertEqual(ISOCountry.NL.independent, True)
        
        self.assertEqual(ISOCountry.NO.independent, True)
        
        self.assertEqual(ISOCountry.NP.independent, True)
        
        
        self.assertEqual(ISOCountry.NR.independent, True)
        
        
        self.assertEqual(ISOCountry.NU.independent, False)
        
        self.assertEqual(ISOCountry.NZ.independent, True)
        
        
        self.assertEqual(ISOCountry.OM.independent, True)
        
        self.assertEqual(ISOCountry.PA.independent, True)
        
        
        self.assertEqual(ISOCountry.PE.independent, True)
        
        self.assertEqual(ISOCountry.PF.independent, False)
        
        self.assertEqual(ISOCountry.PG.independent, True)
        
        self.assertEqual(ISOCountry.PH.independent, True)
        
        
        self.assertEqual(ISOCountry.PK.independent, True)
        
        self.assertEqual(ISOCountry.PL.independent, True)
        
        self.assertEqual(ISOCountry.PM.independent, False)
        
        self.assertEqual(ISOCountry.PN.independent, False)
        
        self.assertEqual(ISOCountry.PR.independent, False)
        
        self.assertEqual(ISOCountry.PS.independent, False)
        
        self.assertEqual(ISOCountry.PT.independent, True)
        
        
        self.assertEqual(ISOCountry.PW.independent, True)
        
        self.assertEqual(ISOCountry.PY.independent, True)
        
        
        self.assertEqual(ISOCountry.QA.independent, True)
        
        
        
        
        self.assertEqual(ISOCountry.RE.independent, False)
        
        
        
        
        
        
        
        self.assertEqual(ISOCountry.RO.independent, True)
        
        
        self.assertEqual(ISOCountry.RS.independent, True)
        
        self.assertEqual(ISOCountry.RU.independent, True)
        
        self.assertEqual(ISOCountry.RW.independent, True)
        
        self.assertEqual(ISOCountry.SA.independent, True)
        
        self.assertEqual(ISOCountry.SB.independent, True)
        
        self.assertEqual(ISOCountry.SC.independent, True)
        
        self.assertEqual(ISOCountry.SD.independent, True)
        
        self.assertEqual(ISOCountry.SE.independent, True)
        
        
        self.assertEqual(ISOCountry.SG.independent, True)
        
        self.assertEqual(ISOCountry.SH.independent, False)
        
        self.assertEqual(ISOCountry.SI.independent, True)
        
        self.assertEqual(ISOCountry.SJ.independent, False)
        
        self.assertEqual(ISOCountry.SK.independent, True)
        
        
        self.assertEqual(ISOCountry.SL.independent, True)
        
        self.assertEqual(ISOCountry.SM.independent, True)
        
        self.assertEqual(ISOCountry.SN.independent, True)
        
        self.assertEqual(ISOCountry.SO.independent, True)
        
        self.assertEqual(ISOCountry.SR.independent, True)
        
        self.assertEqual(ISOCountry.SS.independent, True)
        
        self.assertEqual(ISOCountry.ST.independent, True)
        
        
        self.assertEqual(ISOCountry.SV.independent, True)
        
        self.assertEqual(ISOCountry.SX.independent, False)
        
        self.assertEqual(ISOCountry.SY.independent, True)
        
        self.assertEqual(ISOCountry.SZ.independent, True)
        
        
        self.assertEqual(ISOCountry.TC.independent, False)
        
        self.assertEqual(ISOCountry.TD.independent, True)
        
        self.assertEqual(ISOCountry.TF.independent, False)
        
        self.assertEqual(ISOCountry.TG.independent, True)
        
        self.assertEqual(ISOCountry.TH.independent, True)
        
        self.assertEqual(ISOCountry.TJ.independent, True)
        
        self.assertEqual(ISOCountry.TK.independent, False)
        
        self.assertEqual(ISOCountry.TL.independent, True)
        
        self.assertEqual(ISOCountry.TM.independent, True)
        
        self.assertEqual(ISOCountry.TN.independent, True)
        
        self.assertEqual(ISOCountry.TO.independent, True)
        
        
        self.assertEqual(ISOCountry.TR.independent, True)
        
        self.assertEqual(ISOCountry.TT.independent, True)
        
        self.assertEqual(ISOCountry.TV.independent, True)
        
        self.assertEqual(ISOCountry.TW.independent, False)
        
        self.assertEqual(ISOCountry.TZ.independent, True)
        
        self.assertEqual(ISOCountry.UA.independent, True)
        
        self.assertEqual(ISOCountry.UG.independent, True)
        
        
        self.assertEqual(ISOCountry.UM.independent, False)
        
        
        self.assertEqual(ISOCountry.US.independent, True)
        
        self.assertEqual(ISOCountry.UY.independent, True)
        
        self.assertEqual(ISOCountry.UZ.independent, True)
        
        self.assertEqual(ISOCountry.VA.independent, True)
        
        self.assertEqual(ISOCountry.VC.independent, True)
        
        
        self.assertEqual(ISOCountry.VE.independent, True)
        
        self.assertEqual(ISOCountry.VG.independent, False)
        
        self.assertEqual(ISOCountry.VI.independent, False)
        
        self.assertEqual(ISOCountry.VN.independent, True)
        
        self.assertEqual(ISOCountry.VU.independent, True)
        
        self.assertEqual(ISOCountry.WF.independent, False)
        
        
        
        
        
        self.assertEqual(ISOCountry.WS.independent, True)
        
        
        
        self.assertEqual(ISOCountry.YE.independent, True)
        
        self.assertEqual(ISOCountry.YT.independent, False)
        
        
        
        self.assertEqual(ISOCountry.ZA.independent, True)
        
        self.assertEqual(ISOCountry.ZM.independent, True)
        
        
        self.assertEqual(ISOCountry.ZW.independent, True)