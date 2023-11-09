// /////     __________________________________________________________________________________________________________________
// /////
// /////     ___________           _____    ________           .__                  _________                                    
// /////     \_   _____/  ____    /  _  \   \_____  \  _______ |__|  ____    ____   \_   ___ \   ____    _____    _____    ______
// /////      |    __)   /  _ \  /  /_\  \   /   |   \ \_  __ \|  | /  _ \  /    \  /    \  \/  /  _ \  /     \  /     \  /  ___/
// /////      |     \   (  <_> )/    |    \ /    |    \ |  | \/|  |(  <_> )|   |  \ \     \____(  <_> )|  Y Y  \|  Y Y  \ \___ \ 
// /////      \___  /    \____/ \____|__  / \_______  / |__|   |__| \____/ |___|  /  \______  / \____/ |__|_|  /|__|_|  //____  >
// /////          \/                    \/          \/                          \/          \/               \/       \/      \/ 
// /////
// /////                                                                             FG Falcon Diagnostic Utility - by Jakka351
// /////     __________________________________________________________________________________________________________________
// /////      |--------------------------------------------------------------------------------------------------------------|
// /////      |https://github.com/jakka351/FG-Falcon| bjakkaleighton@gmail.com | https://github.com/jakka351/FG-Falcon-Hidden|
// /////      |--------------------------------------------------------------------------------------------------------------|
// /////      | Copyright (c) 2022/2023 Benjamin Jack Leighton                                                               |          
// /////      | All rights reserved.                                                                                         |
// /////      |--------------------------------------------------------------------------------------------------------------|
// /////        Redistribution and use in source and binary forms, with or without modification, are permitted provided that
// /////        the following conditions are met:
// /////        1.    With the express written consent of the copyright holder.
// /////        2.    Redistributions of source code must retain the above copyright notice, this
// /////              list of conditions and the following disclaimer.
// /////        3.    Redistributions in binary form must reproduce the above copyright notice, this
// /////              list of conditions and the following disclaimer in the documentation and/or other
// /////              materials provided with the distribution.
// /////        4.    Neither the name of the organization nor the names of its contributors may be used to
// /////              endorse or promote products derived from this software without specific prior written permission.
// /////      _________________________________________________________________________________________________________________
// /////      THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
// /////      INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// /////      DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// /////      SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// /////      SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
// /////      WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
// /////      USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
// /////      _________________________________________________________________________________________________________________
// /////
// /////       This software can only be distributed with my written permission. It is for my own educational purposes and  
// /////       is potentially dangerous to ECU health and safety. Gracias a Gato Blancoford desde las alturas del mar de chelle.                                                        
// /////      _________________________________________________________________________________________________________________
// /////
// /////
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//6.3.1 DTC Classifications
//There are two classifications of DTCs that an ECU shall support:
//• Continuous DTCs
//• On-demand DTCs, see Section 10.4 for more information regarding on-demand DTCs.
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
namespace FGCOM
{
	public partial class Orion
	{
		/////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
		//
		//   ██████╗██╗     ███████╗ █████╗ ██████╗     ██████╗ ████████╗ ██████╗
		//  ██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗    ██╔══██╗╚══██╔══╝██╔════╝
		//  ██║     ██║     █████╗  ███████║██████╔╝    ██║  ██║   ██║   ██║     
		//  ██║     ██║     ██╔══╝  ██╔══██║██╔══██╗    ██║  ██║   ██║   ██║     
		//  ╚██████╗███████╗███████╗██║  ██║██║  ██║    ██████╔╝   ██║   ╚██████╗
		//   ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝    ╚═╝    ╚═════╝                                                                       
		// s
		/////////////////////////////////////////////////////////////////////////////
		/// CLEART DIAGNOSTIC TROUBLE CODES TOP MENU ITEM FUNCTION REQUESTS THE CURRENTLY SELECTED ECU TO CLEAR FAULT CODES
		/// SERVICE 0x14 CLEAR DTC - PSR 0x54 NRC 0x7F
		/// Parses the response and instructs the operator on the outcome need to provide direction on appropriate action for operator in case of
		/// a negative response.
		/// ////////////////////////////////////
		/// SID CLEAR DTC:                  0x14
		/// SID READ  DTC:                  0x15 
		/// SID CONT CODE:                  0x22
		/// DID LOCATION FOR CONT. CODES: 0xE6F3
		////////////////////////////////////////
		/// CAN LOG:
		///   (1662865757.573871) can0 726#0322E6F300000000
		///   (1662865757.582868) can0 72E#0462E6F30C000000
		///   (1662865757.586310) can0 726#0322020000000000
		///   (1662865757.592949) can0 72E#0462020000000000
		///   (1662865757.599693) can0 720#0322E6F300000000
		///   (1662865757.602675) can0 728#0462E6F30A000000
		///   (1662865757.605856) can0 720#0322020000000000
		///   (1662865757.612718) can0 728#0462020000000000
		///   (1662865759.195110) can0 726#0314FF0000000000
		///   (1662865759.204603) can0 72E#0354FF0000000000
		///   (1662865760.531975) can0 720#0314FF0000000000
		///   (1662865760.562499) can0 728#0354FF0000000000
		///   (1662865764.141895) can0 726#041800FF00000000
		///   (1662865764.149996) can0 72E#0258000000000000
		///   (1662865764.439037) can0 720#041800FF00000000
		///   (1662865764.442910) can0 728#0258000000000000
		/////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
		void clearDtc()
		{
			//textBoxVinCode.Text.ToCharArray
			hidesend = 1;
			Enabled = false;
			dtcFlag = false;
			waitfor = 0x54;
			addTxt1("[0x14 clearDiagnosticInfo]\r\n");
			Write("14FF00\r");
			if (timeout == 0)
			{
				delayloop(0xFA);
				int sidByte = rxBuf[1];
				switch (sidByte)
				{
					case 0x54:
						textBoxDtc.Text += "Diagnostic Codes Cleared Successfuly \r\n";
						addTxt1("Diagnostic Codes Cleared Successfuly \r\n");
						break;
					case 0x7F:
						textBoxDtc.Text += "DTC Clearing Fail\r\n";
						textBoxDtc.Text += printerr(rxBuf[3]) + "\r\n";
						addTxt1("Diagnostic Codes failed to clear \r\n");
						break;
					default:
						addTxt1("No Response from ECU...\r\n");
						break;
				}
			}
			textBoxDtc.Text = "";
			waitfor = 0x00;
			Enabled = true;
			return;

		}
		//////////////////////////////////////////////////////////////////
		// 16.7 Mandatory PIDs 
		// Table 16.3 defines the mandatory PIDs that shall be supported by all ECUs connected to the diagnostic 
		// link connectosr. 
		// PID Description Classification Size 
		// $0200 Number of Continuous DTCs NUM 1 Byte 
		// $0202 Number of DTCs from most recent test NUM 1 Byte 
		// Global Diagnostic Specification – Part One R&VT/EESE - Core Systems Engineering Dept. 
		// FORD CONFIDENTIAL Page 70 of 148 4/25/03, version 2003.0 
		// $D100 ECU Operating State / Mode SED 1 Byte 
		// $E200 Software Version Number PKT 3 Bytes 
		// $E217 Part Number Identification Base PKT 4 Bytes 
		// $E219 Part Number Identification Suffix PKT 2 Bytes 
		// $E21A Part Number Identification Prefix PKT 4 Bytes 
		// Table 16.3 Mandatory Supported PIDs 
		// 16.7.1 Number of Continuous DTCs (PID $0200) 
		// The Number of Continuous DTCs PID contains the number of continuous DTCs currently being stored by 
		// the ECU. 
		// 16.7.2 Number of Trouble Codes Set Due to Diagnostic Test (PID $0202) 
		// The number of trouble codes Set due to diagnostic test PID contains the number of on-demand DTCs 
		// generated during the most recent diagnostic test executed by an ECU. 
		// 16.7.3 ECU Operating State (PID $D100) 
		// ECU Operating State PID contains the ECU’s current operating state/mode, see Table 16.4.


