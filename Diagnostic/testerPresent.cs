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
		////////////////////////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
		//    _____          ________ ___________ ___________              __              __________                                      __   
		//   /  _  \ ___  ___\_____  \\_   _____/ \__    ___/___   _______/  |_  __________\______   \_______   ____   ______ ____   _____/  |_ 
		//  /  /_\  \\  \/  /  _(__  < |    __)_    |    |_/ __ \ /  ___/\   __\/ __ \_  __ \     ___/\_  __ \_/ __ \ /  ___// __ \ /    \   __\
		//  \  \_/   \>    <  /       \|        \   |    |\  ___/ \___ \  |  | \  ___/|  | \/    |     |  | \/\  ___/ \___ \\  ___/|   |  \  |  
		//   \_____  /__/\_ \/______  /_______  /   |____| \___  >____  > |__|  \___  >__|  |____|     |__|    \___  >____  >\___  >___|  /__|  
		//         \/      \/       \/        \/               \/     \/            \/                             \/     \/     \/     \/      
		//////////////////////////////////////////////////////////////////
		/// <summary> SERVICE: 0X31 TESTER PRESENT
		/// useage: "testerPresent(responseType, object sender, e);"
		/// </summary>
		/// responseTypes:  \\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////
		string requestResponse = "01";
		string suppressResponse = "02";
		//////////////////////////////////////////////////////////////////
		/// ELM327 Function for 0x3E testerPresent  
		//////////////////////////////////////////////////////////////////
		public void testerPresent(string responseType)
		{
			for (;;)
			{
				addTxt1("0x3E testerPresent\r\n");
				waitfor = 0x7E;
				Write("3E" + responseType + "\r");				
			}
			if (rxBuf[1] == 0x7F)
			{
				hidesend = 0;
				Enabled = true;
				return;
			}
			if (timeout == 0) delayloop(0xFA);
			hidesend = 0;
			Enabled = true;
			return;
		}

		//////////////////////////////////////////////////////////////////
		/// J2534 Function for 0x3E testerPresent  
		//////////////////////////////////////////////////////////////////

		//////////////////////////////////////////////////////////////////
		/***
                //Sample 02: Declare the Timer Reference
                static Timer testerPresentTask = null;
                //Sample 03: Timer Callback - 
                //  Just Ticks in the Console

                //////////////////////////////////////////////////////////////////
                /// <summary> SERVICE: 0X31 TESTER PRESENT
                /// useage: "testerPresent(responseType, object sender, e);"
                /// </summary>
                /// responseTypes:
                /////////////////////////////////////
                string requestResponse = "01";
                string suppressResponse = "02";

                /////////////////////////////////////
                /// 
                //////////////////////////////////////////////////////////////////
                static void esterPresent(string responseType, object state)
                {
                    addTxt1("0x3E testerPresent\r\n");
                    waitfor = 0x7E;
                    Write("3E" + responseType + "\r");
                    if (rxBuf[1] == 0x7F)
                    {
                        addTxt1(printerr((int)rxBuf[3]) + "\r\n");
                        hidesend = 1;
                        Enabled = true;
                        hidesend = 0;
                        Enabled = true;
                        return;

                    }
                    if (timeout == 0) delayloop(0xFA);
                    hidesend = 0;
                    Enabled = true;
                    return;

                }
                //////////////////////////////////////////////////////////////////

                static void runTesterPresentTask(string[] args)
                {
                    while (true)
                    {
                        testerPresentTask = new Timer(
                            new TimerCallback(testerPresent(suppressResponse)),
                            null,
                            2000,
                            2000);
                     }
                    if (testerPresentTask == null)
                    {
                        continue;
                    }
                    //Sample 05: Stop The Timer
                    testerPresentTask.Change(
                        Timeout.Infinite,
                        Timeout.Infinite);
                    break;    
                }
                ***/
		// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	}
}

