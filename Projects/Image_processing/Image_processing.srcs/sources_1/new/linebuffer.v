`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2026 11:26:07
// Design Name: 
// Module Name: linebuffer
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

//hare krishna
//haribol
module linebuffer(
input i_clk,
input i_rst,
input [7:0] i_data,
input i_data_valid,
//there is no ready signal bcoz memory is always ready
//read entire 3 pixesls at a time for better performence(in the premade ip we dont have this flexibility)
output [23:0] o_data,  // 3 pixels ->3 bytes of data ==> 24 bits
//WE CANNNOT DO 
//output [7:0] o_data [2:0]  -> this is only for memory
input i_rd_data // ~ ready signal from slave
    );
    
 reg [7:0] line [511:0];  //line buffer
 reg [8:0] wrPntr;
 reg [8:0] rdPntr;
 
 always @(posedge i_clk)
 begin
        if(i_data_valid)
                line[wrPntr] <= i_data;
 end
 
 always @(posedge i_clk)
 begin
    if(i_rst)
        wrPntr <='d0;
    else if (i_data_valid)
        wrPntr  <=wrPntr + 'd1;
 end
 
 //nowlets come to the read 
 assign o_data= { line[rdPntr], line[rdPntr+1], line[rdPntr+2] };
 
  always @(posedge i_clk)
 begin
    if(i_rst)
        rdPntr <='d0;
    else if (i_rd_data)
        rdPntr  <=rdPntr + 'd1;
 end
 
endmodule