		///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		//   ██████╗ ██████╗ ███╗   ██╗████████╗██╗███╗   ██╗██╗   ██╗ ██████╗ ██╗   ██╗███████╗    ██████╗ ████████╗ ██████╗
		//  ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██║████╗  ██║██║   ██║██╔═══██╗██║   ██║██╔════╝    ██╔══██╗╚══██╔══╝██╔════╝
		//  ██║     ██║   ██║██╔██╗ ██║   ██║   ██║██╔██╗ ██║██║   ██║██║   ██║██║   ██║███████╗    ██║  ██║   ██║   ██║     
		//  ██║     ██║   ██║██║╚██╗██║   ██║   ██║██║╚██╗██║██║   ██║██║   ██║██║   ██║╚════██║    ██║  ██║   ██║   ██║     
		//  ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║██║ ╚████║╚██████╔╝╚██████╔╝╚██████╔╝███████║    ██████╔╝   ██║   ╚██████╗
		//   ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝    ╚═════╝    ╚═╝    ╚═════╝
		//                                                                                                                   
		///////////////////////////////////////////////////////////////////////////////////
		/// READ STANDARD AND CONTINUOUS DIAGNOSTIC CODES - SERVICE 0X18, 0X22
		/// 
		///	6.3.2.3 Reporting Continuous DTCs (Ford-9141, SCP and UBP)
		///	In response to a Request Parameter by PID (mode $22) message, with the address set to $0200 - Number
		///	of Continuous DTCs, an ECU shall return a Report Parameter by PID (mode $62) message with the
		///	number of continuous DTCs currently logged. In response to a single Request Stored Codes (mode $13)
		///	message, an ECU shall report all continuous DTCs logged by returning as many consecutive Report
		///	Stored Codes (mode $53) messages as is required. Refer to Table 6.4 for an example of the number of
		///	consecutive messages returned in relation to the number of continuous codes in a module.
		///	NOTE: There is no provision for a tester to request, or for an ECU to report, less than all of the
		///	continuous DTCs logged by a module.
		///	Continuous DTCs
		///	Logged
		///	Messages
		///	Returned
		///	Method
		///	0 1 All six Bytes of the message reserved for three DTCs shall be padded with $00
		///	1 or 2 1 DTC(s) in Data Bytes 2 & 3 and/or Data Bytes 4 & 5; the remaining Bytes shall be
		///	padded with $00
		///	3 1 All three DTCs shall be reported in Data Bytes 2 to 7 of the message
		///	4 or 5 2 The first message shall return three DTCs. The second message shall follow the
		///	method used for one or two DTCs as explained above
		///	6 2 Each message shall return three DTCs
		///	n m Follow the same method presented above for four to six DTCs
		///	Table 6.4 Consecutive Messages Returned When Reporting DTCs
		/// <summary>
		/// CONTINUOUS DTC AND STANDARD DTC READ AND CLEAR LOG
		/// </summary>

