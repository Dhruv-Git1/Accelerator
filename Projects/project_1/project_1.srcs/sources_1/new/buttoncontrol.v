`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04.07.2026 12:21:14
// Design Name: 
// Module Name: buttoncontrol
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

//if pressed for more than 1 second then only "yes"- and pressing more than
//1 second wont create any output
module buttoncontrol(
input clock,
input reset,
input button,
output reg valid_vote
    );
    reg [30:0] counter;
    //100 mhz clock- we want to measure 1 second.
    //here we are usiing the counter to check if someone is pressiung the button
    always @(posedge clock)
    begin
        if(reset)
        counter <=0;
        else
            begin
                if(button & counter < 10000001)
                        counter <= counter+1;
                else if(!button)
                    counter <=0;
                 end
    end
    
    always @(posedge clock)
    begin
    if(reset)    
    valid_vote <= 1'b0;
    else
        begin 
        if(counter == 100000000)
            valid_vote <= 1'b1;
        else
            valid_vote <= 1'b0;
            
        
        end
    
    end
    
endmodule
