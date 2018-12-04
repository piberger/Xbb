
import ROOT
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()

###
##Check the regression sys
###

#pathin_ = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V24/TEST2/ZmmH.BestCSV.heppy.DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1.root'
#
#f = ROOT.TFile.Open(pathin_)
#t = f.Get("tree")
#
#
#VarList = ['HCSV_reg_corrSYSUD_mass_CAT','HCSV_reg_corrSYSUD_pt_CAT', 'HCSV_reg_corrSYSUD_eta_CAT', 'HCSV_reg_corrSYSUD_phi_CAT','Jet_pt_reg_corrSYSUD_CAT_INDEX0','Jet_pt_reg_corrSYSUD_CAT_INDEX1', 'Sum$(Jet_pt_reg_corrSYSUD_CAT>30&&abs(Jet_eta)<2.4&&Jet_puId==7&&Jet_id>0&&aJCidx!=(hJCidx[0])&&(aJCidx!=(hJCidx[1])))']

###
##Check the BDT sys
###

#pathin_ = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/ZllHbb13TeV_V25/mva_v8_TEST/ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1/tree_VHBB_HEPPY_V25_ggZH_HToBB_ZToLL_M125_13TeV_powheg_Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6_ext1-v1_4_a4085e20b6f3529b24861250b2d0c6748eed84fb3c9aaa402e946fba.root'

#TT

# global path
pathin_ = 'root://t3dcachedb03.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/gaperrin/VHbb/VHbbPostNano2016_V4_Zvv/MVA/v3/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/'