		public string dtc(int a, string dtc)
		{
			switch (a)
			{
				case 0x58:
					if (rxBuf[2] > 0x00)
					{
						dtc += rxBuf[2].ToString() + rxBuf[3].ToString();
					}
					if (rxBuf[4] > 0x00)
					{
						dtc += rxBuf[4].ToString() + rxBuf[5].ToString();
					}
					if (rxBuf[6] > 0x00)
					{
						dtc += rxBuf[6].ToString() + rxBuf[7].ToString();
					}
					textBoxDtc.Text += "Fault Code:" + dtc + "\r\n";
					addTxt1("Fault Code:" + dtc + "\r\n");
					dtcFlag = false;
					break;
				case 0x62:
					if (rxBuf[2] > 0x00)
					{
						dtc += rxBuf[2].ToString() + rxBuf[3].ToString();
					}
					if (rxBuf[4] > 0x00)
					{
						dtc += rxBuf[4].ToString() + rxBuf[5].ToString();
					}
					if (rxBuf[6] > 0x00)
					{
						dtc += rxBuf[6].ToString() + rxBuf[7].ToString();
					}
					textBoxDtc.Text += "Fault Code:" + dtc + "\r\n";
					addTxt1("Fault Code:" + dtc + "\r\n");
					dtcFlag = false;
					break;
				case 0x7F:
					addTxt1("[DEV] string dtc(7F) \r\n");
					addTxt1("Reading DTC Failed...\r\n");
					break;
			}
			Enabled = true;
			return dtc;
			//waitfor = 0;
		}

