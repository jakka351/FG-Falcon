# Can Ids Above 700

	 							
![image](https://user-images.githubusercontent.com/57064943/131293518-aa0cebd1-0875-4407-b406-fd59370fc62e.png)


				FORD AUSTRALIA			FALCON				FG				2008-2016				MSCAN HSCAN Pr-HSCAN LINBUS OBDII ISO90401																																																			
				MANUFACTURER			VEHICLE				CODE				MODEL YEARS				BUS																																																			
																																																																						
	Bus	TX	ID	 DLC 	Labels		Byte [0]								Byte [1]						Byte [2]		Byte [2]								Byte [3]								Byte [4]								Byte [5]								Byte [6]								Byte [7]							
	CAN	BU_	Arbitration	len	Data		Message.Data[0]								Message.Data[1]								Message.Data[2]								Message.Data[3]								Message.Data[4]								Message.Data[5]								Message.Data[6]								Message.Data[7]							
																																																																						
	Midspeed CANBus	Instrument Cluster	0x128	[8]	HighBeamStatus FogLampStatus ParkAndLowBeamStatus AutoHeadlampSwitchStatus IllumLevelDisplay IllumLevelSwitch TurnStalkSwitchStatus RearBeltMinderStatus		HeadLightsOnAuto	HeadlightsOn	FoglightsOn	HighBeamsOn													TurnStalkSwitchStatus	IndicatingLeft	IndicatingRight																						IllumLevelSwitch								RearBeltMinderStatus															
		Instrument Cluster	BO_ 296	[8]	CAN Data:		0x01	0x02 	0x06	0x0E					0xFF	0xF1							IndicatorLightsStatus	0x08	0x10						0x00	0x08	0x10						IllumLevelDisplay								IllumLevelSwitch								 															
																																																																						
	Midspeed CANBus		0x2CA	[8]																																																																		
		Instrument Cluster	BO_	[8]	CAN Data:																																																																	
																																																																						
	Midspeed CANBus		0x2C4	[8]																																																																		
			BO_	[8]	CAN Data:																																																																	
																																																																						
																																																																						
		Bluetooth Phone Module	0x2CE	[8]			Bluetooth Pairing Info Text  [ASCII Data ICC]  																																																															
			BO_	[8]	CAN Data:		0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00																																
																																																																						
		Audio Control Module	0x2D4	[8]																																																																		
		Audio Control Module	BO_		CAN Data:		0x00								0x00								0x00								0x00								0x00	0x10							0x00	0x10							0x00								0x00							
																																																																						
		Audio Control Module	0x2EC	[8]																																																																		
		Audio Control Module	BO_748		CAN Data:		0x03	0x2B	0x32						0x1E	0xC6	0xCA						0x02	0x2C	0x34						0x00	0x1E	0xD5						0x03	0x30	0x32						0x15	0x32	0xDA						0x00	0x01	0x02	0x04	0x10	0x11	0x12	0x14	0x00							
																																																																						
		Audio Control Module	0x2E1	[8]	ICC 																																																																	
		Audio Control Module	BO_ 724		CAN Data:		0x00								0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00
																																																																						
																																																																						
		Audio Control Module	0x2E2	[8]	ICC 			ICC MENU ACTIVE	ICC MENU OPTION																																																													
		Audio Control Module	BO_ 725		CAN Data:		0x00	0x01	0x04						0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00
																																																																						
		Audio Control Module	0x2E6	[8]	AudioTunedFreqency AudioTunerBandPreset AudioFMFrequencyStep RDS_PSN_State 		Message.Data[0] * 2 = AudioTunedFrequency								Message.Data[1]  = AudioFMFrequencyStep * 0.01								AM RADIO					AudioTuneBandPreset																											Preset Switches	P														
			BO_ 742		CAN Data:		Eg 100.3 FM = (Message.Data[0x32] * 2 ) + (Message.Data[ 0x1E ] * 0.01)								0x00	0xA	0x14	0x15	0x1E	0x28	0x32	0x3C	0x00	0x02	0x03	0x10	0x12				0x00								0x00								0x00								0x00	0x01	0x02						0x00							
																																																																						
		Audio Control Module	0x2EF	[8]																																																																		
		Audio Control Module	BO_ 751		CAN Data:		0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00
																																																																						
		Audio Control Module	0x2F2	[8]	AudioCurrentMediaMode		VolumeLevel = Message.Data[0] * 2 																																								irstly thank you to JasonACT for all his contribution to this thread, without his help and r&d I wouldn't be tinkering away on this project.  I found the following 2 frames wake the screen for 60 seconds before going into Power Saving Mode and set the screen brightness.  0x2F2, 8, 00x0 0x00 0x00 0x00 0x12 0x00 0x00 0x00 5th Byte defines Selected source (0x00 Screen off, 0x11 CD, 0x12 CP/MP3, 0x18 Blank main screen, 0x19 AUX)  &  0x128, 8, 0x00 0x10 0x00 0x00 0x00 0x00 0x00 0x00 2nd Byte defines screen brightness (00 > 19) 								AudioCurrentMediaMode	AUX1	AUX	ACM OFF	SteeringWheelControls	SwcPhoneBtn	SwcPhoneBtn	SwcPhoneBtn	SeekButton	SeekButton	SeekButton	SwcVolUp	SwcVolUp=0x12	SwcVolUp=0x14	SwcVolDown	SwcVolDown=0x19
		Audio Control Module		[8]	CAN Data:		0x01	0x02 	0x03	0x04	0x05	0x06	0x07	0x08	0x12								0x11								0x0E								0x09								0x49								AudioCurrentMediaMode	0x41	0x45	0x48		 0x61	0x65	 0x68	0x08	0X09	0x0C	0x11	0x12	0x14	0x18	0x19
							0x09	0x0A	0x0B	0x0C	0x0D	0x0E	0x00																																																									
		Audio Control Module	0x2F2	[8]																																																				AUX2	CD/MP3		FM1	PHONE	Audip Off		Menu Active	Audio Off						
		Audio Control Module	BO_ 754	[8]	CAN Data:																																																			0x42	0x43	0x44	0x45	0x46	0x47		0x01	0x48						
																																																																						
																																																																						
		Audio Control Module	0x2F4	[8]			[ASCII DATA]																																																															
			BO_ 756																																																																			
		Audio Control Module	0x2F5	[8]			RDS Artist Name																																																															
			BO_ 757																																																																			
		Audio Control Module	0x2F6	[8]			RadioStationMessageData [ASCII Data]								RadioStationTextData								RadioStationTextData								RadioStationTextData								RadioStationTextData								RadioStationTextData								RadioStationTextData								RadioStationTextData							
			BO_758																																																																			
		Front Entertainment Module	0x2F9	[8]	MP3_Folder MP3_Track																																																																	
			BO_ 761																																																																			
																																																																						
		Audio Control Module	0x2FC	[8]	ROTVOLENCD_RT ROTENVOLENCD_LFT AM_FM_SW BACK_HOME_SW MENU_SW_FDM AUDIO_OFF_SW OK_SW_APIM SEEK_UP_SW SEEK_DW_SW CD_-AUX_SW SCAN_SW LOAD_SW EJECT_SW_FDM PRE_1_SW(1-6)		ICC Buttons	AM_FM_SW	SCAN_SW	MENU_SW_FDM	SEEK_DW_SW	SEEK_UP_SW	CD_AUX_SW	PWR_SW	ICC Buttons	LoadCD	EjectCD 	ROTVOLENCD_RT	ROTENVOLENCD_LFT	BACK_HOME_SW	MENU_SW_FDM	AUDIO_OFF_SW	Menu Active	OK_SW_APIM							ROTVOLENCD_RT	ROTENVOLENCD_LFT	ICC Buttons	OK_SW_APIM					Menu Active	OK_SW_APIM																														
		Audio Control Module	BO_ 764		CAN Data:		0x20	0x20	0x40	0x01	0x08	0x04	0x80	0X01		0x40 	 0X80  						0x01								0x41	0x81							0x04																															
																																																																						
		Front Display Interface Module	0X307	[8]	IllumBatsaverRequest_MS		 ICC HVAC Buttons	 Close/Open Cabin	RearDemistOnOff	AcButton	AcOffBtn	WindowDefogBtn			 ICC HVAC Buttons	FanSpeedDown	FanSpeedUp	AcOffBtn	AutoACbtn	CycleVentButton				LowerTemp 	RaiseTemp					HazardSwitch			UnlockBtn	LockBtn	DSCButton																																			
		FDIM	BO_ 775	[8]	CAN Data:		0x40	0x40	0x20	0x80	0x10	0x02				0x04	0x08	0x10	0x20	0x80				0x40	0x80					0x01 | 0x80			0x84	0xC0	0x90																																			
																																																																						
		Audio Control Module	0X309	[8]	AudioRDS_PSName_1-_8		RadioStationNameData [ASCII Data ICC]																																																															
			 BO_ 777		CAN Data:		0x47								0x4F								0x4C								0x44								0x31								0x30								0x34								0x33							
							G								O								L								D 								1								0								4								3							
																																																																						
		ICC	0x313	[8]	INTACTTEMP		CabinTempSense Message.Data[0] = Temperature - 100 / 2								-__																																																							
		ICC	BO_ 787		CAN Data:		0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00	0x00
																																																																						
		ICC	0x315	[8]	Cycle Drive Away Locking Cycle Locking confirm with Indicators Cycle Confirm with horn Cycle 2 stage unlock Cycle confirm unlock with indicators Follow Me Home Lighting (X) Auto Headlight Adjustment (Y) Interior Lighting - Reset Settings Interior Lighting - On with ignition off Interior Lighting - On with key out Interior Lighting - On with door open Interior Lighting - On with unlock 			Cycle Drive Away Locking	CycleLockConfirmIndicators	CycleTwoStageUnlock	CycleConfirmUnlockIndicators 					CabLightsResetSettings	CabLightsOnDoorOpen	CabLightsOnDoorOpen	CabLightsOnUnlock					CabLightsOnIgnitionOff	CabLightsOnKeyOut	CabLightsOnKeyOut																																												
		ICC	BO_ 789	[8]	CAN Data:			0x40	0x80	0x04	0x08 					0x40 	0x80	0x80	0x20					0x04	0x20	0x20																																												
																																																																						
			0x317	[8]	VehicleIdentificationNumber		Vehicle Identification Number																																																															
			BO_ 791																																																																			
			0x30B	[8]																																																																		
			BO_ 779																																																																			
			0x30D	[8]	CD_TrackNumber  CD_Type  CD_PlayingNow																																																																	
			781																																																																			
			0x30F	[8]																																																																		
			BO_ 783																																																																			
																																																																						
		Restraints Control Module	0x330	[8]	ParkBrakeOn_MS																																																																	
		ICC	BO_ 816	[8]	CAN Data:																																																																	
		Restraints Control Module	0x340	[8]	FuelCutOffStatus																																																																	
			BO_ 832	[8]	CAN Data:																																																																	
		Restraints Control Module	0x350	[8]	RestraintIndicatorLamp																																																																	
			BO_ 848	[8]	CAN Data:																																																																	
																																																																						
		Audio Control Module	0x33D	[8]																																																																		
			BO_																																																																			
																																																																						
		HVAC Intergrated Module	0x353	[8]			Vent Position	 Foot Vents, Open Cabin	 Window and Feet Vets, Open Cabin	 Window and Feet Vents, Close Cabin	 Face, Foot, Close Cabin	 Face, Foot, Open Cabin	 Face, Open Cabin	 Face, Close Cabin									AirConPassengerTargetTemp =	 Face, Close Cabin							AirConditionerTargetTemp =								External Temperature = 								AirConditionerOff	AirConOffState															Fan Off	Fan Speed 2	Fan Speed 3	Fan Speed 4	Fan Speed 5	Fan Speed 6	Fan Speed 7	Fan Speed 8
		HVAC Intergrated Module	0x353	[8]	CAN Data:			0x2B	0x2F	0x4F	0x5B	0x3B	0x33	0x53									0x33	0x53																								0xAB															0x01	+0x02	+0x03	+0x04	+0x05	+0x06	+0x07	+0x08
		HVAC Intergrated Module	0x353	[8]			Vent Position	 Window, Auto Fan	 A/C Off, Open Cabin	 A/C Off, Foot Vents, Open Cabin	 A/C Off, Foot and Window Vents, Open Cabin	 A/C Off, Foot and Face Vents, Open Cabin	 A/C Off, Window Vents, Open Cabin	 A/C Off, Manual Fan, Open Cabin																																																	Fan Speed 9	Fan Speed Max	AC-Auto-Fan-Off	AC-Auto-Fan-Speed 2	AC-Auto-Fan-Speed 3	AC-Auto-Fan-Speed 4	AC-Auto-Fan-Speed 5	AC-Auto-Fan-Speed 6
		HVAC Intergrated Module	0x353	[8]	CAN Data:			0x26	0x83	0x8B	0x8F	0x9B	0xA6	0xA7																																																	+0x09	+0x0A	0x81	0x082	0x83	0x84	0x85	0x86
		HVAC Intergrated Module	0x353	[8]			Vent Position	 A/C Off, Foot Vents, Close Cabin	 A/C Off, Foot and Window Vents, Close Cabin	 A/C Off, Foot and Face Vents, Close Cabin	 Auto, Close Cabin	 Auto, Open Cabin	 Window, Manual Fan	 A/C Off, Close Cabin																																																	AC-Auto-Fan-Speed 7	AC-Auto-Fan-Speed 8	AC-Auto-Fan-Speed 9	AC-Auto-Fan-Speed 10				
		HVAC Intergrated Module	BO_ 851	[8]	CAN Data:			0xCB	0xCF	0xDB	0x43	0x23	0x27	0xC3																																																	0x87	0x88	0x89	0x8A				
																																																																						
		Parking Aid Module	0x360	[8]	ParkFailedFRONT_TONEFRT_CONFIHInhibitedLC_DISTLM_DISTMODSTATECCNT_PAMDisabledFLT_CONDDisturbedPAM_SW_STPARK_SYSRC_DISTREAR_SENSEREAR_TONERM_DISTSENSOR_SPL_VSPEED_DEACTSYS_OZ TRAILINSTRANSRVVBATDEACT		Sonar Active																																								Sonar Active																							
		Parking Aid Module	BO_ 864		CAN Data:		0x05																																								0xFF																							
																																																																						
		Body Electric Module	0x365	[8]	Reverse Gear Engage																																																																	
			BO_ 869		CAN Data:																																																																	
																																																																						
		Body Electric Module	0x403	[8]	RFD_Ajar LFD_Ajar RRD_Ajar LRD_Ajar BootTailgateAjar Head_lamp_fail HazardOnRequest Priority_key_1 and Priority_key_2 SmartShieldLED_Request IllumMode BonnetAjar RFD_Locked 		DriverDoorOpen	PsngrDoorOpen	RearRightDoorOpen	RearDoorsOpen	RightDoorsOpen	LeftDoorsOpen	AllDoors 					AllExceptDriverDoor	AllExceptPassengerDoor	AllExceptRearLeft						Interior Lighting - Reset Settings	Interior Lighting - On with ignition off	Interior Lighting - On with key out	Interior Lighting - On with door open	Interior Lighting - On with unlock																																								
			BO_ 1027		CAN Data:		0x82	0x42	0x22	0x34	0xA2	0x52	0xF2	0x02				0x72	0xB2	0xE2																																																		
																																																																						
		Body Electric Module	0x406	[8]	SeatbeltStatusRearLeft SeatbeltStatusRearLeft SeatbeltStatusRearCentre SeatbeltStatusRearRight										Ignition State	Ignition Off	Accessory On	Ignition On	Wake ICC				InteriorLightStatus																																															
			BO_ 1030		CAN Data:											0x01	0x02	0x04	0x05																																																			
			0x409	[8]	AdditionalBodyInformation		409#2480524440914921																																																															
			BO_ 1033																																																																			
																																																																						
			0x501	[8]			501#0C026E0000000000																																																															
			BO_ 1281		CAN Data:		0x0C								0x02								0xEE																																								0x00	0x01						
			0x50C	[8]	ACM KEEP ALIVE SIGNAL		50C#11026E0000000000																																																															
			BO_ 1292		CAN Data:		0x0C								0x02																																																0x00	0x01						
		Instrument Cluster	0x511	[8]			511#41026E0000040400																																																															
			BO_ 1297																																																																			
					541#5502000000000000																																																																	
			0x555	[8]	555#5C02000000000000																																																																	
			BO_ 1365		CAN Data:										0x02																																																0x00	0x01						
			0x55C	[8]	FDIM KEEP ALIVE SIGNAL		55C#0102000000000000																																																															
			BO_ 1372		CAN Data:		0x01								0x02																																																0x00	0x01						
		Instrument Cluster	0x640	[8]	ManualTrans																																																																	
			BO_ 1600																																																																			
		0x6F6		[8]	ImmobTransfer_PCM_1 to 8   PATS					Passive Anti Theft System																																																												
		1784																																																																				
		Instrument Cluster	0x6F8	[8]																																																																		
			BO_																																																																			
																																																																						
																																																																						
																																																																						
			0x714	[8]																																																																		
			BO_		CAN Data:		0x03								0x22								0xF4								0x0C								0x55								0x455								0x55								0x55							
																																																																						
		Instrument Cluster	0x720	[8]	IC_DiagSig_Rx		Diagnostic Service Keep Alive Signal																																																															
			BO_																																																																			
																																																																						
	HS CANBUS		0x0FC	[8]																																																																		
			BO_																																																																			
																																																																						
			0x120	[8]																			Byte 2 Byte 3 - Engine Torque minus 0x097 Byte2&3																																															
			BO_		CAN Data:																																																																	
																																																																						
		Instrument Cluster	0x128	[8]	HighBeamStatus FogLampStatus ParkAndLowBeamStatus AutoHeadlampSwitchStatus IllumLevelDisplay IllumLevelSwitch TurnStalkSwitchStatus RearBeltMinderStatus		HeadLightsOnAuto	HeadlightsOn	FoglightsOn	HighBeamsOn					:								TurnStalkSwitchStatus	IndicatingLeft	IndicatingRight														IllumLevelDisplay								IllumLevelSwitch								RearBeltMinderStatus															
		Instrument Cluster	BO_ 296	[8]	CAN Data:		0x01	0x02 	0x06	0x0E													IndicatorLightsStatus	0x08	0x10														IllumLevelDisplay								IllumLevelSwitch								 															
																																																																						
		Powertrain Control Module	0x12D	[8]	0x12D - Byte 0 - Engine Speed rate of change? / Byte 1 - Throttle Pedal (MaxValue 200) / Byte 2 - Some Shift value maybe??? / Byte 4&5 - Engine Speed * 4 / Byte 7 - Mask 0x01 Brake State Mask 0x04 Cranking State										AcceleratorPedalPosition 0%	AcceleratorPedalPosition 100%		AcceleratorPedalPosition					AcceleratorPedalPosition 0%	AcceleratorPedalPosition 100%		AcceleratorPedalPosition																			EngineRevolutionsPerMinute = (( Message.Data[4] * 255) + Message.Data[5] ) / 4										Flags??								BrakeOff  	BrakeOn			BrakeHardwareStatus			
			BO_ 301		CAN Data:										0x00	0xC8							0x00	0xC8																																							0x00	0x01						
																																																																						
		Powertrain Control Module	0X200	[8]	CrankStatusPCM_HS		(Actual Wheel Torque in N-M / Wheel torque to Engine torque) + 512.0 																(Minimum Wheel Torque in N-M / Wheel torque to Engine torque) + 512.0																 (Maximum Wheel Torque in N-M / Wheel torque to Engine torque) + 512.0 																Flags								Key-Off Timer in Minutes							
			BO_ 512		CAN Data:																																																																	
																																																																						
		Powertrain Control Module	0x207	[8]	Engine_RPM_HS VehicleSpeed_HS 		Engine RPM								Engine RPM																								Vehicle Speed = (Message.Data[4] + (Message.Data[5] /255)) * 2								Vehicle Speed = (Message.Data[4] + (Message.Data[5] /255)) * 2								ManifoldThrotPosition 0%	ManifoldThrotPosition 100%		ManifoldThrottlePosition												
			BO_ 519		Labels																 																												s						0x00	0xC8														
																																																																						
		ABS DSC Module	0x210	[8]	EBD_Failed ABS_Failed TCS_DisabledByUser TCS_Event TCS_Failed VDC_DisabledByUser VDC_Evemt VDC_Failed 																										DSC DisabledByOperator		DSC Event		DSC Failed		ABS Fault																																	
			BO_ 528		CAN Data:																																																																	
																																																																						
		PCM	0x230	[8]	TransGearPosition_HS TransOverheat TransFault TransMode 				TransMode									TargetGearPos					First Gear	2nd Gear	3rd Gear	4th Gear																																					TransOverheat	TransFault	TransMode					
			BO_ 560		CAN Data:										0xFF								0xFF	0x95	0x61	0s48	-'file:///home/agl/Documents/SecondStreetBudget.xlsx'#$Sheet1.CB1:CB1048576```BO77:BR77BQ77																																											
																																																																						
			0x3E9	[8]	TrransmissionActualGear		Reverse	Neutral	Drive[1]	Drive[2]	Drive[3]	Drive[4]	Drive[5]	Drive[6]																																																								
			BO_ 1001		CAN Data:																																																																	
																																																																						
		Restraints Control Module	0x340	[8]	RIL_RQST RIL_STAT SEATBLT_INDCTR_RQST SEATBLT_CHIME_RQST BLTMNDR_PRGRM_CONFRM_RQST RCM_STAT_DPLY_ENABLED_RCRD_HS 				                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     						AirBagWarningLight	AirBagFault	SeatBeltWarningRequest	SeatBeltChineRequest																																																				
			BO_		CAN Data:																																																																	
																																																																						
		Instrument Cluster	0x350	[8]	SEATBEAT_INDICATR_STAT RSTRNT_SEATBLTWRNCHME_STAT 																																																																	
			BO_		CAN Data:																																																																	
																																																																						
		Body Electric Module	0x403	[8]	RFD_Ajar LFD_Ajar RRD_Ajar LRD_Ajar BootTailgateAjar Head_lamp_fail HazardOnRequest Priority_key_1 and Priority_key_2 SmartShieldLED_Request IllumMode BonnetAjar RFD_Locked 																																																																	
a			BO_ 1027		CAN Data:																																																																	
			0x407	[8]																																																																		
			BO_ 1031		CAN Data:																																																																	
																																																																						
		Powertrain Control Module	0x425	[8]	Cruise CruiseTargetSetSpeed TurboBoostPressure InstantEconomyMode InstantEconomy 		Cruise	CruiseTargetSetSpeed	KeyOnEngineOff CruiseFlashing																																																													
			BO_ 1061		CAN Data:				0x01																																																													
		Powertrain Control Module	0x427	[8]	EngineCoolantTemperature ODO_Count ALT_FAILURE_STAT OilPressureWarning EngineOverheat ETC_Warning ImmobLamp MIL_Lamp FuelPulse SEATBEAT_INDICATR_STAT EngineOilPressure AC Pressure		EngineCoolantTemperature								Air Conditioner Pressure								Air Conditioner Pressure								Battery Voltage								Odometer Count								.	LowOilPressure	AlternatorFail	EngineLight	EngineLightFlash	ETC Fault	VehicleImmobilized		SystemCommmsFault								EngineLight	EngineLightFlash	ETC Fault	VehicleImmobilized	EngineSpeedCount			
			BO_ 1063		CAN Data:																																																																	
		PCM	0x437	[8]	DampedFuelLevel InstFuelValue FuelSenderFail ParkBrakeOn_HS MaxLitres 		MaxLitres			MaxLitres					Fuel								HandBrakeStatus	Handbrake Off	Handbrake On 																																						Fuel							
			BO_ 1079		CAN Data:			0x43	0x44	0x45	0x46													0x01	0x11																																													
		PCM	0x44D	[8]	EngineOilTemperature										.																								Engine Coolant Temperature								Engine Coolant Temperature								Engine Oil Temperature								Atmospheric Pressure/kPa?							
			BO_ 1101		CAN Data:																																																																	
																																																																						
			0x453	[8]	ODO ODO_Overflow 																																		ODOMETER KILOMETRES TOTAL																															
			BO_ 1107		CAN Data:																																																																	
																																																																						
			0x4B0	[8]	ABSWheelSpeedSensors		FrontLeftWheelSpeed	message.data[0] * 255 + message.data[1] = wheel speed							FrontLeftWheelSpeed	message.data[0] * 255 + message.data[1] = wheel speed							FrontRightWheelSpeed	message.data[2] * 255 + message.data[3] = wheel speed							FrontRightWheelSpeed	message.data[2] * 255 + message.data[3] = wheel speed							RearLeftWheelSpeed	message.data[4] * 255 + message.data[5] = wheel speed							RearLeftWheelSpeed	message.data[4] * 255 + message.data[5] = wheel speed							RightRearWheelSpeed	message.data[6] * 255 + message.data[7] = wheel speed							RightRearWheelSpeed	message.data[6] * 255 + message.data[7] = wheel speed						
			BO_ 1200		CAN Data:																																																																	
																																																																						
		Powertrain Control Module	0x623	[8]	CylindersEng 		( Engine Capacity Litres = Message.Data[0]  / 10 )								Engine Cylinders & Valves								Engine Aspiration								Engine Peak Torque = Message.Data[3] * 4  / 1																																							
							4.0 Litres	5.4 Litres	5.0 Litres						Unknown								Unknown	Natural Aspiration	Turbocharged	Supercharged	Petrol	LPG	DualFuel		500 Newton Metres																																							
			BO_ 1571		CAN Data:			0x36																							0x7D																																							
																																																																						
		PCM	0x640	[8]	ManualTrans		640#1000000000000000																																																															
			BO_ 1600		CAN Data:																																																																	
			0x650	[8]																																																																		
			BO_ 1616																																																																			
																																																																						
		0x6f6		[8]	ImmobTransfer_PCM_1 to 8   PATS					Passive Anti Theft System																																																												
																																																																						
			0x6f8	[8]	 																																																																	
			BO_ 1784																																																																			
			0x6fc	[8]																																																																		
			BO_ 1788																																																																			
																																																																						
																																																																						
																																																																						
			0x6f8	[8]	 																																																																	
			0x6fc	[8]																																																																		
	Private  HS CAN																																																																					
	Private  HS CAN	 Module	0x85	[8]	Yaw Rate Sensor																																																																	
			BO_																																																																			
																																																																						
		 Module	0x090	[8]	Steering		Steering Wheel Angle	message.data[0] * 255 + message.data[1]     =    steering wheel angle positive							Steering Wheel Angle	message.data[0] * -255 + message.data[1]     =    steering wheel angle negative																																																						
			BO_		CAN Data:																																																																	
																																																																						
		 Module	0x97	[8]																																																																		
			BO_																																																																			
																																																																						
																																																																						
		On Board Diagnostics	0x7E0	[8]																																																																		
			0x7E8	[8]																																																																		
																																																																						
																																																																						
	OBDII Protocol	On Board Diagnostics		[8]	Key On Engine Off On Demand Self-Test																																																																	
		OBDII		[8]	Key On Engine Running On Demand Self-Test																																																																	
		OBDII		[8]	Read system monitor status																																																																	
		OBDII		[8]	Mode 6 – Test Results fo r Specific Monitored Systems																																																																	
		OBDII		[8]	ABS On Demand Self-Test																																																																	
		OBDII		[8]	RCM On Demand Self-Test																																																																	
		OBDII		[8]	HIM On Demand Self-Test																																																																	
		OBDII		[8]	FDIM On Demand Self-Test																																																																	
		OBDII		[8]	ACM On Demand Self-Test																																																																	
		OBDII		[8]	AIM On Demand Self-Test																																																																	
		OBDII		[8]	BPM On Demand Self-Test																																																																	
				[8]	PAM On Demand Self-Test																																																																	
		OBDII		[8]	Read Fault Codes																																																																	
		OBDII		[8]	Clear Fault Codes																																																																	
	LINBUS																																																																					
																																																																						
																																																																						
																																																																						
																																																																						
																																																																						
																																																																						
	ISO 9141 (6AT)																																																																					
