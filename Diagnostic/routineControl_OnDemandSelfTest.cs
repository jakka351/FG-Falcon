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
using System;
using System.Windows.Forms;
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
namespace FGCOM
{
 	public partial class Orion
	{
		bool flagSelfTesting;
		//
		//   ██████╗ ███╗   ██╗      ██████╗ ███████╗███╗   ███╗ █████╗ ███╗   ██╗██████╗       ███████╗███████╗██╗     ███████╗ ████████╗███████╗███████╗████████╗
		//  ██╔═══██╗████╗  ██║      ██╔══██╗██╔════╝████╗ ████║██╔══██╗████╗  ██║██╔══██╗      ██╔════╝██╔════╝██║     ██╔════╝ ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
		//  ██║   ██║██╔██╗ ██║█████╗██║  ██║█████╗  ██╔████╔██║███████║██╔██╗ ██║██║  ██║█████╗███████╗█████╗  ██║     █████╗█████╗██║   █████╗  ███████╗   ██║   
		//  ██║   ██║██║╚██╗██║╚════╝██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║██║  ██║╚════╝╚════██║██╔══╝  ██║     ██╔══╝╚════╝██║   ██╔══╝  ╚════██║   ██║   
		//  ╚██████╔╝██║ ╚████║      ██████╔╝███████╗██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝      ███████║███████╗███████╗██║         ██║   ███████╗███████║   ██║   
		//   ╚═════╝ ╚═╝  ╚═══╝      ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝       ╚══════╝╚══════╝╚══════╝╚═╝         ╚═╝   ╚══════╝╚══════╝   ╚═╝   
		//                                                                                                                                                         
		/////////////////////////////////////////////////////////////////////////////////////////////////
		/// ON DEMAND SELF TEST
		/// Service 33 requestRoutineResults requires better NRC 0x78 Handling - see fjds logs for example
		/// 01/01/2023 0x31`and 0x33 request self test and request self test result handling implemented
		bool flagFaultCodesAfterSelfTest;
		public void routineControl_onDemandSelfTest()
		{

			// GFX ECU SELF TESTING JUST PUT CODE HERE TO TEST GFX NEeD TO MOVE TO ROUTINE CONTROL SELF TEST CODE
			pictureBox_selfTesting.Enabled = true;
			pictureBox_selfTesting.Visible = true;
			Enabled = false;
			hidesend = 0;
			flagSelfTesting = false;
			int attempt = 1;
			if (comboBoxBaBfFgFgx.SelectedIndex == 0x02) // FG2 
			{
				startDiagnosticSession(standardDiagnosticUds);
			}
			else
			{
				startDiagnosticSession(standardDiagnostic);
			}
			waitfor = 0x71;
			Write("310200\r");
			addTxt1("[0x31 startRoutineByLocalId]\r\n");
			if (timeout == 0) delayloop(0xFA);
			int sidByte = rxBuf[1];
			switch (sidByte)
			{
				case 0x71:
					flagSelfTesting = true;
					Write("330200\r");  // request routine results
					/// WHILE WAITING FOR SELF TEST TO COMPLETE WE ARE REQUESTING THE RESULTS OF THE SELF TEST ROUTINE 
					/// VIA SERVICE 0X33 - NEEDS TO BE TIMED CORRECTLY IN ORDER TO GET ROUTINE RESULTS VIA PSR 0X73  
					break;
				case 0x7F:
					addTxt1("Self Test Failed to start\r\n");
					flagSelfTesting = false;
					Enabled = true;
					return;
				default:
					flagSelfTesting = false;
					addTxt1("No Response from ECU.\r\n");
					break;
			}
			delayloop(25);
			int sidByte2 = rxBuf[1];
			do
			{
				sidByte2 = rxBuf[1];
				if (timeout == 0 && sidByte2 == 0x73)
				{
					addTxt1("Self Test Completed\r\n");
					addTxt1("[0x33 requestRoutineResultsByLocalId]\r\n");
					delayloop(0xFA);
					addTxt1("Received Routine Result\r\n");
					int faultCodesAfterSelfTest = rxBuf[3];
					switch (faultCodesAfterSelfTest)
					{
						case 0x00:
							addTxt1("No Fault Codes Generated \r\nby On-Demand Self-Test\r\n");
							break;
						case 0x01:
							addTxt1(faultCodesAfterSelfTest.ToString() + " Fault Codes Generated \r\nby On-Demand Self-Test\r\n");
							string dtc01 = rxBuf[4].ToString() + rxBuf[5].ToString();
							//string dtc02 = (rxBuf[6] + rxBuf[7]).ToString();
							addTxt1("Code: " + dtc01 + "\r\n");
							//addTxt1("Code: " + dtc02 + "\r\n");
							Write("320200\r");  // request routine results
							break;
						default:
							addTxt1("No Fault Codes Generated \r\nby On-Demand Self-Test\r\n");
							break;
					}
					flagSelfTesting = false;
					break;
					/// SELF TEST HAS COMPLETED AND THE ROUTINE RESULTS ARE SENT FROM THE ECU WITH PSR 0X73
					/// RESULTS NEED TO BE PARSED TO HUMAN READABLE FORM
					//  waitfor = 0x00;
				}
				else if (rxBuf[1] == 0x7F && rxBuf[3] == 0x12)
				{
					flagSelfTesting = false;
					break;
				}
				else
				{
					if (attempt >= 10)
					{
						flagSelfTesting = false;
						delayloop(25);
						addTxt1("An Error Occurred\r\nECU is unresponsive\r\n");
						break;
					}
					else
					{
						attempt++;
						addTxt1("Self Test in Progress...\r\n");
						Write("330200\r");  // request routine results
						delayloop(0xFA);
					}
				}
			}
			while (flagSelfTesting = true);
			//}
			pictureBox_selfTesting.Visible = false;
			pictureBox_selfTesting.Enabled = false;
			waitfor = 0;
			hidesend = 1;
			Enabled = true;
			return;
			//////////////////////////////////////////////////////////////////////////////////////////////////////
		}
		// ///////////////////////////////////////////////////////////////////////////
		//   ____ __ _ ___    ____ ____   _    _ __ _ ____
		//   |=== | \| |__>   [__] |---   |___ | | \| |===
		//   ____ ____ _    ____   ___ ____ ____ ___      
		//   ==== |=== |___ |---    |  |=== ====  |       
		///////////////////////////////////////////////////////////////////////
		void routineControl_endOfLineSelfTest()
		{
			// GFX ECU SELF TESTING JUST PUT CODE HERE TO TEST GFX NEeD TO MOVE TO ROUTINE CONTROL SELF TEST CODE
			pictureBox_selfTesting.Enabled = true;
			pictureBox_selfTesting.Visible = true;
			Enabled = false;
			hidesend = 1;
			flagSelfTesting = false;
			int attempt = 1;
			
			if (comboBoxBaBfFgFgx.SelectedIndex == 0x02) // FG2 
			{
				startDiagnosticSession(standardDiagnosticUds);
			}
			else
			{
				startDiagnosticSession(standardDiagnostic);
			}
			pictureBox_selfTesting.Visible = true;
			waitfor = 0x71;
			Write("311100\r");
			//if (timeout == 0) delayloop(0xFA);
			int sidByte = rxBuf[1];
			switch (sidByte)
			{
				case 0x71:
					flagSelfTesting = true;
					Write("331100\r");  // request routine results
					/// WHILE WAITING FOR SELF TEST TO COMPLETE WE ARE REQUESTING THE RESULTS OF THE SELF TEST ROUTINE 
					/// VIA SERVICE 0X33 - NEEDS TO BE TIMED CORRECTLY IN ORDER TO GET ROUTINE RESULTS VIA PSR 0X73  
					break;
				case 0x7F:
					addTxt1("EOL Assembly Self Test Failed to start\r\n");
					flagSelfTesting = false;
					Enabled = true;
					return;

			}
			int sidByte2 = rxBuf[1];
			while (flagSelfTesting = true)
			{

				sidByte2 = rxBuf[1];
				if (timeout == 0 && sidByte2 == 0x73)
				{
					addTxt1("Successfully got Routine Result\r\n");
					delayloop(0xFA);
					int faultCodesAfterSelfTest = rxBuf[3];

					switch (faultCodesAfterSelfTest)
					{
						case 0x00:
							addTxt1("No Fault Codes Generated \r\nby EOL Assembly Self-Test\r\n");
							break;
						case 0x01:
							addTxt1(faultCodesAfterSelfTest.ToString() + " Fault Codes Generated \r\nby EOL Assembly Self-Test\r\n");
							string dtc01 = (rxBuf[4] + rxBuf[5]).ToString();
							//string dtc02 = (rxBuf[6] + rxBuf[7]).ToString();
							addTxt1("Code: " + dtc01 + "\r\n");
							//addTxt1("Code: " + dtc02 + "\r\n");
							break;
					}
					flagSelfTesting = false;
					break;
					/// SELF TEST HAS COMPLETED AND THE ROUTINE RESULTS ARE SENT FROM THE ECU WITH PSR 0X73
					/// RESULTS NEED TO BE PARSED TO HUMAN READABLE FORM
					//waitfor = 0x00;
				}
				else if (rxBuf[1] == 0x7F && rxBuf[3] == 0x12)
				{
					flagSelfTesting = false;
					break;
				}
				else
				{
					if (attempt >= 10)
					{
						flagSelfTesting = false;
						addTxt1("An Error Occurred\r\nECU is unresponsive\r\n");
						break;
					}
					else
					{
						attempt++;
						addTxt1("Self Testing...\r\n");
						Write("330200\r");  // request routine results
						delayloop(0x3E8);
					}
				}
			}
			//}
			pictureBox_selfTesting.Visible = false;
			waitfor = 0;
			hidesend = 1;
			Enabled = true;
			// GFX ECU SELF TESTING JUST PUT CODE HERE TO TEST GFX NEeD TO MOVE TO ROUTINE CONTROL SELF TEST CODE
			pictureBox_selfTesting.Enabled = false;
			pictureBox_selfTesting.Visible = false;
			
			return;
			//////////////////////////////////////////////////////////////////////////////////////////////////////
		}
		//////////////////////////////////////////////////////////////////////////////////////////////////
		///////////////////////////////////////////////////////////////////////////////
		////////////////////////////////////////////////////////
		///////////////////////////////////
		///////////////////
		/// END OF LINE SELF TEST ROUTINE ID - CAN MIMIC OR BE IMPLEMENTED WITH A SWITCH
		/// IN ABOVE CODE ^^
		/***
		void buttonEndOfLineSelfTestMaster_Click(object sender, EventArgs e)
		{
		
		}
		***////////////////////////////////////////////////////////
		///  SELF TEST FUNC CALLS 
		///  resets buffers and sets header for each ecu in prepa
		///  ration to conduct on demand self test
		///  /////////////////////////////////////
		void buttonSelfTestIpc_Click(object sender, EventArgs e)
		{
			Enabled = false;
			reset2Ipc();
			System.Windows.Forms.MessageBox.Show("On Demand Module Self Test Requested. Be aware that actuators on the vehicle will become active.", "Caution", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
			routineControl_onDemandSelfTest();
			return;

		}
		/// FDIM FUNC CALL
		void buttonSelfTestFdim_Click(object sender, EventArgs e)
		{
			Enabled = false;
			reset2Fdim();
			System.Windows.Forms.MessageBox.Show("On Demand Module Self Test Requested. Be aware that actuators on the vehicle will become active.", "Caution", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
			routineControl_onDemandSelfTest();
			return;

		}
		/// BEM FUNC CALL
		void buttonSelfTestBem_Click(object sender, EventArgs e)
		{
			Enabled = false;
			reset2Bem();
			System.Windows.Forms.MessageBox.Show("On Demand Module Self Test Requested. Be aware that actuators on the vehicle will become active.", "Caution", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
			routineControl_onDemandSelfTest();
			return;
		}
		// BPM FUNC CALL
		void buttonSelfTestBpm_Click(object sender, EventArgs e)
		{
			Enabled = false;
			reset2Bpm();
			System.Windows.Forms.MessageBox.Show("On Demand Module Self Test Requested. Be aware that actuators on the vehicle will become active.", "Caution", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
			routineControl_onDemandSelfTest();
			return;
		}
		/// ACM FUNC CALL
		void buttonSelfTestAcm_Click(object sender, EventArgs e)
		{
			Enabled = false;
			reset2Acm();
			System.Windows.Forms.MessageBox.Show("On Demand Module Self Test Requested. Be aware that actuators on the vehicle will become active.", "Caution", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
			routineControl_onDemandSelfTest();
			return;
		}
		/// AIM FUNC CALL
		void buttonSelfTestAim_Click(object sender, EventArgs e)
		{
			Enabled = false;
			reset2Aim();
			System.Windows.Forms.MessageBox.Show("On Demand Module Self Test Requested. Be aware that actuators on the vehicle will become active.", "Caution", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
			routineControl_onDemandSelfTest();
			return;
		}
		/// PAM FUNC CALL
		void buttonSelfTestPam_Click(object sender, EventArgs e)
		{
			Enabled = false;
			reset2Pam();
			System.Windows.Forms.MessageBox.Show("On Demand Module Self Test Requested. Be aware that actuators on the vehicle will become active.", "Caution", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
			routineControl_onDemandSelfTest();
			return;
		}

		/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		//
		//  ██╗ ██████╗ ██████╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗    ████████╗███████╗███████╗████████╗
		//  ██║██╔════╝██╔════╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
		//  ██║██║     ██║         ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║       ██║   █████╗  ███████╗   ██║   
		//  ██║██║     ██║         ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║       ██║   ██╔══╝  ╚════██║   ██║   
		//  ██║╚██████╗╚██████╗    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║       ██║   ███████╗███████║   ██║   
		//  ╚═╝ ╚═════╝ ╚═════╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝       ╚═╝   ╚══════╝╚══════╝   ╚═╝   
		//                                                                                                                    
		////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		private void buttonInteriorCommandCentreSelfTestAndReadDiagnosticTroubleCodes()
		{
			///////////////////////////////////////////////////////////////
			hidesend = 0;
			Enabled = false;
			addTxt1("\r\n Testing Interior Command Centre\r\n");
			pictureBox_selfTesting.Visible = true;
			pictureBox_selfTesting.Enabled = true;
			reset2Fdim();
			clearDtc();
			addTxt1("FDIM Self Testing\r\n");
			routineControl_onDemandSelfTest();
			dtcFlag = true;
			readContinuousCodes();
			dtcFlag = false;
			delayloop(0xFA);
			reset2Acm();
			clearDtc();
			addTxt1("ACM Self Testing\r\n");
			routineControl_onDemandSelfTest();
			dtcFlag = true;
			readContinuousCodes();
			dtcFlag = false;
			delayloop(0xFA);
			reset2Aim();
			clearDtc();
			addTxt1("AIM Self Testing\r\n");
			routineControl_onDemandSelfTest();
			dtcFlag = true;
			readContinuousCodes();
			dtcFlag = false;
			delayloop(0xFA);
			reset2Bpm();
			clearDtc();
			addTxt1("BPM Self Testing\r\n");
			routineControl_onDemandSelfTest();
			dtcFlag = true;
			readContinuousCodes();
			dtcFlag = false;
			delayloop(0xFA);
			addTxt1("Interior Command Centre Self-Tests Finished\r\n");
			System.Windows.Forms.MessageBox.Show("Module Self Tests Complete.", "FoA Orion Comms - Interior Command Centre", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
			delayloop(0xFA);
			pictureBox_selfTesting.Visible = false;
			pictureBox_selfTesting.Enabled = false;
			Enabled = true;
			hidesend = 0;
			return;
			///////////////////////////////////////////////////////////////
		}


		// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	}
}