		void readContinuousCodes()
		{
			string detectedFaultCodes = "";
			Enabled = false;
			hidesend = 0;
			readingDtc_pictureBox.Enabled = true;
			readingDtc_pictureBox.Visible = true;
			dtcFlag = true;
			if (comboBoxBaBfFgFgx.SelectedIndex == 0x02) // FG2 
			{
				startDiagnosticSession(standardDiagnosticUds);
			}
			else
			{
				startDiagnosticSession(standardDiagnostic);
			}
			addTxt1("[0x18 readDTCByStatus] \r\n");
			textBoxDtc.Text += "Reading Diagnostic Fault Memory\r\n";
			waitfor = 0x58;
			addTxt1("Reading Standard Codes\r\n");
			Write("1800FF00\r");
			if (timeout == 0)
			{
				delayloop(0xFA);
				int sidByte = rxBuf[1];
				dtc(sidByte, detectedFaultCodes);
				waitfor = 0;
			}
			dtcFlag = true;
			waitfor = 0x62;
			addTxt1("Reading Continous Trouble Code Memory #1: \r\n");
			Write("22E6F3\r");
			if (timeout == 0)
			{
				delayloop(0xFA);
				int sidByte = rxBuf[1];
				dtc(sidByte, detectedFaultCodes);
				waitfor = 0;
			}
			waitfor = 0x62;
			dtcFlag = true;
			addTxt1("Reading Continous Trouble Code Memory #2: \r\n");
			Write("220200\r");
			if (timeout == 0)
			{
				delayloop(0xFA);
				int sidByte = rxBuf[1];
				dtc(sidByte, detectedFaultCodes);
				waitfor = 0;
			}
			waitfor = 0x62;
			dtcFlag = true;
			addTxt1("Number of Fault Codes from Recent Test: \r\n");
			Write("220202\r");
			if (timeout == 0)
			{
				delayloop(0xFA);
				int sidByte = rxBuf[1];
				switch (sidByte)
				{
					case 0x7F:
						addTxt1("Error.\r\n");
					    break;
					case 0x62:
						dtc(sidByte, detectedFaultCodes);
						break;
					default:
						addTxt1("No Response from ECU ... \r\n");
						break;
				}
			    int faultCodesFromRecentTest = rxBuf[5];
			    if (faultCodesFromRecentTest > 0x00)
			    {
			    	addTxt1("Codes:" + faultCodesFromRecentTest + "\r\n");
			    }
				// rx response 04 62 02 02 00 00 00 00 if no codes from test
				waitfor = 0;
			}
			//reset();
			hidesend = 1;
			readingDtc_pictureBox.Enabled = false;
			readingDtc_pictureBox.Visible = false;
			dtcFlag = false;
			Enabled = true;
			return;
		}
		// fault code parser via FGCOM.Orion.faultCodeDefinitions
		// if (string in FGCOM.Orion.faultCodeDefinitions)
		// {
		//	   print string to textBoxDTC
		//	}
		///////////////////////////////////////////////////////////////////////////////
		/// <summary>
		/// CLEAR DTC ALL MSCAN ECU FUNCTION
		/// </summary>
		/////////////////////////////////////////////////////////////////////////////
		void clearAllDTCAllModules()
		{
			hidesend = 1;
			Enabled = false;
			dtcFlag = false;
			reset2Aim();
			clearDtc();
			reset2Acm();
			clearDtc();
			reset2Bem();
			clearDtc();
			reset2Bpm();
			clearDtc();
			reset2Fdim();
			clearDtc();
			reset2Ipc();
			clearDtc();
			reset2Pam();
			clearDtc();
			textBoxDtc.Text = "";
			hidesend = 0;
			Enabled = true;
			reset();
			return;
		}
		///////////////////////////////////////////////////////////////////////////////////////////////
		///
		///
		///                                        
		///////////////////////////////////////////////////////////////////////////////////////////
		void readAllDTCForAllModules()
		{
			Enabled = false;
			hidesend = 1;
			dtcFlag = true;
			addTxt1("Reading Standard Diagnostic Trouble Codes...\r\n");
			if (instrumentCluster = true)
			{
				dtcFlag = true;
				reset2Ipc();
				addTxt1("IPC Fault Codes:\r\n");
				readContinuousCodes();
			}
			if (bodyElectronicModule = true)
			{
				dtcFlag = true;
				reset2Bem();
				addTxt1("BEM Fault Codes:\r\n");
				readContinuousCodes();
			}
			if (audioControlModule = true)
			{
				dtcFlag = true;
				reset2Acm();
				addTxt1("ACM Fault Codes:\r\n");
				readContinuousCodes();
			}
			if (parkingAidModule = true)
			{
				dtcFlag = true;
				reset2Pam();
				addTxt1("PAM Fault Codes:");
				readContinuousCodes();
			}
			if (audioInterfaceModule = true)
			{
				dtcFlag = true;
				reset2Aim();
				addTxt1("AIM Fault Codes:");
				readContinuousCodes();
			}
			if (bluetoothPhoneModule = true)
			{
				dtcFlag = true;
				reset2Bpm();
				addTxt1("BPM Fault Codes:");
				readContinuousCodes();
			}
			if (frontDisplayInterfaceModule = true)
			{
				dtcFlag = true;
				reset2Fdim();
				addTxt1("FDIM Fault Codes:");
				readContinuousCodes();
			}
			reset();
			waitfor = 0;
			hidesend = 1;
			dtcFlag = false;
			Enabled = true;
			return;
		}
	}
}

