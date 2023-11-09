```
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
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
namespace FGCOM
{
	public partial class Orion
	{
		// /////
		// //////////////////////////
		// ////////////////////////////////////////
		// //////////////////////////////////////////////////////
		// ////////////////////////////////////////////////////////////////////
		// ///////////////////////////////////////////////////////////////////////////////////
		// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		//  _______          ___________         .___.__                                      __  .__         _________                    .__              _________                __                .__   
		//  \   _  \ ___  __/_   \   _  \      __| _/|__|____     ____   ____   ____  _______/  |_|__| ____  /   _____/ ____   ______ _____|__| ____   ____ \_   ___ \  ____   _____/  |________  ____ |  |  
		//  /  /_\  \\  \/  /|   /  /_\  \    / __ | |  \__  \   / ___\ /    \ /  _ \/  ___/\   __\  |/ ___\ \_____  \_/ __ \ /  ___//  ___/  |/  _ \ /    \/    \  \/ /  _ \ /    \   __\_  __ \/  _ \|  |  
		//  \  \_/   \>    < |   \  \_/   \  / /_/ | |  |/ __ \_/ /_/  >   |  (  <_> )___ \  |  | |  \  \___ /        \  ___/ \___ \ \___ \|  (  <_> )   |  \     \___(  <_> )   |  \  |  |  | \(  <_> )  |__
		//   \_____  /__/\_ \|___|\_____  /  \____ | |__(____  /\___  /|___|  /\____/____  > |__| |__|\___  >_______  /\___  >____  >____  >__|\____/|___|  /\______  /\____/|___|  /__|  |__|   \____/|____/
		//         \/      \/           \/        \/         \//_____/      \/           \/               \/        \/     \/     \/     \/               \/        \/            \/                         
		/// /////////////////////////////////                                                            /////////////////////////////////////
		// Token: 0x0600000D RID: 13 RVA: 0x00002444 File Offset: 0x00000644
		/// <summary> SERVICE: 0x10 DIAGNOSTIC SESSION CONTROL
		/// usage: startDiagnosticSession(sessionType);
		/// can.Message(arbitration_id = _DiagSig_Rx, data = [0x02, 0x10, sessionType, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id = False)
		/// </summary>
		/// Code is working in present state 10/03/2023
		/// /////////////////////////////////                                                           /////////////////////////////////////
		/// sessionTypes:
		string standardDiagnostic = "81";
		string ecuProgramming = "85";
		string ecuAdjustment = "87";
		string eolExtended = "FE";
		string systemSupplierSpecific = "FA";
		// 01-Default session 02-Programming session 03-Extended Diagnostic session
		string standardDiagnosticUds = "01";
		string ecuProgrammingUds = "02";
		string extendedDiagnosticUds = "03";
		/// /////////////////////////////////                                                  /////////////////////////////////////
		/// <param name="sessionType">standardDiagnostic, ecuAdjustment, ecuProgramming, eolExtended, systemSupplierSpecific</param>
		/////////////////////////////////////                                                  /////////////////////////////////////
		public void startDiagnosticSession(string sessionType)
		{
            waitfor = 0x50;
            addTxt1("[0x10 startDiagnosticSess] \r\n");
            Write("10" + sessionType + "\r");
			if (timeout == 0)
			{
				delayloop(250);
				int sidByte = rxBuf[1];
	            switch(sidByte)
				{
					case 0x50:
						addTxt1(sessionType + " Session started successfully...\r\n");
						break;
					case 0x7F:
						addTxt1(sessionType + " Session failed to start...\r\n");
						break;
					default:
						addTxt1("No Response from ECU...\r\n");
						break;
				}
				waitfor = 0;
			}           
			delayloop(250);
			return;
		}
		/////////////////////////////////////                              /////////////////////////////////////
		/// startDiagnosticSession (ref. KWP-GRP-1.5, 6.1.1)
		///  The parameters values supported for the diagnosticMode parameter of the startDiagnosticSession
		///  service are listed in Table 5. No other diagnosticMode values shall be supported.
		///  The baudrateIdentifier parameter shall not be used with this or any service.
		///  One and only one diagnostic session shall be active in an ECU at all times. Diagnostic session $81
		///  shall be active by default upon power-up of an ECU (i.e., a tester request message shall not be
		///  required). A tester shall have the capability of changing from any one diagnostic session to another
		///  without performing any type of security access (refer to section 2.2.2.7.6 for additional details).
		///  Diagnostic session $87 (ECUAdjustmentMode), if implemented, shall be an extended diagnostic
		///  session that is a superset of the diagnostic functionality supported in diagnostic session $81.
		///  Diagnostic session $85 (ECUProgrammingMode), if implemented, shall be used only for Method 3
		///  file download and shall be the implementation of the Method 3 programming requirements as
		///  described in MC-v2003.0.
		///  When an ECU transitions from any diagnostic session to another diagnostic session, the ECU shall
		///  reset all active diagnostic functionality that is not supported in the new diagnostic session (e.g.,
		///  security access, I/O control), with the exception of changes written to long term memory. For
		///  example, if an ECU only supports service $2F (inputOutputControlByCommonID) in diagnostic
		///  session $87 then any actively controlled inputs or outputs shall revert back to the normal value as
		///  determined by the control system upon a transition from session $87 to session $81.
		///  An ECU is allowed a 750ms re-initialization period upon returning to the default diagnostic session
		///  ($81) from any other diagnostic session. During this re-initialization period the ECU is not required to
		///  respond to any diagnostic requests.//
		///  The only defined vehicleManufacturerSpecific diagnostic session is $F0 and is defined as
		///  EOLExtendedDiagnosticSession. Any ECU that needs to grant special privileges to an End of Line
		///  test tool shall implement diagnostic session $F0 to provide access to these privileges. For example, an
		///  ABS module that normally exits to the defaultDiagnosticSession when vehicle speed is greater than a
		///  given value may maintain the EOLExtendedDiagnosticSession (despite the vehicle speed). Diagnostic
		///  session $F0 shall be reserved only for use by End of Line test tools in assembly plants and shall be
		///  implemented only when needed to verify communication with an End of Line tester. This
		///  EOLExtendedDiagnosticSession shall grant access to all functionality (e.g., diagnostic services,
		///  privileges, input/output control, etc.) that is necessary during the assembly testing and shall contain a
		///  superset of the diagnostic functionality supported in diagnostic session $87 (ECUAdjustmentMode).
		///  SystemSupplierSpecific diagnostic sessions shall not be supported by Ford test tools. All implemented
		///  systemSupplierSpecific diagnostic sessions shall be specified by the module designer and documented
		///  in the ECU's Subsystem Specific Diagnostic Specification (SSDS/Part 2).'''
		//        DIAGNOSTIC SERVICE FUNCTIONS
		//        const int reportDiagnosticState = 0x50;
		//        const int readFreezeFrameData = 0x12;
		//        const int requestStoredCodes = 0x13;
		//        const int clearDiagnosticInformation = 0x14;
		//        const int readDTCByStatus = 0x18;
		//        const int operationalStateEntryRequest = 0x20;
		//        const int readDataByLocalID = 0x21;
		//        const int readMemoryByCommonID = 0x22;
		//        const int readMemoryByAddress = 0x23;
		//        const int requestCommonIDScalingMasking = 0x24;
		//        const int stopTransmittingRequestedData = 0x25;
		//        const int requestSecurityAccess = 0x27;
		//        const int reportSecurityAccess = 0x67;
		//        const int requestCommunicationControl = 0x28;
		//        const int requestDiagnosticdataPacket = 0x2A;
		//        const int dynamicallyDefineDiagnosticDataPacket = 0x2C;
		//        const int writeDataByCommonID = 0x2E;
		//        const int inputOutputControlByLocalID = 0x2F;
		//        const int startRoutineByLocalIdentifier = 0x31;
		//        const int stopRoutineByLocalIetdentifier = 0x32;
		//        const int requestRoutineResultsByLocalID = 0x33;
		//        const int requestDownload = 0x34;
		//        const int requestUpload = 0x35;
		//        const int transferData = 0x36;
		//        const int requestTransferExit = 0x37;
		//        const int writeDataByLocalId = 0x3B;
		//        const int requestReadMemoryBlock = 0x3C;
		//        const int writeMemoryByAddress = 0x3D;
		//        const int testerPresent = 0x3E;
		//        const int RequestResponse = 0x01;
		//        const int SuppressResponse = 0x02;
		//        const int controlDTCSetting = 0x85;
		//        const int requestDiagnosticDataPacket = 0xA0;
		//        const int dynamicallyDefineDataPacket = 0xA1;
		//        const int noStoredCodesLoggingStateEntry = 0xB0;
		//        const int diagnosticCommand = 0xB1;
		//        const int inputIntegrityTestStateEntry = 0xB2;
		//        const int requestManufacturerStateEntry = 0xB4;
	}
}

``` 