samples = [
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_121_431eec543c586d7843839b0e4fea5846e068ed7c3cd75a00d552af18.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_28_7cd5911f7dc275a52184645bef1d865a1e3a8ae2272eb1ec6dade307.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_91_730e08f709d817a974901c3cf67349cf469a047fb156c58f93556cf5.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_6_869062750a566e103496b1f7ce735bff0a369e5fbbc53c0b52eb9d24.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_14_8c6fbc0a982b43afeacc48055aa58c899f974d7d06afb944df975238.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_64_e6fdd2ae26f3f4f3b7d75227f4796e940e8a963f3ad9b57435d1975b.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_96_97c72d331c544479214aa141e16f307e54bc64639bf9e0daa624a1e6.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_46_f20faac835c18c85cc10398b9b19fa7d3d058c93fa772c408b85fb49.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_19_b0b85a54c349151b657689e022365a316956e19bec0134e1ee30701c.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_78_0cb82acb35b533f6530ae5d6701068636b638a6d9fa9926dccc9bff2.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_37_b9996b644a07b160e1eee413490909dfae271658db39e8a9f408efa1.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_55_0f65841083eb9e7a52e9f0b5f746d07e6ead131da7f27a798a4502dd.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_41_dbace567e2d342d98d519ff1265a3d4b12baabe2f4cfe53247142361.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_126_7a05575ff6ab3d0368f676db5ad00430b759f9e685c010cf41ca40df.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_112_0e39c5c22892961f8cd3d7b8d127cb23a7812b25c61eebdf3fdd2eb8.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_117_d1a0684acc0e14fc8697be33af2b13492251df946aaad850b04024ae.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_32_4c0353bb061b75bcdfe4fe4e71f5d87f691c03c3af70d8b3358b4688.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_73_9a0d4f2d9a0811e2cda0809600b8ab60e97c4b3492848a6c6bbee342.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_69_f655f8416ce6f7b3140033bc823a57733d080eb520eae151e320c0b7.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_23_0da7ce09510da629a7eb2d550e5fd064bad1b830feb14591dbb44a50.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_50_98a2e4b4a9c2e5e6083f7ea457df808beab14e3ae54b4750d4896926.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_1_ba7510e8d00ff2342b75294d393722e1b496ff20b5c37f79d631a9a6.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_103_2fc24634303e63bff6e9fe675430dcd15d48057ee774788d1f6b01b5.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_108_5779db05e30001366ac7f9495d85b217631cf03182934a76d1b893e0.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_87_79ffcf6e518d22040ae196835036337f323d38be993d740fa80455cb.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_82_17e43b1ca7b61d2538927c061e353bfc4c24f6b7c6a2f64e3d717f3a.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_29_7d1940cc8664dd8f6ca4bc897d5e0471eab42ac32507cd8b736c6993.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_47_b4919e914247118756594805c9dc321902cb22ffd01974fb50cae955.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_38_93ca37f4a0561d19f5fdafe98f40fa579ccb485107153d1c20e1a12a.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_56_46cb2416b8271bfca014a486880c6f71d38c1414a5d2f476372111f8.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_122_1565b9799f6aefb1bd1e87b8bc5c3f20ab436179ee7ea527839052ba.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_33_f2ca10b875cbb34779626b1fabe51af787bf6736c177ac0ea89b36ac.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_92_e5fe30704bb4badf3d6fb8d6579699b2211cff43b6c5e4d9f9e5a029.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_60_561b879c3ec59dc79bd8fa4bfe8f4747a5aa4e662f047d68b6cc0e16.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_15_e6f482b2885925cd192d5c14313482021916965756cda403455cb034.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_2_dca9765a4dff130cd377d6096373d0a71c2966254ee7dc29ec799bde.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_79_4210700b8898958f4d9979de5f8cf82f304267c15e1534fb72618631.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_118_f9496d110cf6bbfbbfe170006249a59d43a9c43004a9af31589bafac.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_127_e783e90fd25a87d47a6a15542d9fd9ad8c681cdeb3458aa834a37d33.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_51_f75f17d6585b0a2c7ad896b5c155eb0805b83c30e0aaa05e5c4e3d06.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_65_5436b4c1158c08d64feef3ca3908d72e3cecd6255924e19fe6964ba5.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_42_c56dc8c0cf671d6d0a84f39723cdd9ab9c8d40ee700507c50e7e7923.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_97_6687718f5a1478edf7e39af52094bdbd9de0313d5d3bb07c60887d11.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_74_a0cca1f5c13cf0942905ff120e2d0ae0d1eacce4cf9e0de39390b847.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_7_6ba9fba0eca83b8d82470757fa66246b1152d3a04736121d88a6ccca.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_104_b3add2d34559184565da93faefff78e254e1708e7a6f3969a89700f4.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_113_2a88f1b85ca6e0ed3de8c2e3f5fd5508c38602690d8ca8dea2265c71.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_88_604d92ca240844d5f2b4b26a519a65e5176989e5e0ffb3153fb32c2f.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_24_f8c6d5d242749bedb8583acdc11aff2d707b9e4d10d3a397aedc6410.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_10_86907b50ce9e54b8c28fceb70eee61560daad8eb0f991aff27de0b5b.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_109_d3dd80abc012e752fc51969c1694e9ce86479e8abb1d0723e7550f07.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_83_8be4241d83339c16ea01c2b4dbfeeca596af56a53ee2e37bfbf387e1.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_48_0c82da09e625150083bfd16e3bfbd06b07b653b747ff0e5ed11443bf.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_39_3254d9154162f0100fd32aca328a597e1747cc5146eda5594f79783e.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_34_0760c45a9ed456742ff01df42bc779da466e04b8935c7da93c5bfaca.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_61_33d3b76d09fbe3102651e05713cfecc684604730c13661a331f8b001.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_93_93bf17276ffc2f1adf435596621f55bf4cd2e56f71cecb2671ef1e24.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_3_1d2b228314ac72750bb930f43cc35fd17688fe791fec4b592e151e2b.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_20_4ae53cd7a6bd21679c4a559c63753544afb3debe0f32adac82b50b48.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_66_321db0f8537b20be16ba0778f1f090e195756971cf9ea13f04cdebee.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_57_2f935710409cf32488ecdbe888aee81e3c1020539bad69e24ce5a248.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_43_5560662178a4c2da7ca88f89097e80c8d24091fbbbfd771a765f1476.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_98_532a8ebf742c72563f6dbaa272e2919587befa1b7a184c6c24de25d8.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_8_2544ff392c6748faeaed5a8ce7d950cdd0e8f26c2fcd68a872810b5e.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_89_06a2137772bffb914fdd946ec46d23caa317882d7ce7908f06ad20b7.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_123_161b85c18a33b657a6aad85157808ebf5a2124ed22fef59754d0aabb.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_16_47148e474770778d5ca9bc50522fbeb9c661b32dbb97e06903ae10e6.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_128_2bf811164b3e3e8d087eb4f1a7fa09b5a999759fe98aa684187708b7.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_119_df5163e2f3fea8d2e618ed63b85aa3852951105b44afdadd077a3916.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_100_2ae7c832d813c876a33c844b4f905ccea9ea676d4470cf60dc37b013.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_75_ea6da9752f2741ce0df6ae894e1f451b9c7ac3afbc0f60a144c1e680.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_25_b9f070919949aa8c1f877d65810f3e945245e326149bbbe4cfcf1298.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_70_ac4e35fef9443611140ab69bc2c4fcd73d71025cb6ec0f9680cbee71.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_105_ba07a19af1fe5fc9f971d2dbd10297fc15ad24a721fda52218be2920.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_52_8760426ea0448c459d612c6c49ca0386dd477e257da5fe7a0203f420.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_11_7925706321f1ffe64347b9219a2a58b4d57396bb7900799325089cfd.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_84_19e62b69e6894d0d2a28ba81509feccd1ce8cf61258c401d6404c368.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_114_2648b0c299c0701a846c4ae72735abfac820dc578a8698804e4f8a37.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_129_bf86828fd3156caf202a78c3e0dec9e1ae1ad27772e4663b4a51edda.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_49_883a08d815a10e32bbf4d1500b631390d2cd4ff97868d4629f0c6aab.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_62_27471465f340d43863974e4bb74468e41dcc3fbc3f33e613b816b31d.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_35_ff8db476344fb3f70b39c3876d75cacfa440318998e315864b5be4d7.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_67_21586f50ff75a9175941a159db01900f0d6e2485a50313f7992b44ed.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_4_833db14465286b21b71550dcae1a67cd401b9e9fb16148b3fa44e2a4.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_80_ac4249352d516606285fc5aa7ead45803e2057f55f791d4c3e9b8fde.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_17_0e6cae23988393b2d62bf00b974288424367b67b024af5528cd3ee27.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_9_0a680cf84cf1d923cc47afa9aa458798e4c215fa89765f83d4c17e00.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_94_c3daeb55445ac5246fd6c688133762c5360c55c7b2a91fea9ff477d0.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_12_fa5e1ae1081c9df6463785d845d5b01def4d6f6cae4189638da52f8d.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_76_17efce8f690e579f893474082a8e59256096cf6a21450c3189558af4.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_21_cc70d9420a899f4639639f9ec18cd0605621c755241c93712a16b4a8.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_30_043c099a8fd1bf42550488240658e9cc294d4ffbd2606b12a9816a3d.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_26_638f79459bc7ac9e29fbffcbe5529ad2aa8ca80c85edf6502325697c.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_58_e4d0a85e8054bb32a8f4064ca89a4742cd537ba41398445a6d3000d0.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_99_a82f7befef4b2b63cf7e2f00a287f8c875fc3f1f689879b3a6d701b4.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_44_080c5bef000cef8dfe767ce0b21489e47f7a438a5b0146ff8fd1f1f7.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_101_14a73a20d6447f575b0b3057ec6fab50b9c5b1295b910f7c59508efe.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_124_61a17c7e6d0805414549a808d714d71da67f146208b0e88c81d32f67.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_106_1917be2255997df18dc49e949f70a7a8bce09f1d865591b8d52ae938.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_85_9436bfb291d062373c8e143d27dad7fe7a605ba0efab664e1604bcae.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_71_182630982ba2d878ea15467d41369a13ab6322f42195808a7c6a39fd.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_110_396ea7b5b6310070ed93e708e851449349093de32ec6aa5092bea62a.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_53_eb39246f2c24270199666504cecee0490dab1da708bdfe2102a70ffd.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_115_260610ca1f10110503621bcc92b7e59c71d6c2cf94aa98c547feedaf.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_13_e48d2bfd3d4ce25b0218388a0f5a77c170fbbe7d5304769f786a5d58.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_5_714746a50f14c002da39ed6c7c88204ee5940653e64c5ea475e9657f.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_63_0a394153f787eee6f3b0dde7288c30aa58caedcd1150ccce92dd617f.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_68_67e3a50f90f4417645e5b62d3789362e832d3733d9fa73313246ea0c.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_36_22d59d730e8fce954d6a3fb2df0b913ada41a02db78b5ec12b1de0e6.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_40_731112e6cb91f7ca796ec4510896e4447b0a808c06ef227b2ea21cdf.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_81_df76e14411644a4e9aee11bcf33575443d1e9a9839c9d5f88a0d0f64.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_95_0ee3bcf8f6211c9af75213ed9e315fc1f59995b15d2e28f51b01f347.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_18_ea2567846620e1c925e42f8df9dbb2ba59513a0b5cf90d22a37971f5.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_31_a0b14286c101d622bfcff4a09e01f9a842f8f69607543f93c92ea1aa.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_22_2f29982ce3d7db814831d45b450fe0ab9be374e0bfdd9fc76353d509.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_77_71870fe65e4a0c32053aab4f236b8c18882a27a3aaa691962d4416d5.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_90_590123016f1a0388d56cbe62eb0fba0890255a87026c0f8077828d9f.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_120_e9f58a292bdd1b1987dcf41f3f619a432e233889605c9d091a7732ff.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_27_dbbd184b771e47c1d20a6e96d3e44c849ff9291b2fe24110378514eb.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_59_966d7c8784c2ba18979e766d357a70ef885b35eaa2e822907a4f5853.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_86_a3f6239d2ba2f607a5e3798f06d20ceacb5dd22a68fa3cfc68d45cb6.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_116_81a86ae499a0f38e3758ceedf154875fad381f36d705065e99af18ee.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_72_2ca6dbe1a66f326a194181db4fd664c9deace38d2aee6ec7750488d8.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_107_f8995724ae8a98e2d0f4c15c9420ed4ed81563086738345dc3388335.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_125_9666e74e1de6961caac2c6509efcde226e53702a7b52a2d78628445a.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_45_4deab496c16aee6ed038a76fa6d4eee3dfc63def66540b620d4233fa.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_111_ae3d0e854ad398eb381505dadce87eb3bbb7082418ec0ceab1405f5e.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_102_1f187ee4d4c88e1be6ec6a15af79d467d1bbda47ceaffc385468c8a0.root',
    'tree_arizzi-RunIIMoriond17-DeepAndR133_180517_165540_0000_54_efb369daa49c9c400f359fb96829f2b2b53db7b2672d83bdad2bff61.root'
    ]

