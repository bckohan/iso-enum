"""The standard enum type for ISO 3166-1 common countrys"""
from enum_properties import (
    s,
    p
)
from django_enum import TextChoices
#from django.utils.translation import gettext as _


class ISOCountry(
    TextChoices,
    s('numeric'),
    s('alpha3', case_fold=True),
    p('independent'),
    s('full_name', case_fold=True)
):
    """
    An enumeration for ISO 3166-1 Country codes.
    """

    _symmetric_builtins_ = [s('label', case_fold=True)]

    
    AD = "AD", "Andorra", 20, "AND", True, "the Principality of Andorra"
    AE = "AE", "United Arab Emirates (the)", 784, "ARE", True, "the United Arab Emirates"
    AF = "AF", "Afghanistan", 4, "AFG", True, "the Islamic Republic of Afghanistan"
    AG = "AG", "Antigua and Barbuda", 28, "ATG", True, "Antigua and Barbuda"
    
    AI = "AI", "Anguilla", 660, "AIA", False, "Anguilla"
    AL = "AL", "Albania", 8, "ALB", True, "the Republic of Albania"
    AM = "AM", "Armenia", 51, "ARM", True, "the Republic of Armenia"
    
    AO = "AO", "Angola", 24, "AGO", True, "the Republic of Angola"
    
    AQ = "AQ", "Antarctica", 10, "ATA", False, "Antarctica"
    AR = "AR", "Argentina", 32, "ARG", True, "the Argentine Republic"
    AS = "AS", "American Samoa", 16, "ASM", False, "American Samoa"
    AT = "AT", "Austria", 40, "AUT", True, "the Republic of Austria"
    AU = "AU", "Australia", 36, "AUS", True, "Australia"
    AW = "AW", "Aruba", 533, "ABW", False, "Aruba"
    AX = "AX", "Åland Islands", 248, "ALA", False, "Åland Islands"
    AZ = "AZ", "Azerbaijan", 31, "AZE", True, "the Republic of Azerbaijan"
    BA = "BA", "Bosnia and Herzegovina", 70, "BIH", True, "Bosnia and Herzegovina"
    BB = "BB", "Barbados", 52, "BRB", True, "Barbados"
    BD = "BD", "Bangladesh", 50, "BGD", True, "the People's Republic of Bangladesh"
    BE = "BE", "Belgium", 56, "BEL", True, "the Kingdom of Belgium"
    BF = "BF", "Burkina Faso", 854, "BFA", True, "Burkina Faso"
    BG = "BG", "Bulgaria", 100, "BGR", True, "the Republic of Bulgaria"
    BH = "BH", "Bahrain", 48, "BHR", True, "the Kingdom of Bahrain"
    BI = "BI", "Burundi", 108, "BDI", True, "the Republic of Burundi"
    BJ = "BJ", "Benin", 204, "BEN", True, "the Republic of Benin"
    BL = "BL", "Saint Barthélemy", 652, "BLM", False, "Saint Barthélemy"
    BM = "BM", "Bermuda", 60, "BMU", False, "Bermuda"
    BN = "BN", "Brunei Darussalam", 96, "BRN", True, "Brunei Darussalam"
    BO = "BO", "Bolivia (Plurinational State of)", 68, "BOL", True, "the Plurinational State of Bolivia"
    
    BQ = "BQ", "Bonaire, Sint Eustatius and Saba", 535, "BES", False, "Bonaire, Sint Eustatius and Saba"
    BR = "BR", "Brazil", 76, "BRA", True, "the Federative Republic of Brazil"
    BS = "BS", "Bahamas (the)", 44, "BHS", True, "the Commonwealth of the Bahamas"
    BT = "BT", "Bhutan", 64, "BTN", True, "the Kingdom of Bhutan"
    
    BV = "BV", "Bouvet Island", 74, "BVT", False, "Bouvet Island"
    BW = "BW", "Botswana", 72, "BWA", True, "the Republic of Botswana"
    
    
    BY = "BY", "Belarus", 112, "BLR", True, "the Republic of Belarus"
    BZ = "BZ", "Belize", 84, "BLZ", True, "Belize"
    CA = "CA", "Canada", 124, "CAN", True, "Canada"
    CC = "CC", "Cocos (Keeling) Islands (the)", 166, "CCK", False, "Cocos (Keeling) Islands (the)"
    CD = "CD", "Congo (the Democratic Republic of the)", 180, "COD", True, "the Democratic Republic of the Congo"
    CF = "CF", "Central African Republic (the)", 140, "CAF", True, "the Central African Republic"
    CG = "CG", "Congo (the)", 178, "COG", True, "the Republic of the Congo"
    CH = "CH", "Switzerland", 756, "CHE", True, "the Swiss Confederation"
    CI = "CI", "Côte d'Ivoire", 384, "CIV", True, "the Republic of Côte d'Ivoire"
    CK = "CK", "Cook Islands (the)", 184, "COK", False, "Cook Islands (the)"
    CL = "CL", "Chile", 152, "CHL", True, "the Republic of Chile"
    CM = "CM", "Cameroon", 120, "CMR", True, "the Republic of Cameroon"
    CN = "CN", "China", 156, "CHN", True, "the People's Republic of China"
    CO = "CO", "Colombia", 170, "COL", True, "the Republic of Colombia"
    
    
    CR = "CR", "Costa Rica", 188, "CRI", True, "the Republic of Costa Rica"
    
    
    
    CU = "CU", "Cuba", 192, "CUB", True, "the Republic of Cuba"
    CV = "CV", "Cabo Verde", 132, "CPV", True, "the Republic of Cabo Verde"
    CW = "CW", "Curaçao", 531, "CUW", False, "Curaçao"
    CX = "CX", "Christmas Island", 162, "CXR", False, "Christmas Island"
    CY = "CY", "Cyprus", 196, "CYP", True, "the Republic of Cyprus"
    CZ = "CZ", "Czechia", 203, "CZE", True, "the Czech Republic"
    
    DE = "DE", "Germany", 276, "DEU", True, "the Federal Republic of Germany"
    
    DJ = "DJ", "Djibouti", 262, "DJI", True, "the Republic of Djibouti"
    DK = "DK", "Denmark", 208, "DNK", True, "the Kingdom of Denmark"
    DM = "DM", "Dominica", 212, "DMA", True, "the Commonwealth of Dominica"
    DO = "DO", "Dominican Republic (the)", 214, "DOM", True, "the Dominican Republic"
    
    
    DZ = "DZ", "Algeria", 12, "DZA", True, "the People's Democratic Republic of Algeria"
    
    EC = "EC", "Ecuador", 218, "ECU", True, "the Republic of Ecuador"
    EE = "EE", "Estonia", 233, "EST", True, "the Republic of Estonia"
    
    EG = "EG", "Egypt", 818, "EGY", True, "the Arab Republic of Egypt"
    EH = "EH", "Western Sahara*", 732, "ESH", False, "Western Sahara*"
    
    
    ER = "ER", "Eritrea", 232, "ERI", True, "the State of Eritrea"
    ES = "ES", "Spain", 724, "ESP", True, "the Kingdom of Spain"
    ET = "ET", "Ethiopia", 231, "ETH", True, "the Federal Democratic Republic of Ethiopia"
    
    
    
    
    FI = "FI", "Finland", 246, "FIN", True, "the Republic of Finland"
    FJ = "FJ", "Fiji", 242, "FJI", True, "the Republic of Fiji"
    FK = "FK", "Falkland Islands (the) [Malvinas]", 238, "FLK", False, "Falkland Islands (the) [Malvinas]"
    
    FM = "FM", "Micronesia (Federated States of)", 583, "FSM", True, "the Federated States of Micronesia"
    FO = "FO", "Faroe Islands (the)", 234, "FRO", False, "Faroe Islands (the)"
    
    FR = "FR", "France", 250, "FRA", True, "the French Republic"
    
    GA = "GA", "Gabon", 266, "GAB", True, "the Gabonese Republic"
    GB = "GB", "United Kingdom of Great Britain and Northern Ireland (the)", 826, "GBR", True, "the United Kingdom of Great Britain and Northern Ireland"
    
    GD = "GD", "Grenada", 308, "GRD", True, "Grenada"
    
    GE = "GE", "Georgia", 268, "GEO", True, "Georgia"
    GF = "GF", "French Guiana", 254, "GUF", False, "French Guiana"
    GG = "GG", "Guernsey", 831, "GGY", False, "Guernsey"
    GH = "GH", "Ghana", 288, "GHA", True, "the Republic of Ghana"
    GI = "GI", "Gibraltar", 292, "GIB", False, "Gibraltar"
    GL = "GL", "Greenland", 304, "GRL", False, "Greenland"
    GM = "GM", "Gambia (the)", 270, "GMB", True, "the Republic of the Gambia"
    GN = "GN", "Guinea", 324, "GIN", True, "the Republic of Guinea"
    GP = "GP", "Guadeloupe", 312, "GLP", False, "Guadeloupe"
    GQ = "GQ", "Equatorial Guinea", 226, "GNQ", True, "the Republic of Equatorial Guinea"
    GR = "GR", "Greece", 300, "GRC", True, "the Hellenic Republic"
    GS = "GS", "South Georgia and the South Sandwich Islands", 239, "SGS", False, "South Georgia and the South Sandwich Islands"
    GT = "GT", "Guatemala", 320, "GTM", True, "the Republic of Guatemala"
    GU = "GU", "Guam", 316, "GUM", False, "Guam"
    GW = "GW", "Guinea-Bissau", 624, "GNB", True, "the Republic of Guinea-Bissau"
    GY = "GY", "Guyana", 328, "GUY", True, "the Co-operative Republic of Guyana"
    HK = "HK", "Hong Kong", 344, "HKG", False, "the Hong Kong Special Administrative Region of China"
    HM = "HM", "Heard Island and McDonald Islands", 334, "HMD", False, "Heard Island and McDonald Islands"
    HN = "HN", "Honduras", 340, "HND", True, "the Republic of Honduras"
    HR = "HR", "Croatia", 191, "HRV", True, "the Republic of Croatia"
    HT = "HT", "Haiti", 332, "HTI", True, "the Republic of Haiti"
    HU = "HU", "Hungary", 348, "HUN", True, "Hungary"
    
    
    
    ID = "ID", "Indonesia", 360, "IDN", True, "the Republic of Indonesia"
    IE = "IE", "Ireland", 372, "IRL", True, "Ireland"
    IL = "IL", "Israel", 376, "ISR", True, "the State of Israel"
    IM = "IM", "Isle of Man", 833, "IMN", False, "Isle of Man"
    IN = "IN", "India", 356, "IND", True, "the Republic of India"
    IO = "IO", "British Indian Ocean Territory (the)", 86, "IOT", False, "British Indian Ocean Territory (the)"
    IQ = "IQ", "Iraq", 368, "IRQ", True, "the Republic of Iraq"
    IR = "IR", "Iran (Islamic Republic of)", 364, "IRN", True, "the Islamic Republic of Iran"
    IS = "IS", "Iceland", 352, "ISL", True, "the Republic of Iceland"
    IT = "IT", "Italy", 380, "ITA", True, "the Republic of Italy"
    
    JE = "JE", "Jersey", 832, "JEY", False, "Jersey"
    JM = "JM", "Jamaica", 388, "JAM", True, "Jamaica"
    JO = "JO", "Jordan", 400, "JOR", True, "the Hashemite Kingdom of Jordan"
    JP = "JP", "Japan", 392, "JPN", True, "Japan"
    
    KE = "KE", "Kenya", 404, "KEN", True, "the Republic of Kenya"
    KG = "KG", "Kyrgyzstan", 417, "KGZ", True, "the Kyrgyz Republic"
    KH = "KH", "Cambodia", 116, "KHM", True, "the Kingdom of Cambodia"
    KI = "KI", "Kiribati", 296, "KIR", True, "the Republic of Kiribati"
    KM = "KM", "Comoros (the)", 174, "COM", True, "the Union of the Comoros"
    KN = "KN", "Saint Kitts and Nevis", 659, "KNA", True, "Saint Kitts and Nevis"
    KP = "KP", "Korea (the Democratic People's Republic of)", 408, "PRK", True, "the Democratic People's Republic of Korea"
    KR = "KR", "Korea (the Republic of)", 410, "KOR", True, "the Republic of Korea"
    KW = "KW", "Kuwait", 414, "KWT", True, "the State of Kuwait"
    KY = "KY", "Cayman Islands (the)", 136, "CYM", False, "Cayman Islands (the)"
    KZ = "KZ", "Kazakhstan", 398, "KAZ", True, "the Republic of Kazakhstan"
    LA = "LA", "Lao People's Democratic Republic (the)", 418, "LAO", True, "the Lao People's Democratic Republic"
    LB = "LB", "Lebanon", 422, "LBN", True, "the Lebanese Republic"
    LC = "LC", "Saint Lucia", 662, "LCA", True, "Saint Lucia"
    
    LI = "LI", "Liechtenstein", 438, "LIE", True, "the Principality of Liechtenstein"
    LK = "LK", "Sri Lanka", 144, "LKA", True, "the Democratic Socialist Republic of Sri Lanka"
    LR = "LR", "Liberia", 430, "LBR", True, "the Republic of Liberia"
    LS = "LS", "Lesotho", 426, "LSO", True, "the Kingdom of Lesotho"
    LT = "LT", "Lithuania", 440, "LTU", True, "the Republic of Lithuania"
    LU = "LU", "Luxembourg", 442, "LUX", True, "the Grand Duchy of Luxembourg"
    LV = "LV", "Latvia", 428, "LVA", True, "the Republic of Latvia"
    LY = "LY", "Libya", 434, "LBY", True, "the State of Libya"
    MA = "MA", "Morocco", 504, "MAR", True, "the Kingdom of Morocco"
    MC = "MC", "Monaco", 492, "MCO", True, "the Principality of Monaco"
    MD = "MD", "Moldova (the Republic of)", 498, "MDA", True, "the Republic of Moldova"
    ME = "ME", "Montenegro", 499, "MNE", True, "Montenegro"
    MF = "MF", "Saint Martin (French part)", 663, "MAF", False, "Saint Martin (French part)"
    MG = "MG", "Madagascar", 450, "MDG", True, "the Republic of Madagascar"
    MH = "MH", "Marshall Islands (the)", 584, "MHL", True, "the Republic of the Marshall Islands"
    
    MK = "MK", "North Macedonia", 807, "MKD", True, "the Republic of North Macedonia"
    ML = "ML", "Mali", 466, "MLI", True, "the Republic of Mali"
    MM = "MM", "Myanmar", 104, "MMR", True, "the Republic of the Union of Myanmar"
    MN = "MN", "Mongolia", 496, "MNG", True, "Mongolia"
    MO = "MO", "Macao", 446, "MAC", False, "Macao Special Administrative Region of China"
    MP = "MP", "Northern Mariana Islands (the)", 580, "MNP", False, "the Commonwealth of the Northern Mariana Islands"
    MQ = "MQ", "Martinique", 474, "MTQ", False, "Martinique"
    MR = "MR", "Mauritania", 478, "MRT", True, "the Islamic Republic of Mauritania"
    MS = "MS", "Montserrat", 500, "MSR", False, "Montserrat"
    MT = "MT", "Malta", 470, "MLT", True, "the Republic of Malta"
    MU = "MU", "Mauritius", 480, "MUS", True, "the Republic of Mauritius"
    MV = "MV", "Maldives", 462, "MDV", True, "the Republic of Maldives"
    MW = "MW", "Malawi", 454, "MWI", True, "the Republic of Malawi"
    MX = "MX", "Mexico", 484, "MEX", True, "the United Mexican States"
    MY = "MY", "Malaysia", 458, "MYS", True, "Malaysia"
    MZ = "MZ", "Mozambique", 508, "MOZ", True, "the Republic of Mozambique"
    NA = "NA", "Namibia", 516, "NAM", True, "the Republic of Namibia"
    NC = "NC", "New Caledonia", 540, "NCL", False, "New Caledonia"
    NE = "NE", "Niger (the)", 562, "NER", True, "the Republic of the Niger"
    NF = "NF", "Norfolk Island", 574, "NFK", False, "Norfolk Island"
    NG = "NG", "Nigeria", 566, "NGA", True, "the Federal Republic of Nigeria"
    
    NI = "NI", "Nicaragua", 558, "NIC", True, "the Republic of Nicaragua"
    NL = "NL", "Netherlands (the)", 528, "NLD", True, "the Kingdom of the Netherlands"
    NO = "NO", "Norway", 578, "NOR", True, "the Kingdom of Norway"
    NP = "NP", "Nepal", 524, "NPL", True, "Nepal"
    
    NR = "NR", "Nauru", 520, "NRU", True, "the Republic of Nauru"
    
    NU = "NU", "Niue", 570, "NIU", False, "Niue"
    NZ = "NZ", "New Zealand", 554, "NZL", True, "New Zealand"
    
    OM = "OM", "Oman", 512, "OMN", True, "the Sultanate of Oman"
    PA = "PA", "Panama", 591, "PAN", True, "the Republic of Panama"
    
    PE = "PE", "Peru", 604, "PER", True, "the Republic of Peru"
    PF = "PF", "French Polynesia", 258, "PYF", False, "French Polynesia"
    PG = "PG", "Papua New Guinea", 598, "PNG", True, "the Independent State of Papua New Guinea"
    PH = "PH", "Philippines (the)", 608, "PHL", True, "the Republic of the Philippines"
    
    PK = "PK", "Pakistan", 586, "PAK", True, "the Islamic Republic of Pakistan"
    PL = "PL", "Poland", 616, "POL", True, "the Republic of Poland"
    PM = "PM", "Saint Pierre and Miquelon", 666, "SPM", False, "Saint Pierre and Miquelon"
    PN = "PN", "Pitcairn", 612, "PCN", False, "Pitcairn"
    PR = "PR", "Puerto Rico", 630, "PRI", False, "Puerto Rico"
    PS = "PS", "Palestine, State of", 275, "PSE", False, "the State of Palestine"
    PT = "PT", "Portugal", 620, "PRT", True, "the Portuguese Republic"
    
    PW = "PW", "Palau", 585, "PLW", True, "the Republic of Palau"
    PY = "PY", "Paraguay", 600, "PRY", True, "the Republic of Paraguay"
    
    QA = "QA", "Qatar", 634, "QAT", True, "the State of Qatar"
    
    
    
    RE = "RE", "Réunion", 638, "REU", False, "Réunion"
    
    
    
    
    
    
    RO = "RO", "Romania", 642, "ROU", True, "Romania"
    
    RS = "RS", "Serbia", 688, "SRB", True, "the Republic of Serbia"
    RU = "RU", "Russian Federation (the)", 643, "RUS", True, "the Russian Federation"
    RW = "RW", "Rwanda", 646, "RWA", True, "the Republic of Rwanda"
    SA = "SA", "Saudi Arabia", 682, "SAU", True, "the Kingdom of Saudi Arabia"
    SB = "SB", "Solomon Islands", 90, "SLB", True, "Solomon Islands"
    SC = "SC", "Seychelles", 690, "SYC", True, "the Republic of Seychelles"
    SD = "SD", "Sudan (the)", 729, "SDN", True, "the Republic of the Sudan"
    SE = "SE", "Sweden", 752, "SWE", True, "the Kingdom of Sweden"
    
    SG = "SG", "Singapore", 702, "SGP", True, "the Republic of Singapore"
    SH = "SH", "Saint Helena, Ascension and Tristan da Cunha", 654, "SHN", False, "Saint Helena, Ascension and Tristan da Cunha"
    SI = "SI", "Slovenia", 705, "SVN", True, "the Republic of Slovenia"
    SJ = "SJ", "Svalbard and Jan Mayen", 744, "SJM", False, "Svalbard and Jan Mayen"
    SK = "SK", "Slovakia", 703, "SVK", True, "the Slovak Republic"
    
    SL = "SL", "Sierra Leone", 694, "SLE", True, "the Republic of Sierra Leone"
    SM = "SM", "San Marino", 674, "SMR", True, "the Republic of San Marino"
    SN = "SN", "Senegal", 686, "SEN", True, "the Republic of Senegal"
    SO = "SO", "Somalia", 706, "SOM", True, "the Federal Republic of Somalia"
    SR = "SR", "Suriname", 740, "SUR", True, "the Republic of Suriname"
    SS = "SS", "South Sudan", 728, "SSD", True, "the Republic of South Sudan"
    ST = "ST", "Sao Tome and Principe", 678, "STP", True, "the Democratic Republic of Sao Tome and Principe"
    
    SV = "SV", "El Salvador", 222, "SLV", True, "the Republic of El Salvador"
    SX = "SX", "Sint Maarten (Dutch part)", 534, "SXM", False, "Sint Maarten (Dutch part)"
    SY = "SY", "Syrian Arab Republic (the)", 760, "SYR", True, "the Syrian Arab Republic"
    SZ = "SZ", "Eswatini", 748, "SWZ", True, "the Kingdom of Eswatini"
    
    TC = "TC", "Turks and Caicos Islands (the)", 796, "TCA", False, "Turks and Caicos Islands (the)"
    TD = "TD", "Chad", 148, "TCD", True, "the Republic of Chad"
    TF = "TF", "French Southern Territories (the)", 260, "ATF", False, "French Southern Territories (the)"
    TG = "TG", "Togo", 768, "TGO", True, "the Togolese Republic"
    TH = "TH", "Thailand", 764, "THA", True, "the Kingdom of Thailand"
    TJ = "TJ", "Tajikistan", 762, "TJK", True, "the Republic of Tajikistan"
    TK = "TK", "Tokelau", 772, "TKL", False, "Tokelau"
    TL = "TL", "Timor-Leste", 626, "TLS", True, "the Democratic Republic of Timor-Leste"
    TM = "TM", "Turkmenistan", 795, "TKM", True, "Turkmenistan"
    TN = "TN", "Tunisia", 788, "TUN", True, "the Republic of Tunisia"
    TO = "TO", "Tonga", 776, "TON", True, "the Kingdom of Tonga"
    
    TR = "TR", "Türkiye", 792, "TUR", True, "the Republic of Türkiye"
    TT = "TT", "Trinidad and Tobago", 780, "TTO", True, "the Republic of Trinidad and Tobago"
    TV = "TV", "Tuvalu", 798, "TUV", True, "Tuvalu"
    TW = "TW", "Taiwan (Province of China)", 158, "TWN", False, "Taiwan (Province of China)"
    TZ = "TZ", "Tanzania, the United Republic of", 834, "TZA", True, "the United Republic of Tanzania"
    UA = "UA", "Ukraine", 804, "UKR", True, "Ukraine"
    UG = "UG", "Uganda", 800, "UGA", True, "the Republic of Uganda"
    
    UM = "UM", "United States Minor Outlying Islands (the)", 581, "UMI", False, "United States Minor Outlying Islands (the)"
    
    US = "US", "United States of America (the)", 840, "USA", True, "the United States of America"
    UY = "UY", "Uruguay", 858, "URY", True, "the Eastern Republic of Uruguay"
    UZ = "UZ", "Uzbekistan", 860, "UZB", True, "the Republic of Uzbekistan"
    VA = "VA", "Holy See (the)", 336, "VAT", True, "Holy See (the)"
    VC = "VC", "Saint Vincent and the Grenadines", 670, "VCT", True, "Saint Vincent and the Grenadines"
    
    VE = "VE", "Venezuela (Bolivarian Republic of)", 862, "VEN", True, "the Bolivarian Republic of Venezuela"
    VG = "VG", "Virgin Islands (British)", 92, "VGB", False, "British Virgin Islands (the)"
    VI = "VI", "Virgin Islands (U.S.)", 850, "VIR", False, "the Virgin Islands of the United States"
    VN = "VN", "Viet Nam", 704, "VNM", True, "the Socialist Republic of Viet Nam"
    VU = "VU", "Vanuatu", 548, "VUT", True, "the Republic of Vanuatu"
    WF = "WF", "Wallis and Futuna", 876, "WLF", False, "Wallis and Futuna Islands"
    
    
    
    
    WS = "WS", "Samoa", 882, "WSM", True, "the Independent State of Samoa"
    
    
    YE = "YE", "Yemen", 887, "YEM", True, "the Republic of Yemen"
    YT = "YT", "Mayotte", 175, "MYT", False, "Mayotte"
    
    
    ZA = "ZA", "South Africa", 710, "ZAF", True, "the Republic of South Africa"
    ZM = "ZM", "Zambia", 894, "ZMB", True, "the Republic of Zambia"
    
    ZW = "ZW", "Zimbabwe", 716, "ZWE", True, "the Republic of Zimbabwe"
    # pylint: disable=C0303

    @property
    def alpha2(self):
        return self.value

    @property
    def short_name(self):
        return self.label

    def __str__(self):
        """
        The string representation of this enum is its alpha-2 country code
        """
        return self.value
