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
		//  _______          ____ ____                     __________                      __   
		//  \   _  \ ___  __/_   /_   |   ____   ____  __ _\______   \ ____   ______ _____/  |_ 
		//  /  /_\  \\  \/  /|   ||   | _/ __ \_/ ___\|  |  \       _// __ \ /  ___// __ \   __\
		//  \  \_/   \>    < |   ||   | \  ___/\  \___|  |  /    |   \  ___/ \___ \\  ___/|  |  
		//   \_____  /__/\_ \|___||___|  \___  >\___  >____/|____|_  /\___  >____  >\___  >__|  
		//         \/      \/                \/     \/             \/     \/     \/     \/      
		////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		/// <summary> SERVICE: 0X11 ECU RESET 
		/// usage: "ecuReset(resetType, sender, e);"
		/// can.Message(arbitration_id = _DiagSig_Rx, data = [0x02, 0x11, resetType, 0, 0, 0, 0, 0], is_extended_id = False)
		//  ECUReset
		//      Only the powerOn value of the resetMode (RM_) parameter shall be supported. The resetStatus (RS_)
		//      parameter shall not be supported.
		//      The positive response to an ECUReset (service $11) request shall occur before the ECU performs the
		//      reset. An ECU is allowed a 750ms re-initialization period after providing a positive response to an
		//      ECUReset request. During this re-initialization period the ECU is not required to respond to any
		//      diagnostic requests.
		/// </summary>
		/////////////////////////////////////
		/// resetTypes:
		string hardReset = "01";
		string keyOffOnReset = "02";
		string softReset = "03";
		string enableRapidPowerShutDown = "04";
		string disableRapidPowerShutDown = "05";
		/////////////////////////////////////
		/// <param name="resetType">01 = hardReset 02 = keyOffOnReset 03 = softReset 04 = enableRapidPowerShutDown 05 = disableRapidPowerShutdown</param>
		void ecuReset(string resetType)
		{
		    hidesend = 1;
			Enabled = false;
			waitfor = 0x51;
			addTxt1("[0x11 ecuReset]\r\n");
			Write("11" + resetType + "\r");
			if (timeout == 0)
			{
				delayloop(250);
				int sidByte = rxBuf[1];
				switch (sidByte)
				{
					case 0x51:
						addTxt1(resetType + " Resetting ECU...\r\n");
						break;
					case 0x7F:
						addTxt1(resetType + " Reset ECU Failed...\r\n");
						break;
				}
			}
			waitfor = 0;
			Enabled = true;
			return;
		}
	}
}