##TChain
t = ROOT.TChain('Events')
for sample in samples:
    t.Add(pathin_+sample+'/Events')


##TFile
#f = ROOT.TFile.Open(pathin_)
#t = f.Get("tree")


#VarList = ['H_mass_noFSR_SYS_UD']
VarList = ['BDT_Znn_Opt5.SYS_UD']
#VarList = ['top_mass_SYS_UD','H_mass_SYS_UD']

JECsys = ['jer','jesAbsoluteStat','jesAbsoluteScale','jesAbsoluteFlavMap','jesAbsoluteMPFBias','jesFragmentation','jesSinglePionECAL','jesSinglePionHCAL','jesFlavorQCD','jesRelativeJEREC1','jesRelativeJEREC2','jesRelativeJERHF','jesRelativePtBB','jesRelativePtEC1','jesRelativePtEC2','jesRelativePtHF','jesRelativeBal','jesRelativeFSR','jesRelativeStatFSR','jesRelativeStatEC','jesRelativeStatHF','jesPileUpDataMC','jesPileUpPtRef','jesPileUpPtBB','jesPileUpPtEC1','jesPileUpPtEC2','jesPileUpPtHF','jesPileUpMuZero','jesPileUpEnvelope','jesTotal']

SysList = JECsys
UDList = ['Up','Down']
#CatList = ['HighCentral','LowCentral','HighForward','LowForward']
AxisList = {'mass':[20,0,400],'HCSV_reg_pt':[20,0,400],'phi':[20,-3.2, 3.2],'eta':[20,0,5],'Jet_pt':[20,0,300],'CMVA':[20,-1,1],'BDT':[20,-1,1]}
for var in VarList:
    for syst in SysList:
        #for cat in CatList:
        c = ROOT.TCanvas('c','c',800,800) 
        pad1 = ROOT.TPad('pad1','pad1', 0, 0.3, 1, 1.0)
        pad1.SetBottomMargin(0)
        pad1.SetGridx()
        pad1.Draw()
        pad1.cd()

        nbin = 0
        xmin = 0
        xmax = 0
        var_nom = var.replace('.SYS_UD','.Nominal').replace('_SYS','').replace('_UD','').replace('_CAT','').replace('_corr','').replace('.SYS_UD','.Nominal')
        for axis in AxisList:
            if axis in var_nom:
                nbin = AxisList[axis][0]
                xmin = AxisList[axis][1]
                xmax = AxisList[axis][2]

        h_nom = ROOT.TH1D('h_nom','h_nom',nbin, xmin, xmax)
        print 'var nom is', var_nom
        if 'Jet_pt' in var_nom:
            if '_INDEX0'in var_nom: t.Draw(var_nom.replace('_INDEX0','[hJidxCMVA[0]]')+'>>h_nom')
            elif '_INDEX1'in var_nom: t.Draw(var_nom.replace('_INDEX1','[hJidxCMVA[1]]')+'>>h_nom')
        else:
            t.Draw(var_nom+'>>h_nom')
        print 'Drawn'
        h_nom.SetLineColor(1)
        h_nom.SetMarkerStyle(20)
        h_nom.SetMarkerColor(1)
        h_nom.SetLineWidth(2)
        h_nom.Sumw2()

        h_ud = {} 
        for ud in UDList:
            #fill Dic
            SysDic = {}
            SysDic['var'] = var 
            SysDic['sys'] = syst
            SysDic['UD'] = ud 
            #SysDic['cat'] = cat 
            #SysDic['varname'] = var.replace('SYS',syst).replace('UD',ud).replace('CAT',cat)
            SysDic['varname'] = var.replace('SYS',syst).replace('UD',ud)
            h_ud[ud] = ROOT.TH1D('h_%s'%ud,'h_%s'%ud,nbin, xmin, xmax)
            if 'Jet_pt' in SysDic['varname']:
                if '_INDEX0'in SysDic['varname']: 
                    t.Draw(SysDic['varname'].replace('_INDEX0','[hJCidx[0]]')+'>>h_%s'%ud)
                elif '_INDEX1'in SysDic['varname']: 
                    t.Draw(SysDic['varname'].replace('_INDEX1','[hJCidx[1]]')+'>>h_%s'%ud)
            else:
                t.Draw(SysDic['varname']+'>>h_%s'%ud)
            #h_ud[ud].Draw('same')
            #t.Draw(SysDic['varname'])

        h_nom.Draw()
        h_nom.GetXaxis().SetTitle(var_nom)
        h_ud['Up'].Draw('same')
        h_ud['Up'].SetLineColor(4)
        h_ud['Up'].SetLineStyle(4)
        h_ud['Up'].SetLineWidth(2)
        h_ud['Up'].GetYaxis().SetNdivisions(505)
        h_ud['Up'].GetYaxis().SetTitleSize(20)
        h_ud['Up'].GetYaxis().SetTitleFont(43)
        h_ud['Up'].GetYaxis().SetTitleOffset(1.55)
        h_ud['Up'].GetYaxis().SetLabelFont(43)
        h_ud['Up'].GetYaxis().SetLabelSize(15)
        h_ud['Up'].GetXaxis().SetTitleSize(20)
        h_ud['Up'].GetXaxis().SetTitleFont(43)
        h_ud['Up'].GetXaxis().SetTitleOffset(4.)
        h_ud['Up'].GetXaxis().SetLabelFont(43)
        h_ud['Up'].GetXaxis().SetLabelSize(15)
        h_ud['Up'].GetXaxis().SetTitle(var_nom)

        h_ud['Down'].Draw('same')
        h_ud['Down'].SetLineColor(2)
        h_ud['Down'].SetLineStyle(2)
        h_ud['Down'].SetLineWidth(2)


        leg = ROOT.TLegend(0.7, 0.8, 1 , 1)
        leg.AddEntry(h_nom,'nominal')
        leg.AddEntry(h_ud['Up'],'up')
        leg.AddEntry(h_ud['Down'],'down')
        leg.Draw('same')

        c.cd()
        pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
        pad2.SetTopMargin(0)
        pad2.SetBottomMargin(0.2)
        pad2.SetGridx()
        pad2.SetGridy()
        pad2.Draw()
        pad2.cd()

        ratio_up =  h_ud['Up'].Clone()
        ratio_up.Divide(h_nom) 
        ratio_up.Draw()
        ratio_up.GetYaxis().SetRangeUser(0.9,1.1)
        ratio_down =  h_ud['Down'].Clone()
        ratio_down.Divide(h_nom) 
        ratio_down.Draw('same')

        c.SaveAs('TT_SYSUpDown/'+SysDic['varname']+'.pdf')
        c.SaveAs('TT_SYSUpDown/'+SysDic['varname']+'.png')
        c.SaveAs('TT_SYSUpDown/'+SysDic['varname']+'.root')
        c.SaveAs('TT_SYSUpDown/'+SysDic['varname']+'.C')

