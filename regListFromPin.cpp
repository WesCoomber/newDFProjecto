//register list from PIN
//Make it more complete as we need
map<string, string> regMap = {
        {"(3,4)" , "edi"},
        {"(3,2)" , "di"},
        {"(4,4)" , "esi"},
        {"(4,2)" , "si"},
        {"(5,4)", "ebp"},
        {"(5,2)", "bp"},
        {"(6,4)" , "esp"},
        {"(6,2)" , "sp"},
        {"(7,4)" , "ebx"},
        {"(7,2)" , "bx"},
        {"(7,1)" , "bl"},
        {"(7,-1)" , "bh"},
        {"(8,4)" , "edx"},
        {"(8,2)" , "dx"},
        {"(8,1)" , "dl"},
        {"(8,-1)" , "dh"},
        {"(9,4)" , "ecx"},
        {"(9,2)" , "cx"},
        {"(9,1)" , "cl"},
        {"(9,-1)" , "ch"},
        {"(10,4)" , "eax"},
        {"(10,2)" , "ax"},
        {"(10,1)" , "al"},
        {"(10,-1)" , "ah"},
        {"(54,16)" , "xmm0"},
        {"(55,16)" , "xmm1"},
        {"(56,16)" , "xmm2"},
        {"(57,16)" , "xmm3"},
        {"(58,16)" , "xmm4"},
        {"(59,16)" , "xmm5"},
        {"(60,16)" , "xmm6"},
        {"(61,16)" , "xmm7"}
};
