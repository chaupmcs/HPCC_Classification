467 Computes, each has 288 points, each point has 9 dimensions namely `['CPU1 Temp', 'CPU2 Temp', 'Inlet Temp', 'Memory usage', 'Fan1 speed', 'Fan2 speed', 'Fan3 speed', 'Fan4 speed', 'Power consumption']
`

Num of clusters: 7

Color of clusters: 
`colors_dict ={0:"#1f77b4",
1:"#ff7f0e",
2:"#2ca02c",
3:"#d62728",
4:"#9467bd",
5:"#8c564b",
6:"#e377c2"}`

Running time:
 + Run SHAP for each compute: 276.05 seconds
 + Run SHAP for all computes (combine all the computes into 1 data): 84.33 seconds. 
 Results for the combine data:
 [SHAP_VALUES](https://github.com/chaupmcs/HPCC_Classification/blob/master/SHAP_HPCC_cluster/SHAP_For_All_Computes/shap_dataframe/shap_importance_TotalData.csv); [SHAP_PICTURE](https://github.com/chaupmcs/HPCC_Classification/blob/master/SHAP_HPCC_cluster/SHAP_For_All_Computes/shap_pictures/dot_plot_TotalData.png) 

Results:
 + 235 computes were skipped because they have only 1 label
 + Num of computes having SHAP: 232 + 1 (TotalData)  

 + SHAP values: https://github.com/chaupmcs/HPCC_Classification/tree/master/SHAP_HPCC_cluster/SHAP_For_All_Computes/shap_dataframe
 + SHAP picture: https://github.com/chaupmcs/HPCC_Classification/tree/master/SHAP_HPCC_cluster/SHAP_For_All_Computes/shap_pictures
 
 ----
 List of skip: Format "computeName_Index"
 
`['compute-1-10_1', 'compute-1-13_4', 'compute-1-14_5', 'compute-1-18_9', 'compute-1-19_10', 'compute-1-22_14', 'compute-1-23_15', 'compute-1-24_16', 'compute-1-26_18', 'compute-1-29_21', 'compute-1-3_22', 'compute-1-30_23', 'compute-1-31_24', 'compute-1-36_29', 'compute-1-37_30', 'compute-1-4_33', 'compute-1-40_34', 'compute-1-42_36', 'compute-1-43_37', 'compute-1-45_39', 'compute-1-46_40', 'compute-1-47_41', 'compute-1-49_43', 'compute-1-53_48', 'compute-1-55_50', 'compute-1-58_53', 'compute-1-59_54', 'compute-1-6_55', 'compute-1-60_56', 'compute-1-7_57', 'compute-1-8_58', 'compute-10-26_61', 'compute-10-27_62', 'compute-10-28_63', 'compute-10-30_65', 'compute-10-31_66', 'compute-10-33_68', 'compute-10-34_69', 'compute-10-35_70', 'compute-10-36_71', 'compute-10-37_72', 'compute-10-38_73', 'compute-10-39_74', 'compute-10-40_75', 'compute-10-41_76', 'compute-10-44_79', 'compute-2-1_80', 'compute-2-10_81', 'compute-2-12_83', 'compute-2-19_90', 'compute-2-2_91', 'compute-2-20_92', 'compute-2-22_94', 'compute-2-26_98', 'compute-2-29_101', 'compute-2-30_103', 'compute-2-32_105', 'compute-2-33_106', 'compute-2-37_110', 'compute-2-40_114', 'compute-2-42_116', 'compute-2-43_117', 'compute-2-46_120', 'compute-2-49_123', 'compute-2-5_124', 'compute-2-50_125', 'compute-2-53_128', 'compute-2-54_129', 'compute-2-56_131', 'compute-2-57_132', 'compute-2-60_136', 'compute-2-9_139', 'compute-3-10_141', 'compute-3-11_142', 'compute-3-13_144', 'compute-3-14_145', 'compute-3-15_146', 'compute-3-16_147', 'compute-3-17_148', 'compute-3-19_150', 'compute-3-2_151', 'compute-3-20_152', 'compute-3-22_154', 'compute-3-23_155', 'compute-3-25_157', 'compute-3-26_158', 'compute-3-29_161', 'compute-3-31_164', 'compute-3-33_166', 'compute-3-35_168', 'compute-3-36_169', 'compute-3-40_174', 'compute-3-44_178', 'compute-3-45_179', 'compute-3-46_180', 'compute-3-5_184', 'compute-3-51_186', 'compute-3-53_188', 'compute-3-54_189', 'compute-3-55_190', 'compute-3-7_193', 'compute-3-8_194', 'compute-3-9_195', 'compute-4-1_196', 'compute-4-10_197', 'compute-4-12_199', 'compute-4-18_205', 'compute-4-19_206', 'compute-4-2_207', 'compute-4-22_210', 'compute-4-23_211', 'compute-4-24_212', 'compute-4-27_215', 'compute-4-3_218', 'compute-4-31_220', 'compute-4-34_223', 'compute-4-36_225', 'compute-4-37_226', 'compute-4-38_227', 'compute-4-39_228', 'compute-4-40_230', 'compute-4-42_232', 'compute-4-43_233', 'compute-4-44_234', 'compute-4-47_237', 'compute-4-48_238', 'compute-4-5_239', 'compute-4-6_240', 'compute-4-7_241', 'compute-4-8_242', 'compute-4-9_243', 'compute-5-11_246', 'compute-5-14_249', 'compute-5-15_250', 'compute-5-16_251', 'compute-5-17_252', 'compute-5-4_262', 'compute-5-6_264', 'compute-5-8_266', 'compute-6-10_269', 'compute-6-12_271', 'compute-6-15_274', 'compute-6-17_276', 'compute-6-18_277', 'compute-6-19_278', 'compute-6-5_283', 'compute-6-6_284', 'compute-6-8_286', 'compute-7-11_290', 'compute-7-14_293', 'compute-7-15_294', 'compute-7-18_297', 'compute-7-19_298', 'compute-7-21_301', 'compute-7-23_303', 'compute-7-26_306', 'compute-7-27_307', 'compute-7-28_308', 'compute-7-32_313', 'compute-7-33_314', 'compute-7-34_315', 'compute-7-35_316', 'compute-7-36_317', 'compute-7-40_321', 'compute-7-42_323', 'compute-7-43_324', 'compute-7-45_326', 'compute-7-46_327', 'compute-7-47_328', 'compute-7-49_330', 'compute-7-51_333', 'compute-7-6_342', 'compute-7-9_346', 'compute-8-10_348', 'compute-8-11_349', 'compute-8-12_350', 'compute-8-15_353', 'compute-8-16_354', 'compute-8-17_355', 'compute-8-18_356', 'compute-8-19_357', 'compute-8-24_363', 'compute-8-27_366', 'compute-8-28_367', 'compute-8-29_368', 'compute-8-3_369', 'compute-8-31_371', 'compute-8-32_372', 'compute-8-34_374', 'compute-8-35_375', 'compute-8-38_378', 'compute-8-39_379', 'compute-8-42_383', 'compute-8-43_384', 'compute-8-46_387', 'compute-8-47_388', 'compute-8-48_389', 'compute-8-5_391', 'compute-8-50_392', 'compute-8-53_395', 'compute-8-54_396', 'compute-8-57_399', 'compute-8-59_401', 'compute-8-6_402', 'compute-8-8_405', 'compute-8-9_406', 'compute-9-1_407', 'compute-9-11_409', 'compute-9-13_411', 'compute-9-14_412', 'compute-9-16_414', 'compute-9-17_415', 'compute-9-19_417', 'compute-9-2_418', 'compute-9-20_419', 'compute-9-23_422', 'compute-9-24_423', 'compute-9-25_424', 'compute-9-26_425', 'compute-9-27_426', 'compute-9-3_429', 'compute-9-32_432', 'compute-9-33_433', 'compute-9-41_442', 'compute-9-45_446', 'compute-9-47_448', 'compute-9-48_449', 'compute-9-49_450', 'compute-9-5_451', 'compute-9-50_452', 'compute-9-52_454', 'compute-9-55_457', 'compute-9-57_459', 'compute-9-59_461', 'compute-9-7_464']`
 
