`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02.07.2026 13:23:13
// Design Name: 
// Module Name: haribol
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


module haribol(
  input clk,
    input a,
    input b,
    output wire out_assign,
    output reg out_always_comb,
    output reg out_always_ff 
    );

    assign out_assign = a ^ b;
    
    always@(*)
        begin
            out_always_comb= a^b;
        end
    
    always@(posedge clk)
        begin
            out_always_ff <= a^b;
        end
endmodule
